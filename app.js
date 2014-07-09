var IS_LOCAL = false;
if (window.location.protocol == 'file:') IS_LOCAL = true;

var SERVER_URL = "http://www.redflood.com:8080";
	
if (IS_LOCAL){
	SERVER_URL = "http://0.0.0.0:8080";
}

scene = new TDScene('canvas');

//Input
var dragging = false;
var shouldPan = false;
var lastX, lastY = 0;

function mouseDown(event){
	dragging = true;
	lastX = event.x;
	lastY = event.y;
}

function mouseMove(event){
	if (dragging){
		
		var diffX = (event.x - lastX);
		var diffY = (event.y - lastY);
		
		if (shouldPan){
			scene.translationX += diffX/scene.scale;
			scene.translationY += diffY/scene.scale;
		}else{
			scene.rotationHorizontal += diffX/100;
			scene.rotationVertical += diffY/100;

			console.log("Rotation x: " + scene.rotationX + " y: " + scene.rotationY + " z: " + scene.rotationZ);
		}
	}else{
        //highlight point that mouse is closest to
		var rect = scene.canvas.getBoundingClientRect();
		var mouseX = event.x - rect.left;
		var mouseY = event.y - rect.top;

        var closestPoint;
        var dist = 10;
        for (var i = 0; i < scene.points.length; i++){
            var point = scene.points[i];
			point.isTargeted = false;

            var testDist = Math.sqrt(Math.pow(point.flatX - mouseX, 2) + Math.pow(point.flatY - mouseY, 2));
            if (testDist < dist){
                dist = testDist;
                closestPoint = point;
            }
        }

        if (closestPoint){
			closestPoint.isTargeted = true;
        }
    }
	
	lastX = event.x;
	lastY = event.y;
}

function mouseUp(event){
	dragging = false;
}

function keyDown(event){
	if (event.keyCode == 91){ //left window aka command
		shouldPan = true;
	}
}

function keyUp(event){
	if (event.keyCode == 91){
		shouldPan = false;
	}
}

function mouseWheel(event){
	scene.scale += event.wheelDelta/-300;
}

scene.loop = function(){
	document.body.scrollTop = "0px";
}

// Cross-browser support for requestAnimationFrame
var w = window;
requestAnimationFrame = w.requestAnimationFrame || w.webkitRequestAnimationFrame || w.msRequestAnimationFrame || w.mozRequestAnimationFrame;

//Run it
$( document ).ready(function() {
	main();
	reloadNetworkData();
});

//Interface
$("#buttonRefresh").click(function(){
	reloadNetworkData();
});

$("#buttonRandomize").click(function(){
	$.post(SERVER_URL + "/randomize", function(){
		reloadNetworkData();
	});
});

$("#buttonCreate").click(function(){
	$.ajax({
		url: SERVER_URL + '/create',
		type: 'POST',
		data: {'size': $("#count").val()},
		success: function(){
			reloadNetworkData();
		}
	});
});

$("#buttonProcess").click(function(){
	processState()
});

$("#buttonRun").click(function(){
	isRunning = !isRunning;
	var color = '#FF0000';
	if (isRunning){
		processState();
		$("#buttonRun").text("Stop");
		color = '#0000FF';
	}else{
		showLoading(false);
		$("#buttonRun").text("Run");
	}

	$("#buttonRun").animate({backgroundColor:color}, 200);
});

//Network

var networkData = [];
var isRunning = false;

function reloadNetworkData()
{
	showLoading(true);

	$.ajax(SERVER_URL + "/data").done(function(data) {
		scene.clear();

		networkData = JSON.parse(data);

		showLoading(false);

		constructClientNetwork();

		console.log("Got data" + value);
	});
}

function constructClientNetwork(){
	for (var i = 0; i < networkData.length; i++)
	{
		var neuron = networkData[i];
		var nextNeuron;
		if (i < networkData.length-1){
			nextNeuron = networkData[i+1];
		}

		var xp = (parseFloat(neuron['p'][0]) - 0.5 ) * 200;
		var yp = (parseFloat(neuron['p'][1]) - 0.5 ) * 200;
		var zp = (parseFloat(neuron['p'][2]) - 0.5 ) * 200;

		var point = new TDPoint(xp, yp, zp);
		point.blue = parseInt(parseFloat(neuron['e']) * 255);
		scene.points.push(point);

		if (nextNeuron){
			var x2 = (parseFloat(nextNeuron["p"][0]) - 0.5 ) * 200;
			var y2 = (parseFloat(nextNeuron["p"][1]) - 0.5 ) * 200;
			var z2 = (parseFloat(nextNeuron["p"][2]) - 0.5 ) * 200;
			var point2 = new TDPoint(x2, y2, z2);
			var line = new TDLine(point, point2);
			line.blue = point.blue;
			scene.lines.push(line);
		}

	}
}

function processState(){
	$.post(SERVER_URL + "/processState", function(){
		reloadNetworkData();

		if (isRunning){
			setTimeout(processState, 200);
		}
	});
}

function showLoading(show){
	if (show){
		$("#loading").fadeIn(0);
	}else{
		if (!isRunning) {
			$("#loading").fadeOut(100);
		}
	}
}