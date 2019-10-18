import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

def calculBtoD(a):
    decimal=0
    for i in range ((len(a))):
        poidsdubit = int(a[(len(a))-1-i])
        decimal = decimal+ (poidsdubit * (2**(i)))
    return decimal

def calculDtoB(a):
    x = int(a)
    k = ""
    while x>=1:
        if(x%2==0):
            print("O", end='')
            k = k + "0"
        else:
            print("1", end='')
            k = k + "1"
        x = x//2
    print(k)
    return k[::-1]


def conversion():
    if (ui.binText.text()!=""):
        value = ui.binText.text()
        value = calculBtoD(value) #Test
        value = str(value)
        ui.decText.setText(value)
    elif (ui.decText.text()!=""):
        value = int(ui.decText.text())
        value = calculDtoB(value)
        value = str(value)
        ui.binText.setText(value)
    else:
        ui.label.setText("Erreur : Le champs de saisie est vide")
def clear():
    NaN = ""
    ui.binText.setText(NaN)
    ui.decText.setText(NaN)
app = QApplication(sys.argv)

ui = uic.loadUi("project.ui")
ui.show()


ui.btn_start.clicked.connect(conversion)
ui.btn_clear.clicked.connect(clear)

sys.exit(app.exec_())
