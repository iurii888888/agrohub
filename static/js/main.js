document.addEventListener('DOMContentLoaded', () => {
  // Модальное окно и спиннер
  const modal = document.getElementById('resultModal');
  const modalTitle = document.getElementById('modalTitle');
  const modalBody = document.getElementById('modalBody');
  const spinner = document.getElementById('loadingSpinner');

  function openModal(title, html) {
    modalTitle.textContent = title;
    modalBody.innerHTML = html;
    modal.classList.add('active');
  }

  function closeModal() {
    modal.classList.remove('active');
  }

  function showSpinner() {
    spinner.classList.remove('hidden');
  }

  function hideSpinner() {
    spinner.classList.add('hidden');
  }

  // Закрытие модалки
  document.querySelector('.close-btn').addEventListener('click', closeModal);
  modal.addEventListener('click', e => {
    if (e.target === modal) closeModal();
  });

  // Запрос с модальным результатом
  async function fetchAndShow(endpoint, title, method = 'POST', body = {}) {
    showSpinner();
    try {
      const res = await fetch(endpoint, {
        method,
        headers: { 'Content-Type': 'application/json' },
        body: method === 'POST' ? JSON.stringify(body) : undefined
      });
      const data = await res.json();
      openModal(title, `<pre>${JSON.stringify(data, null, 2)}</pre>`);
    } catch (err) {
      openModal('Error', `<p>${err.message || err}</p>`);
      console.error(err);
    }
    hideSpinner();
  }

  // Кнопки анализа
  document.getElementById('start-analysis').addEventListener('click', () => {
    fetchAndShow('/analyze_plant/', 'Analysis Result');
  });

  document.getElementById('get-recommendation').addEventListener('click', () => {
    fetchAndShow('/recommend', 'Recommendation');
  });

  document.getElementById('analyze-plant-button').addEventListener('click', () => {
    document.getElementById('start-analysis').click();
  });

  document.getElementById('recommend-button').addEventListener('click', () => {
    document.getElementById('get-recommendation').click();
  });

  // Загрузка файла
  document.getElementById('upload-data').addEventListener('click', () => {
    const input = document.createElement('input');
    input.type = 'file';
    input.accept = '.csv, .json, image/*';
    input.onchange = () => {
      openModal('File Selected', `<p>Файл: ${input.files[0].name}</p>`);
    };
    input.click();
  });

  // Кнопки с переходами
  document.getElementById('generate-report').onclick = () =>
    window.location.href = 'generate_report.html';

  document.getElementById('upload-data').onclick = () =>
    window.location.href = 'upload_data.html';

  document.getElementById('toggle-background').onclick = () =>
    document.querySelector('.background-overlay').classList.toggle('active');

  document.getElementById('go-github').onclick = () =>
    window.open('https://github.com/iurii888888/agrohub', '_blank');

  // Переходы по пунктам меню
  const navLinks = {
    'Dashboard': 'dashboard.html',
    'Plant Health': 'plant_health.html',
    'Livestock Health': 'livestock_health.html',
    'Alerts': 'alerts.html',
    'Insights': 'insights.html',
    'Reports': 'reports.html'
  };

  document.querySelectorAll('.navbar ul li a').forEach(link => {
    link.addEventListener('click', e => {
      e.preventDefault();
      const target = navLinks[link.textContent.trim()];
      if (target) window.location.href = target;
    });
  });
});
