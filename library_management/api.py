import frappe

@frappe.whitelist()
def get_name():
    return "This is working"

@frappe.whitelist()
def hello(name):
    return f"Hello, {name}!"

# GET Person by name
@frappe.whitelist()
def get_person(person_id):
    if not person_id:
        frappe.throw("Missing person_id")

    doc = frappe.get_doc("Person", person_id)
    return {
        "first_name": doc.first_name,
        "last_name": doc.last_name,
        "age": doc.age
    }

# POST to create a new Person
@frappe.whitelist(allow_guest=False)
def create_person():
    data = frappe.form_dict

    # Validate required fields
    for field in ["first_name", "last_name", "age"]:
        if not data.get(field):
            frappe.throw(f"Missing field: {field}")

    doc = frappe.get_doc({
        "doctype": "Person",
        "first_name": data.first_name,
        "last_name": data.last_name,
        "age": data.age
    })
    doc.insert()
    return {"message": "Person created", "name": doc.name}