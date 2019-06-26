frappe.ui.form.on('Asset Movement', {
  barcode: function(frm){
    if(frm.doc.barcode){
      frappe.call({
  			method: "dashboard.dashboard.reference.get_asset_barcode_for_asset_movement",
        args:{
          bcode: frm.doc.barcode,
          type: frm.doc.doctype
        },
  			callback: function(r) {
          if(r.message) {
            frm.set_value(r.message);
            frm.set_value("barcode_image", "");
            refresh_field("barcode_image");
          }
          // frm.refresh_fields('barcode_image');
  			}
  		});
    }
  }
})
