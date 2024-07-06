from PyQt5 import QtWidgets, uic
from Service import PromedioService
class PromedioController:
        
    def __init__(self) -> None:
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/frm_PromedioNotas.ui")
        self.ventana.btncalcular.clicked.connect(self.onclickcalcular)
        self.ventana.show()
        app.exec()
    def onclickcalcular(self):
        resultado1 = 0
        resultado2 = 0
        operacion = ""
        try:
            nota1 = self.ventana.Nota1.text()
            nota2 = self.ventana.Nota2.text()
            nota3 = self.ventana.Nota3.text()
            nota4 = self.ventana.Nota4.text()
        
            if nota1 == "" or nota2 == "" or nota3 == "" or nota4 == "":
                operacion = "Por favor, ingrese todas las notas"
            else:
                n1 = int(nota1)
                n2 = int(nota2)
                n3 = int(nota3)
                n4 = int(nota4)
                resultado1 = PromedioService.eliminar_menor(n1, n2, n3, n4)
                resultado2 = PromedioService.Promedio(resultado1)
        except ValueError:
            operacion = "Ingresar valores numéricos"
        finally:
            if operacion != "":
                self.ventana.Resultado.setText(operacion)
            else:
                self.ventana.Resultado.setText("Promedio = " + str(resultado2))