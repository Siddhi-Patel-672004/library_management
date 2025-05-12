# Copyright (c) 2025, XYZ and contributors
# For license information, please see license.txt

import frappe

# def execute(filters=None):
#     # Default filters if none are provided
#     if filters is None:
#         filters = {}

#     # Query with the provided filters
#     data = frappe.get_all('Person', fields=["first_name", "last_name", "age"], filters=filters)
    
#     # Return data to be displayed in the report
#     return data
def execute(filters=None):
	# columns, data = [], []
	columns = [
        {"label": "First Name", "fieldname": "first_name", "fieldtype": "Data", "width": 150},
        {"label": "Last Name", "fieldname": "last_name", "fieldtype": "Data", "width": 150},
        # {"label": "Age", "fieldname": "age", "fieldtype": "Int", "width": 80},
    ]
	data = frappe.get_all("Person", fields=["first_name", "last_name"],filters=filters)

	return columns, data
    