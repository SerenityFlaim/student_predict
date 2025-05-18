from PySide6.QtWidgets import QMessageBox
import re

class ErrorHandler():
    def __init__(self):
        self.msg_box = QMessageBox()
        self.msg_box.setIcon(QMessageBox.Critical)
        self.msg_box.setWindowTitle("Error")
        self.msg_box.setText("An error occurred!")
        self.msg_box.setStandardButtons(QMessageBox.Ok)

    @staticmethod
    def check_positive(value, er_text):
        integer_regex = r'^[-+]?\d+$'
        float_regex = r'^[-+]?\d+(\.\d+)?$'
        if (type(value) is str):
            if (re.match(float_regex, value)):
                value = float(value)
            elif (re.match(integer_regex, value)):
                value = int(value)
            elif (value == ""):
                value = None
        else:
            ErrorHandler.create_error(er_text)
        
        if (value is not None and value > 0):
            return value
        else:
            ErrorHandler.create_error(er_text)

    @staticmethod
    def check_positive_integer(value, er_text):
        if (type(value) is str and value.isnumeric()):
            value = int(value)
        else:
            ErrorHandler.create_error(er_text)
        
        if (value > 0 and type(value) is int):
            return value
        else:
            ErrorHandler.create_error(er_text)
    
    @staticmethod
    def create_error(er_text):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setWindowTitle("Error")
        msg_box.setText("An error occurred!")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.setInformativeText(er_text)
        msg_box.exec()