var q = d3.queue()
.defer(d3.request, "/getData")
.defer(d3.request, "/test2")
.await(function(error,results,results2) {
  if (error) throw error;
  console.log(results);
  console.log(results2);
  output(results.responseText);
});

function output(data){
    console.log(data);
    console.log(new Date);
    //var parseTime = d3.timeParse("%B %d, %Y");
    console.log(parseTime("June 30, 2015"));
}

var svg = d3.select("svg"),
    margin = {top: 20, right: 20, bottom: 30, left: 50},
    width = +svg.attr("width") - margin.left - margin.right,
    height = +svg.attr("height") - margin.top - margin.bottom,
    g = svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var x = d3.scaleTime()
    .rangeRound([0, width]);

var y = d3.scaleLinear()
    .rangeRound([height, 0]);

var line = d3.line()
    .x(function(d) { return x(d.date); })
    .y(function(d) { return y(d.close); });




