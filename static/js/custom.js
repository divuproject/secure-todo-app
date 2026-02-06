document.addEventListener('DOMContentLoaded', function () {
    const toggleBtn = document.getElementById('theme-toggle');
    const html = document.documentElement;

    // Load saved preference
    if (localStorage.getItem('theme') === 'dark') {
        html.setAttribute('data-bs-theme', 'dark');
        toggleBtn.innerHTML = '<i class="fas fa-sun"></i>';
    } else {
        html.setAttribute('data-bs-theme', 'light');
        toggleBtn.innerHTML = '<i class="fas fa-moon"></i>';
    }

    // Toggle theme
    toggleBtn.addEventListener('click', function () {
        if (html.getAttribute('data-bs-theme') === 'dark') {
            html.setAttribute('data-bs-theme', 'light');
            toggleBtn.innerHTML = '<i class="fas fa-moon"></i>';
            localStorage.setItem('theme', 'light');
        } else {
            html.setAttribute('data-bs-theme', 'dark');
            toggleBtn.innerHTML = '<i class="fas fa-sun"></i>';
            localStorage.setItem('theme', 'dark');
        }
    });
});