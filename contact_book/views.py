import json

from pyramid.view import view_config,forbidden_view_config, notfound_view_config
from pyramid.response import Response
from pyramid.location import lineage

from resources import Root, Contacts, Contact


class ContactBookViews:
    
    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.parents = reversed(list(lineage(context)))

    @view_config(renderer='json', context=Root)
    def home(self):
        return {'info': 'Contact Book API'}


    @view_config(request_method='PUT', context=Contact, renderer='json')
    def update_contact(self):
        r = self.context.update(self.request.json_body, True)

        return Response(
            status='202',
            content_type='application/json; charset=UTF-8')

    @view_config(request_method='GET', context=Contact, renderer='json')
    def get_contact(self):

        r = self.context.retrieve()

        if r is None:
            raise HTTPNotFound()
        else:
            return Response(
            status='202',
            content_type='application/json; charset=UTF-8',
            body=json.dumps(r))

    @view_config(request_method='GET', context=Contacts, renderer='json')
    def list_contacts(self):
        from utils import retrieve as ret
        
        data = ret(self.context,self.request)
        
        return Response(
            status='202',
            content_type='application/json; charset=UTF-8',
            body=json.dumps(data))


    @view_config(request_method='DELETE', context=Contact, renderer='json')
    def delete_contact(self):

        self.context.delete()

        return Response(
            status='202',
            content_type='application/json; charset=UTF-8')


    @view_config(request_method='POST', context=Contacts, renderer='json')
    def create_contact(self):
        try:
            from utils import validate

            document = self.request.json_body

            if validate(document) == False:
                return Response(
                    status='400',
                    content_type='application/json; charset=UTF-8',
                    body="{'error_message':'email_address/contact_name field missing'}")
            r = self.context.create(document)
            return Response(
                status='201',
                content_type='application/json; charset=UTF-8')
        except pymongo.errors.DuplicateKeyError:
            return Response(
                status='400 Bad request',
                body='{"error_message":"email_address is already present"}',
                content_type='application/json; charset=UTF-8')

    @notfound_view_config()
    def notfound(self):
        return Response(
            body=json.dumps({'message': 'Custom \'Not Found\' message'}),
            status='404',
            content_type='application/json')
