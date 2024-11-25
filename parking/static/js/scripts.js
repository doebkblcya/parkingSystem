// 动态更新当前时间
function updateCurrentTime() {
    const currentTimeElement = document.getElementById('current-time');
    const now = new Date();
    currentTimeElement.innerText = now.toLocaleString(); // 显示当地时间
}

// 每秒钟更新一次时间
setInterval(updateCurrentTime, 1000);

// 侧边栏折叠功能：鼠标悬停展开，离开收起
const sidebar = document.getElementById('sidebar');

sidebar.addEventListener('mouseenter', function () {
    sidebar.classList.remove('sidebar-closed');
    sidebar.classList.add('sidebar-open');
});

sidebar.addEventListener('mouseleave', function () {
    sidebar.classList.remove('sidebar-open');
    sidebar.classList.add('sidebar-closed');
});