frappe.ui.form.on('Asset Maintenance', {
  barcode: function(frm){
    if(frm.doc.barcode){
      frappe.call({
  			method: "dashboard.dashboard.reference.get_asset_barcode",
        args:{
          bcode: frm.doc.barcode,
          doctype: frm.doc.doctype
        },
  			callback: function(r) {
          if(r.message) {
            frm.set_value(r.message);
            frm.set_value("barcode_image", "");
          }
          frm.refresh_fields('barcode_image');
  			}
  		});
    }
  }
})
