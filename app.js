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
			scene.rotationY += diffX/100;
			scene.rotationX += diffY/100;
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
$("#buttonRefresh").click( function(){
	reloadNetworkData();
});

$("#buttonRandomize").click( function(){
	randomizeNetwork();
});

//Network

function randomizeNetwork(){
	$.get(SERVER_URL + "/randomize", function(data){
		console.log("randomized");
		reloadNetworkData();
	});
}

function reloadNetworkData(){
	/*
	ctx.fillStyle = "#FFFFFF";
	ctx.fillRect(0, 0, canvas.width, canvas.height);
	*/
	
	scene.clear();
	
	$("#loading").fadeIn(0);

	$.ajax( SERVER_URL + "/data" )
	  .done(function(data) {
		  
		var value = 0;
		var parsed = JSON.parse(data);
		
		for (var x = 0; x < parsed.length; x++)
		{
			for (var y = 0; y < parsed[0].length; y++)
			{
				neuron = parsed[x][y];
				
				var xp = (parseFloat(neuron["p"][0]) - 0.5 ) * 200;
				var yp = (parseFloat(neuron["p"][1]) - 0.5 ) * 200;
				var zp = (parseFloat(neuron["p"][2]) - 0.5 ) * 200;
				
				var point = new TDPoint(xp, yp, zp);
				scene.points.push(point);
			}
		}
		
		$("#loading").fadeOut(50);
		
		console.log("Got data" + value);
	});
}