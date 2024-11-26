document.addEventListener("DOMContentLoaded", function () {
    const chartData = JSON.parse(document.getElementById("chartData").textContent);

    // 图表：在场车辆构成
    const ctxInVehicles = document.getElementById("chartInVehicles").getContext("2d");
    new Chart(ctxInVehicles, {
        type: "pie",
        data: {
            labels: ["大型车", "小型车"],
            datasets: [{
                data: [chartData.large_in_vehicles, chartData.small_in_vehicles],
                backgroundColor: ["#4CAF50", "#FFC107"],
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { position: "top" }
            }
        }
    });

    // 图表：离场车辆构成
    const ctxOutVehicles = document.getElementById("chartOutVehicles").getContext("2d");
    new Chart(ctxOutVehicles, {
        type: "pie",
        data: {
            labels: ["大型车", "小型车"],
            datasets: [{
                data: [chartData.large_out_vehicles, chartData.small_out_vehicles],
                backgroundColor: ["#007BFF", "#FF5733"],
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { position: "top" }
            }
        }
    });

    // 图表：在场与离场车辆数量对比
    const ctxComparison = document.getElementById("chartComparison").getContext("2d");
    new Chart(ctxComparison, {
        type: "bar",
        data: {
            labels: ["在场车辆", "离场车辆"],
            datasets: [{
                label: "数量",
                data: [chartData.total_in_vehicles, chartData.total_out_vehicles],
                backgroundColor: ["#17A2B8", "#DC3545"],
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: { beginAtZero: true }
            }
        }
    });

    // 图表：近 7 天缴费金额变化
    const ctxPaymentTrend = document.getElementById("chartPaymentTrend").getContext("2d");
    new Chart(ctxPaymentTrend, {
        type: "line",
        data: {
            labels: chartData.payment_trend_labels || [], // 日期数组
            datasets: [{
                label: "缴费金额 (元)",
                data: chartData.payment_trend_data || [], // 对应数据
                borderColor: "#28A745",
                fill: false,
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: { title: { display: true, text: "日期" } },
                y: { beginAtZero: true, title: { display: true, text: "金额 (元)" } }
            }
        }
    });
});
