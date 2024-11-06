from PySide6.QtWidgets import  QPushButton,  QVBoxLayout,  QComboBox, QDialog
from PySide6.QtCore import Slot
from PySide6.QtCore import Signal

class TaskEditor(QDialog):
    """
    This class represents a dialog window for editing the status of a task.

    The class provides a simple interface allowing users to change the 
    status of a task. It inherits from QDialog and emits a custom signal 
    when a task's status is updated.

    Attributes:
        row (int): The row index of the task being edited.
        status (str): The initial status of the task.
    """
    task_updated = Signal(int, str)

    def __init__(self, row: int, status: str):
        """
        The function initializes the TaskEditor dialog with the specified row and status. It sets up the dialog window,
        initializes widgets, and connects the save button to emit the task_updated signal when the status 
        is saved.

        Args:
            row (int): The row index of the task to be edited.
            status (str): The current status of the task.
        """
        super().__init__()
        self.initialize_widgets(row, status)

        self.row = row
        self.status_combo.setCurrentText(status) 

        self.save_button.clicked.connect(self.__on_save_status)




    def initialize_widgets(self, row: int, status: str):
        """
        Given:  Code to create and initialize the QWindow
        and all of the widgets on the window.
        DO NOT EDIT.
        """
        self.setWindowTitle("Edit Task Status")

        self.row = row

        self.status_combo = QComboBox(self)
        self.status_combo.addItems(["Backlog", "In Progress", "Done"])
        

        self.save_button = QPushButton("Save", self)

        layout = QVBoxLayout()
        layout.addWidget(self.status_combo)
        layout.addWidget(self.save_button)
        self.setLayout(layout)
        self.setFixedWidth(150)

    @Slot()
    def __on_save_status(self):
        """
        A Slot function to handle saving the status.

        This method retrieves the currently selected status from the combo box,
        emits the task_updated signal with the row index and new status, and 
        closes the dialog.
        """
        current_status = self.status_combo.currentText()
        self.task_updated.emit(self.row, current_status)
        self.accept()



        


