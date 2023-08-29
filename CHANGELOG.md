# Changelog

## [Unreleased]

## [2.2] - 2023-08-29

### Changed

- Python 版本更新至 3.11.5 。
- 關於頁面中的版本號碼改由變數控制。
- 修改 Nuitka 的編譯指令。
- Linux 的編譯平臺改為 Ubuntu 22.04 LTS 。

### Fixed

- 修復 Linux 平臺執行更新功能時找不到 SSL 證書的問題。

## [2.1] - 2023-08-27

### Changed

- 以 PySide6 取代 PyQt6 。
- 更改編譯方式，以 Nuitka 取代 pyinstaller ，執行效能大幅提升。
- 將和 path 有關的函式，以 pathlib.Path 取代 os.path 。
- 為避免 Windows 系統防毒軟體誤報，以及改善程式啟動速度，不編譯成單一執行檔， Linux 平臺將使用 zip 檔將執行檔和依賴檔案打包， Windows 平臺則使用 Inno Setup 6 製作 Installer 。
- bugs 修復。

## [2.0.0] - 2023-08-24

### Added

- 第一個發布版本。
- 提供 Linux 的執行檔。
