# Установка NocLauncher (RU)

## Windows

1. Скачайте нужный файл из Release Assets:
   - `NocLauncher-1.0.0-windows-x64.exe` (64-bit)
   - `NocLauncher-1.0.0-windows-x86.exe` (32-bit)
2. Запустите установщик.
3. После установки откройте лаунчер и выполните первый запуск.

## Linux (AppImage)

1. Скачайте `NocLauncher-1.0.0-linux-x64.AppImage`.
2. Дайте права на запуск:

```bash
chmod +x NocLauncher-1.0.0-linux-x64.AppImage
```

3. Запустите:

```bash
./NocLauncher-1.0.0-linux-x64.AppImage
```

## macOS (beta)

1. Скачайте сборку под свою архитектуру (x64/arm64).
2. Если macOS блокирует запуск, откройте через **ПКМ → Open**.
3. При необходимости снимите quarantine:

```bash
xattr -dr com.apple.quarantine /Applications/NocLauncher.app
```

## Первый запуск

1. Выберите режим: **JAVA** или **BEDROCK**.
2. Для JAVA выберите версию и профиль (Vanilla/Forge/OptiFine).
3. Укажите ник.
4. Нажмите **Играть**.
