from frappe import _

def get_data():
	return [
		{
			"label": _("HR Training Section"),
			"icon": "fa fa-print",
			"items": [
				{
					"type": "report",
					"name": "Training Summary",
					"is_query_report": True,
					"route": "query-report/Training Summary",
					"description": _("Training Summary Report.")
				},
				{
					"type": "report",
					"name": "Training Detail",
					"is_query_report": True,
					"route": "query-report/Training Detail",
					"description": _("Training Detail Report.")
				}
			]
		}
    ]
