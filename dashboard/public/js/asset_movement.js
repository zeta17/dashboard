frappe.ui.form.on('Asset Movement', {
  barcode: function(frm){
    frappe.call({
			method: "dashboard.dashboard.reference.get_asset_barcode",
      args:{
        bcode: frm.doc.barcode
      },
			callback: function(r) {
        if(r.message) {
          frm.set_value(r.message);
          frm.refresh_fields();
        }
        frm.refresh_fields();
			}
		});
  }
})
