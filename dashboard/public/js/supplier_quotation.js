frappe.ui.form.on('Supplier Quotation', {
  onload: function(frm){
    var refresh = setInterval(function (){
      frm.events.atur_badge(frm);
    }, 2000);
  },
  atur_badge: function(frm){
    frappe.call({
      method: "procurement.procurement.reference.get_badge",
      args:{
        sq: frm.doc.name,
      },
      callback: function (data) {
        frm.set_value(data.message);
      }
    })
  },
  refresh: function(frm){
    if (frm.doc.docstatus == 0) {
      frm.trigger("make_dashboard");
    }
  },
  make_dashboard: function(frm) {
    if(frm.doc.__islocal)
			return;

		frm.dashboard.refresh();
		const timer = `
			<div class="stopwatch" style="font-weight:bold">
        <span class="days">00</span>
        <span class="colon">days, </span>
				<span class="hours">00</span>
				<span class="colon">hours, </span>
				<span class="minutes">00</span>
				<span class="colon">minutes, </span>
				<span class="seconds">00</span>
        <span class="colon">seconds</span>
			</div>`;

		var section = frm.dashboard.add_section(timer);

		if (frm.doc.start_time && frm.doc.stop_time) {
			// let currentIncrement = moment(frappe.datetime.now_datetime()).diff(moment(frm.doc.start_time),"seconds");
      let currentIncrement = moment(frm.doc.stop_time).diff(moment(frappe.datetime.now_datetime()),"seconds");
			initialiseTimer();

			function initialiseTimer() {
				const interval = setInterval(function() {
					var current = setCurrentIncrement();
					updateStopwatch(current);
				}, 1000);
			}

			function updateStopwatch(increment) {
        var days = Math.floor(increment / 86400);
				var hours = Math.floor((increment - (days * 86400)) / 3600);
				var minutes = Math.floor((increment - (days * 86400) - (hours * 3600)) / 60);
				var seconds = increment - (days * 86400) - (hours * 3600) - (minutes * 60);

        if(Math.round(increment) >= 1){
          $(section).find(".days").text(days < 10 ? ("0" + days.toString()) : days.toString());
          $(section).find(".hours").text(hours < 10 ? ("0" + hours.toString()) : hours.toString());
  				$(section).find(".minutes").text(minutes < 10 ? ("0" + minutes.toString()) : minutes.toString());
  				$(section).find(".seconds").text(seconds < 10 ? ("0" + seconds.toString()) : seconds.toString());
        }else{
          $(section).find(".days").text('00');
          $(section).find(".hours").text('00');
  				$(section).find(".minutes").text('00');
  				$(section).find(".seconds").text('00');
        }
			}

			function setCurrentIncrement() {
				currentIncrement -= 1;
				return currentIncrement;
			}
    }
  },
  material_request: function(frm){
    if(frm.doc.material_request){
      frappe.call({
        method: "frappe.client.get",
        args: {
          doctype: "Material Request",
          filters:{
            name: frm.doc.material_request,
          }
        },
        callback: function (data) {
          if (data.message){
            frm.set_value("start_time", data.message.start_time);
            frm.set_value("stop_time", data.message.stop_time);
          }else{
            frm.set_value("start_time", "");
            frm.set_value("stop_time", "");
          }
        }
      })
    }else{
      frm.set_value("start_time", "");
      frm.set_value("stop_time", "");
    }
  }

})
