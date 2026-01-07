import json
from dataclasses import dataclass, field
from pathlib import Path
from pprint import pprint
from typing import List

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QDialog,
    QFileDialog,
    QFormLayout,
    QHBoxLayout,
    QHeaderView,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

import file_folder_manager
from window import Ui_MainWindow

test_list = []


@dataclass
class Point:
    x: float
    y: float


@dataclass
class CarProfile:
    front: List[Point] = field(default_factory=list)
    side: List[Point] = field(default_factory=list)
    back: List[Point] = field(default_factory=list)


@dataclass
class CarDimensions:
    length: float
    width: float
    profile: CarProfile


@dataclass
class CarInfo:
    year: str
    number: str
    model_name: str
    oem: str
    vin: str
    sw_version: str


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setFixedSize(self.size())

        # Loading the json for the test names for the two combo boxes
        with open("test_types.json", "r", encoding="utf-8") as f:
            self.database_test_types = json.load(f)
        # Populating the first combo box
        for entry in self.database_test_types["test_list"]:
            self.ui.combo_test_type.addItem(entry["type"], entry["tests"])

        # Populating the second one everytime we select something in the first one
        self.ui.combo_test_type.currentIndexChanged.connect(self.test_type_selection)

        # Automatically populating the second one at startup
        if self.ui.combo_test_type.count() > 0:
            self.test_type_selection(self.ui.combo_test_type.currentIndex())

        table = self.ui.tableWidget

        table.setEditTriggers(QTableWidget.EditTrigger.AllEditTriggers.NoEditTriggers)
        table.horizontalHeader().setVisible(False)
        table.verticalHeader().setVisible(False)

        self.database_test_specs = test_json_loading(Path("test_json"))

        with open("robustness.json", "r", encoding="utf-8") as f:
            self.database_robustness = json.load(f)

        self.ui.button_add_new_test.clicked.connect(self.add_new_test_button_press)
        self.ui.button_create_folders.clicked.connect(self.create_folder_press)

    def test_type_selection(self, index):
        tests = self.ui.combo_test_type.itemData(index)
        self.ui.combo_test_name.clear()

        for test_name in tests:
            self.ui.combo_test_name.addItem(test_name)

    def add_new_test_button_press(self):
        selected_test_name = self.ui.combo_test_name.currentText()

        if not selected_test_name:
            return

        spec = self.database_test_specs[selected_test_name]

        # destroy previous window if needed
        if hasattr(self, "test_window"):
            self.test_window.close()

        self.test_window = TestSpecWindow(
            spec, self.database_robustness, self.ui.combo_test_type.currentText(), self
        )

        self.test_window.test_created.connect(self.on_test_created)
        self.test_window.exec()

    def on_test_created(self, test: dict):
        test_list.append(test)

        self.refresh_table()

    def refresh_table(self):
        table = self.ui.tableWidget
        table.clearContents()
        max_cols = 10

        table.setRowCount(len(test_list))
        table.setColumnCount(max_cols)

        for row_index, test in enumerate(reversed(test_list)):
            for col_index, column in enumerate(test["_ui"]["columns"]):
                item = QTableWidgetItem(column[1])
                table.setItem(row_index, col_index, item)

            button_delete_test = QPushButton("X")
            button_delete_test.setFixedWidth(30)

            button_delete_test.clicked.connect(
                lambda _, btn=button_delete_test: self.delete_test(btn)
            )

            table.setCellWidget(row_index, max_cols - 1, button_delete_test)

        for col in range(max_cols - 1):
            table.horizontalHeader().setSectionResizeMode(
                col, QHeaderView.ResizeMode.Stretch
            )

        # Set the last column to fixed width
        table.horizontalHeader().setSectionResizeMode(
            max_cols - 1, QHeaderView.ResizeMode.Fixed
        )
        table.setColumnWidth(max_cols - 1, 30)

        # print("-----------------------------------------------------------------")
        # pprint(test_list)

    def delete_test(self, button: QPushButton):
        table = self.ui.tableWidget
        index_to_delete = table.indexAt(button.pos())

        displayed_row = index_to_delete.row()

        data_row = len(test_list) - 1 - displayed_row

        del test_list[data_row]
        self.refresh_table()

    def create_folder_press(self):
        main_folder_string = QFileDialog.getExistingDirectory(
            None, "Select where you want the folder to be created: "
        )
        if not main_folder_string:
            QMessageBox.warning(self, "Warning", "No folder was selected.")
            return
        else:
            main_folder = Path(main_folder_string)
            file_folder_manager.folder_creations(
                main_folder, test_list, self.loadDimensions(), self.loadInfo()
            )
            QMessageBox.information(self, "Completed.", "The folders were created.")

    def loadDimensions(self) -> CarDimensions:
        profile = CarProfile()

        SECTIONS = ("front", "side", "back")

        for section in SECTIONS:
            for i in range(1, 8):  # 7 points each
                x_text = getattr(self.ui, f"x{i}{section.capitalize()}")
                y_text = getattr(self.ui, f"y{i}{section.capitalize()}")

                x = float(x_text.text().strip()) * 1000.0
                y = float(y_text.text().strip()) * 1000.0
                getattr(profile, section).append(Point(x, y))

        output = CarDimensions(
            length=float(self.ui.textLenght.text().strip()) * 1000.0,
            width=float(self.ui.textWidth.text().strip()) * 1000.0,
            profile=profile,
        )

        return output

    def loadInfo(self) -> CarInfo:
        output = CarInfo(
            year=self.ui.textbox_year.text().strip(),
            number=self.ui.textbox_number.text().strip(),
            model_name=self.ui.textbox_model.text().strip(),
            oem=self.ui.textbox_oem.text().strip(),
            vin=self.ui.textbox_vin.text().strip(),
            sw_version=self.ui.textbox_software.text().strip(),
        )
        return output


