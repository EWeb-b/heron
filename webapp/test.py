from app import app, models, db
import unittest
import flask_testing
from flask import Flask, request
from flask_testing import TestCase
from flask_login import LoginManager, current_user, AnonymousUserMixin
from app.models import Account


class Anonymous(AnonymousUserMixin):

    def __init__(self):
        self.email = 'jack@yahooo.com'

# Set up test user


class BaseTestCase(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config.from_object('config.TestConfig')
        db.init_app(app)
        login_manager = LoginManager()
        login_manager.init_app(app)
        login_manager.anonymous_user = Anonymous
        return app

    def setUp(self):
        db.create_all()
        db.session.add(Account(email='jack@yahooo.com', password='password'))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class FlaskTestCase(BaseTestCase):

    # ensure flask set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/home', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # ensure login page loads
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Log into Your Account' in response.data)

    # ensure login works with correct account
    def test_working_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login', data=dict(email='jack@yahooo.com', password='password'), follow_redirects=True)
        self.assertTrue(b'' in response.data)

    # ensure user can register
    def test_registration(self):
        with self.client:
            tester = app.test_client(self)
            response = tester.post('create_account/', data=dict(
                email='jack@yahooo.com', password='password'), follow_redirects=True)
            self.assertTrue(current_user.email == 'jack@yahooo.com')


if __name__ == '__main__':
    unittest.main()
