from PySide6.QtCore import Qt, QAbstractTableModel
from models.error_handler import ErrorHandler
import pandas as pd

class PandasModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, parent = None):
        return self._data.shape[0]
    
    def columnCount(self, parent = None):
        return self._data.shape[1]
    
    def data(self, index, role = Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return str(self._data.iloc[index.row(), index.column()])
        return None
    
    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])
            else:
                return str(self._data.index[section])
        return None
    
    def setHeaderData(self, section, orientation, value, role=Qt.EditRole):
        if role == Qt.EditRole and orientation == Qt.Horizontal:
            try:
                # Сохраняем старые данные
                old_data = self._data.copy()
                
                # Меняем названия столбцов
                new_columns = self._data.columns.tolist()
                new_columns[section] = value
                self._data.columns = new_columns
                
                # Сохраняем типы данных
                for col in new_columns:
                    if col in old_data.columns:
                        self._data[col] = old_data[col].astype(old_data[col].dtype)
                    else:
                        self._data[col] = ""  # Для новых столбцов
                
                self.headerDataChanged.emit(orientation, section, section)
                return True
            except Exception as e:
                print(f"Header change error: {e}")
                return False
        return False

    def flags(self, index):
        flags = super().flags(index)
        if not index.isValid():  
            return flags | Qt.ItemIsEditable
        return flags | Qt.ItemIsEditable

    def setData(self, index, value, role=Qt.EditRole):
        if role == Qt.EditRole:
            try:
                try:
                    value = float(value)
                except ValueError:
                    pass
                self._data.iloc[index.row(), index.column()] = value
                self.dataChanged.emit(index, index)
                return True
            except Exception as e:
                ErrorHandler.create_error("Ошибка при редактировании")
                return False
        return False
    
    def clear_data(self, rows=50, columns=12):
        self.beginResetModel()
        self._data = pd.DataFrame(
            [[None]*columns for _ in range(rows)],  # Явные пустые значения
            columns=[f"Column_{i+1}" for i in range(columns)]
        )
        self.endResetModel()
        self.layoutChanged.emit()
    
    def get_updated_data(self):
        return self._data.copy()