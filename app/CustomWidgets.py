import os
from pathlib import Path

import filetype
from PIL import Image
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QThread, Signal


class DropListWidget(QtWidgets.QListWidget):
    """This custom widget based on  QListWidget.

    Added features:

        1.Drag and drop features

        2.Placeholder

        3.validate the dropped files format

    Emit:
        send_new_item -> list[str]: Sending the input images's path
    """

    send_new_item = QtCore.Signal(list)

    def __init__(self, parent):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self._placeholder_text: str = "拖曳至此新增圖片"
        self.support_format = ["jpg", "png", "bmp", "tif"]

    @property
    def placeholder_text(self):
        return self._placeholder_text

    @placeholder_text.setter
    def placeholder_text(self, text):
        self._placeholder_text = text
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.count() == 0:
            painter = QtGui.QPainter(self.viewport())
            painter.save()
            col = self.palette().placeholderText().color()
            painter.setPen(col)
            fm = self.fontMetrics()
            elided_text = fm.elidedText(
                self.placeholder_text,
                QtCore.Qt.TextElideMode.ElideRight,
                self.viewport().width(),
            )
            painter.drawText(
                self.viewport().rect(), QtCore.Qt.AlignmentFlag.AlignCenter, elided_text
            )
            painter.restore()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            super(DropListWidget, self).dragEnterEvent(event)

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.DropAction.CopyAction)
            event.accept()
        else:
            super(DropListWidget, self).dragMoveEvent(event)

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.DropAction.CopyAction)
            event.accept()

            valid_links: list[str] = list()
            invalid_links: list[str] = list()

            for url in event.mimeData().urls():
                if url.isLocalFile():
                    link = url.toLocalFile()
                    if Path(link).is_dir():
                        messabebox = QtWidgets.QMessageBox(self)
                        messabebox.warning(self, "Error", "不支援資料夾")
                    else:
                        link_format = filetype.guess(link)
                        if link_format is None:
                            invalid_links.append(link)
                        elif link_format.extension in self.support_format:
                            valid_links.append(link)
                        else:
                            invalid_links.append(link)
                else:
                    messabebox = QtWidgets.QMessageBox(self)
                    messabebox.warning(self, "Error", "不支援的檔案")

            if invalid_links:
                invalid_files = "\n".join(invalid_links)
                messabebox = QtWidgets.QMessageBox(self)
                messabebox.warning(self, "Error", f"以下檔案不支援\n {invalid_files}")

            self.send_new_item.emit(valid_links)
        else:
            super(DropListWidget, self).dropEvent(event)


class LoadImage(QThread):
    """This custom widget based on QThread.

    Added features:

        1.read the image and turn it info QPixmap format

    Args:

        picture_list(list): The list that contains input images's path

    Emit:

        send_progress -> str: Send the current progress

        send_img_item -> tuple(img: QPixmap, picture: str): Send the tuple that contains image instance and image path
    """

    send_img_item = Signal(tuple)
    send_progress = Signal(str)

    def __init__(self, picture_list: list[str]):
        self.picture_list = picture_list
        self.is_continue = False
        super().__init__()

    def add_items(self):
        for count, picture in enumerate(self.picture_list, start=1):
            with Image.open(picture) as img:
                img.thumbnail(size=(96, 64))
                img_raw_data = img.convert("RGB").tobytes("raw", "RGB")
                img = QtGui.QImage(
                    img_raw_data,
                    img.size[0],
                    img.size[1],
                    img.size[0] * 3,
                    QtGui.QImage.Format.Format_RGB888,
                )

            img = QtGui.QPixmap.fromImage(img)

            self.send_progress.emit(f"{count} / {len(self.picture_list)}")
            self.send_img_item.emit((img, picture))
        self.send_progress.emit("無")

    def run(self):
        self.add_items()


class QListWidgetItemPlus(QtWidgets.QListWidgetItem):
    """This custom widget based on QListWidgetItem.

    Added features:

        1.add the variable 'text' on QListWidgetItem that store the file's absolute path

    Args:

        test(str): The absolute path of the image
    """

    def __init__(self, text: str):
        super().__init__()
        self.text: str = text
