import logging
import asyncio
import uvloop
import redis
import tornado.web
import tornado.locks
from tornado.options import define, options
from tornado.log import enable_pretty_logging
from lib.cache import RedisCacheBackend
from lib import redis_connect
from config.routes import urlpatterns
from config.settings import TEMPLATES, STATIC, PORT, HOST, DEBUG, ENGINE, AUTOESCAPE

define("host", default=HOST, help="hostname", type=str)
define("port", default=PORT, help="port to listen on", type=int)
define("static", default=STATIC, help="files statics", type=str)
define("templates", default=TEMPLATES, help="templates .html", type=str)
define("debug", default=DEBUG, help="Debug", type=bool)
define("autoescape", default=AUTOESCAPE, help="autoescape html")

logging.getLogger("tornado.general")
enable_pretty_logging()


class Application(tornado.web.Application):
    def __init__(self):
        handlers = urlpatterns
        self.redis = redis_connect.connect()
        self.cache = RedisCacheBackend(self.redis)
        settings = dict(
            template_path=options.templates,
            static_path=options.static,
            debug=options.debug,
            autoescape=options.autoescape,
            session_engine=ENGINE,
            xsrf_cookies=True,
            cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
        )
        super(Application, self).__init__(handlers, **settings)


async def main():
    tornado.options.parse_command_line()
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    app = Application()
    app.listen(options.port, address=options.host)
    
    shutdown_event = tornado.locks.Event()
    await shutdown_event.wait()


if __name__ == "__main__":
    if DEBUG:
        print("Listening on http://%s:%i" % (options.host, options.port))
    tornado.ioloop.IOLoop.current().run_sync(main)
