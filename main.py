import json
from dataclasses import dataclass
from pathlib import Path
from pprint import pprint

from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QDialog,
    QFormLayout,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from window import Ui_MainWindow


@dataclass
class Robustness:
    type: str
    robustness: str
    parameter: str


@dataclass
class Test:
    name: str
    type: str
    test_condition: str
    long_speed_VUT: float
    lat_speed_VUT: float
    impact_side: str
    overlap: int
    target_type: str
    target_speed: float
    target_accelleration: float
    target_heading: float
    robustness: Robustness


test_list = []


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

        self.database_test_specs = test_json_loading(Path("test_json"))

        self.ui.button_add_new_test.clicked.connect(self.add_new_test_button_press)

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

        self.test_window = TestSpecWindow(spec, self)
        self.test_window.exec()


class TestSpecWindow(QDialog):
    def __init__(self, test_spec: dict, parent=None):
        super().__init__(parent)
        self.test_spec = test_spec
        self.setWindowTitle(test_spec["name"])
        self._build_ui()

        self.adjustSize()
        self.setFixedSize(self.size())

        self.button_add_test.clicked.connect(self.insert_test_button_pressed)

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

    def insert_test_button_pressed(self):
        current_test_property = self.fixed_parameters.copy()
        current_test_property["_ui"] = {}

        for combo in self.parameter_widget.findChildren(QComboBox):
            key = combo.property("parameter_key")
            current_test_property[key] = combo.currentData()
            current_test_property["_ui"][key] = combo.currentText()

        test_list.append(current_test_property)

        pprint(test_list)


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
