document.addEventListener("DOMContentLoaded", () => {
    
    const yearSpan = document.getElementById("year");
    if (yearSpan) {
        yearSpan.textContent = new Date().getFullYear();
    }

    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeIcon = document.getElementById('theme-icon');
    const currentTheme = localStorage.getItem('theme') || 'dark';
    
    const sunIcon = `<circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>`;
    const moonIcon = `<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>`;

    const updateIcon = (theme) => {
        themeIcon.innerHTML = (theme === 'dark') ? sunIcon : moonIcon;
    };

    document.documentElement.setAttribute('data-theme', currentTheme);
    updateIcon(currentTheme);

    themeToggleBtn.addEventListener('click', function(e) {
        e.preventDefault();
        let theme = document.documentElement.getAttribute('data-theme');
        let newTheme = theme === 'dark' ? 'light' : 'dark';
        
        document.documentElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        
        updateIcon(newTheme);
        
        if (typeof window.renderChart === 'function') {
            let currentType = document.getElementById('btn-candle').classList.contains('active') ? 'candlestick' : 'line';
            window.renderChart(currentType);
        }
    });

    // chart
    const chartData = window.CHART_DATA || [];
    if (chartData && chartData.length > 0) {
        let chart;
        window.renderChart = function(type) {
            const seriesData = chartData.map(d => ({ x: new Date(d.date).getTime(), y: type === 'candlestick' ? [d.open, d.high, d.low, d.close] : d.close }));
            const activeTheme = document.documentElement.getAttribute('data-theme');
            const options = {
                series: [{ name: 'Price', data: seriesData }],
                chart: { type: type, height: 350, background: 'transparent', toolbar: { show: false }, animations: { enabled: false } },
                theme: { mode: activeTheme },
                stroke: { curve: 'smooth', width: type === 'line' ? 2 : 1, colors: type === 'line' ? (activeTheme === 'light' ? ['#4F46E5'] : ['#7C83FD']) : [] },
                xaxis: { type: 'datetime', labels: { style: { colors: activeTheme === 'light' ? '#4B5563' : '#9ca3af' } } },
                yaxis: { labels: { style: { colors: activeTheme === 'light' ? '#4B5563' : '#9ca3af' }, formatter: function(val) { return '$' + val.toFixed(2); } } },
                grid: { borderColor: activeTheme === 'light' ? '#E5E7EB' : '#1f2937' },
                plotOptions: { candlestick: { colors: { upward: '#10b981', downward: '#ef4444' }, wick: { useFillColor: true } } }
            };
            if (chart) chart.destroy();
            chart = new ApexCharts(document.querySelector("#priceChart"), options);
            chart.render();
        }
        window.renderChart('candlestick');
        window.changeChartType = function(type) {
            document.getElementById('btn-candle').classList.remove('active');
            document.getElementById('btn-line').classList.remove('active');
            if (type === 'candlestick') document.getElementById('btn-candle').classList.add('active');
            if (type === 'line') document.getElementById('btn-line').classList.add('active');
            window.renderChart(type);
        };
    }

    // modal
    const modal = document.getElementById('about-modal');
    const openBtn = document.getElementById('open-about');
    const closeBtn = document.getElementById('close-about');

    if (openBtn && modal && closeBtn) {
        openBtn.addEventListener('click', (e) => {
            e.preventDefault();
            modal.classList.add('active');
        });
        
        closeBtn.addEventListener('click', () => {
            modal.classList.remove('active');
        });
        
        modal.addEventListener('click', (e) => {
            if (e.target === modal) modal.classList.remove('active');
        });
    }
});