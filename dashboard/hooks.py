# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "dashboard"
app_title = "Dashboard"
app_publisher = "hendrik"
app_description = "User Dashboard"
app_icon = "fa fa-tachometer"
app_color = "red"
app_email = "hendrik.zeta@gmail.com"
app_license = "No Copy"

# Includes in <head>
# ------------------
fixtures = ["Custom Field"]
# include js, css files in header of desk.html
# app_include_css = "/assets/dashboard/css/dashboard.css"
app_include_css = "/assets/dashboard/css/custom.css"
# app_include_js = "/assets/dashboard/js/dashboard.js"

# include js, css files in header of web template
# web_include_css = "/assets/dashboard/css/dashboard.css"
# web_include_js = "/assets/dashboard/js/dashboard.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_js = {
    "Asset": "public/js/asset.js",
    "Asset Movement": "public/js/asset_movement.js",
    "Asset Maintenance": "public/js/asset_maintenance.js",
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------
on_login = "dashboard.dashboard.event.redirect"
# on_session_creation = [
# 	"dashboard.dashboard.event.redirect"
# ]


# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "dashboard.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "dashboard.install.before_install"
# after_install = "dashboard.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "dashboard.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events
doc_events = {
    "Asset": {
        "validate": [
            "dashboard.dashboard.event.update_asset_barcode",
        ]
    },
}
# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"dashboard.tasks.all"
# 	],
# 	"daily": [
# 		"dashboard.tasks.daily"
# 	],
# 	"hourly": [
# 		"dashboard.tasks.hourly"
# 	],
# 	"weekly": [
# 		"dashboard.tasks.weekly"
# 	]
# 	"monthly": [
# 		"dashboard.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "dashboard.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "dashboard.event.get_events"
# }
