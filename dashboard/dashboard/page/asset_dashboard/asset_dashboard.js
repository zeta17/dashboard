frappe.pages['asset-dashboard'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Asset Dashboard',
		single_column: true
	});

	frappe.breadcrumbs.add("Dashboard");

	wrapper.asset_dashboard = new erpnext.AssetDashboard(wrapper);
}
erpnext.AssetDashboard = class AssetDashboard {
	constructor(wrapper) {
		var me = this;
		setTimeout(function() {
			me.setup(wrapper);
			me.get_data();
		}, 0);
	}

	setup(wrapper) {
		var me = this;

		this.elements = {
			layout: $(wrapper).find(".layout-main"),
			main_section: $(wrapper).find(".layout-main-section"),
			fiscal_year: wrapper.page.add_field({
				fieldname: 'excel',
				label: __('Excel'),
				fieldtype: 'Button',
				click: function() {
					me.get_excel();
				}
			}),
			refresh_btn: wrapper.page.set_primary_action(__("Refresh"), function() {
				me.get_data();
			}, "fa fa-refresh"),
		};
		this.elements.asset_wrapper = $('<div class="asset-wrapper"></div>')
			.appendTo(this.elements.main_section);

		this.elements.asset_wrapper_1 = $('<div class="asset-wrapper-1"></div>')
			.appendTo(this.elements.asset_wrapper);

		this.options = {};
	}

	get_data() {
		var me = this;

		frappe.call({
			method: "dashboard.dashboard.page.asset_dashboard.asset_dashboard.get_chart_asset",
			callback: function(r) {
				if(!r.exc) {
					me.options.data_monthly = r.message;
					me.chart_monthly();
				}
			}
		});
	}

	chart_monthly(){
		let me = this;

		let chart_data = me.options.data_monthly ? me.options.data_monthly : null;

		const parent = me.elements.asset_wrapper_1[0];

		this.chart = new Chart(parent, {
			// title: __("Monthly"),
			height: 250,
			data: chart_data,
			type: 'axis-mixed',
		})
	}

	get_excel(){
		var me = this;

		frappe.call({
			method: "dashboard.dashboard.page.asset_dashboard.asset_dashboard.set_asset_excel",
			callback: function(r) {
				if(!r.exc) {
					// me.options.data_monthly = r.message;
					me.export_excel(r.message);
				}
			}
		});
		// var file_url = "/files/asset_list_20190704231013.xlsx";
		// file_url = file_url.replace(/#/g, '%23');
		// window.open(file_url);
	}

	export_excel(filepath){
		let me = this;

		var file_url = filepath;
		file_url = file_url.replace(/#/g, '%23');
		window.open(file_url);
	}

}
