let chart;

async function fetchData() {
    const res = await fetch("/api/weather");
    const json = await res.json();
    document.getElementById("last-updated").innerText = "Last updated: " + json.timestamp;
    updateChart(json.data);
}

function updateChart(data) {
    const labels = data.map(d => d.district);
    const rainfall = data.map(d => d.rainfall);
    const temp = data.map(d => d.temperature);

    if (!chart) {
        const ctx = document.getElementById('rainChart').getContext('2d');
        chart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [
                    {
                        label: 'Rainfall (mm)',
                        data: rainfall,
                        backgroundColor: '#007bff'
                    },
                    {
                        label: 'Temperature (°C)',
                        data: temp,
                        backgroundColor: '#ff9933'
                    }
                ]
            },
            options: {
                responsive: true,
                scales: { y: { beginAtZero: true } }
            }
        });
    } else {
        chart.data.labels = labels;
        chart.data.datasets[0].data = rainfall;
        chart.data.datasets[1].data = temp;
        chart.update();
    }
}

// Refresh every 60 seconds
setInterval(fetchData, 60000);
window.onload = fetchData;
