# Copyright (c) 2025, XYZ and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Article(Document):
	pass

def get_permission_query_conditions(user):
	roles=frappe.get_roles(user)
	if "Librarian" in roles:
		return """(`tabArticle`.`status` = 'Issued' OR `tabArticle`.`status` = 'Available')"""
	elif "Lib2" in roles:
		return """(`tabArticle`.`status` = 'Issued')"""
	elif "Student" in roles:
		return """(`tabArticle`.`status` = 'Available')"""

	return None

def has_permission(doc, ptype, user):
	roles=frappe.get_roles(user)
	if "Librarian" in roles and (doc.status == "Issued" or doc.status == "Available"):
		return True	
	elif "Lib2" in roles and doc.status == "Issued":
		return True	
	elif "Student" in roles and doc.status == "Available":
		return True
	
	return False

def get_context(context):
    # context.doc will contain the Article record
    context.article_name = context.doc.article_name
    context.isbn = context.doc.isbn
