from __future__ import unicode_literals
import frappe, urllib2
from frappe.utils import flt, fmt_money, get_url, now_datetime, get_datetime
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

def submit_asset(doc, method):
    doc.db_set("book_value", doc.gross_purchase_amount)

def sum_amount_asset(doc, method):
    for row in doc.accounts:
        if row.reference_type == "Asset":
            sum_amount_credit = frappe.db.sql("""select sum(credit) from `tabJournal Entry Account` where docstatus = '1' and reference_type = 'Asset' and reference_name = %s""", row.reference_name)[0][0]
            gross_purchase_amount = frappe.db.get_value("Asset", row.reference_name, "gross_purchase_amount")
            book_value = flt(gross_purchase_amount - sum_amount_credit)
            frappe.db.set_value("Asset", row.reference_name, "book_value", book_value)

def validate_material_request(doc, method):
    if doc.start_time or doc.stop_time:
        if doc.stop_time < doc.start_time:
            frappe.throw(_("<b>Start Time</b> must be less than <b>Stop Time</b>"))

def validate_sq_timer(doc, method):
    if now_datetime() > get_datetime(doc.stop_time):
        frappe.throw(_("Tender time is up"))

def validate_sq_badge(doc, method):
    if doc.material_request:
        grand_total_another_sq = frappe.db.sql("""select count(*) from `tabSupplier Quotation` where docstatus != '2' and material_request = %s and `name` != %s and grand_total < %s""", (doc.material_request, doc.name, doc.grand_total))[0][0]
        if flt(grand_total_another_sq) == 0:
            doc.badge = "menang"
            frappe.db.sql("""update `tabSupplier Quotation` set badge = 'kalah' where docstatus != '2' and material_request = %s and `name` != %s""", (doc.material_request, doc.name))
        else:
            doc.badge = "kalah"

@frappe.whitelist()
def download_file():
    import urllib2
    filedata = urllib2.urlopen('https://barcode.tec-it.com/barcode.ashx?data=1400079&code=Code128&dpi=150')
    datatowrite = filedata.read()

    with open('/home/frappe/frappe-bench/sites/erpnext.vm/public/files/1400079.png', 'wb') as f:
        f.write(datatowrite)

@frappe.whitelist()
def excel():
    import xlsxwriter

    workbook = xlsxwriter.Workbook(frappe.get_site_path("public", "files", "hello.xlsx"))
    # workbook = xlsxwriter.Workbook('/home/frappe/frappe-bench/sites/erpnext.vm/public/files/hello.xlsx')
    worksheet = workbook.add_worksheet()

    # Widen the first column to make the text clearer.
    worksheet.set_column('A:A', 20)
    worksheet.set_column('B:B', 15)

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

    # Write some simple text.
    worksheet.write('A1', 'Hello')

    # Text with formatting.
    worksheet.write('A2', 'World', bold)

    # Write some numbers, with row/column notation.
    worksheet.write(2, 0, 123)
    worksheet.write(2, 1, 'Disini')
    worksheet.write(3, 0, 123.456)

    workbook.close()
