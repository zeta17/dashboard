from __future__ import unicode_literals
import frappe
from frappe.utils import flt, fmt_money, get_url
from frappe import msgprint, _
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

@frappe.whitelist()
def get_asset_barcode(bcode):
    if frappe.db.exists("Asset", {"barcode":bcode}):
        asset, barcode_link = frappe.db.get_value("Asset", {"barcode":bcode}, ["name", "barcode_link"])
        aa = {
            'asset': asset,
            'barcode_link': barcode_link
        }
        return aa
    else:
        frappe.throw(_("Barcode not identified"))
