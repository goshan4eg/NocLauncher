# NocLauncher v1.0.5

<p align="center">
  <img src="assets/icon.png" alt="NocLauncher" width="120" />
</p>

<p align="center">
  <b>Кастомный Minecraft Launcher (Java + Bedrock)</b><br>
  <i>Стабильный offline-first UX, быстрый запуск, удобные инструменты и встроенная диагностика.</i>
</p>

<p align="center">
  <a href="https://github.com/NocCorporation/NocLauncher/releases/latest">
    <img alt="Latest Release" src="https://img.shields.io/github/v/release/NocCorporation/NocLauncher?style=flat-square" />
  </a>
  <a href="https://github.com/NocCorporation/NocLauncher/releases">
    <img alt="Downloads" src="https://img.shields.io/github/downloads/NocCorporation/NocLauncher/total?style=flat-square" />
  </a>
  <img alt="Platform" src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-4caf50?style=flat-square" />
  <img alt="License" src="https://img.shields.io/badge/License-MIT-blue?style=flat-square" />
</p>

---

## ✨ Возможности (актуально)

- **Java + Bedrock** в одном лаунчере
- Профили Java: **Vanilla / Forge / OptiFine**
- **Offline-first** режим (стабильный локальный запуск)
- Библиотека модов/ресурсов/шейдеров
- Инструменты диагностики и логи запуска
- Упрощённые Bedrock-инструменты и контент-менеджмент
- Мини-панель Bedrock Hub с быстрыми переключателями
- Внешний **FPS-монитор** (NocFpsCounter) вместо нестабильного старого оверлея

---

## 🆕 Что нового в v1.0.5

- Полностью заменён старый FPS-бэкенд на внешний **NocFpsCounter.exe**
- Удалён старый нерабочий внутренний оверлей `FPS: 0`
- FPS-монитор переведён в **ручной запуск** (без автозапуска при входе в Bedrock)
- Переработан Bedrock mini-hub: плавность, выравнивание, компактность, кнопка закрытия
- Кнопка открытия mini-панели: **«Мультиплеер [Beta]»**
- Убран дублирующий пункт «Живой FPS» из лишнего раздела настроек
- В интерфейсе лаунчера отображается версия **v1.0.5**

---

## 📦 Скачать

**Текущий релиз:** `v1.0.5`

- Windows x64: `NocLauncher-1.0.5-windows-x64.exe`
- Windows x86: `NocLauncher-1.0.5-windows-x86.exe`
- Linux x64: `NocLauncher-1.0.5-linux-x64.AppImage`
- macOS x64: `NocLauncher-1.0.5-macos-x64.dmg` / `.zip`

Все файлы:
<https://github.com/NocCorporation/NocLauncher/releases>

---

## 🔐 Проверка целостности

В каждом релизе есть файлы `SHA256SUMS-*.txt`.

Пример проверки (PowerShell):

```powershell
Get-FileHash .\NocLauncher-1.0.5-windows-x64.exe -Algorithm SHA256
```

Сверьте хэш с опубликованным в релизе.

---

## 🚀 Быстрый старт

1. Скачай сборку под свою ОС из Releases.
2. Запусти NocLauncher.
3. Выбери режим: **JAVA** или **BEDROCK**.
4. Для JAVA выбери версию/профиль и ник.
5. Нажми **Играть**.

---

## 🌐 Multiplayer Status (Beta)

- Текущий мультиплеер в NocLauncher — **локальный Beta**.
- Для полноценного общего (глобального) мультиплеера нужны:
  - мощные хосты,
  - постоянная серверная инфраструктура,
  - стабильное финансирование.
- На текущий момент финансирование закрыто, поэтому до полностью рабочего общего мультиплеера ещё далеко.

---

## 🧭 Документация

- `docs/GUIDE_RU.md`
- `docs/QUICK_TUTORIALS_RU.md`
- `docs/INSTALL_RU.md`
- `docs/USER_MANUAL_RU.md`
- `docs/FEATURES_RU.md`
- `docs/TROUBLESHOOTING_RU.md`
- `docs/FAQ_RU.md`
- `docs/ROADMAP_RU.md`
- `docs/TRUST_AND_SECURITY_RU.md`
- `docs/RELEASE_TEMPLATE_RU.md`

---

## 🛠 Сборка из исходников

```bash
npm install
npm run build:win
npm run build:linux
npm run build:mac
```

Артефакты сборки: `dist/`

---

## 📄 Лицензия

MIT (`LICENSE`)
