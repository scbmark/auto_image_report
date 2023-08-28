# Auto Image Report

一個用來自動生成一頁二圖式的圖片報告的軟體。

本專案開發主要基於 Python 3.10.11、 PySide6 、 Pillow 和 python-docx。

## 注意事項

**任何圖片在進入此程式使用前，請務必做好備份，並且使用副本來操作。本程式雖然不會對匯入的圖片檔案本身進行寫入的操作，但資料寶貴無價，最好避免一切會造成圖片原檔消失的可能性。**

## 安裝

### 執行檔

支援 Windows_x64 及 Linux_x64 ，請至 [Release](https://github.com/scbmark/auto_image_report/releases) 下載。

編譯環境：於 Windows 11 22H2 x64 及 Arch Linux x64 的系統環境下，在 Poetry 建立的虛擬環境中用 Nuitka 編譯，C++ 編譯器為 gcc。

### 從原始碼執行

#### 安裝依賴套件

本專案使用 Python 開發，並且用 Poetry 管理依賴套件。下載原始碼之後，至專案根目錄使用 Poetry 建立虛擬環境並安裝依賴套件。

```bash
poetry install  # 建立虛擬環境並安裝依賴套件
```

或者使用其他方式建立虛擬環境並安裝依賴套件，依賴套件見 [pyproject.toml](./pyproject.toml) 。

#### 設定自訂 docx 模版

在執行之前，因為本程式的自動編號功能用到了自訂的編號設定，因此要先替換 python-docx 套件中的模版文件。若不替換文件，程式中的 Word 自動編號功能會無法正常使用。

將專案根目錄下的 ```template.docx``` 替換掉 ```./.venv/lib/python/site-packages/docx/templates/``` 中的 ```default.docx``` ，並將其重新命名成 ```default.docx```

如果不想更動套件庫，可以在 app/controller.py 當中，將專案根目錄下的 template.docx 檔案路徑傳入用來建立 Document 物件的參數，亦可達成相同目的，其位於 controller.py 中的函式 generate_docx 裡面。

```python
# 傳入模版檔案路徑
doc = Document("template.docx")
```

#### 執行主程式

以上都設定好之後，入口程式為 ```auto_image_report.py```。進入虛擬環境後，直接執行即可。

```bash
python ./auto_image_report.py
```

### 從原始碼編譯

如上「[從原始碼執行](#從原始碼執行)」所述，安裝完虛擬環境及設定好模版文件後，使用 Nuitka 進行原始碼打包。

#### Linux

首先要針對 python-docx 的路徑問題做修正，將 ```path = path.replace('parts/../', '')``` 寫入 python-docx 套件目錄中的 ```parts/hdrftr.py``` 中，最下面的 ```with open``` 的前一行。

```bash
# Linux
## 安裝依賴
sudo apt install patchelf   # Ubuntu
sudo pacman -S patchelf # Arch Linux

## 開始編譯
python -m nuitka --standalone --static-libpython=no --enable-plugin=pyside6 --include-data-dir=./.venv/lib/python3.10/site-packages/docx/templates=docx/templates --follow-imports --include-package=certifi --disable-console --output-dir=output auto_image_report.py

```

#### Windows

```bash
# Windows
python -m nuitka --standalone --static-libpython=no --enable-plugin=pyside6 --include-data-dir=C:\Users\scbma\Downloads\code\.venv\Lib\site-packages\docx\templates=docx\templates --follow-imports --include-package=certifi --disable-console --windows-icon-from-ico=.\statics\icon.ico --output-dir=output auto_image_report.py
```

執行 output/auto_image_report.dist 內的執行檔即可。

專案內有提供 Windows 平臺 Inno Setup 6 的 compiler script ，可自行打包。

## Docx 模版文件說明

見 [xml_parse.md](./xml_parse.md)

## 功能說明

見 [manual.md](./manual.md)

## 貢獻

感謝您的使用，對於本專案有任何建議或 Bug 的回報，歡迎發 Issue 或者使用 Email 和作者連繫。

## 作者

Mark Hsiao

Email：[Twilight3847@skiff.com](#作者)

## 授權

[GNU GPL v3](https://choosealicense.com/licenses/gpl-3.0/)
