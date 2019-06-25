frappe.pages['user-dashboard'].on_page_load = function(wrapper) {
	var me = this;
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'User Dashboard',
		single_column: true
	});

	setTimeout(
		function () {
			graph.draw(!0),
			graph2.draw(!0),
			chat3.draw(!0)
		}, 1
	);

	this.elements = {
		refresh_btn: wrapper.page.set_primary_action(__("Refresh"),
			function() { me.get_data(); }, "fa fa-refresh"),
	};
	this.elements.refresh_btn.on("click", function() {
		me.get_data(this);
	});

	var $container = $(`
		<div class="form-layout">
			<div class="form-page">
				<div class="row form-section visible-section shaded-section">
					<h2>Welcome</h2>
					<div class="task" style="float:left; width:50%; padding-right:10px"></div>
					<div class="sales_order" style="float:left; width:50%; padding-left:10px"></div>
					<div class="delivery_note" style="float:left; width:50%; padding-right:10px"></div>
					<div class="sales_invoice" style="float:left; width:50%; padding-left:10px"></div>
					<div class="chart" style="float:left; width:50%; padding-right:10px"></div>
					<div class="chart2" style="float:right; width:50%; padding-left:10px"></div>
					<div class="chart3" style="float:left; width:50%; padding-right:10px"></div>
				</div>
			</div>
		</div>
	`).appendTo(me.page.main);

	frappe.call({
		method: "dashboard.dashboard.page.user_dashboard.user_dashboard.get_task",
		callback: function(r) {
			if(r.message) {
				$container.find(".task").html(r.message);
			}
		}
	})

	frappe.call({
		method: "dashboard.dashboard.page.user_dashboard.user_dashboard.get_sales_order",
		callback: function(r) {
			if(r.message) {
				$container.find(".sales_order").html(r.message);
			}
		}
	})

	delivery_note = "\
		<h4>Your open Delivery</h4>\
		<table class='table table-bordered table-hover'>\
			<thead>\
				<tr>\
					<th class='text-left'>No Document</th>\
					<th class='text-left'>Customer</th>\
					<th class='text-left'>Delivery Date</th>\
					<th class='text-right'>Grand Total</th>\
				</tr>\
			</thead>\
			<tbody>\
				<tr>\
					<td>DN-2019-00004</td>\
					<td>Indosat Ooredoo</td>\
					<td>29 Mei 2019</td>\
					<td class='text-right'>4.648.780</td>\
				</tr>\
				<tr>\
					<td>DN-2019-00006</td>\
					<td>Mitra Adiperkasa, PT</td>\
					<td>29 Mei 2019</td>\
					<td class='text-right'>9.254.360</td>\
				</tr>\
			</tbody>\
		</table>"
	$container.find(".delivery_note").html(delivery_note);

	sales_invoice = "\
		<h4>Your open Sales Invoice</h4>\
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
				<tr>\
					<td>SINV-201900054</td>\
					<td>Bumi Resources</td>\
					<td>28 Mei 2019</td>\
					<td class='text-right'>31.210.500</td>\
				</tr>\
				<tr>\
					<td>SINV-201900069</td>\
					<td>Golden Toy's</td>\
					<td>29 Mei 2019</td>\
					<td class='text-right'>4.958.094</td>\
				</tr>\
			</tbody>\
		</table>"
	$container.find(".sales_invoice").html(sales_invoice);

	var chart1_label = [];
	frappe.call({
		method: "dashboard.dashboard.page.user_dashboard.user_dashboard.get_chart",
		callback: function(r) {
			if(r.message) {
				chart1_label = r.message.lable;
			}
		}
	})

	const chart_data = {
		labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
		datasets: [
			{
					values:['0','10','20','30','40','50','60','70','50','40','30','20']
			}
		]
	};
	const graph = new Chart(".chart", {
		data: chart_data,
		type: 'line',
		height: 250,
		title: "Buying"
	})

	const chart_data2 = {
		labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'],
		datasets: [
			{
				name: "Some Data", chartType: 'bar',
				values:[25, 40, 30, 35, 8, 52, 17, -4]
			},
			{
				name: "Another Set", chartType: 'bar',
				values:[25, 50, -10, 15, 18, 32, 27, 14]
			},
			{
				name: "Yet Another", chartType: 'line',
				values:[15, 20, -3, -15, 58, 12, -17, 37]
			}
		]
	};
	const graph2 = new Chart(".chart2", {
		data: chart_data2,
		type: 'axis-mixed',
		height: 250,
		title: "My Awesome Chart",
		colors: ['purple', '#ffa3ef', 'light-blue']
	})

	const chart3 = new Chart(".chart3", {
		type: 'percentage',
		data: {
			labels: ["Januari", "Februari", "Maret", "April", "May", "June"],
			datasets: [{
				label: "Data Set",
				borderColor: "white",
				values:[25, 40, 30, 35, 8, 52, 17]
			}]
		},
		colors: ["orange", "blue", "purple", "yellow", "aqua", "green"],
		height: 250,
	});

}
