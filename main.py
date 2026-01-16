import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import List

from PySide6.QtCore import QLocale, Signal
from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QDialog,
    QFileDialog,
    QFormLayout,
    QHBoxLayout,
    QHeaderView,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

# test altro commento
import file_folder_manager

# Imports the main UI from the window.py file that is generated from window.ui
from window import Ui_MainWindow

test_list = []


# Data structure definition for easier management of the car dimensions to create the .mme file
@dataclass
class Point:
    x: float
    y: float


@dataclass
class CarProfile:
    front: List[Point] = field(default_factory=list)
    left: List[Point] = field(default_factory=list)
    back: List[Point] = field(default_factory=list)
    right: List[Point] = field(default_factory=list)


@dataclass
class CarDimensions:
    length: float
    width: float
    overhang: float
    profile: CarProfile


@dataclass
class CarInfo:
    year: str
    number: str
    make: str
    model: str
    oem: str
    vin: str
    sw_version: str


# MainWindow class that manages the whole program
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

        # Making the text boxes only accept floats values
        self.apply_float_validators()

        # Loading the database with all the test spec in the folder /test_json
        self.database_test_specs = test_json_loading(Path("test_json"))

        # Loading the robustness
        with open("robustness.json", "r", encoding="utf-8") as f:
            self.database_robustness = json.load(f)

        # Conneting the clicking of the two buttons with the functions
        self.ui.button_add_new_test.clicked.connect(self.add_new_test_button_press)
        self.ui.button_create_folders.clicked.connect(self.create_folder_press)

    # Populating the second combo box everytime the first one is selected
    def test_type_selection(self, index):
        tests = self.ui.combo_test_type.itemData(index)
        self.ui.combo_test_name.clear()

        for test_name in tests:
            self.ui.combo_test_name.addItem(test_name)

    # Creating the second window when you press the New Test Button
    def add_new_test_button_press(self):
        selected_test_name = self.ui.combo_test_name.currentText()

        # If there is not test selected in the second combo box it doesnt do anything
        if not selected_test_name:
            return

        spec = self.database_test_specs[selected_test_name]

        # Destroy previous window if needed
        if hasattr(self, "test_window"):
            self.test_window.close()

        self.test_window = TestSpecWindow(
            spec, self.database_robustness, self.ui.combo_test_type.currentText(), self
        )

        self.test_window.test_created.connect(self.on_test_created)
        self.test_window.exec()

    # Appending the new test to the list and updating the table to show the new added test
    def on_test_created(self, test: dict):
        test_list.append(test)
        self.refresh_table()

    def refresh_table(self):
        table = self.ui.tableWidget
        table.clearContents()
        # Max number of column in the table, 10 seemed like a good compromise, can be increased
        max_cols = 10

        table.setRowCount(len(test_list))
        table.setColumnCount(max_cols)

        # The list is reversed so the new tests are at the top
        for row_index, test in enumerate(reversed(test_list)):
            # In the test dictionary is present both the actual data that needs to be added
            # and a "_ui" part that manages what is shown in the table
            for col_index, column in enumerate(test["_ui"]["columns"]):
                item = QTableWidgetItem(column[1])
                table.setItem(row_index, col_index, item)

            # Adding the delete button at the end and managing the deletion
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

    def delete_test(self, button: QPushButton):
        table = self.ui.tableWidget
        index_to_delete = table.indexAt(button.pos())

        displayed_row = index_to_delete.row()

        # The items are displayed backwards in the table but are "normal" in the data list
        # so this is why we need to do this
        data_row = len(test_list) - 1 - displayed_row
        del test_list[data_row]
        self.refresh_table()

    def create_folder_press(self):
        for text_box in self.findChildren(QLineEdit):
            if text_box.text() == "":
                QMessageBox.warning(
                    self, "Warning", "Some veichle information is missing."
                )
                return

        # Selection of the folder
        main_folder_string = QFileDialog.getExistingDirectory(
            None, "Select where you want the folder to be created: "
        )
        if not main_folder_string:
            QMessageBox.warning(self, "Warning", "No folder was selected.")
            return
        else:
            main_folder = Path(main_folder_string)
            # Creation of the folders
            file_folder_manager.folder_creations(
                main_folder, test_list, self.loadDimensions(), self.loadInfo()
            )
            QMessageBox.information(self, "Completed.", "The folders were created.")

    def loadDimensions(self) -> CarDimensions:
        profile = CarProfile()
        SECTIONS = ("front", "side", "back")

        # Parsing of the text in the dimension tab, the textboxes are named like
        # x1Front,y1Front etc..., so that text is for that

        # Front
        front_profile = []
        for i in range(1, 8):
            x_text = getattr(self.ui, f"x{i}{'Front'}")
            y_text = getattr(self.ui, f"y{i}{'Front'}")
            x = float(x_text.text().strip()) * 1000.0
            y = float(y_text.text().strip()) * 1000.0
            front_profile.append(Point(x, y))

        front_profile.reverse()
        profile.front = front_profile

        # Right
        right_profile = []
        for i in range(1, 6):
            x_text = getattr(self.ui, f"x{i}{'Side'}")
            y_text = getattr(self.ui, f"y{i}{'Side'}")
            x = float(x_text.text().strip()) * 1000.0
            y = float(y_text.text().strip()) * 1000.0
            right_profile.append(Point(x, y))

        right_profile.reverse()
        profile.right = right_profile

        # Left
        left_profile = []
        for point in profile.right:
            left_profile.append(Point(point.x, -point.y))

        left_profile.reverse()
        profile.left = left_profile

        # Back
        back_profile = []
        for i in range(1, 8):
            x_text = getattr(self.ui, f"x{i}{'Back'}")
            y_text = getattr(self.ui, f"y{i}{'Back'}")
            x = float(x_text.text().strip()) * 1000.0
            y = float(y_text.text().strip()) * 1000.0
            back_profile.append(Point(x, y))

        profile.back = back_profile

        # Same thing for the other dimentions
        output = CarDimensions(
            length=float(self.ui.textLenght.text().strip()) * 1000.0,
            width=float(self.ui.textWidth.text().strip()) * 1000.0,
            overhang=float(self.ui.textOverhang.text().strip()) * 1000.0,
            profile=profile,
        )

        return output

    # Loading the main car info
    def loadInfo(self) -> CarInfo:
        output = CarInfo(
            year=self.ui.textbox_year.text().strip(),
            number=self.ui.textbox_number.text().strip(),
            make=self.ui.textbox_make.text().strip(),
            model=self.ui.textbox_model.text().strip(),
            oem=self.ui.textbox_oem.text().strip(),
            vin=self.ui.textbox_vin.text().strip(),
            sw_version=self.ui.textbox_software.text().strip(),
        )
        return output

    # Make sure that the dimension textboxes accept only numbers (and points)
    def apply_float_validators(self):
        validator = QDoubleValidator(0, 100, 2)
        validator.setLocale(QLocale(QLocale.Language.English))

        for dimenstion_text_boxes in self.ui.tab_dimensions.findChildren(QLineEdit):
            dimenstion_text_boxes.setValidator(validator)


