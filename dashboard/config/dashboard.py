from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
        {
			"label": _("Report"),
			"items": [
				{
					"type": "page",
					"name": "asset-dashboard",
					"label": _("Asset Dashboard"),
					"icon": "fa fa-bar-chart",
				},
				{
					"type": "page",
					"name": "user-dashboard",
					"label": _("User Dashboard"),
					"icon": "fa fa-bar-chart",
				},
            ]
        }
    ]
