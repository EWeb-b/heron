from app import app, models, db
import unittest
import flask_testing
from flask import Flask, request
from flask_testing import TestCase
from flask_login import LoginManager, current_user, AnonymousUserMixin
from app.models import Account, FilmDetails




class BaseTestCase(TestCase):

    #Configures the app to a flask-testing supported configuration
    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    #Create all the tables and destroy them with each unit test to ensure
    # Add film to database so film dependent routes can be tested.
    # they're clean and self contained.
    def setUp(self):
        db.create_all()
        db.session.add(FilmDetails(film_certificate_id=3,
        film_blurb="""An astronaut becomes stranded on Mars after his team
        assume him dead, and must rely on his ingenuity to find
        a way to signal to Earth that he is alive.""",
        film_director="Ridley Scott",
        film_name="The Martian",
        film_actor="Matt Damon"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()



class FlaskTestCase(BaseTestCase):

    #Functions to reduce repeated code in test suite.

    #Function to speed up login requests
    def login(self, email, password):
        return self.client.post('/login', data=dict(
        email=email,
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
        follow_redirects=True)

#------------------------------------------------------------------------------#


    # ensure flask set up correctly
    def test_index(self):
        response = self.client.get('/home', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # ensure login page loads
    def test_login_page_loads(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertTrue(b'Log into Your Account' in response.data)

    # ensure sign_up page loads
    def test_sign_up_page_loads(self):
        response = self.client.get('/create_account', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # ensure screenings page loads
    def test_screenings_page_loads(self):
        response = self.client.get('/screenings', content_type='html/text',follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'On Today' in response.data)

    # ensure order ticket page loads
    def test_order_ticket_page_requires_login(self):
        response = self.client.get('/order_ticket', content_type='html/text',follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    # ensure order ticket page loads
    def test_change_password_page_loads(self):
        self.register('jack@yah.com','password', 'password')
        self.login('jack@yeh.com', 'password')
        response = self.client.get('/change_password', content_type='html/text',follow_redirects=True)
        self.assertTrue(b'Change Password' in response.data)

    # ensure film_details page loads
    def test_film_details_page_loads(self):
        response = self.client.get('/film_details',content_type='html/text')
        self.assertEqual(response.status_code, 200)

    #ensure profile requires login.
    def test_profile_requires_login(self):
        response = self.client.get('/profile', follow_redirects=True)
        self.assertTrue(b'Please log in to access this page.', response.data)

    # Ensure that logout page requires user login
    def test_logout_route_requires_login(self):
        response = self.client.get('/logout', follow_redirects=True)
        self.assertIn(b'Please log in to access this page', response.data)

#-----------------------Form Validation---------------------------------------#

    # ensure login works with correct account
    def test_working_login(self):
        self.register('jack@yah.com','password', 'password')
        with self.client:
            response = self.client.post(
                '/login', data=dict(email='jack@yah.com', password='password'),
                 follow_redirects=True)
            self.assertTrue(current_user.email == 'jack@yah.com')
            self.assertTrue(current_user.is_active())
            self.assertIn(b'Logged in successfully', response.data)


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
                email='jack@yah.com', password='password', passwordCheck='password' ),
                follow_redirects=True)
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


    #Test adding a card to an account
    def test_add_payment_method(self):
        self.register("bob@gmail.com", "bob", 'bob')
        response = self.client.post('/add_card',
                data=dict( password='bob', name_on_card='bob',
                billing_address='house',
                card_number=1234123412341234,cvc=123,expiry_date_month=12,
                expiry_date_year=2018
                ), follow_redirects=True)
        self.assertIn(b'successfully added card', response.data)

    #Test change password.
    def test_change_password(self):
        self.register('jonah@me.com', 'jonah','jonah')
        response = self.client.post('/change_password',
                    data=dict(prev_password='jonah',
                    new_password='jack', confirmation='jack'),
                    follow_redirects=True)
        self.assertIn(b'Password changed successfully', response.data)

    #ensure film_details page loads
    def test_select_screening(self):
        response = self.client.get('/film_info?passed=The+Martian',content_type='html/text')
        self.assertEqual(response.status_code, 200)

    #Test select viewing time.
    def test_select_viewing_time(self):
        self.register('jonah@me.com', 'jonah','jonah')
        response = self.client.post('/film_info?passed=The+Martian',
                data=dict(times='10am')
                ,follow_redirects=True)
        self.assertIn(b'Ticket Type', response.data)


    #Test order_ticket
    def test_order_ticket(self):
        self.register('jonah@me.com', 'jonah','jonah')
        self.client.post('/film_info?passed=The+Martian',
                        data=dict(times='10am')
                        ,follow_redirects=True)
        response = self.client.post('/order_ticket',
                    data=dict(ticket_type='student',
                    seat_number=('1')),
                    follow_redirects=True)
        self.assertIn(b'Checkout', response.data)

    #fully test the purchasing a ticket.
    def test_purchase_ticket(self):
        self.register('jonah@me.com', 'jonah','jonah')
        self.client.post('/add_card',
                        data=dict( password='jonah', name_on_card='bob',
                        billing_address='house',
                        card_number=1234123412341234,cvc=123,expiry_date_month=12,
                        expiry_date_year=2018
                        ), follow_redirects=True)
        self.client.post('/film_info?passed=The+Martian',
                        data=dict(times='10am')
                        ,follow_redirects=True)
        self.client.post('/order_ticket',
                        data=dict(ticket_type='student',
                        seat_number=('1')),
                        follow_redirects=True)
        response = self.client.post('/basket',
                        data=dict( first_name='jonah', last_name='poo',
                        address='i like turtles',
                        postcode='bradley stoke boy', card=1234),
                        follow_redirects=True)
        self.assertIn(b'Order successfully registered', response.data)






if __name__ == '__main__':
    unittest.main()
