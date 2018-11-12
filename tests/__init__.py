# import pytest
# from tornado.testing import AsyncHTTPTestCase
# from config.settings import PORT, HOST, STATIC
# import run


# class BaseTest(AsyncHTTPTestCase):
#     @pytest.fixture
#     def get_app(self):
#         yield run.main()

#     def get_url(self, path):
#         return "http://{host}:{port}{path}".format(host=HOST, port=PORT, path=path)
