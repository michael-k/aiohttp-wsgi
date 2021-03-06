from wsgiref.validate import validator
from tests.base import AsyncTestCase, noop_application


validator_application = validator(noop_application)


class EnvironTest(AsyncTestCase):

    def testValidWsgi(self):
        with self.run_server(validator_application) as client:
            client.assert_response()
