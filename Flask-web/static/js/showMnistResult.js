var margin = {top: 20, right: 20, bottom: 30, left: 40},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var x = d3.scale.linear()
    .range([0, width]);

var y = d3.scale.linear()
    .range([height, 0]);

//var color = d3.scale.category10();
value2color = {'#B40431':'识别率>90%','#0B610B':'识别率>89%','#0404B4':'识别率>88%','#819FF7':'识别率<88%'}
colorList = ['#B40431','#0B610B','#0404B4','#819FF7']
var color = function(data){
       if(data > 0.9){
        return colorList[0];
       }else if(data > 0.89){
        return colorList[1];
       }else if(data > 0.88){
        return colorList[2];
       }else{
        return colorList[3];}
}

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");

var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var format = function(d){
    //+ used to change the data from string to digit(int, float)
    d.epoch = +d.epoch;
    d.learning_rate = + d.learning_rate;
    d.result = +d.result;
    return d;
}

d3.csv("/static/data/testResult.csv", format, function(error, data) {
    //here foreach functions as the same of format function
    //same function as the format function, but when you call the json api, there is no format function
    dresultMax = data[10].result
    dresultMin = data[10].result
    data.forEach(function(d){
        d.epoch = +d.epoch;
        d.learning_rate = + d.learning_rate;
        d.result = +d.result;
        if(d.result < 0.5){
            return;
        }
        if(d.result > dresultMax){
           dresultMax = d.result;
        }else if(d.result < dresultMin){
           dresultMin = d.result;
        }
    });
    console.log(data);
    x.domain(d3.extent(data, function(d) { return d.epoch; })).nice();
    y.domain(d3.extent(data, function(d) { return d.learning_rate; })).nice();

    svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis)
    .append("text")
      .attr("class", "label")
      .attr("x", width)
      .attr("y", -6)
      .style("text-anchor", "end")
      .text("Epoch (times)");

    svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
    .append("text")
      .attr("class", "label")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Learning Rate");

    svg.selectAll(".dot")
      .data(data)
    .enter().append("circle")
      .attr("class", "dot")
      .attr("r", function(d) { dl = dresultMax - dresultMin; if(d.result < 0.5){return 0;}return (d.result-dresultMin)/dl*10; })
      .attr("cx", function(d) { return x(d.epoch); })
      .attr("cy", function(d) { return y(d.learning_rate); })
      .style("fill", function(d) {
            return color(d.result);
       });

    var legend = svg.selectAll(".legend")
      .data(colorList)
    .enter().append("g")
      .attr("class", "legend")
      .attr("transform", function(d, i) { return "translate(0," + i * 25 + ")"; });

     console.log(legend)

    legend.append("rect")
      .attr("x", width - 18)
      .attr("width", 18)
      .attr("height", 18)
      .style("fill", function(d) { return d; });

    legend.append("text")
      .attr("x", width - 24)
      .attr("y", 9)
      .attr("dy", ".35em")
      .style("text-anchor", "end")
      .text(function(d) { return value2color[d]; });

})