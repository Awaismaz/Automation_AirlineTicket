import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtCore import QUrl
import os
from automation import process_form

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Set window title
        self.setWindowTitle('Airline Booking Automation')

        self.urlInput = QLineEdit()
        self.fileInput = QLineEdit()

        self.urlInput.setText("file:///" + os.path.join(os.getcwd(), 'Group Sales Ryanair website', 'Group Sales website.html').replace('\\', '/'))
        self.fileInput.setText(os.path.join(os.getcwd(), 'Passengers list.xlsx'))

        self.urlButton = QPushButton('Select HTML file (Not needed in case of Online URL)')
        self.fileButton = QPushButton('Select Excel Spreadsheet')
        self.startButton = QPushButton('Start Process')
        self.startButton.setStyleSheet("""
        QPushButton{
                    background-color: #008CBA;
            color: white;
            border: none;
            padding: 5px 2px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 12px;
        }

                            QPushButton:hover {
        background-color: #4CAF50; /* Green */
        color: white;
    }
        """)

        self.urlButton.clicked.connect(self.select_url)
        self.fileButton.clicked.connect(self.select_file)
        self.startButton.clicked.connect(self.start_process)

        layout = QVBoxLayout()
        layout.addWidget(self.urlInput)
        layout.addWidget(self.urlButton)
        layout.addWidget(self.fileInput)
        layout.addWidget(self.fileButton)
        layout.addWidget(self.startButton)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Set window dimensions
        self.setGeometry(100, 100, 800, 400)
        
        # Set the stylesheet
        self.setStyleSheet("""
            QWidget {
                background-color: #434547;
            }
            QPushButton {
                background-color: #00AABB;
                color: black;
                font-weight: bold;
                height: 40px;
                border-radius: 20px;
                font-size: 12px;
            }
            QLineEdit {
                background-color: #F0F0F0;
                height: 30px;
            }
                QPushButton:hover {
        background-color: #4CAF50; /* Green */
        color: white;
    }
        """)

    def select_url(self):
        url = QFileDialog.getOpenFileUrl()[0]
        if url.isValid():
            self.urlInput.setText(url.toString())

    def select_file(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select File")
        if file:
            self.fileInput.setText(file)

    def start_process(self):
        url = self.urlInput.text()
        file = self.fileInput.text()
        process_form(url, file)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec_())
