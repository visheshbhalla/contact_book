import unittest
import resources

from mock import patch
from pyramid import testing
from resources import Root, Contacts, Contact

@patch('contact_book.resources.Contacts')
@patch('contact_book.resources.Contact')

class HelloWorldViewTests(unittest.TestCase):
    def _makeOne(self, context, request):
        from .views import ContactBookViews

        inst = ContactBookViews(context, request)
        return inst

    def test_home(self,mock_contact,mock_contacts):
        request = testing.DummyRequest()
        context = testing.DummyResource()
        inst = self._makeOne(context, request)
        response = inst.home()
        dict_data = {'info': 'Contact Book API'}
        self.assertDictEqual(response, dict_data)

    def test_save(self,mock_contact,mock_contacts):
        json_params = {'email_address':'test@test.com','contact_name':'test'}
        request = testing.DummyRequest(json_body=json_params, method='POST')
        context = resources.Contacts()
        inst = self._makeOne(context, request)
        response = inst.create_contact()
        self.assertEqual(response.status, '201 Created')

    def test_update(self,mock_contact,mock_contacts):
        json_params = {'email_address':'test@test.com'}
        request = testing.DummyRequest(json_body=json_params, method='POST')
        context = resources.Contact()
        inst = self._makeOne(context, request)
        response = inst.update_contact()
        self.assertEqual(response.status, '202 Accepted')

    def test_get(self,mock_contact,mock_contacts):
        request = testing.DummyRequest()
        context = resources.Contact()
        inst = self._makeOne(context, request)
        response = inst.get_contact()
        self.assertEqual(response.status, '202 Accepted')

    def test_get_list(self,mock_contact,mock_contacts):
        request = testing.DummyRequest()
        context = resources.Contacts()
        inst = self._makeOne(context, request)
        response = inst.list_contacts()
        self.assertEqual(response.status, '202 Accepted')

    def test_delete(self,mock_contact,mock_contacts):
        request = testing.DummyRequest()
        context = resources.Contact()
        inst = self._makeOne(context, request)
        response = inst.delete_contact()
        self.assertEqual(response.status, '202 Accepted')

        #self.assertIn(b'Visit', response.body)

    #def test_retrieve(self):

    
    """def test_hello(self):
        from .views import hello

        request = testing.DummyRequest()
        response = hello(request)
        self.assertEqual(response.status_code, 200)
        #self.assertIn(b'Go back', response.body)"""

"""class HelloWorldFunctionalTests(unittest.TestCase):
    def setUp(self):
        from hello_world import main
        app = main({})
        from webtest import TestApp

        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/', status=200)
        self.assertIn(b'<body>Visit', res.body)

    def test_hello(self):
        res = self.testapp.get('/howdy', status=200)
        self.assertIn(b'<body>Go back', res.body)"""
