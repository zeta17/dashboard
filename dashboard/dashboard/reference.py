from __future__ import unicode_literals
import frappe
from frappe.utils import flt, fmt_money, get_url
from frappe import msgprint, _
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

@frappe.whitelist()
def get_asset_barcode_for_asset_movement(bcode, type):
    if frappe.db.exists("Asset", {"barcode":bcode}):
        asset, barcode_link = frappe.db.get_value("Asset", {"barcode":bcode}, ["name", "barcode_link"])
        aa = {
            'asset': asset,
            'barcode_link': barcode_link
        }
        return aa
    else:
        frappe.throw(_("Barcode not identified"))

@frappe.whitelist()
def get_asset_barcode(bcode):
    if frappe.db.exists("Asset", {"barcode":bcode}):
        barcode_link = frappe.db.get_value("Asset", {"barcode":bcode}, "barcode_link")
        barcode = {
            'barcode_link': barcode_link
        }
        return barcode
    else:
        frappe.throw(_("Barcode not identified"))

@frappe.whitelist()
def get_asset_detail(bcode):
    if frappe.db.exists("Asset", {"barcode":bcode}):
        asset = frappe.db.get_value("Asset", {"barcode":bcode}, "name")
        detail = {
            'asset_name': asset,
            'asset_category': frappe.db.get_value("Asset", asset, "asset_category"),
            'item_code': frappe.db.get_value("Asset", asset, "item_code"),
            'item_name': frappe.db.get_value("Asset", asset, "item_name")
        }
        return detail

@frappe.whitelist()
def get_badge(sq):
    if frappe.db.exists("Supplier Quotation", sq):
        badge = frappe.db.sql("""select badge from `tabSupplier Quotation` where `name` = %s""", sq)[0][0]
        aa = {
            'badge': badge
        }
    else:
        aa = {
            'badge': ''
        }
    return aa
