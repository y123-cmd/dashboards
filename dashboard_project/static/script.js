// Ensure the DOM is fully loaded before running scripts
document.addEventListener('DOMContentLoaded', function () {

    // Add event listener for the form submission
    document.getElementById('dataForm').addEventListener('submit', function(e) {
        e.preventDefault();  // Prevent the default form submission

        // Get the value of the selected dataset
        var selectedDataset = document.getElementById('dataset').value;

        // Define the data for the selected dataset
        var data;
        if (selectedDataset == 'dataset1') {
            data = [{ x: ['A', 'B', 'C'], y: [10, 20, 30], type: 'bar' }];
        } else {
            data = [{ x: ['X', 'Y', 'Z'], y: [15, 25, 35], type: 'bar' }];
        }

        // Update the bar chart with the new data
        Plotly.react('bar-chart', data);
    });

    // Render the initial charts on page load
    Plotly.newPlot('bar-chart', [{ x: ['A', 'B', 'C'], y: [10, 20, 30], type: 'bar' }]);
    Plotly.newPlot('line-chart', [{ x: [1, 2, 3], y: [2, 4, 6], type: 'scatter' }]);
    Plotly.newPlot('pie-chart', [{ labels: ['Category A', 'Category B', 'Category C'], values: [10, 20, 30], type: 'pie' }]);
});

