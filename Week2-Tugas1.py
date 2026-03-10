print("Nama: Cindy Natasya Aulia Putri")
print("NIM: F1D02310109")
print("Kelas: C")



import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, 
    QPushButton, QLabel, QComboBox, QMessageBox, 
    QHBoxLayout, QFrame
)
from PySide6.QtCore import Qt

class FormBiodata(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Biodata Mahasiswa")
        self.setFixedWidth(420)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(25, 25, 25, 25)
        main_layout.setSpacing(8)

        def add_input_field(label_text, widget):
            lbl = QLabel(label_text)
            lbl.setStyleSheet("font-weight: bold; color: #444; margin-top: 5px;")
            main_layout.addWidget(lbl)
            main_layout.addWidget(widget)

        self.nama = QLineEdit()
        self.nim = QLineEdit()
        self.nim.setPlaceholderText("Masukkan NIM")
        self.kelas = QLineEdit()
        self.kelas.setPlaceholderText("TI-2A")
        self.jk = QComboBox()
        self.jk.addItems(["Laki-laki", "Perempuan"])

        add_input_field("Nama Lengkap:", self.nama)
        add_input_field("NIM:", self.nim)
        add_input_field("Kelas:", self.kelas)
        add_input_field("Jenis Kelamin:", self.jk)

        btn_layout = QHBoxLayout()
        btn_layout.setContentsMargins(0, 10, 0, 10)

        self.btn_tampilan = QPushButton("Tampilkan")
        self.btn_reset = QPushButton("Reset")

        btn_layout.addWidget(self.btn_tampilan)
        btn_layout.addWidget(self.btn_reset)
        btn_layout.addStretch()
        main_layout.addLayout(btn_layout)

        self.result_container = QFrame()
        self.result_container.setObjectName("boxHasil")

        res_layout = QVBoxLayout(self.result_container)
        res_layout.setContentsMargins(15, 15, 15, 15)
        res_layout.setSpacing(5)

        self.lbl_judul = QLabel("DATA BIODATA")
        self.lbl_judul.setStyleSheet("font-weight: bold; font-size: 14px; color: #1b5e20; background: transparent;")

        self.lbl_info = QLabel("Nama:\nNIM:\nKelas:\nJenis Kelamin:")
        self.lbl_info.setStyleSheet("color: #1b5e20; background: transparent; line-height: 150%;")

        res_layout.addWidget(self.lbl_judul)
        res_layout.addWidget(self.lbl_info)

        main_layout.addWidget(self.result_container)

        self.btn_tampilan.clicked.connect(self.proses_data)
        self.btn_reset.clicked.connect(self.reset_data)

    def proses_data(self):
        nama_txt = self.nama.text()
        nim_txt = self.nim.text()
        kelas_txt = self.kelas.text()
        jk_txt = self.jk.currentText()

        if not nama_txt or not nim_txt or not kelas_txt:
            QMessageBox.warning(self, "Error", "Semua field harus diisi!")
            return

        hasil_teks = (
            f"Nama: {nama_txt}\n"
            f"NIM: {nim_txt}\n"
            f"Kelas: {kelas_txt}\n"
            f"Jenis Kelamin: {jk_txt}"
        )
        self.lbl_info.setText(hasil_teks)

    def reset_data(self):
        self.nama.clear()
        self.nim.clear()
        self.kelas.clear()
        self.jk.setCurrentIndex(0)
        self.lbl_info.setText("Nama:\nNIM:\nKelas:\nJenis Kelamin:")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setStyleSheet("""
        QWidget { 
            background-color: #ffffff; 
            font-family: 'Segoe UI', Arial; 
            color: #333333;
        }

        QMessageBox QLabel {
            color: #333333;
            background: transparent;
        }

        QMessageBox QPushButton {
            color: #333333;
            background-color: #e0e0e0;
            padding: 5px 15px;
        }

        QLineEdit, QComboBox {
            border: 1px solid #a5d6a7;
            border-radius: 6px;
            padding: 8px;
            background-color: #f1f8e9;
            color: #333333;
        }

        QComboBox QAbstractItemView {
            background-color: white;
            color: #333333;
            selection-background-color: #a5d6a7;
        }

        QPushButton {
            padding: 10px 25px;
            border-radius: 6px;
            font-weight: bold;
            color: white;
            font-size: 13px;
        }

        QPushButton[text="Tampilkan"] { 
            background-color: #3498db; 
        }

        QPushButton[text="Reset"] { 
            background-color: #95a5a6; 
        }

        QFrame#boxHasil {
            background-color: #dcedc8;
            border-left: 8px solid #2e7d32;
            border-radius: 4px;
        }
    """)

    win = FormBiodata()
    win.show()
    sys.exit(app.exec())