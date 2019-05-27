from __future__ import unicode_literals
import frappe
from frappe.utils import nowdate, cstr, flt, now
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
