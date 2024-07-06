from PyQt5 import QtWidgets, uic
from Service import CompaService
class CompaController:

    def __init__(self) -> None:
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/frm_CompaDatos.ui")
        self.ventana.btncalcular.clicked.connect(self.onclickcalcular)
        self.ventana.show()
        app.exec()
    def onclickcalcular(self):
        resultado = 0
        operacion = ""
        try:
            dato1 = self.ventana.Dato1.text()
            dato2 = self.ventana.Dato2.text()
            if dato1 == "" or dato2 == "":
               operacion = "Por favor, ingrese ambos valores"
            else:
                n1 = int(dato1)
                n2 = int(dato2)
                resultado = CompaService.operacion_especial(n1, n2)
        except ValueError:
            operacion = "Ingresar valores numéricos"
        finally:
            if operacion!= "":
                self.ventana.ResultadoTD.setText(operacion)
            else:
                self.ventana.ResultadoTD.setText(str(resultado))