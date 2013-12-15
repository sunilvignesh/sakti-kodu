//Flot Line Chart with Tooltips
$(document).ready(function(){
	console.log("document ready");
	var offset = 0;
	plot();
	function plot(){
		var sin ={{headers.energy_dist}};
	
		var options = {
			series: {
				lines: { show: true },
				points: { show: true }
			},
			grid: {
				hoverable: true //IMPORTANT! this is needed for tooltip to work
			},
			yaxis: { min: -1.2, max: 1.2 },
			tooltip: true,
			tooltipOpts: {
				content: "'%s' of %x.1 is %y.4",
				shifts: {
					x: -60,
					y: 25
				}
			}
		};
	
		var plotObj = $.plot( $("#flot-chart-line"),
			[ { data: sin, label: "x-axis: Time in seconds, y-axis: Energy(kWh)"}],
			options );
	}
});



