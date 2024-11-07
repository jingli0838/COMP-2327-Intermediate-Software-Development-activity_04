import signal
from PySide6.QtWidgets import QMainWindow, QLineEdit, QPushButton, QTableWidget, QLabel, QMessageBox, QVBoxLayout, QWidget, QTableWidgetItem, QComboBox
from PySide6.QtCore import Slot
from to_do_list.task_editor import TaskEditor
import csv

class ToDoList(QMainWindow):
    """
    This class reprsents a main window application that allows users to manage a to-do list.
    It provides an interface for users to add tasks,edit task statuses, 
    load tasks from a CSV file, and save tasks to a CSV file.
    It uses a QTableWidget to display tasks and their statuses, allowing users
    to add new tasks with a text input and a combo box for status selection.
    """
    
    def __init__(self):
        """
        Initializes the ToDoList window by setting up widgets, loading initial data
        from a CSV file, and connecting signals to relevant slots.
        """
        super().__init__()
        self.__initialize_widgets()
        self.add_button.clicked.connect(self.__on_add_task)
        self.task_table.cellClicked.connect(self.__on_edit_task)
        self.__load_data("data/todo.csv")
        self.save_button.clicked.connect(self.__save_to_csv)


    def __initialize_widgets(self):
        """
        Given:  Code to create and initialize the QWindow
        and all of the widgets on the window.
        DO NOT EDIT.
        """
        self.setWindowTitle("To-Do List")

        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("New Task")

        self.status_combo = QComboBox(self)
        self.status_combo.addItems(["Backlog", "In Progress", "Done"])

        self.add_button = QPushButton("Add Task", self)

        self.save_button = QPushButton("Save to CSV", self)
        

        self.task_table = QTableWidget(self)
        self.task_table.setColumnCount(2)
        self.task_table.setHorizontalHeaderLabels(["Task", "Status"])


        self.status_label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(self.task_input)
        layout.addWidget(self.status_combo)
        layout.addWidget(self.add_button)
        layout.addWidget(self.task_table)
        layout.addWidget(self.save_button)
        layout.addWidget(self.status_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    @Slot()
    def __on_add_task(self):
        """
        A meathod to add a new task to the task table. It checks if the task input field and status combo box are not empty.
        If both fields are filled, the task is added to the table with the specified status, and a message is displayed in the status label.
        If either field is empty, prompts the user to enter a task and select a status.
        """
        if(len(self.task_input.text().strip())>0 and
            len(self.status_combo.currentText()) > 0):
            row_count = self.task_table.rowCount()
            self.task_table.insertRow(row_count)

            new_task = QTableWidgetItem(self.task_input.text())
            new_status = QTableWidgetItem(self.status_combo.currentText())

            self.task_table.setItem(row_count, 0, new_task)
            self.task_table.setItem(row_count, 1, new_status)

            self.status_label.setText(f'Added task: {new_task.text()}')
        else:
            self.status_label.setText("Please enter a task and select its status.")

    @Slot()
    def __on_edit_task(self):
        """
        A meathod to open the TaskEditor dialog to edit the status of the selected task. 
        """
        selected_task_row = self.task_table.currentRow()
        current_status = self.task_table.item(selected_task_row, 1).text()
        task_editor = TaskEditor(selected_task_row, current_status)
        task_editor.task_updated.connect(self.__update_task_status)
        task_editor.exec()

    @Slot()
    def __update_task_status(self, row:int, new_status:str ):
        """
        Updates the status of the specified task in the task table
        and displays a message in the status label indicating the update.

        Args:
            row (int): The row index of the task to update.
            new_status (str): The new status to set for the task.
        """

        status_item = QTableWidgetItem(new_status)
        self.task_table.setItem(row, 1, status_item)
     
        self.status_label.setText(f'Task status updated to: {new_status}')



    # Part 3
    def __load_data(self, file_path: str):
        """
        Reads data from the .csv file provided.
        Calls the __add_table_row method (to be implemented) 
        for each row of data.
        Args:
            file_path (str): The name of the file (including relative path).
        """
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            # Skip the header row
            header = next(reader)  
            for row in reader:
                self.__add_table_row(row)
    
    def __add_table_row(self, row_data):
        """
        Adds a row of data to the task table in the appropriate columns.

        Args:
            row_data (list): A list containing the task description and status.
                             Expected format: [task, status].
        """
        row_count = self.task_table.rowCount()
        self.task_table.insertRow(row_count)
        task_item = QTableWidgetItem(row_data[0])
        status_item = QTableWidgetItem(row_data[1])

        self.task_table.setItem(row_count, 0, task_item)
        self.task_table.setItem(row_count, 1, status_item)


    def __save_to_csv(self):
        """
        Saves the QTable data to a file.
        """
        file_path = 'output/todo.csv'
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Write header
            writer.writerow(["Task", "Status"])

            for row in range(self.task_table.rowCount()):
                task = self.task_table.item(row, 0).text()
                status = self.task_table.item(row,1).text()
        
                writer.writerow([task, status]) 
