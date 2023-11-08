import frappe

@frappe.whitelist()
def get_retailers():
	cust_list = frappe.get_list('Customer')
	data = []
	for row in cust_list:
		cust_doc = frappe.get_doc('Customer', row['name'])
		parent_cg = frappe.db.get_value('Customer Group', cust_doc.customer_group, 'parent_customer_group')
		if not parent_cg == 'Distributors':
			addr = frappe.db.get_value('Dynamic Link', {'link_doctype': 'Customer',
			'link_name': cust_doc.name, 'parenttype': 'Address'}, 'parent')
			contact = frappe.db.get_value('Dynamic Link', {'link_doctype': 'Customer',
			'link_name': cust_doc.name, 'parenttype': 'Contact'}, 'parent')
			data_set = {
				"syncId": cust_doc.name,
				"creation": cust_doc.creation,
				"modified": cust_doc.modified,
				"customer_name": cust_doc.customer_name,
				"customer_group": cust_doc.customer_group,
				"customer_type": "Retailer",                                                                                                                                                     
				"area": cust_doc.beat,                                     
				"gstin": cust_doc.gstin,
				"pan": cust_doc.pan,
				"gst_category": cust_doc.gst_category,
				"dob": cust_doc.posa_birthday,
				"country": None,
				"state": None,
				"city": None,
				"pincode": None,
				"address1": None,
				"address2": None,
				"fax": None,
				"email_id": None,
				"mobile_no": None,
				"company": None,
				"credit_limit": None
				}
			if addr:
				addr_doc = frappe.get_doc('Address', addr)
				data_set['country'] = addr_doc.country
				data_set['state'] = addr_doc.state
				data_set['city'] = addr_doc.city
				data_set['pincode'] = addr_doc.pincode
				data_set['address1'] = addr_doc.address_line1
				data_set['address2'] = addr_doc.address_line2
				data_set['fax'] = addr_doc.fax
			if contact:
				contact_doc = frappe.get_doc('Contact', contact)
				data_set['email_id'] = contact_doc.email_id
				data_set['mobile_no'] = contact_doc.mobile_no
			for limit in cust_doc.credit_limits:
				data_set['company'] = limit.company
				data_set['credit_limit'] = limit.credit_limit
			data.append(data_set)
	return data


@frappe.whitelist()
def get_distributors():
	cust_list = frappe.get_list('Customer')
	data = []
	for row in cust_list:
		cust_doc = frappe.get_doc('Customer', row['name'])
		parent_cg = frappe.db.get_value('Customer Group', cust_doc.customer_group, 'parent_customer_group')
		if parent_cg == 'Distributors':
			addr = frappe.db.get_value('Dynamic Link', {'link_doctype': 'Customer',
			'link_name': cust_doc.name, 'parenttype': 'Address'}, 'parent')
			contact = frappe.db.get_value('Dynamic Link', {'link_doctype': 'Customer',
			'link_name': cust_doc.name, 'parenttype': 'Contact'}, 'parent')
			data_set = {
				"syncId": cust_doc.name,
				"creation": cust_doc.creation,
				"modified": cust_doc.modified,
				"customer_name": cust_doc.customer_name,
				"customer_group": cust_doc.customer_group,
				"customer_type": "Distributor",                                                                                                                                                     
				"area": cust_doc.beat,                                     
				"gstin": cust_doc.gstin,
				"pan": cust_doc.pan,
				"gst_category": cust_doc.gst_category,
				"dob": cust_doc.posa_birthday,
				"country": None,
				"state": None,
				"city": None,
				"pincode": None,
				"address1": None,
				"address2": None,
				"fax": None,
				"email_id": None,
				"mobile_no": None,
				"company": None,
				"credit_limit": None
				}
			if addr:
				addr_doc = frappe.get_doc('Address', addr)
				data_set['country'] = addr_doc.country
				data_set['state'] = addr_doc.state
				data_set['city'] = addr_doc.city
				data_set['pincode'] = addr_doc.pincode
				data_set['address1'] = addr_doc.address_line1
				data_set['address2'] = addr_doc.address_line2
				data_set['fax'] = addr_doc.fax
			if contact:
				contact_doc = frappe.get_doc('Contact', contact)
				data_set['email_id'] = contact_doc.email_id
				data_set['mobile_no'] = contact_doc.mobile_no
			for limit in cust_doc.credit_limits:
				data_set['company'] = limit.company
				data_set['credit_limit'] = limit.credit_limit
			data.append(data_set)
	return data





@frappe.whitelist()
def get_item_groups():
	
	fields = ['name','creation','modified',
	'item_group_name','parent_item_group',
	'name as SyncId']

	number_fields = ['disabled']

	item_groups = frappe.db.get_values("Item Group",{},fields,as_dict=True)

	for itm in item_groups:
		for fld in number_fields:
			if fld in itm:
				itm[fld] = int(itm[fld])
		itm['disabled'] = 0
		itm['doctype'] = 'Item Group'

	return item_groups

