var str = "China";

var body = d3.select("body");
var p = body.selectAll("p");

p.datum(str);

p.text(function(d, i){
    return "第 "+ i + " 个元素绑定的数据是 " + d;
});

body.append("p")
    .text("append p element");

body.insert("p","#main")
  .text("insert p element");

var width = 300;  //画布的宽度
var height = 300;   //画布的高度

var svg = d3.select("body")     //选择文档中的body元素
    .append("svg")          //添加一个svg元素
    .attr("width", width)       //设定宽度
    .attr("height", height);    //设定高度

var dataset = [ 250 , 210 , 170 , 130 , 90 ];
