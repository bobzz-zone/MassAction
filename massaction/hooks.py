# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "massaction"
app_title = "Mass Action"
app_publisher = "bobzz.zone@gmail.com"
app_description = "To Do Mass Action"
app_icon = "octicon octicon-checklist"
app_color = "grey"
app_email = "bobzz.zone@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/massaction/css/massaction.css"
# app_include_js = "/assets/massaction/js/massaction.js"

# include js, css files in header of web template
# web_include_css = "/assets/massaction/css/massaction.css"
# web_include_js = "/assets/massaction/js/massaction.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "massaction.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "massaction.install.before_install"
# after_install = "massaction.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "massaction.notifications.get_notification_config"

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
# 		"massaction.tasks.all"
# 	],
# 	"daily": [
# 		"massaction.tasks.daily"
# 	],
# 	"hourly": [
# 		"massaction.tasks.hourly"
# 	],
# 	"weekly": [
# 		"massaction.tasks.weekly"
# 	]
# 	"monthly": [
# 		"massaction.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "massaction.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "massaction.event.get_events"
# }

