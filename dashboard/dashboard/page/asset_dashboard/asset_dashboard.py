from __future__ import unicode_literals
import frappe
from frappe.utils import nowdate, cstr, flt, now, fmt_money
from frappe import msgprint, _
from frappe.model.document import Document

@frappe.whitelist()
def get_chart_asset():
    result = {}
    result['labels'] = []
    result['datasets'] = []
    for loc in frappe.get_all("Location", filters={"is_group":0}, fields=["*"], order_by="name asc"):
        result['labels'].append(loc.name)

    for row in frappe.get_all("Asset Category", fields=["*"], order_by="name asc"):
        count_asset = []
        for lok in frappe.get_all("Location", filters={"is_group":0}, fields=["*"], order_by="name asc"):
            count_asset_perlocation = frappe.db.sql("""select count(*) from `tabAsset` where docstatus = '1' and asset_category = %s and location = %s""", (row.name, lok.name))[0][0]
            count_asset.append(count_asset_perlocation)
        result['datasets'].append({'name': row.name, 'values': count_asset, 'chartType': 'bar'})
    return result

@frappe.whitelist()
def set_asset_excel():
    from datetime import datetime
    import xlsxwriter

    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    file_name = "asset_list_{0}.xlsx".format(timestamp)

    workbook = xlsxwriter.Workbook(frappe.get_site_path("public", "files", file_name))
    worksheet = workbook.add_worksheet()

    # Widen column.
    worksheet.set_column('A:A', 6)
    worksheet.set_column('B:B', 30)
    worksheet.set_column('C:C', 30)
    worksheet.set_column('D:D', 30)
    worksheet.set_column('E:E', 20)
    worksheet.set_column('F:F', 20)
    worksheet.set_column('G:G', 20)

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})
    money = workbook.add_format({'num_format': '#,##0'})

    # header.
    worksheet.write('A1', 'ASSET LIST', bold)

    worksheet.write('A3', 'NO', bold)
    worksheet.write('B3', 'ASSET NAME', bold)
    worksheet.write('C3', 'ITEM CODE', bold)
    worksheet.write('D3', 'ITEM NAME', bold)
    worksheet.write('E3', 'ASSET CATEGORY', bold)
    worksheet.write('F3', 'LOCATION', bold)
    worksheet.write('G3', 'AMOUNT', bold)

    # content
    count = flt(2)
    idx = flt(0)
    for row in frappe.get_all("Asset", fields=["*"]):
        count += 1
        idx += 1
        worksheet.write(int(count), 0, idx)
        worksheet.write(int(count), 1, row.name)
        worksheet.write(int(count), 2, row.item_code)
        worksheet.write(int(count), 3, 'tunjukkan')
        worksheet.write(int(count), 4, row.asset_category)
        worksheet.write(int(count), 5, row.location)
        worksheet.write(int(count), 6, row.gross_purchase_amount, money)

    workbook.close()
    file_path = "/files/{0}".format(file_name)
    return file_path
