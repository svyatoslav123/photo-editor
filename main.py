import os
from PIL import ImageEnhance
from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image
from PIL import ImageFilter
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPixmap
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
def pil2pixmap(im):
    if im.mode == "RGB":
        r, g, b = im.split()
        im = Image.merge("RGB", (b, g, r))
    elif im.mode == "RGBA":
        r, g, b, a = im.split()
        im = Image.merge("RGBA", (b, g, r, a))
    elif im.mode == "L":
        im = im.convert("RGBA")
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32)
    pixmap = QPixmap.fromImage(qim)
    return pixmap






window = QWidget()
window.resize(700, 500)
papka_btn = QPushButton("Папка")
left_btn = QPushButton("Вліво")
right_btn = QPushButton("Вправо")
dzerkalo_btn = QPushButton("Дзеркало")
rizkist_btn = QPushButton("Різкість")
rotare_btn = QPushButton("Перевернути")
negr_btn = QPushButton("ЧОРНО-БІЛИЙ")
contor_btn = QPushButton("КОНТОР")
emboss_btn = QPushButton("ТИСНЕННЯ")
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
h1.addWidget(negr_btn)
h1.addWidget(contor_btn)
h1.addWidget(emboss_btn)
h1.addWidget(rotare_btn)
v2.addWidget(photo)
v2.addLayout(h1)


window.setLayout(main_line)


class WorkWithPhoto:
    def __init__(self):
        self.image = None
        self.folder = None
    def load(self):
        full_path = os.path.join(self.folder, self.image_name)
        self.image = Image.open(full_path)




    def show_image(self):
        pixel = pil2pixmap(self.image)
        photo.setPixmap(pixel)
    def rozmitya(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.show_image()
    def ROTARE(self):
        self.image = self.image.transpose(Image.ROTATE_180)
        self.show_image()
    def DZERKALO(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.show_image()
    def LEFT(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.show_image()
    def RIGHT(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.show_image()
    def NEGR(self):
        self.image = self.image.convert("L")
        self.show_image()
    def CONTOR(self):
        self.image = self.image.filter(ImageFilter.CONTOUR)
        self.show_image()
    def EMBOSS(self):
        self.image = self.image.filter(ImageFilter.EMBOSS)
        self.show_image()
work_with_photo = WorkWithPhoto()

def show_directory():
    work_with_photo.folder = QFileDialog.getExistingDirectory()
    list_f = os.listdir(work_with_photo.folder)

    list.clear()
    for file in list_f:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            list.addItem(file)


def show_photo():
    image_name = list.currentItem().text()
    work_with_photo.image_name = image_name
    work_with_photo.load()
    work_with_photo.show_image()
list.currentRowChanged.connect(show_photo)
papka_btn.clicked.connect(show_directory)
rizkist_btn.clicked.connect(work_with_photo.rozmitya)
rotare_btn.clicked.connect(work_with_photo.ROTARE)
dzerkalo_btn.clicked.connect(work_with_photo.DZERKALO)
left_btn.clicked.connect(work_with_photo.LEFT)
right_btn.clicked.connect(work_with_photo.RIGHT)
negr_btn.clicked.connect(work_with_photo.NEGR)
contor_btn.clicked.connect(work_with_photo.CONTOR)
emboss_btn.clicked.connect(work_with_photo.EMBOSS)
window.show()
app.exec()

























































































