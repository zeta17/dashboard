from __future__ import unicode_literals
import frappe
from frappe.utils import nowdate, cstr, flt, now, fmt_money
from frappe import msgprint, _
from frappe.model.document import Document


@frappe.whitelist()
def get_task():
    list = []
    if frappe.db.exists("Task", {"docstatus":"0"}):
        task = frappe.get_all("Task", filters={"docstatus":"0"}, fields=["*"], order_by="idx asc")
        for ta in task:
            tr = "<tr><td><a href='#Form/Task/{0}'>{0}</a></td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td></tr>".format(ta.name, ta.subject, ta.status, ta.priority, ta.exp_end_date.strftime("%-d %B %Y"))
            list.append(tr)
    else:
        tr = "<tr><td colspan='5' class='text-center'>No Data</td></tr>"
        list.append(tr)
    table = "<h4>You have Task</h4>\
    <table class='table table-bordered table-hover'>\
        <thead>\
            <tr>\
                <th class='text-left'>No Document</th>\
                <th class='text-left'>Subject</th>\
                <th class='text-left'>Status</th>\
                <th class='text-left'>Priority</th>\
                <th class='text-left'>Expected End Date</th>\
            </tr>\
        </thead>\
        <tbody>\
            {0}\
        </tbody>\
    </table>".format(tr)
    return table

@frappe.whitelist()
def get_sales_order():
    list = []
    if frappe.db.exists("Sales Order", {"docstatus":"0"}):
        sales_order = frappe.get_all("Sales Order", filters={"docstatus":"0"}, fields=["*"], order_by="idx asc")
        for so in sales_order:
            tr = "<tr><td><a href='#Form/Sales Order/{0}'>{0}</a></td><td><a href='#Form/Customer/{1}'>{1}</a></td><td>{2}</td><td class='text-right'>{3}</td></tr>".format(so.name, so.customer, so.transaction_date.strftime("%-d %B %Y"), fmt_money(so.grand_total))
            list.append(tr)
    else:
        tr = "<tr><td colspan='4' class='text-center'>No Data</td></tr>"
        list.append(tr)
    table = "<h4>Your open Sales Order</h4>\
    <table class='table table-bordered table-hover'>\
        <thead>\
            <tr>\
                <th class='text-left'>No Document</th>\
                <th class='text-left'>Customer</th>\
                <th class='text-left'>Date</th>\
                <th class='text-right'>Grand Total</th>\
            </tr>\
        </thead>\
        <tbody>\
            {0}\
        </tbody>\
    </table>".format(tr)
    return table

@frappe.whitelist()
def get_chart():
    list = {
        'lable': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        'value': ['0','10','20','30','40','50','60','70','50','40','30','20']
    }
    return list
