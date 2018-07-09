    frappe.query_reports["Training Detail"] = {
        "filters": [
            {
                "fieldname":"from_date",
                "label": __("From Date"),
                "fieldtype": "Date",
                "default": frappe.defaults.get_user_default("year_start_date"),
                "width": "80"
            },
            {
                "fieldname":"to_date",
                "label": __("To Date"),
                "fieldtype": "Date",
                "default": frappe.datetime.get_today()
            },

        ]
    }
