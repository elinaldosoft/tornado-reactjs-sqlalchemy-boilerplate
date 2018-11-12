from sqlalchemy.orm import sessionmaker
from tornado.ioloop import IOLoop
from tornado.concurrent import return_future
from contextlib import contextmanager

class SessionMixin:
    # _session = None

    # @property
    # def session(self):
    #     self._make_session()
    #     return self._session

    # def on_finish(self):
    #     self._session.close()

    @return_future
    def as_future(self, query, callback):
        callback(query)

    # @contextmanager
    def make_session(self):
        engine = self.application.settings.get("session_engine")
        Session = sessionmaker()
        Session.configure(bind=engine)
        # self._session = Session()
        return Session()
