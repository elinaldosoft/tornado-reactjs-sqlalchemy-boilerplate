from lib import gson
import tornado
from tornado.web import RequestHandler
from lib.factory import SessionMixin
from lib.cache import CacheMixin, cache
from tornado.escape import json_decode, json_encode
from .models import Article, Comment


class BaseHandler(CacheMixin, RequestHandler, SessionMixin):
    def prepare(self):
        super(BaseHandler, self).prepare()


class HomeHandler(BaseHandler):
    @cache(10)
    async def get(self):
        session = self.make_session()
        articles = await self.as_future(session.query(Article).all())
        self.render("home.html", articles=articles)


class NewsHandler(BaseHandler):
    @cache(10)
    async def get(self, slug, id):
        session = self.make_session()
        article = await self.as_future(
            session.query(Article)
            .filter(Article.id == id, Article.slug == slug)
            .first()
        )
        if not article:
            raise tornado.web.HTTPError(404)
        self.set_cookie('article_id', str(article.id))
        self.render("news.html", article=article)


class CommentHandler(RequestHandler, SessionMixin):
    async def get(self, page):
        session = self.make_session()
        page = int(self.get_argument('page', 0))
        comments = await self.as_future(session.query(Comment).order_by(Comment.id.desc()).limit(4).offset(page * 4))
        self.set_header('Content-Type', 'application/json')
        self.write(gson.dumps({'comments': [comment.serialize for comment in comments]}))

    async def post(self):
        comment = Comment(name=self.get_argument('name'), email=self.get_argument('email'), text=self.get_argument('text'), article_id=self.get_argument('article_id'))
        session = self.make_session()
        await self.as_future(session.add(comment))
        await self.as_future(session.commit())
        self.write({'status': 'ok'})
