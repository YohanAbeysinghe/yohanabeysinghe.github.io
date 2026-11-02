// Site override of al_folio_core's theme runtime. Called in <head> before paint.
// This site uses a two-state switch with dark as the default, rather than system mode.
const DEFAULT_THEME = "dark";

function readThemeSetting() {
  try {
    const saved = localStorage.getItem("theme");
    if (saved === "dark" || saved === "light") return saved;
  } catch {
    // Storage can be unavailable in private or restricted browsing contexts.
  }
  return DEFAULT_THEME;
}

let themeSetting = readThemeSetting();

function determineThemeSetting() {
  return themeSetting;
}

function determineComputedTheme() {
  return themeSetting;
}

function applyTheme() {
  const root = document.documentElement;
  root.setAttribute("data-theme", themeSetting);
  root.setAttribute("data-theme-setting", themeSetting);

  const dark = themeSetting === "dark";
  const lightStyles = document.getElementById("highlight_theme_light");
  const darkStyles = document.getElementById("highlight_theme_dark");
  if (lightStyles) lightStyles.media = dark ? "none" : "";
  if (darkStyles) darkStyles.media = dark ? "" : "none";

  const button = document.getElementById("light-toggle");
  if (button) {
    button.setAttribute("aria-pressed", String(dark));
    button.setAttribute("title", dark ? "Switch to light mode" : "Switch to dark mode");
  }
}

function setThemeSetting(theme) {
  themeSetting = theme === "light" ? "light" : "dark";
  try {
    localStorage.setItem("theme", themeSetting);
  } catch {
    // Keep the switch usable for this page even when preferences cannot be saved.
  }
  applyTheme();
}

function toggleThemeSetting() {
  setThemeSetting(themeSetting === "dark" ? "light" : "dark");
}

function initTheme() {
  applyTheme();
  const bindToggle = () => {
    document.getElementById("light-toggle")?.addEventListener("click", toggleThemeSetting);
    applyTheme();
  };
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bindToggle, { once: true });
  } else {
    bindToggle();
  }
  window.addEventListener("storage", (event) => {
    if (event.key === "theme" || event.key === null) {
      themeSetting = readThemeSetting();
      applyTheme();
    }
  });
}
