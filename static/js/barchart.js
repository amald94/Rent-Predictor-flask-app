const city = ['barrie','cornwall','norfolk','thunder']
const rent = [154,255,266,555]
var pluginArrayArg = new Array();
for (var i = 0; i < cities.length; ++i) {
    if(predictedRent > rents[i]){
        this["marker"+i] = new Object();
        this["marker"+i].label = cities[i];
        this["marker"+i].y = rents[i];
        pluginArrayArg.push(this["marker"+i]);
    }
}
const rentArray = JSON.parse(JSON.stringify(pluginArrayArg))


function myFunc(vars) {
    return vars;
}

console.log(rents);
console.log(cities);

window.onload = function () {



    var chart = new CanvasJS.Chart("chartContainer", {
        animationEnabled: true,
        dataPointWidth: 10,
        height:860,
        title:{
            text:"Predicted Rent",
            fontSize: 30
        },
        axisX:{
            interval: 1,
            labelFontSize: 20
        },
        axisY2:{
            interlacedColor: "rgba(1,77,101,.2)",
            gridColor: "rgba(1,77,101,.1)",
            title: "Expected rent across other major cities in Ontario",
            labelFontSize: 20,
            titleFontSize: 25
        },
        data: [{
            type: "bar",
            name: "cities",
            axisYType: "secondary",
            color: "#014D65",
            dataPoints: rentArray,
            
        }]
    });
    chart.render();
    
    }
    