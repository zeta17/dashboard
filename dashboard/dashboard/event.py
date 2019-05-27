from __future__ import unicode_literals
import frappe
from frappe.utils import nowdate, cstr, flt, now, getdate, add_months, fmt_money
from frappe import msgprint, _
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

@frappe.whitelist()
def redirect():
    pass
    # frappe.set_route("List", "Sales Invoice")
    # tp = frappe.new_doc("Temporary")
    # tp.temporary_name = "coba"
    # tp.flags.ignore_permissions = True
    # tp.submit()
    # return {"redirect_to": "http://192.168.16.116:8000/desk#user-dashboard"}
    # frappe.redirect_to_message(_('Some information is missing'))
    # frappe.local.flags.redirect_location = "/contact"
    # raise frappe.Redirect
    # frappe.msgprint(_("redirect"))
