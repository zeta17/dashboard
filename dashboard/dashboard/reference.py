from __future__ import unicode_literals
import frappe
from frappe.utils import flt, fmt_money, get_url
from frappe import msgprint, _
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

@frappe.whitelist()
def get_asset_barcode(bcode, doctype):
    if frappe.db.exists("Asset", {"barcode":bcode}):
        asset, barcode_link, asset_category, item_code, item_name = frappe.db.get_value("Asset", {"barcode":bcode}, ["name", "barcode_link", "asset_category", "item_code", "item_name"])
        if doctype == "Asset Movement":
            aa = {
                'asset': asset,
                'barcode_link': barcode_link
            }
        else:
            aa = {
                'asset_name': asset,
                'barcode_link': barcode_link,
                'asset_category': asset_category,
                'item_code': item_code,
                'item_name': item_name
            }
        return aa
    else:
        frappe.throw(_("Barcode not identified"))
