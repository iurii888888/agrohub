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

  // Утилита для запросов и отображения результата
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

  // События для кнопок анализа и рекомендаций
  document.getElementById('start-analysis').addEventListener('click', () => {
    fetchAndShow('/analyze_plant/', 'Analysis Result');
  });

  document.getElementById('get-recommendation').addEventListener('click', () => {
    fetchAndShow('/recommendations/', 'Recommendation', 'GET');
  });

  document.getElementById('analyze-plant-button').addEventListener('click', () => {
    document.getElementById('start-analysis').click();
  });

  document.getElementById('recommend-button').addEventListener('click', () => {
    document.getElementById('get-recommendation').click();
  });

  // Остальные кнопки (загрузка файла, отчёт, фон, GitHub)
  document.getElementById('upload-data').addEventListener('click', () => {
    const input = document.createElement('input');
    input.type = 'file';
    input.accept = '.csv, .json, image/*';
    input.onchange = () => {
      openModal('File Selected', `<p>Файл: ${input.files[0].name}</p>`);
    };
    input.click();
  });

  document.getElementById('generate-report').addEventListener('click', () => {
    window.open('/generate_report', '_blank');
  });

  document.getElementById('toggle-background').addEventListener('click', () => {
    document.querySelector('.background-overlay').classList.toggle('active');
  });

  document.getElementById('go-github').addEventListener('click', () => {
    window.open('https://github.com/iurii888888/agrohub', '_blank');
  });
});

