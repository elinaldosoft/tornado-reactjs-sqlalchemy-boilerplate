import pytest
from tornado.testing import AsyncHTTPTestCase, gen_test
from server import Application


class WebTestCase(AsyncHTTPTestCase):
    @pytest.fixture
    def get_app(self):
        self.app = Application()
        return self.app


class TestRoutesHandler(WebTestCase):
    def test_home_get(self):
        rsp = self.fetch("/")
        assert rsp.code == 200

    def test_home_post(self):
        rsp = self.fetch("/", method="POST", body="name=jonh")
        assert rsp.code == 405

    def test_static_file(self):
        rsp = self.fetch("/static/css/bootstrap.min.css")
        assert rsp.code == 200

    def test_static_file_nofound(self):
        rsp = self.fetch("/staxtic/css/bootstrap.min.css")
        assert rsp.code == 404

    def test_reverse_url_homepage(self):
        assert self.app.reverse_url("homepage") == "/"