class TestSpecWindow(QDialog):
    test_created = Signal(dict)

    def __init__(
        self, test_spec: dict, robustness_spec: dict, macro_type: str, parent=None
    ):
        super().__init__(parent)
        self.test_spec = test_spec
        self.robustness_spec = robustness_spec
        self.macro_type = macro_type

        self.setWindowTitle(test_spec["name"])
        self._build_ui()

        self.adjustSize()
        self.setFixedSize(self.size())

        self.button_add_test.clicked.connect(self.insert_test_button_pressed)

        self.combo_robustness_type.currentIndexChanged.connect(
            self.robustness_type_selection
        )

        self.combo_robustness_layer.currentIndexChanged.connect(
            self.robustness_layer_selection
        )

    def _build_ui(self):
        # The main layout, two verical boxes, one for the columns together and one for the button
        # Here you pass "self" to say that this is the main layout
        main_layout = QVBoxLayout(self)

        self.parameter_widget = QWidget()
        self.robustness_widget = QWidget()
        # Secondary layout two orizontal boxes for the two columns
        columns_layout = QHBoxLayout()
        parameters_layout = QFormLayout(self.parameter_widget)
        robustness_layout = QFormLayout(self.robustness_widget)

        self.fixed_parameters = {"name": self.test_spec["name"]}
        self.fixed_parameters["macro_type"] = self.macro_type

        for parameter in self.test_spec["test_variables"]:
            if parameter["user_input"]:
                combo = QComboBox()
                combo.setProperty("parameter_key", parameter["key"])
                for option in parameter["options"]:
                    combo.addItem(option["label"], option["value"])

                idx = combo.findData(parameter["default"])
                if idx >= 0:
                    combo.setCurrentIndex(idx)

                parameters_layout.addRow(parameter["display_name"], combo)
            else:
                self.fixed_parameters[parameter["key"]] = parameter["value"]

        self.combo_robustness_type = QComboBox()
        self.combo_robustness_layer = QComboBox()
        self.combo_robustness_parameter = QComboBox()

        for robustness_type in self.robustness_spec["robustness"]:
            self.combo_robustness_type.addItem(
                robustness_type["display_name"], robustness_type
            )

        robustness_layout.addRow("Robustness Type", self.combo_robustness_type)
        robustness_layout.addRow("Robustness Layer", self.combo_robustness_layer)
        robustness_layout.addRow(
            "Robustness Parameter", self.combo_robustness_parameter
        )

        columns_layout.addWidget(self.parameter_widget)
        columns_layout.addWidget(self.robustness_widget)

        self.button_add_test = QPushButton("Insert Test")
        main_layout.addLayout(columns_layout)
        main_layout.addWidget(self.button_add_test)

        if self.combo_robustness_type.count() > 0:
            self.robustness_type_selection(self.combo_robustness_type.currentIndex())

    def insert_test_button_pressed(self):
        current_test_property = self.fixed_parameters.copy()
        current_test_property["_ui"] = {}
        current_test_property["_ui"]["columns"] = []
        current_test_property["_ui"]["columns"].append(
            ("name", current_test_property["name"])
        )

        for combo in self.parameter_widget.findChildren(QComboBox):
            key = combo.property("parameter_key")
            current_test_property[key] = combo.currentData()
            current_test_property["_ui"]["columns"].append((key, combo.currentText()))

        # Managing the robustness
        type_key = self.combo_robustness_type.currentData()["key"]
        current_test_property["robustness_type"] = type_key
        current_test_property["_ui"]["columns"].append(
            ("robustness_type", self.combo_robustness_type.currentText())
        )

        if not self.combo_robustness_type.currentData()["layers"]:
            self.test_created.emit(current_test_property)
            return

        layer_key = self.combo_robustness_layer.currentData()["key"]
        current_test_property["robustness_layer"] = layer_key
        current_test_property["_ui"]["columns"].append(
            ("robustness_layer", self.combo_robustness_layer.currentText())
        )

        if not self.combo_robustness_layer.currentData()["options"]:
            self.test_created.emit(current_test_property)
            return

        parameter_value = self.combo_robustness_parameter.currentData()
        current_test_property["robustness_parameter"] = parameter_value
        current_test_property["_ui"]["columns"].append(
            ("robustness_parameter", self.combo_robustness_parameter.currentText())
        )

        self.test_created.emit(current_test_property)

    def robustness_type_selection(self, index):
        self.combo_robustness_layer.clear()
        self.combo_robustness_parameter.clear()

        layers = self.combo_robustness_type.currentData()["layers"]

        if not layers:
            self.combo_robustness_layer.setEnabled(False)
            self.combo_robustness_parameter.setEnabled(False)
            return

        self.combo_robustness_layer.setEnabled(True)
        for layer in layers:
            self.combo_robustness_layer.addItem(layer["display_name"], layer)

        self.robustness_layer_selection(index)

    def robustness_layer_selection(self, index):
        self.combo_robustness_parameter.clear()
        layer = self.combo_robustness_layer.currentData()

        if not layer:
            self.combo_robustness_parameter.setEnabled(False)
            return

        options = layer.get("options")

        if not options:
            self.combo_robustness_parameter.setEnabled(False)
            return

        self.combo_robustness_parameter.setEnabled(True)

        for option in options:
            self.combo_robustness_parameter.addItem(option["label"], option["value"])


def test_json_loading(folder: Path) -> dict:
    output = {}

    for path in folder.glob("*.json"):
        with open(path) as f:
            spec = json.load(f)
            output[spec["name"]] = spec

    return output


if __name__ == "__main__":
    app = QApplication([])
    w = MainWindow()
    w.show()
    app.exec()
