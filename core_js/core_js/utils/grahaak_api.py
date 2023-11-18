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
			if cust_doc.beat:
				territory_type = frappe.db.get_value('Territory', cust_doc.beat, 'territory_type')
				if territory_type == "Area":
					city = frappe.db.get_value('Territory', cust_doc.beat, 'parent_territory')
					if city:
						city_territory_type = frappe.db.get_value('Territory', city, 'territory_type')
						if city_territory_type == "City":
							data_set['city'] = city
							state = frappe.db.get_value('Territory', city, 'parent_territory')
							if state:
								state_territory_type = frappe.db.get_value('Territory', state, 'territory_type')
								if state_territory_type == "State":
									data_set['state'] = state
									country = frappe.db.get_value('Territory', state, 'parent_territory')
									if country:
										country_territory_type = frappe.db.get_value('Territory', country, 'territory_type')
										if country_territory_type == "Country":
											data_set['country'] = country
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
			if cust_doc.beat:
				territory_type = frappe.db.get_value('Territory', cust_doc.beat, 'territory_type')
				if territory_type == "Area":
					city = frappe.db.get_value('Territory', cust_doc.beat, 'parent_territory')
					if city:
						city_territory_type = frappe.db.get_value('Territory', city, 'territory_type')
						if city_territory_type == "City":
							data_set['city'] = city
							state = frappe.db.get_value('Territory', city, 'parent_territory')
							if state:
								state_territory_type = frappe.db.get_value('Territory', state, 'territory_type')
								if state_territory_type == "State":
									data_set['state'] = state
									country = frappe.db.get_value('Territory', state, 'parent_territory')
									if country:
										country_territory_type = frappe.db.get_value('Territory', country, 'territory_type')
										if country_territory_type == "Country":
											data_set['country'] = country
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




def update_prices(item_doc,itm):
	mrp = frappe.db.get_value("Item Price",{'item_code':item_doc.item_code,
												'price_list':'MRP'},'price_list_rate')
	itm['mrp'] = mrp or 0

	distributors = frappe.db.get_all('Customer Group',{'parent_customer_group':'Distributors'})
	distributors = [d.get('name') for d in distributors]
	price_lists = frappe.get_all('Item Price',{'item_code':item_doc.item_code},['price_list','price_list_rate'],order_by='modified')
	dp = 0
	rp = 0
	for price_list in price_lists:
		if price_list.get('price_list') in distributors:
			dp = price_list.get('price_list_rate')
			break
		rp = price_list.get('price_list_rate')

	itm['dp'] = dp
	itm['rp'] = rp


def update_taxes(item_doc,itm):
	item_taxes = item_doc.taxes
	igst = 0
	cgst = 0
	sgst = 0
	gst = 0

	for row in item_taxes:
		item_tax_template = row.item_tax_template
		gst = int(''.join(filter(str.isdigit, item_tax_template))) or 0
		item_tax_template_doc = frappe.get_doc('Item Tax Template',item_tax_template)
		for tax_row in item_tax_template_doc.taxes:
			tax_type = tax_row.tax_type
			if tax_type.lower().startswith('output'):
				if 'igst' in tax_type.lower():
					igst = tax_row.tax_rate
				if 'cgst' in tax_type.lower():
					cgst = tax_row.tax_rate
				if 'sgst' in tax_type.lower():
					sgst = tax_row.tax_rate

	itm.update({'gst':gst,'igst':igst,'cgst':cgst,'sgst':sgst})



@frappe.whitelist()
def get_items():
	
	fields = ['name','creation','modified',
	'item_code','item_name','item_group','gst_hsn_code',
	'disabled','description','stock_uom as base_unit']

	number_fields = ['disabled']

	items = frappe.db.get_values("Item",{},fields,as_dict=True)

	for itm in items:
		itm['doctype'] = 'Item'
		item_group = itm.get('item_group','')
		item_segment = frappe.db.get_value('Item Group',{'name':item_group},'parent_item_group')
		itm['item_segment'] = item_segment

		item_doc = frappe.get_doc('Item',itm.get('name'))
		uoms = item_doc.uoms
		uom_keys = ['primary_unit','secondary_unit']
		for idx,uom_key in enumerate(uom_keys):
			if idx < len(uoms) -1:
				itm[uom_key] = uoms[idx].uom
			else:
				itm[uom_key] = None

		for fld in number_fields:
			if fld in itm:
				itm[fld] = int(itm[fld])


		
		update_taxes(item_doc,itm)
		update_prices(item_doc,itm)


	return items

@frappe.whitelist()
def get_distributorwise_item_price():
	final_list = []
	distributor_list = frappe.get_list("Customer Group", 
						{
							"parent_customer_group": "Distributors"
						})
	for distributor in distributor_list:	
		distributor_name_list = frappe.get_list("Customer", {"customer_group": distributor['name']})

		for distributor_name in distributor_name_list:
			item_price_list = frappe.get_list("Item Price", {
			"price_list": distributor['name'],
			"selling": 1
			})
			for item_price in item_price_list:
				item_price_doc = frappe.get_doc("Item Price", item_price['name'])
				mrp = frappe.db.get_value("Item Price", 
				{'item_code':item_price_doc.item_code,
				"price_list": "MRP",
				"selling": 1}, "price_list_rate")
				final_list.append(
					{
					"sync_id": item_price_doc.name,
					"creation": item_price_doc.creation,
					"modified": item_price_doc.modified,
					"distributor_name": distributor_name['name'],
					"customer_group": distributor['name'],       
					"item_name": item_price_doc.item_name,
					"mrp": mrp if mrp else 0.0,
					"dp": item_price_doc.price_list_rate,
					"rp": 0.0
				}
				)
	return final_list