from PySide6.QtWidgets import  QMainWindow, QLineEdit, QPushButton, QTableWidget, QLabel, QVBoxLayout, QWidget, QTableWidgetItem
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QMessageBox

class ContactList(QMainWindow):
    """
    Contact List Class (QMainWindow). Provides users a 
    way to manage their contacts.
    """
    def __init__(self):
        """
        Initializes a Contact List window in which 
        users can add and remove contact data.
        """
        super().__init__()
        self.__initialize_widgets()      
        self.add_button.clicked.connect(self.__on_add_contact)
        self.remove_button.clicked.connect(self.__on_remove_contact)


    def __initialize_widgets(self):
        """
        Given:  Code to create and initialize the QWindow
        and all of the widgets on the window.
        DO NOT EDIT.
        """
        self.setWindowTitle("Contact List")

        self.contact_name_input = QLineEdit(self)
        self.contact_name_input.setPlaceholderText("Contact Name")

        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Phone Number")

        self.add_button = QPushButton("Add Contact", self)
        self.remove_button = QPushButton("Remove Contact", self)
        
        self.contact_table = QTableWidget(self)
        self.contact_table.setColumnCount(2)
        self.contact_table.setHorizontalHeaderLabels(["Name", "Phone"])

        self.status_label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(self.contact_name_input)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.remove_button)
        layout.addWidget(self.contact_table)
        layout.addWidget(self.status_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    @Slot()
    def __on_add_contact(self):
        """
        Adds a new contact to the contact table if both the contact name and phone number fields are filled.

        This method checks if both the contact name and phone number inputs are non-empty.
        If valid, it adds a new row to the contact table, populates it with the contact name
        and phone number, and updates the status label with a success message. If either field
        is empty, it prompts the user to fill in both fields via the status label.
        """
        row_count = self.contact_table.rowCount()
        if(len(self.contact_name_input.text().strip()) > 0 and
            len(self.phone_input.text()) > 0):
            
            self.contact_table.insertRow(row_count)
            contact_name = QTableWidgetItem(self.contact_name_input.text())
            contact_phone = QTableWidgetItem(self.phone_input.text())
            '''Add each of the QTableWidgetItems to the QTable.'''
                
            self.contact_table.setItem(row_count, 0, contact_name)
            self.contact_table.setItem(row_count, 1, contact_phone)

            self.status_label.setText(f'Added contact: {contact_name.text()}')
        else:
            self.status_label.setText('Please enter a contact name and phone number.')

    @Slot()
    def __on_remove_contact(self):
        """_summary_
        """
        selected_row = self.contact_table.currentRow()
        if(selected_row >= 0):
            reply = QMessageBox.information(self, 
                                            "Remove Contact", 
                                            "Are you sure you want to remove the selected contact?",
                                            QMessageBox.Yes | QMessageBox.No, 
                                            QMessageBox.No)
            if(reply == QMessageBox.Yes):
                self.contact_table.removeRow(selected_row)
                self.status_label.setText('Contact removed.')
        else:
            self.status_label.setText('Please select a row to be removed.')
       


        


    
            









   













