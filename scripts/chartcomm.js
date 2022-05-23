var xValues = ["Positive", "Neutral", "Negative"];
var yValues = [12, 22, 56];
var barColors = ["green", "blue","red"];

new Chart("myChart", {
  type: "pie",
  data: {
    labels: xValues,
    datasets: [{
      backgroundColor: barColors,
      data: yValues
    }]
  },
  options: {
    title: {
      display: true,
      text: "Feelings in the comments"
    }
  }
});