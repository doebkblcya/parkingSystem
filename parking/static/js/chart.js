document.addEventListener("DOMContentLoaded", function () {
    const chartData = JSON.parse(document.getElementById("chartData").textContent);

    const ctx = document.getElementById('vehicleChart').getContext('2d');
    const vehicleChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['在场车辆', '大型在场车辆', '小型在场车辆', '已离场车辆', '大型已离场车辆', '小型已离场车辆', '已缴费金额'],
            datasets: [{
                label: '车辆统计',
                data: [
                    chartData.total_in_vehicles,
                    chartData.large_in_vehicles,
                    chartData.small_in_vehicles,
                    chartData.total_out_vehicles,
                    chartData.large_out_vehicles,
                    chartData.small_out_vehicles,
                    chartData.total_payment_out
                ],
                backgroundColor: [
                    'rgba(0, 123, 255, 0.6)',
                    'rgba(40, 167, 69, 0.6)',
                    'rgba(255, 193, 7, 0.6)',
                    'rgba(220, 53, 69, 0.6)',
                    'rgba(23, 162, 184, 0.6)',
                    'rgba(255, 159, 64, 0.6)',
                    'rgba(108, 117, 125, 0.6)'
                ],
                borderColor: [
                    'rgba(0, 123, 255, 1)',
                    'rgba(40, 167, 69, 1)',
                    'rgba(255, 193, 7, 1)',
                    'rgba(220, 53, 69, 1)',
                    'rgba(23, 162, 184, 1)',
                    'rgba(255, 159, 64, 1)',
                    'rgba(108, 117, 125, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});
