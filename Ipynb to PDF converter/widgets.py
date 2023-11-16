from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QListWidget, QMessageBox
from PyQt5.QtCore import Qt
import os
from converter import NotebookConverter

class PDFConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.conversionQueue = []  # Initialize conversion queue
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Python Notebook to PDF Converter')
        self.setGeometry(300, 300, 600, 400)

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        layout = QVBoxLayout(centralWidget)

        buttonStyle = """
        QPushButton {
            border: 2px solid #9EC1CF;
            border-radius: 10px;
            background-color: #F1F1F1;
            color: #555;
            font-size: 14px;
            font-weight: bold;
            padding: 5px;
            min-height: 40px;
        }
        QPushButton:hover {
            background-color: #BDD7EE;
        }
        QPushButton:pressed {
            background-color: #9EC1CF;
        }
        """

        self.selectButton = QPushButton('Select Files', centralWidget)
        self.selectButton.setStyleSheet(buttonStyle)
        layout.addWidget(self.selectButton)
        self.selectButton.clicked.connect(self.selectFiles)

        self.fileListWidget = QListWidget(centralWidget)
        layout.addWidget(self.fileListWidget)

        self.convertButton = QPushButton('Convert', centralWidget)
        self.convertButton.setStyleSheet(buttonStyle)
        layout.addWidget(self.convertButton)
        self.convertButton.clicked.connect(self.processConversionQueue)

        layout.addStretch()

    def isValidFile(self, file_name):
        return file_name.endswith('.ipynb') and os.path.exists(file_name)

    def selectFiles(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_filter = 'IPython Notebook (*.ipynb)'
        file_names, _ = QFileDialog.getOpenFileNames(self, 'Select Notebook Files to convert', '', file_filter, options=options)

        if file_names:
            for file_name in file_names:
                if self.isValidFile(file_name):
                    print(f'Selected file: {file_name}')
                    self.conversionQueue.append(file_name)
                    self.fileListWidget.addItem(file_name)
                else:
                    print(f'Invalid file format: {file_name}')
        else:
            print('No files selected.')

    def updateUIOnError(self, notebook_path):
        print(f"Failed to convert: {notebook_path}")
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Failed to convert the notebook to PDF.")
        msg.setInformativeText(f"An error occurred while converting {notebook_path}.")
        msg.setWindowTitle("Conversion Error")
        msg.exec_()

    def updateUIAfterConversion(self, notebook_path):
        QMessageBox.information(self, 'Conversion Successful',
                                f'The file {notebook_path} has been converted to PDF successfully.',
                                QMessageBox.Ok, QMessageBox.Ok)
    
    def processConversionQueue(self):
        converter = NotebookConverter()
        total_files = len(self.conversionQueue)
        for i, notebook_path in enumerate(self.conversionQueue, start=1):
            pdf_file_path, error = converter.convert_to_pdf(notebook_path)
            if pdf_file_path:
                self.updateUIAfterConversion(notebook_path)
            else:
                self.updateUIOnError(notebook_path, error)

        self.conversionQueue.clear()
