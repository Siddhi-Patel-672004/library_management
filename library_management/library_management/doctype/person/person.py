# Copyright (c) 2025, XYZ and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class Person(WebsiteGenerator):
	# pass
	def before_insert(self):
		self.full_name = f"{self.first_name} {self.last_name or ''}"

	# def before_validate(self):
	# 	frappe.msgprint("This is a before_validate method")
	
	def validate(self):
		if int(self.age)<=18:
			# frappe.msgprint("Person's age must be greater than 18")
			frappe.throw("Person's age must be greater than 18")

	def get_full_name(self):
		return f"{self.first_name} {self.last_name or ''}"
	
	"""
	def create_person(first_name, last_name, age):
		person = frappe.get_doc({
			"doctype": "Person",
			"first_name": first_name,
			"last_name": last_name,
			"age": age
		})
		person.insert()  # Saves the document to the database
		frappe.db.commit()  # Optional but good for scripts and batch jobs
		return person.name
	"""
	# def before_save(self):
	# 	frappe.msgprint("This is a before_save method")

def get_context(context):
   context.full_name = f"{context.doc.first_name} {context.doc.last_name}"