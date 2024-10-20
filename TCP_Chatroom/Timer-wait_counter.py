#function to add time to a counter
#function to remove time from the counter
#time module?
#ticket system to manage customers

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the GUI
        self.initUI()

    def initUI(self):
        # Create buttons
        self.addButton = QPushButton('Add Customer', self)
        self.removeButton = QPushButton('Remove Customer', self)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.removeButton)

        # Set the layout for the main window
        self.setLayout(layout)

        # Set the window title and size
        self.setWindowTitle('Customer Management')
        self.setGeometry(300, 300, 300, 200)
        self.show()


timer = 0.0
rounded_timer = round(timer, 2)
formatted_timer = f"{rounded_timer:.2f}"

customer_queue = 0

def add_time():
    timer += 5
    customer_queue += 1

def rem_time():
    timer -= 5
    customer -= 1

def ticket_system_add():
    customer_queue += 1
    
def ticket_system_rem():
    customer_queue -= 1
    

print(f"There is an estimated wait time of {formatted_timer} minutes.")
print(f"There are {customer_queue}'s currently waiting.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())