frappe.ui.form.on('Asset Repair', {
  barcode: function(frm){
    if(frm.doc.barcode){
      frappe.call({
  			method: "dashboard.dashboard.reference.get_asset_barcode",
        args:{
          bcode: frm.doc.barcode
        },
  			callback: function(r) {
          if(r.message) {
            frm.set_value(r.message);
            frm.set_value("barcode_image", "");
            refresh_field("barcode_image");
          }
  			}
  		});
      frappe.call({
  			method: "dashboard.dashboard.reference.get_asset_detail",
        args:{
          bcode: frm.doc.barcode
        },
  			callback: function(r) {
          if(r.message) {
            frm.set_value(r.message);
          }
  			}
  		});
    }
  }
})