# The class for the dialog window that pops-up when you press "Add a new test"
class TestSpecWindow(QDialog):
    test_created = Signal(dict)

    def __init__(
        self, test_spec: dict, robustness_spec: dict, macro_type: str, parent=None
    ):
        super().__init__(parent)
        # Saving in the function the database with the test and robustness parameters
        self.test_spec = test_spec
        self.robustness_spec = robustness_spec
        # The "macro type" is needed for the creation of the top-level folder
        # (AEBC, AEBB, etc...)
        self.macro_type = macro_type

        self.setWindowTitle(test_spec["name"])
        self._build_ui()

        self.adjustSize()
        self.setFixedSize(self.size())

        self.button_add_test.clicked.connect(self.insert_test_button_pressed)

        # Update of the Robustness Type combobox and Robustness Layer combobox depending
        # on the selection
        self.combo_robustness_type.currentIndexChanged.connect(
            self.robustness_type_selection
        )
        self.combo_robustness_layer.currentIndexChanged.connect(
            self.robustness_layer_selection
        )

    # Method to build the ui of the dialog window
    def _build_ui(self):
        # The main layout, two verical boxes, one for the columns together and one for the button
        # Here you pass "self" to say that this is the main layout
        main_layout = QVBoxLayout(self)

        # The structure of the UI is organized in this way:
        # comboboxes -inside of-> layouts -inside of-> widgets
        self.parameter_widget = QWidget()
        self.robustness_widget = QWidget()
        # Secondary layout two orizontal boxes for the two columns
        columns_layout = QHBoxLayout()
        parameters_layout = QFormLayout(self.parameter_widget)
        robustness_layout = QFormLayout(self.robustness_widget)

        self.fixed_parameters = {"name": self.test_spec["name"]}
        self.fixed_parameters["macro_type"] = self.macro_type

        # Assigning the data and label to the combo box
        for parameter in self.test_spec["test_variables"]:
            if parameter["user_input"]:
                combo = QComboBox()
                # Creating a custom property in the combo box for the parameter key
                combo.setProperty("parameter_key", parameter["key"])
                for option in parameter["options"]:
                    combo.addItem(option["label"], option["value"])

                # Selecting the "default" value for the test specified in the test json
                idx = combo.findData(parameter["default"])
                if idx >= 0:
                    combo.setCurrentIndex(idx)

                # Adding the combo to the layout
                parameters_layout.addRow(parameter["display_name"], combo)
            else:
                self.fixed_parameters[parameter["key"]] = parameter["value"]

        # Same stuff but for the robustness, in this case all the comboboxes are
        # created statically because we know that the maximum amount of "parameters" is
        # 3 so we will need 3 combo boxes at max. For the test parameters we needed to
        # generate the UI depending on the specific test because the parameters number could change
        # drastically
        self.combo_robustness_type = QComboBox()
        self.combo_robustness_layer = QComboBox()
        self.combo_robustness_parameter = QComboBox()

        # Adding rows in the combobox
        for robustness_type in self.robustness_spec["robustness"]:
            self.combo_robustness_type.addItem(
                robustness_type["display_name"], robustness_type
            )

        # Adding the rows in the layout
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

    # Method to manage the inserting the "insert button"
    def insert_test_button_pressed(self):
        current_test_property = self.fixed_parameters.copy()
        # Initializing the "_ui" part of the test that will be used in the
        # table to display the parameters
        current_test_property["_ui"] = {}
        current_test_property["_ui"]["columns"] = []
        current_test_property["_ui"]["columns"].append(
            ("name", current_test_property["name"])
        )

        # Filling the rest of the parameters
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

        # If it doesnt have a robustness layer, return early
        if not self.combo_robustness_type.currentData()["layers"]:
            self.test_created.emit(current_test_property)
            return

        # Saving layer_key and display name (from the "currentText() of the comboBox")
        layer_key = self.combo_robustness_layer.currentData()["key"]
        current_test_property["robustness_layer"] = layer_key
        current_test_property["_ui"]["columns"].append(
            ("robustness_layer", self.combo_robustness_layer.currentText())
        )

        # If it doesnt have a robustness parameter, return early
        if not self.combo_robustness_layer.currentData()["options"]:
            self.test_created.emit(current_test_property)
            return

        parameter_value = self.combo_robustness_parameter.currentData()
        current_test_property["robustness_parameter"] = parameter_value
        current_test_property["_ui"]["columns"].append(
            ("robustness_parameter", self.combo_robustness_parameter.currentText())
        )

        # Emit the current_test_property that will get appended to the tests list
        self.test_created.emit(current_test_property)

    # Method to manage the change of the robustness type
    def robustness_type_selection(self, index):
        # Clearing the two comboboes that are subordinate
        self.combo_robustness_layer.clear()
        self.combo_robustness_parameter.clear()

        layers = self.combo_robustness_type.currentData()["layers"]

        # Disabling the layer and parameter comboboxes if its empty
        if not layers:
            self.combo_robustness_layer.setEnabled(False)
            self.combo_robustness_parameter.setEnabled(False)
            return

        # Adding the items in the combobox
        self.combo_robustness_layer.setEnabled(True)
        for layer in layers:
            self.combo_robustness_layer.addItem(layer["display_name"], layer)

        # Calling the next function to manage the selection of the layer
        self.robustness_layer_selection(index)

    # Method to manage the change of the robustness layer, same logic as the one before
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


# Loading the json file in the test_json folder
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
