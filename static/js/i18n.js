document.addEventListener('DOMContentLoaded', () => {
  const switcher = document.getElementById('language-switcher');
  if (!switcher) return;

  const applyTranslations = (dict) => {
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      if (dict[key]) {
        // если элемент содержит вложенные теги (например <span>)
        if (el.children.length > 0) {
          el.innerHTML = dict[key];
        } else {
          el.textContent = dict[key];
        }
      }
    });

    // поддержка placeholder и title
    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
      const key = el.getAttribute('data-i18n-placeholder');
      if (dict[key]) el.setAttribute('placeholder', dict[key]);
    });

    document.querySelectorAll('[data-i18n-title]').forEach(el => {
      const key = el.getAttribute('data-i18n-title');
      if (dict[key]) el.setAttribute('title', dict[key]);
    });
  };

  const loadLanguage = async (lang) => {
    try {
      const res = await fetch(`/static/i18n/${lang}.json`);
      const dict = await res.json();
      localStorage.setItem("lang", lang);
      applyTranslations(dict);
    } catch (e) {
      console.error("Language loading failed", e);
    }
  };

  switcher.addEventListener('change', e => loadLanguage(e.target.value));

  const defaultLang = localStorage.getItem("lang") || "en";
  switcher.value = defaultLang;
  loadLanguage(defaultLang);
});
