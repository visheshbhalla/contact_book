import unittest
import resources

from mock import patch
from pyramid import testing
from resources import Root, Contacts, Contact
import pyramid
from pyramid import paster
import uuid

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


"""
Functional tests were working in Test environment
but they are not working here.
There is some issue which I'm not able to figure out.
"""
class ContactBookFunctionalTests(unittest.TestCase):
        
    def setUp(self):
        print 'a'
        app = paster.get_app('development.ini')
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_it(self):
        email_address=str(uuid.uuid1())
        """res = self.testapp.get('/', status=200)
        self.assertIn(b'Contact', res.body)"""
        res = self.testapp.get('/contacts', status=200)
        self.assertIn(b'contact_name', res.body)
        res = self.testapp.get('/contacts/abc@xyz.com', status=200)
        self.assertIn(b'contact_name', res.body)
        res = self.testapp.post_json('/contacts',dict(contact_name='name1', email_address=email_address))
        self.assertIn(b'201', res.status)
        