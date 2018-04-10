

def validate(document):
	if 'email_address' not in document.keys() or 'contact_name' not in document.keys():
		return False
	return True

def retrieve(context,request):
	response = {}
	filter_dict = {}
	
	email_address = request.GET.get("email_address",None)
	contact_name = request.GET.get("contact_name",None)
	page_no = request.GET.get("page_no",1)
	limit_count = request.GET.get("page_size",10)

	if contact_name is not None:
		filter_dict['contact_name'] = contact_name
	if email_address is not None:
		filter_dict['email_address'] = email_address

	skip = limit_count*(int(page_no)-1)

	response['current_page'] = page_no
	response['limit_count'] = limit_count

	response['data'] = context.retrieve(filter_dict,limit_count,skip)
	response['total_records'] = context.retrieve_length(filter_dict)

	return response       

    