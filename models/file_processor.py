import pandas as pd
from PySide6.QtWidgets import QFileDialog, QMessageBox
from models.error_handler import ErrorHandler


class FileProcessor:
    def __init__(self, file_path=None):
        self.file_path = file_path

    def select_csv_file(self):
        file_dialog = QFileDialog()
        file_dialog.setWindowTitle("Выберите CSV-файл")
        file_dialog.setNameFilter("CSV Files (*.csv);;All Files (*)")
        file_dialog.setFileMode(QFileDialog.ExistingFile)

        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            self.file_path = selected_files[0]
            #return selected_files[0]
        return None
    
    def csv_to_dataframe(self, file_path=None):
        file_path = file_path if file_path != None else self.file_path
        if not file_path:
            ErrorHandler.create_error("Файл не выбран!")
            return None
        try:
            df = pd.read_csv(file_path)
            QMessageBox.information(
                None, "Success",
                f"Файл '{file_path.split('/')[-1]}' успешно загружен!"
            )
            return df
        except:
            ErrorHandler.create_error("Не удалось загрузить файл.")
        return None
    
    def select_res_dest(self):
        folder_path = QFileDialog.getExistingDirectory(
            None,
            "Выберите папку для сохранения",
            "",
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
        )

        if folder_path:
            return folder_path
        else:
            ErrorHandler.create_error("Папка не выбрана.")
            return None