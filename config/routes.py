from tornado.web import url
from app.views import HomeHandler, NewsHandler, CommentHandler

urlpatterns = [
    url(r"/", HomeHandler, name="homepage"),
    url(r"/noticia/([^/]+)-([\d]+).html", NewsHandler, name="news"),
    url(r"/comment/add", CommentHandler, name="new_comment"),
    url(r"/comments/([\d]+)", CommentHandler, name="comments"),
]
