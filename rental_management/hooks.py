from . import __version__ as app_version

app_name = "rental_management"
app_title = "Rental Management"
app_publisher = "Fadil"
app_description = "Manages rental of a business"
app_email = "fadilsiddique@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/rental_management/css/rental_management.css"
# app_include_js = "/assets/rental_management/js/rental_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/rental_management/css/rental_management.css"
# web_include_js = "/assets/rental_management/js/rental_management.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "rental_management/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "rental_management.utils.jinja_methods",
#	"filters": "rental_management.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "rental_management.install.before_install"
# after_install = "rental_management.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "rental_management.uninstall.before_uninstall"
# after_uninstall = "rental_management.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "rental_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"rental_management.tasks.all"
#	],
#	"daily": [
#		"rental_management.tasks.daily"
#	],
#	"hourly": [
#		"rental_management.tasks.hourly"
#	],
#	"weekly": [
#		"rental_management.tasks.weekly"
#	],
#	"monthly": [
#		"rental_management.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "rental_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "rental_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "rental_management.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["rental_management.utils.before_request"]
# after_request = ["rental_management.utils.after_request"]

# Job Events
# ----------
# before_job = ["rental_management.utils.before_job"]
# after_job = ["rental_management.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"rental_management.auth.validate"
# ]
