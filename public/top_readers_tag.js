function drawBookList(csvPath) {
	$.ajax({
		url: csvPath,
		success: function(data) {
			var container = $('.book-list')
			$($.csv.toArrays(data)).each(function(index, row) {
				if(row[1] != undefined) {
					container.append("<li><a href='http://book.douban.com/subject/" + row[0] + "' target='_blank'>" + row[1] + "</a></li>")
				}
			})
		}
	});
}

var w = 960,
	h = 600;

function drawTagCloud(dataSource) {
	d3.json(dataSource, function(json) {
		var topReaders = readers(json).children.map(function(reader) {
			return {text: reader.nickName, size: reader.readCount * 5};
		});
	  	d3.layout.cloud().size([w, h])
	      .words(topReaders)
	      .rotate(function() { return ~~(Math.random() * 2) * 90; })
	      .fontSize(function(d) { return d.size; })
	      .on("end", draw)
	      .start();
	});	
}

function draw(data, bounds) {
  scale = bounds ? Math.min(
      w / Math.abs(bounds[1].x - w / 2),
      w / Math.abs(bounds[0].x - w / 2),
      h / Math.abs(bounds[1].y - h / 2),
      h / Math.abs(bounds[0].y - h / 2)) / 2 : 1;
  words = data;
	var svg = d3.select("body").append("svg")
	    .attr("width", w)
	    .attr("height", h);

	var vis = svg.append("g").attr("transform", "translate(" + [w >> 1, h >> 1] + ")");

  var text = vis.selectAll("text").data(words, function(d) { return d.text.toLowerCase(); });

  text.transition()
      .duration(1000)
      .attr("transform", function(d) { return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")"; })
      .style("font-size", function(d) { return d.size + "px"; })
  text.enter()
	  .append("text")
      .attr("text-anchor", "middle")
	  .attr("cursor", "pointer")
      .attr("transform", function(d) { return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")"; })
      .style("font-size", function(d) { return d.size + "px"; })
      .on("click", function(d) {
        window.open('http://www.douban.com/people/' + d.text)
      })
      .style("opacity", 1e-6)
    .transition()
      .duration(1000)
      .style("opacity", 1);
  text.style("font-family", function(d) { return d.font; })
	  .style("fill", function(d) { 
		document.inspect = d;
		var grayScale = 20 - d.size / 5;
		var grayValue = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'][grayScale]
		return '#bb' + grayValue + grayValue + grayValue + grayValue;
  	  })
      .text(function(d) { return d.text; });
  vis.transition()
      .delay(1000)
      .duration(750)
      .attr("transform", "translate(" + [w >> 1, h >> 1] + ")scale(" + scale + ")");
}

// Returns a flattened hierarchy containing all leaf nodes under the root.
function readers(root) {
  var readers = [];

  function recurse(name, node) {
    if (node.children) node.children.forEach(function(child) { recurse(node.name, child); });
    else readers.push({nickName: node.name, readCount: node.size});
  }

  recurse(null, root);
  return {children: readers};
}