# Docx 檔 xml 格式解析

## 模版文件製作方法

docx 檔實際上是一個由許多 xml 檔案所組成的壓縮檔，由 xml 檔控制 docx 檔的各種設定和內容。
本專案提供之 docx 模版文件由以下方式製作：

1. 以 Microsoft Office 2021 Word 開啟一份新文件。
2. 建立一個新樣式，名稱「auto_number」，格式設定如下：

   * 字型：標楷體
   * 字體大小： 14
   * 對齊：置中

   下方勾選「新增至樣式庫」，並選取「依據此範本建立的新文件」。

    打開左下角的格式選單，設定編號方式，並且定義新的編號格式。

    * 編號樣式使用阿拉伯數字，設定字型參數如下：

        * 中文字型：標楷體
        * 字型：使用中文字型
        * 字型樣式：標準
        * 大小：14

    * 編號格式中，在數字前方加上「照片」，並將數字後方的「點」刪除。
    * 對齊方式：置中對齊。

    設定完成後，選擇新增的編號格式並且點選確定。

3. 建立新樣式後，點選編輯頁面的第一行，設定其樣式為新建立的 「auto_number」（因為如果不對文件內容進行更動，檔案內部不會生成 xml 檔，因此至少要有內容變動才可以讓 Word 生成程式所需的模版檔案內容）。
4. 檔案儲存後，命名為 default.docx 。
5. 將 default.docx 重新命名成 default.docx.zip 並解壓縮。
6. 進入解壓縮後的資料夾，打開 word 中的 document.xml 文件，將 <w:body> 中 <w:p> 標籤和其內容刪除， <w:body> 標籤中只留下 <w:sectPr> 標籤和其內容（<w:p> 標籤即是建立模版時，產生的變動時所生成，意即使用者新增的內容，模版檔案不需要這段內容，因此將其刪除），存檔後退出。
7. 將 default.docx 直接以解壓縮程式打開，進入 word 資料夾，將 document.xml 刪除並將剛才修改過的 document.xml 拖曳新增進去。
8. 關閉解壓縮程式，此 default.docx 即為模版文件。

## 模版文件結構

在 docx 解壓縮之後，裡面的 word 資料夾中有三個重要的檔案：

1. document.xml

    記錄 docx 文件的文字內容和所套用的樣式設定。

2. styles.xml

    記錄所有的樣式設定。在[模版文件製作方法](#模版文件製作方法)中所新增的樣式（auto_number）即被記錄在這個檔案中。
    在此文件的最下方，可以觀察到新增的樣式內容。

    ```xml
    <w:style w:type="paragraph" w:customStyle="1" w:styleId="autonumber">
        <w:name w:val="auto_number" />
        <w:basedOn w:val="a" />
        <w:link w:val="autonumber0" />
        <w:qFormat />
        <w:rsid w:val="00B52B10" />
        <w:pPr>
            <w:numPr>
                <w:numId w:val="1" />
            </w:numPr>
            <w:jc w:val="center" />
        </w:pPr>
        <w:rPr>
            <w:rFonts w:ascii="標楷體" w:eastAsia="標楷體" />
            <w:sz w:val="28" />
        </w:rPr>
    </w:style>
    <w:style w:type="character" w:customStyle="1" w:styleId="autonumber0">
        <w:name w:val="auto_number 字元" />
        <w:basedOn w:val="a0" />
        <w:link w:val="autonumber" />
        <w:rsid w:val="00B52B10" />
        <w:rPr>
            <w:rFonts w:ascii="標楷體" w:eastAsia="標楷體" />
            <w:sz w:val="28" />
        </w:rPr>
    </w:style>
    ```

3. numbering.xml

    記錄和自動編號相關的設定。在[模版文件製作方法](#模版文件製作方法)中所新增的樣式（auto_number）中，設定的編號格式參數內容即被記錄在這個檔案中。
    在此文件的下方，可以觀察到新增的樣式編號格式參數內容。

    ```xml
    <w:abstractNum w:abstractNumId="0" w15:restartNumberingAfterBreak="0">
        <w:nsid w:val="3AD52B0E" />
        <w:multiLevelType w:val="hybridMultilevel" />
        <w:tmpl w:val="F83003D4" />
        <w:lvl w:ilvl="0" w:tplc="A1DA921A">
            <w:start w:val="1" />
            <w:numFmt w:val="decimal" />
            <w:pStyle w:val="autonumber" />
            <w:lvlText w:val="照片%1" />
            <w:lvlJc w:val="center" />
            <w:pPr>
                <w:ind w:left="480" w:hanging="480" />
            </w:pPr>
            <w:rPr>
                <w:rFonts w:ascii="標楷體" w:eastAsia="標楷體" w:hint="eastAsia" />
                <w:b w:val="0" />
                <w:i w:val="0" />
                <w:sz w:val="28" />
            </w:rPr>
        </w:lvl>
        .
        .
        .    
    </w:abstractNum>
    <w:num w:numId="1">
        <w:abstractNumId w:val="0" />
    </w:num>
    ```

    而最下方的

    ```xml
    <w:num w:numId="1">
        <w:abstractNumId w:val="0" />
    </w:num>
    ```

    表示 ```numId``` 數值和 ```abstractNumId``` 的數值對應關係，即 ```styles.xml``` 中指定使用 ```numId="1"``` 的編號設定 ，即是對應了 ```numbering.xml``` 中 ```abstractNumId val="0"``` 的編號格式。

## 如何應用

在 ```controller.py``` 當中，函式 generate_docx 裡有這段程式碼：

```python
pStyle = OxmlElement("w:pStyle")
pStyle.set(qn("w:val"), "autonumber")
```

便是指定使用 styleId 為「autonumber」的樣式，而這個樣式在 ```styles.xml``` 中又指定使用 「numId="1"」的編號設定，查看 ```numbering.xml``` 的最下方對應表又可以發現其是指 ```abstractNumId val="0"``` 的編號格式，最後便使用了新增的自訂編號格式。
