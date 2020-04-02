# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\wkspaces\spectrum_visualizer\spectrum_visualizer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from real_time_spectrum_controller import RealTimeSpectrumController
import pyqtgraph as pg


class SpectrumVisualizerView:
    def __init__(self, controller: RealTimeSpectrumController, form):
        self._controller = controller
        self.setupUi(form)
        self.fill_defaults()
        self.connect_signals()
        self.plot_window = pg.GraphicsWindow()
        self.spectrum_plot = self.plot_window.addPlot()
        self.plot_window_layout.addWidget(self.plot_window)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(981, 370)
        self.input_options_box = QtWidgets.QGroupBox(Form)
        self.input_options_box.setGeometry(QtCore.QRect(664, 10, 311, 181))
        self.input_options_box.setObjectName("input_options_box")
        self.gridLayout = QtWidgets.QGridLayout(self.input_options_box)
        self.gridLayout.setObjectName("gridLayout")
        self.output_device_combo_box = QtWidgets.QComboBox(self.input_options_box)
        self.output_device_combo_box.setObjectName("output_device_combo_box")
        self.gridLayout.addWidget(self.output_device_combo_box, 3, 1, 1, 1)
        self.chunk_size_text_field = QtWidgets.QLineEdit(self.input_options_box)
        self.chunk_size_text_field.setObjectName("chunk_size_text_field")
        self.gridLayout.addWidget(self.chunk_size_text_field, 5, 1, 1, 1)
        self.input_device_label = QtWidgets.QLabel(self.input_options_box)
        self.input_device_label.setObjectName("input_device_label")
        self.gridLayout.addWidget(self.input_device_label, 1, 0, 1, 1)
        self.chunk_size_label = QtWidgets.QLabel(self.input_options_box)
        self.chunk_size_label.setObjectName("chunk_size_label")
        self.gridLayout.addWidget(self.chunk_size_label, 5, 0, 1, 1)
        self.sample_rate_text_field = QtWidgets.QLineEdit(self.input_options_box)
        self.sample_rate_text_field.setObjectName("sample_rate_text_field")
        self.gridLayout.addWidget(self.sample_rate_text_field, 6, 1, 1, 1)
        self.output_device_label = QtWidgets.QLabel(self.input_options_box)
        self.output_device_label.setObjectName("output_device_label")
        self.gridLayout.addWidget(self.output_device_label, 2, 0, 2, 1)
        self.host_api_label = QtWidgets.QLabel(self.input_options_box)
        self.host_api_label.setObjectName("host_api_label")
        self.gridLayout.addWidget(self.host_api_label, 0, 0, 1, 1)
        self.host_api_combo_box = QtWidgets.QComboBox(self.input_options_box)
        self.host_api_combo_box.setObjectName("host_api_combo_box")
        self.gridLayout.addWidget(self.host_api_combo_box, 0, 1, 1, 1)
        self.input_device_combo_box = QtWidgets.QComboBox(self.input_options_box)
        self.input_device_combo_box.setObjectName("input_device_combo_box")
        self.gridLayout.addWidget(self.input_device_combo_box, 1, 1, 2, 1)
        self.sample_rate_label = QtWidgets.QLabel(self.input_options_box)
        self.sample_rate_label.setObjectName("sample_rate_label")
        self.gridLayout.addWidget(self.sample_rate_label, 6, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.input_options_box)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 4, 1, 1, 1)
        self.in_channel_idx_label = QtWidgets.QLabel(self.input_options_box)
        self.in_channel_idx_label.setObjectName("in_channel_idx_label")
        self.gridLayout.addWidget(self.in_channel_idx_label, 4, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(660, 200, 311, 51))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.nfft_label = QtWidgets.QLabel(self.groupBox)
        self.nfft_label.setObjectName("nfft_label")
        self.gridLayout_2.addWidget(self.nfft_label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.nfft_text_field = QtWidgets.QLineEdit(self.groupBox)
        self.nfft_text_field.setObjectName("nfft_text_field")
        self.gridLayout_2.addWidget(self.nfft_text_field, 0, 2, 1, 1)
        self.start_button = QtWidgets.QPushButton(Form)
        self.start_button.setGeometry(QtCore.QRect(700, 330, 91, 31))
        self.start_button.setObjectName("start_button")
        self.stop_button = QtWidgets.QPushButton(Form)
        self.stop_button.setGeometry(QtCore.QRect(840, 330, 91, 31))
        self.stop_button.setObjectName("stop_button")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 641, 351))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.plot_window_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.plot_window_layout.setContentsMargins(0, 0, 0, 0)
        self.plot_window_layout.setObjectName("plot_window_layout")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.input_options_box.setTitle(_translate("Form", "Input options"))
        self.host_api_label.setText(_translate("Form", "host API"))
        self.input_device_label.setText(_translate("Form", "input device"))
        self.output_device_label.setText(_translate("Form", "output device"))
        self.chunk_size_label.setText(_translate("Form", "chunk size"))
        self.sample_rate_label.setText(_translate("Form", "sample rate"))
        self.in_channel_idx_label.setText(_translate("Form", "in channel idx label"))
        self.groupBox.setTitle(_translate("Form", "Spectrum options"))
        self.nfft_label.setText(_translate("Form", "nfft"))
        self.start_button.setText(_translate("Form", "Start"))
        self.stop_button.setText(_translate("Form", "Stop"))

    def connect_signals(self):
        self.host_api_combo_box.currentIndexChanged.connect(self.on_host_api_change)
        self.input_device_combo_box.currentIndexChanged.connect(self.on_input_device_change)
        self.output_device_combo_box.currentIndexChanged.connect(self.on_output_device_change)
        self.start_button.pressed.connect(self.on_start_button_press)
        self.stop_button.pressed.connect(self.on_stop_button_press)

    def fill_defaults(self):
        self.fill_host_api_combo_box()
        self.fill_input_device_list()
        self.fill_output_device_list()
        self.mark_current_input_device()
        self.mark_current_output_device()
        self.fill_chunk_size_text_box()
        self.fill_sample_rate_text_box()
        self.fill_nfft_text_box()

    def fill_host_api_combo_box(self):
        host_api_names = self._controller.get_all_host_api_names()
        self.host_api_combo_box.addItems(host_api_names)
        index = self.host_api_combo_box.findText(self._controller.host_api_name)
        self.host_api_combo_box.setCurrentIndex(index)

    def fill_input_device_list(self):
        self.input_device_combo_box.clear()
        host_api_name = self.host_api_combo_box.currentText()
        input_devices_names = self._controller.get_input_devices_names_by_host_api_name(host_api_name)
        self.input_device_combo_box.addItems(input_devices_names)

    def fill_output_device_list(self):
        self.output_device_combo_box.clear()
        host_api_name = self.host_api_combo_box.currentText()
        output_devices_names = self._controller.get_output_devices_names_by_host_api_name(host_api_name)
        self.output_device_combo_box.addItems(output_devices_names)

    def mark_current_input_device(self):
        input_device_name = self._controller.input_device_name
        index = self.input_device_combo_box.findText(input_device_name)
        self.input_device_combo_box.setCurrentIndex(index)

    def mark_current_output_device(self):
        output_device_name = self._controller.output_device_name
        index = self.output_device_combo_box.findText(output_device_name)
        self.output_device_combo_box.setCurrentIndex(index)

    def fill_chunk_size_text_box(self):
        chunk_size = self._controller.chunk_size
        self.chunk_size_text_field.setText(str(chunk_size))

    def fill_sample_rate_text_box(self):
        sample_rate = self._controller.sample_rate
        self.sample_rate_text_field.setText(str(sample_rate))

    def fill_nfft_text_box(self):
        nfft = self._controller.nfft
        self.nfft_text_field.setText(str(nfft))

    def on_host_api_change(self):
        self.fill_input_device_list()
        self.fill_output_device_list()

        input_device_name = self.input_device_combo_box.currentText()
        output_device_name = self.output_device_combo_box.currentText()

        self._controller.set_input_device_by_name(input_device_name)
        self._controller.set_output_device_by_name(output_device_name)

    def on_input_device_change(self):
        input_device_name = self.input_device_combo_box.currentText()
        self._controller.set_input_device_by_name(input_device_name)

    def on_output_device_change(self):
        output_device_name = self.output_device_combo_box.currentText()
        self._controller.set_output_device_by_name(output_device_name)

    def on_start_button_press(self):
        self._controller.start_stream()

    def on_stop_button_press(self):
        self._controller.stop_stream()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()

    controller = RealTimeSpectrumController()
    ui = SpectrumVisualizerView(controller, Form)

    Form.show()
    sys.exit(app.exec_())
