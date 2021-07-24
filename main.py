# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
from time import sleep
import json
import sys
import re
from os import listdir
from os.path import isfile, join
from tempfile import TemporaryDirectory, TemporaryFile

from skimage import exposure
import numpy as np
from PIL import Image
# from PIL.ImageQt import ImageQt

from PySide6.QtWidgets import QTableWidgetItem, QApplication, QMainWindow, QPushButton, QFileDialog, QLabel
from PySide6.QtCore import Slot, QObject, Qt
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from ui_main import Ui_main_window

from pydicom.datadict import dictionary_VR
from pydicom.uid import ImplicitVRLittleEndian
from pydicom.tag import TagType
from pydicom.filewriter import write_file_meta_info
from pynetdicom.sop_class import VerificationSOPClass, CTImageStorage
from pynetdicom import AE
from pynetdicom import evt, AllStoragePresentationContexts
from pydicom.fileset import FileSet
from pydicom import dcmread
from datetime import datetime

import matplotlib.pyplot as plt


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_main_window()
        self.ui.setupUi(self)
        self.ui.push_button_check_file.setEnabled(False)
        self.ui.plain_text_edit_results.setPlainText("Приложение запущено. Выберите файл...")
        self.ui.push_button_open_file.clicked.connect(self.open_file)
        self.ui.push_button_check_file.clicked.connect(self.check_file)
        self.ui.push_button_anonimize.clicked.connect(self.anonymize)
        self.ui.push_button_check_server.clicked.connect(self.check_server)
        self.ui.line_edit_server.returnPressed.connect(self.check_server)
        self.ui.push_button_send_file.clicked.connect(self.send_file)
        self.ui.push_button_start_server.clicked.connect(self.start_server)
        # self.ui.push_button_show_content.clicked.connect(self.show_content)
        self.ui.push_button_clear_logs.clicked.connect(self.clear_logs)
        self.ui.plain_text_edit_results.clear()
        self.ui.label_3.hide()
        self.ui.push_button_send_result.hide()
        self.ui.push_button_show_content.hide()
        self.ui.label_status.hide()
        self.ui.groupBox_files.hide()
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.table_widget_files.setColumnCount(1)
        self.ui.table_widget_files.horizontalHeader().hide()
        self.ui.table_widget_files.itemClicked.connect(self.show_local_file)
        self.ui.table_widget_results.setColumnCount(1)
        self.ui.table_widget_results.horizontalHeader().hide()
        self.ui.table_widget_results.horizontalHeader().setDefaultSectionSize(300)
        self.ui.table_widget_results.itemClicked.connect(self.show_result_file)
        # self.ds = None
        CALLING_AET = 'AE_TEST'  # имя данного клиента
        self.ae = AE(ae_title=CALLING_AET)
        self.ae.add_requested_context(VerificationSOPClass)
        self.addr = '127.0.0.1'
        self.port = 11112
        self.req_contexts = []
        # self.called_ae_title = None  # имя удаленного пакса/сервера
        self.temp_dir = TemporaryDirectory()
        print(f"temp_dir - {self.temp_dir}")

    def closeEvent(self, event):
        print("close event")
        self.temp_dir.cleanup()
        self.ae.shutdown()
        if True:
            event.accept() # let the window close
        else:
            event.ignore()

    @Slot()
    def clear_logs(self):
        self.ui.plain_text_edit_results.clear()
        self.add_result("Логи очищены")

    def view_file(self, file, label):
        if file.exists():
            ds = dcmread(file, force=True)

            plt.figure(figsize=(6, 6), dpi=100)
            p_lo, p_hi = np.percentile(ds.pixel_array, (20, 99.5))
            img_rescale = exposure.rescale_intensity(ds.pixel_array, in_range=(p_lo, p_hi))
            # plt.imshow(img_rescale, cmap=plt.cm.gray)
            # plt.show()

            path = Path.joinpath(Path(self.temp_dir.name), file.name)
            path = path.with_suffix('.jpg')
            plt.imsave(path, img_rescale, cmap=plt.cm.gray)
            image = QImage()
            image.load(str(path))
            pixmap = QPixmap.fromImage(image)
            pixmap = pixmap.scaled(label.size().width(), label.size().width(),
                                   Qt.KeepAspectRatio,
                                   Qt.SmoothTransformation)
            label.setPixmap(pixmap)

    @Slot(QTableWidgetItem)
    def show_local_file(self, item):
        # print(item.text())
        path = self.ui.label_file_path.text()
        file = Path.joinpath(Path(path), item.text())
        self.add_result(f"Просмотр файла - {file}")
        # ds = dcmread(f, force=True)
        self.view_file(file, self.ui.label_image_view)


    @Slot(QTableWidgetItem)
    def show_result_file(self, item):
        # print(item.text())
        file = Path(item.text())
        self.add_result(f"Просмотр файла - {file}")
        # ds = dcmread(f, force=True)
        self.view_file(file, self.ui.label_result_image_view)

    # @Slot()
    # def show_content(self):
    #     print("show content")
    #     self.add_result("Будет показано только последнее изображении в серии")
    #     # image_window = QLabel("", self)
    #     path = self.ui.label_file_path.text()
    #     files = sorted([p for p in Path(path).glob('**/*') if p.is_file()])
    #     try:
    #         for f in files[::-1]:
    #             ds = dcmread(f, force=True)
    #             # # print(ds.file_meta.TransferSyntaxUID)
    #             # if 'TransferSyntaxUID' not in ds.file_meta.elements():
    #             #     ds.file_meta.add_new([0x0002, 0x0010], 'UI', '1.2.840.10008.1.2')
    #             #     # (0002, 0010) Transfer Syntax UID                 UI: Explicit VR Little Endian
    #             #
    #             #     # ds.file_meta['TransferSyntaxUID'] = '1.2.840.10008.1.2'  # ImplicitVRLittleEndian
    #             # print(ds.file_meta.TransferSyntaxUID)
    #             # im = self.get_PIL_image(ds)
    #             # # im.show()
    #             # image_qt = ImageQt(im)
    #             # image = QImage(image_qt)
    #             # pixmap = QPixmap.fromImage(image)
    #             # self.ui.label_image_view.setPixmap(pixmap)
    #             # self.ui.label_image_view.update()
    #             # image_window.show()
    #             # break

    #             # plt.imshow(ds.pixel_array, cmap=plt.cm.gray)

    #             plt.figure(figsize=(6, 6), dpi=100)
    #             p_lo, p_hi = np.percentile(ds.pixel_array, (20, 99.5))
    #             img_rescale = exposure.rescale_intensity(ds.pixel_array, in_range=(p_lo, p_hi))
    #             # plt.imshow(img_rescale, cmap=plt.cm.gray)
    #             # plt.show()

    #             path = Path.joinpath(Path(self.temp_dir.name), f.name)
    #             path = path.with_suffix('.jpg')
    #             plt.imsave(path, img_rescale, cmap=plt.cm.gray)
    #             image = QImage()
    #             image.load(str(path))
    #             pixmap = QPixmap.fromImage(image)
    #             self.ui.label_image_view.setPixmap(pixmap)
    #             break
    #     # except AttributeError as exc:
    #     #     print('AttributeError:')
    #     #     print(exc)
    #     finally:
    #         pass

    @Slot()
    def start_server(self):
        port = self.ui.line_edit_local_server_port.text()
        ae_title = self.ui.line_edit_local_server_ae_title.text()
        directory = self.ui.line_edit_result_dir.text()
        self.add_result(f"Запускаем сервер на порту {port}. Результаты будут сохранены в папку - {directory}")
        if 0 < int(port) < 65536:
            handlers = [(evt.EVT_C_STORE, self.handle_store, [directory])]
            # self.ae.add_supported_context(CTImageStorage)
            # Support presentation contexts for all storage SOP Classes
            self.ae.supported_contexts = AllStoragePresentationContexts
            # Start listening for incoming association requests
            self.ae.start_server(('', int(port)), ae_title=ae_title, block=False, evt_handlers=handlers)
            self.add_result("Сервер запущен")


    @Slot()
    def send_file(self):
        if self.addr and self.port:
            assoc = self.ae.associate(addr=self.addr, port=self.port)

            path = self.ui.label_file_path.text()
            files = sorted([p for p in Path(path).glob('**/*') if p.is_file()])
            for f in files:
                self.add_result(f"Выполняем тестовую отправку файла '{f.name}' на сервер '{self.addr}:{self.port}'")
                ds = dcmread(f)
                if assoc.is_established:
                    status = assoc.send_c_store(ds)
                    # Check the status of the verification request
                    if status:
                        # If the verification request succeeded this will be 0x0000
                        self.add_result('Успешно! Status: 0x{0:04x}'.format(status.Status))
                        self.ui.label_status.setText("Файл отправлен")
                    else:
                        self.add_result('Ошибка: Connection timed out, was aborted or received invalid response')
                else:
                    self.add_result('Ошибка: Association rejected, aborted or never connected')

            assoc.release()

    @Slot()
    def check_server(self):
        host = self.ui.line_edit_server.text()
        ae_title = self.ui.line_edit_dest_ae_title.text()
        addr, port = host.split(":")
        if re.match(r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",
                    addr) and 0 < int(port) < 65536:
            self.addr, self.port = addr, int(port)
            self.add_result(f"Введен валидный адрес хоста addr = {self.addr}, port = {self.port}. "
                            f"Отправляем ECHO-запрос на {ae_title}...")

            assoc = self.ae.associate(addr=self.addr, port=self.port, ae_title=ae_title)
            if assoc.is_established:
                status = assoc.send_c_echo()
                # Check the status of the verification request
                if status:
                    # If the verification request succeeded this will be 0x0000
                    self.add_result('Успешно! C-ECHO request status: 0x{0:04x}'.format(status.Status))
                    self.ui.label_status.setText("Сервер доступен")
                else:
                    self.add_result('Ошибка: Connection timed out, was aborted or received invalid response')
                # Release the association
                assoc.release()
            else:
                self.add_result('Ошибка: Association rejected, aborted or never connected')
            del assoc

    @Slot()
    def anonymize(self):
        # https://pydicom.github.io/pydicom/stable/auto_examples/metadata_processing/plot_anonymize.html
        # self.ds = ...
        print("anonymized")

    @Slot()
    def open_file(self):
        dialog = QFileDialog(self, self.tr("Выберите каталог с исследованиями в DICOM-формате"))
        dialog.setFileMode(QFileDialog.Directory)
        # dialog.setNameFilter(self.tr("DICOM Files (*.dcm *.dicom)"))
        dialog.setViewMode(QFileDialog.List)
        file_names = []
        if dialog.exec():
            file_names = dialog.selectedFiles()
        if file_names:
            self.add_result(f"Была выбрана папка - {file_names[0]}")
            self.ui.label_file_path.setText(file_names.pop())
            self.ui.push_button_check_file.setEnabled(True)

    @Slot()
    def check_file(self):
        self.ui.table_widget_files.model().removeRows(0, self.ui.table_widget_files.rowCount())
        path = self.ui.label_file_path.text()
        # files = [f for f in listdir(path) if isfile(join(path, f))]
        # files = list(Path(path).rglob("*"))
        files = sorted([p for p in Path(path).glob('**/*') if p.is_file()])
        print(files)
        self.add_result(f"Каталог содержит {len(files)} файлов")
        for f in files:
            if f.is_file():
                ds = dcmread(f)
                if ds:
                    self.add_result(f"\nПроверка файла - {f.name}:")
                    # self.add_result(f"File path........: {path}")
                    self.add_result(f"SOP Class........: {ds.SOPClassUID} ({ds.SOPClassUID.name})")
                    self.add_result(f"File meta........:\n {ds.file_meta}")
                    self.add_result(f"Patient ID.......: {ds.PatientID}")
                    self.add_result(f"Modality.........: {ds.Modality}")
                    self.add_result(f"Instance Number..: {ds.InstanceNumber}")
                    self.add_result(f"Image size.......: {ds.Rows} x {ds.Columns}")
                    # self.add_result(f"Pixel Spacing....: {ds.PixelSpacing}")

                    json_data = json.loads(ds.to_json())
                    del json_data["7FE00010"]
                    json_formatted_str = json.dumps(json_data, indent=2)
                    self.add_result(f"JSON:")
                    self.add_result(json_formatted_str)

                    num_rows = self.ui.table_widget_files.rowCount()
                    self.ui.table_widget_files.insertRow(num_rows)
                    # Add text to the row
                    self.ui.table_widget_files.setItem(num_rows, 0, QTableWidgetItem(f.name))
                    # self.ui.table_widget_files.setItem(num_rows, 1, QTableWidgetItem(ds.InstanceNumber))
                    # self.ui.table_widget_files.setItem(num_rows, 2, QTableWidgetItem(z))

                    if ds.SOPClassUID not in self.req_contexts:
                        self.req_contexts.append(ds.SOPClassUID)
                        self.ae.add_requested_context(ds.SOPClassUID)
                    self.ui.push_button_send_file.setEnabled(True)
                    self.ui.push_button_show_content.setEnabled(True)
                    self.ui.label_status.setText("Файл валидный")

    def add_result(self, text):
        print(f"{datetime.now()} - {text}")
        self.ui.plain_text_edit_results.insertPlainText(self.tr(text) + '\n')
        self.ui.plain_text_edit_results.verticalScrollBar().setValue(
            self.ui.plain_text_edit_results.verticalScrollBar().maximum()
        )
        self.ui.plain_text_edit_results.ensureCursorVisible()

    # Implement a handler for evt.EVT_C_STORE
    def handle_store(self, event, storage_dir):
        """Handle a C-STORE request event."""

        try:
            os.makedirs(storage_dir, exist_ok=True)
        except:
            # Unable to create output dir, return failure status
            return 0xC001

        # Decode the C-STORE request's *Data Set* parameter to a pydicom Dataset
        # ds = event.dataset

        self.add_result(f"Получено входящее исследование/результат - {event.request.AffectedSOPInstanceUID}")

        # We rely on the UID from the C-STORE request instead of decoding
        fname = os.path.join(storage_dir, "{}.dcm".format(event.request.AffectedSOPInstanceUID))
        with open(fname, 'wb') as f:
            # Write the preamble, prefix and file meta information elements
            f.write(b'\x00' * 128)
            f.write(b'DICM')
            write_file_meta_info(f, event.file_meta)
            # Write the raw encoded dataset
            f.write(event.request.DataSet.getvalue())
            self.add_result(f"Файл сохранен - {fname}")
            self.ui.label_status.setText("Результат получен")
            self.statusBar().setStatusTip("aaa")

        num_rows = self.ui.table_widget_results.rowCount()
        self.ui.table_widget_results.insertRow(num_rows)
        self.ui.table_widget_results.setItem(num_rows, 0, QTableWidgetItem(fname))

        #
        # # Add the File Meta Information
        # ds.file_meta = event.file_meta
        #
        # # Save the dataset using the SOP Instance UID as the filename
        # ds.save_as(ds.SOPInstanceUID, write_like_original=False)

        # Return a 'Success' status
        return 0x0000

    def get_LUT_value(self, data, window, level):
        """Apply the RGB Look-Up Table for the given
           data and window/level value."""
        return np.piecewise(data,
                            [data <= (level - 0.5 - (window - 1) / 2),
                             data > (level - 0.5 + (window - 1) / 2)],
                            [0, 255, lambda data: ((data - (level - 0.5)) /
                                                   (window - 1) + 0.5) * (255 - 0)])

    def get_PIL_image(self, dataset):
        """Get Image object from Python Imaging Library(PIL)"""
        if 'PixelData' not in dataset:
            raise TypeError("Cannot show image -- DICOM dataset does not have "
                            "pixel data")
        # can only apply LUT if these window info exists
        if ('WindowWidth' not in dataset) or ('WindowCenter' not in dataset):
            bits = dataset.BitsAllocated
            samples = dataset.SamplesPerPixel
            if bits == 8 and samples == 1:
                mode = "L"
            elif bits == 8 and samples == 3:
                mode = "RGB"
            elif bits == 16:
                # not sure about this -- PIL source says is 'experimental'
                # and no documentation. Also, should bytes swap depending
                # on endian of file and system??
                mode = "I;16"
            else:
                raise TypeError("Don't know PIL mode for %d BitsAllocated "
                                "and %d SamplesPerPixel" % (bits, samples))

            # PIL size = (width, height)
            size = (dataset.Columns, dataset.Rows)

            # Recommended to specify all details
            # by http://www.pythonware.com/library/pil/handbook/image.htm
            im = Image.frombuffer(mode, size, dataset.PixelData,
                                      "raw", mode, 0, 1)

        else:
            ew = dataset['WindowWidth']
            ec = dataset['WindowCenter']
            ww = int(ew.value[0] if ew.VM > 1 else ew.value)
            wc = int(ec.value[0] if ec.VM > 1 else ec.value)
            image = self.get_LUT_value(dataset.pixel_array, ww, wc)
            # Convert mode to L since LUT has only 256 values:
            #   http://www.pythonware.com/library/pil/handbook/image.htm
            im = Image.fromarray(image).convert('L')

        return im


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
