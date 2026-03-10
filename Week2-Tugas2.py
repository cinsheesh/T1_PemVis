print("Nama: Cindy Natasya Aulia Putri")
print("NIM: F1D02310109")
print("Kelas: C")


import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel,
    QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout,
    QMessageBox, QFrame
)
from PySide6.QtCore import Qt

class KonversiSuhu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Konversi Suhu")
        self.setFixedWidth(450)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(25, 25, 25, 25)
        layout.setSpacing(15)

        self.judul = QLabel("KONVERSI SUHU")
        self.judul.setObjectName("judulUtama")
        self.judul.setAlignment(Qt.AlignCenter)

        self.label_input = QLabel("Masukkan Suhu (Celsius):")
        self.input_suhu = QLineEdit()
        self.input_suhu.setPlaceholderText("Contoh: 100")

        self.btn_f = QPushButton("Fahrenheit")
        self.btn_k = QPushButton("Kelvin")
        self.btn_r = QPushButton("Reamur")

        tombol_layout = QHBoxLayout()
        tombol_layout.setSpacing(10)
        tombol_layout.addWidget(self.btn_f)
        tombol_layout.addWidget(self.btn_k)
        tombol_layout.addWidget(self.btn_r)

        self.result_box = QFrame()
        self.result_box.setObjectName("resultBox")
        res_layout = QVBoxLayout(self.result_box)

        self.label_hasil = QLabel("Hasil Konversi:")
        self.label_hasil.setObjectName("headerHasil")

        self.hasil = QLabel("Belum ada hasil")
        self.hasil.setObjectName("teksHasil")

        res_layout.addWidget(self.label_hasil)
        res_layout.addWidget(self.hasil)

        layout.addWidget(self.judul)
        layout.addWidget(self.label_input)
        layout.addWidget(self.input_suhu)
        layout.addLayout(tombol_layout)
        layout.addWidget(self.result_box)

        self.btn_f.clicked.connect(self.ke_fahrenheit)
        self.btn_k.clicked.connect(self.ke_kelvin)
        self.btn_r.clicked.connect(self.ke_reamur)

    def ambil_input(self):
        try:
            return float(self.input_suhu.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Input harus berupa angka!")
            return None

    def ke_fahrenheit(self):
        c = self.ambil_input()
        if c is not None:
            f = (c * 9/5) + 32
            self.hasil.setText(f"{c} Celsius = {f:.2f} Fahrenheit")

    def ke_kelvin(self):
        c = self.ambil_input()
        if c is not None:
            k = c + 273.15
            self.hasil.setText(f"{c} Celsius = {k:.2f} Kelvin")

    def ke_reamur(self):
        c = self.ambil_input()
        if c is not None:
            r = c * 4/5
            self.hasil.setText(f"{c} Celsius = {r:.2f} Reamur")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    STYLE_SHEET = """
    QWidget {
        background-color: #fcfcfc;
        font-family: 'Segoe UI', Arial;
        color: #333;
    }

    QLabel#judulUtama {
        background-color: #3498db;
        color: white;
        font-size: 20px;
        font-weight: bold;
        padding: 15px;
        border-radius: 6px;
    }

    QLineEdit {
        border: 1.5px solid #8fc991;
        border-radius: 6px;
        padding: 10px;
        background-color: #f1f8e9;
        font-size: 16px;
        color: #333;
    }

    QPushButton {
        background-color: #3498db;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 12px;
        font-weight: bold;
    }

    QPushButton:hover {
        background-color: #2980b9;
    }

    QFrame#resultBox {
        background-color: #d6ebff;
        border-left: 8px solid #004a99;
        border-radius: 4px;
        padding: 10px;
    }

    QLabel#headerHasil {
        color: #004a99;
        font-weight: bold;
        font-size: 15px;
        background: transparent;
    }

    QLabel#teksHasil {
        color: #004a99;
        font-size: 15px;
        background: transparent;
    }

    QMessageBox QLabel {
        color: #333;
    }
    """

    app.setStyleSheet(STYLE_SHEET)

    window = KonversiSuhu()
    window.show()
    sys.exit(app.exec())