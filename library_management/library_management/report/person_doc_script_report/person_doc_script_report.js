// Copyright (c) 2025, XYZ and contributors
// For license information, please see license.txt

// frappe.query_reports["Person Doc Script REPORT"] = {
// 	"filters": [

// 	]
// };

// frappe.query_reports["Person Doc Script REPORT"] = {
//     "filters": [
//         {
//             "fieldname": "first_name",
//             "label": "First Name",
//             "fieldtype": "Data",
//             "reqd": 0
//         },
//         {
//             "fieldname": "age",
//             "label": "Age",
//             "fieldtype": "Int",
//             "default": 0,
//             "reqd": 0
//         }
//     ]
// };

frappe.query_reports['Person Doc Script REPORT'] = {
    filters: [
    {
    fieldname: 'first_name',
    label: __('First Name'),
    fieldtype: 'Data',
    options: '',
    default: ''
    },
    ]
   }

