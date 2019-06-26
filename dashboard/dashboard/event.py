from __future__ import unicode_literals
import frappe, urllib2
from frappe.utils import flt, fmt_money, get_url
from frappe import msgprint, _
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

@frappe.whitelist()
def redirect():
    pass
    # redirect_to = get_url("#Form/Sales Order/SAL-ORD-2019-00001")
    # return redirect_to
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

def update_asset_barcode(doc, method):
    if doc.barcode:
        filedata = urllib2.urlopen('https://barcode.tec-it.com/barcode.ashx?data='+doc.barcode+'&code=Code128&dpi=150')
        datatowrite = filedata.read()

        with open(frappe.get_site_path("public", "files", doc.barcode+".png"), 'wb') as f:
            f.write(datatowrite)
        barcode_link = "/files/"+doc.barcode+".png"
        doc.db_set("barcode_link", barcode_link)

@frappe.whitelist()
def download_file():
    import urllib2
    filedata = urllib2.urlopen('https://barcode.tec-it.com/barcode.ashx?data=1400079&code=Code128&dpi=150')
    datatowrite = filedata.read()

    with open('/home/frappe/frappe-bench/sites/erpnext.vm/public/files/1400079.png', 'wb') as f:
        f.write(datatowrite)
