from app import app, models, db
import unittest
import flask_testing
from flask import Flask, request
from flask_testing import TestCase
from flask.ext.login import current_user
from flask_login import LoginManager, current_user, AnonymousUserMixin
from app.models import Account




class BaseTestCase(TestCase):

    def create_app(self):

        app.config.from_object('config.TestConfig')

        return app

    def setUp(self):
        db.create_all()
        db.session.add(Account(email='jack@yahooo.com', password='password'))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()



class FlaskTestCase(BaseTestCase):

    #Function to speed up login requests
    def login(self, username, password):
        return self.client.post('/login', data=dict(
        username=username,
        password=password
        ), follow_redirects=True)

    #Function to speed up log out requests
    def logout(self):
        return self.client.get('/logout', follow_redirects=True)

    # Function to quickly register user for further use.
    def register(self, email, password, passwordCheck):
        return self.client.post(
        '/create_account',
        data=dict(email=email, password=password, passwordCheck=passwordCheck),
        follow_redirects=True
        )


    # ensure flask set up correctly
    def test_index(self):
        #tester = app.test_client(self)
        response = self.client.get('/home', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # ensure login page loads
    def test_login_page_loads(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertTrue(b'Log into Your Account' in response.data)

    #ensure profile requires login.
    def test_profile_requires_login(self):
        #tester = app.test_client(self)
        response = self.client.get('/profile', follow_redirects=True)
        self.assertTrue(b'Please log in to access this page.', response.data)

    # #ensure profile requires login.
    # def test_basket_requires_login(self):
    #     response = self.client.get('/profile', follow_redirects=True)
    #     self.assertTrue(b'Please log in to access this page.', response.data)


    # ensure login works with correct account
    def test_working_login(self):
        self.register(email='jack@yah.com', password='password', passwordCheck='password')
        with self.client:
            response = self.client.post(
                '/login', data=dict(email='jack@yah.com', password='password'), follow_redirects=True)
            self.assertTrue(current_user.email == 'jack@yah.com')
            self.assertTrue(current_user.is_active())
            self.assertIn(b'Logged in successfully', response.data)
            #print (response.data)


    #Ensure one email can only be registed once
    def test_user_registration_duplicate_email(self):
         response = self.register('pat@gmail.com', 'FlaskIsAwesome', 'FlaskIsAwesome')
         self.assertEqual(response.status_code, 200)
         response = self.register('pat@gmail.com', 'FlaskIsReallyAwesome', 'FlaskIsReallyAwesome')
         self.assertIn(b'An account has already been registered with that email', response.data)


    #Ensure user can register successfully
    def test_registration(self):
        with self.client:
            response = self.client.post('/create_account', data=dict(
                email='jack@yah.com', password='password', passwordCheck='password' ), follow_redirects=True)
            self.assertTrue(current_user.email == 'jack@yah.com')
            self.assertTrue(current_user.is_active())
            self.assertIn(b'Account created successfully', response.data)

    # Ensure errors are thrown during an incorrect user registration
    def test_incorrect_user_registeration(self):
        with self.client:
            response = self.client.post('/create_account', data=dict(
                email='ed',password='python', confirm='python'
            ), follow_redirects=True)
            self.assertIn(b'Error creating your account. Invalid email.', response.data)







if __name__ == '__main__':
    unittest.main()
