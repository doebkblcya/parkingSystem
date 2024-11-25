document.addEventListener("DOMContentLoaded", function () {
    // 获取侧边栏和侧边栏切换按钮
    const sidebar = document.getElementById("sidebar");
    const sidebarToggle = document.getElementById("sidebar-toggle");

    // 监听鼠标移入事件
    sidebarToggle.addEventListener("mouseover", function () {
        sidebar.classList.add("sidebar-open");  // 鼠标移入时显示侧边栏
    });

    // 监听鼠标移出事件
    sidebar.addEventListener("mouseleave", function () {
        sidebar.classList.remove("sidebar-open");  // 鼠标移出时隐藏侧边栏
    });
});
