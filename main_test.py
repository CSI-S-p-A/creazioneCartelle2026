import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class TestManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test Manager")
        self.setGeometry(100, 100, 800, 600)

        # Central widget
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        # Input section
        input_layout = QHBoxLayout()

        QLabel("Test Name:", parent=central)
        input_layout.addWidget(QLabel("Test Name:"))
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter test name")
        input_layout.addWidget(self.name_input)

        input_layout.addWidget(QLabel("Variable 1:"))
        self.var1_input = QLineEdit()
        self.var1_input.setPlaceholderText("Value")
        input_layout.addWidget(self.var1_input)

        input_layout.addWidget(QLabel("Variable 2:"))
        self.var2_input = QLineEdit()
        self.var2_input.setPlaceholderText("Value")
        input_layout.addWidget(self.var2_input)

        add_btn = QPushButton("Add Test")
        add_btn.clicked.connect(self.add_test)
        input_layout.addWidget(add_btn)

        layout.addLayout(input_layout)

        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(
            ["Test Name", "Variable 1", "Variable 2", ""]
        )

        # Make columns stretch
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Fixed)
        self.table.setColumnWidth(3, 60)

        layout.addWidget(self.table)

        # Connect enter key to add test
        self.name_input.returnPressed.connect(self.add_test)
        self.var1_input.returnPressed.connect(self.add_test)
        self.var2_input.returnPressed.connect(self.add_test)

    def add_test(self):
        name = self.name_input.text().strip()
        var1 = self.var1_input.text().strip()
        var2 = self.var2_input.text().strip()

        if not name:
            return

        # Add new row
        row = self.table.rowCount()
        self.table.insertRow(row)

        # Add data
        self.table.setItem(row, 0, QTableWidgetItem(name))
        self.table.setItem(row, 1, QTableWidgetItem(var1))
        self.table.setItem(row, 2, QTableWidgetItem(var2))

        # Add remove button
        remove_btn = QPushButton("✕")
        remove_btn.setMaximumWidth(50)
        remove_btn.clicked.connect(lambda checked, r=row: self.remove_test(r))
        self.table.setCellWidget(row, 3, remove_btn)

        # Clear inputs
        self.name_input.clear()
        self.var1_input.clear()
        self.var2_input.clear()
        self.name_input.setFocus()

    def remove_test(self, row):
        # Find actual row (in case rows were deleted)
        btn = self.sender()
        for i in range(self.table.rowCount()):
            if self.table.cellWidget(i, 3) == btn:
                self.table.removeRow(i)
                break


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestManager()
    window.show()
    sys.exit(app.exec())
