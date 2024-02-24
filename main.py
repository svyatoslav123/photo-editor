import os
from PIL import ImageEnhance
from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image
from PIL import ImageFilter
from PyQt6.QtWidgets import *
app = QApplication([])
app.setStyleSheet("""
     QWidget {
        background: #ccdaed;
     }
     QPushButton {
        background: #e9edf2;
        border-style: outset;
        min-height: 30px;
        min-width: 100px;
     }
     QListWidget { 
        background: #ccdbd5;
     }
     QTextEdit { 
        background: #e1ede8;
     }

      QPushButton {
        color: blue;
        font-size: 15px;
        font-family: Impact;
        border-width: 2px;
        border-color: black;
        border-radius: 5px;
     }
      QPushButton#save_btn {
        color: green;
        font-size: 20px;
        font-family: Impact;
        border-width: 4px;
        border-color: black;
        border-radius: 5px;
      }

 """)

window = QWidget()
window.resize(700, 500)
papka_btn = QPushButton("Папка")
left_btn = QPushButton("Вліво")
right_btn = QPushButton("Вправо")
dzerkalo_btn = QPushButton("Дзеркало")
rizkist_btn = QPushButton("Різкість")
rotare_btn = QPushButton("Перевернути")
photo = QLabel("img.png")
list = QListWidget()




main_line = QHBoxLayout()
v1 = QVBoxLayout()
v2 = QVBoxLayout()
h1 = QHBoxLayout()
main_line.addLayout(v1)
main_line.addLayout(v2)


v1.addWidget(papka_btn)
v1.addWidget(list)
h1.addWidget(left_btn)
h1.addWidget(right_btn)
h1.addWidget(dzerkalo_btn)
h1.addWidget(rizkist_btn)
h1.addWidget(rotare_btn)
v2.addWidget(photo)
v2.addLayout(h1)


window.setLayout(main_line)




window.show()
app.exec()

























































































