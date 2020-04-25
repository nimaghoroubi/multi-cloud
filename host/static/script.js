console.log("Window:", window.location.host);

const solverButtons = document.querySelectorAll(".solver-button");
const chartElem = document.getElementById("chart");

for (solver of solverButtons) {
  const problemID = solver.dataset.problem;
  const solverName = solver.dataset.solver;
  (function() {
    solver.addEventListener("click", e => {
      getSolverStats(problemID, solverName, e.target);
    });
  })();
}

const getSolverStats = async (problemID, solverName, btn) => {
  btn.classList.add("pulse");
  console.log(
    `http://${window.location.host}/problems/${problemID}/${solverName}`
  );
  try {
    const response = await fetch(
      `http://${window.location.host}/problems/${problemID}/${solverName}`
    );
    btn.classList.remove("pulse");
    console.log(response);
    const res = await response.json();

    const time = res.time;
    console.log("time:", time);
    let id = "" + problemID + "." + solverName;
    index = findIndex(id);
    if (typeof index === "undefined") {
      labels.unshift(id);
      values.unshift(time);
    } else {
      labels[index] = id;
      values[index] = time;
    }

    updateChart();
  } catch (error) {
    console.error(error);
  }
};

const findIndex = id => {
  for (let i = 0; i < labels.length; i++) {
    console.log("id:", id);
    console.log("labels[i:", labels[i]);
    if (id === labels[i]) {
      return i;
    }
  }
  return undefined;
};

labels = [];
values = [];

Chart.defaults.global.legend.onClick = () => {};
const context = chartElem.getContext("2d");
const chart = new Chart(context, {
  type: "bar",
  data: {
    labels: labels,
    datasets: [
      {
        label: "",
        backgroundColor: [],
        borderColor: [],
        data: values
      }
    ]
  },
  options: {
    legend: {
      display: false
    },
    tooltips: {
      enabled: false
    },
    responsive: false,

    scales: {
      yAxes: [
        {
          ticks: {
            beginAtZero: true
          }
        }
      ]
    }
  }
});

const updateChart = () => {
  console.log("labels:", labels);
  console.log("values: ", values);
  chart.data.labels = labels;
  chart.data.datasets[0].data = values;

  for (let i = 0; i < values.length; i++) {
    if (
      isNaN(values[i]) ||
      typeof values[i] === "undefined" ||
      values[i] === 1
    ) {
      chart.data.datasets[0].data[i] = 1;
      chart.data.datasets[0].backgroundColor[i] = "rgb(131, 3, 3)";
      chart.data.datasets[0].borderColor[i] = "rgb(131, 3, 3)";
    } else {
      chart.data.datasets[0].backgroundColor[i] = "rgba(255, 153, 0, 1)";
      chart.data.datasets[0].borderColor[i] = "rgba(255, 153, 0, 1)";
    }
  }

  chart.update();
};
