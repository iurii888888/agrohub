
document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('start-analysis').addEventListener('click', () => {
    alert('Starting plant analysis...');
    fetch('/analyze_plant/', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({})
    })
    .then(res => res.json())
    .then(data => alert('Analysis result: ' + JSON.stringify(data)))
    .catch(err => console.error(err));
  });

  document.getElementById('get-recommendation').addEventListener('click', () => {
    alert('Fetching recommendations...');
    fetch('/recommendations/')
    .then(res => res.json())
    .then(data => alert('Recommendation: ' + JSON.stringify(data)))
    .catch(err => console.error(err));
  });

  document.getElementById('analyze-plant-button').addEventListener('click', () => {
    document.getElementById('start-analysis').click();
  });
  document.getElementById('recommend-button').addEventListener('click', () => {
    document.getElementById('get-recommendation').click();
  });
  document.getElementById('upload-data').addEventListener('click', () => {
    const input = document.createElement('input');
    input.type = 'file';
    input.accept = '.csv, .json, image/*';
    input.onchange = () => alert('File selected.');
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
