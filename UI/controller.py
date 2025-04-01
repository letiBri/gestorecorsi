import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model




    def handlePrintCorsiPD(self, e):
        self._view.lvTxtOut.controls.clear()
        pd = self._view.ddPD.value
        if pd is None:
            #self._view.lvTxtOut.controls.append(ft.Text("Attenzione: selezionare un periodo didattico!", color="red"))
            self._view.create_alert("Attenzione: selezionare un periodo didattico!")
            self._view.update_page()
            return
        # a questo punto pd="I" o pd="II"
        if pd == "I":
            pdInt = 1
        else:
            pdInt = 2
        corsiPD = self._model.getCorsiPD(pdInt)
        self._view.lvTxtOut.controls.append(ft.Text(f"Corsi del {pd} periodo didattico:"))
        for c in corsiPD:
            self._view.lvTxtOut.controls.append(ft.Text(c))
        self._view.update_page()
        return

    def handlePrintIscrittiCorsiPD(self, e):
        pass

    def handlePrintIscrittiCodins(self, e):
        pass

    def handlePrintCDSCodins(self, e):
        pass


    def fillddCodins(self):
        #for cod in self._model.getCodins():
            #self._view.ddCodins.options.append(ft.dropdown.Option(cod))
        for c in self._model.getAllCorsi():
            self._view.ddCodins.options.append(ft.dropdown.Option(key=c.codins, data=c, on_click=self._choiceDDCodins))

    def _choiceDDCodins(self, e):
        self._ddCodinsValue = e.control.data
        print(self._ddCodinsValue)
        print(type(self._ddCodinsValue)) #oggetto Corso

    def ddCodinsSelected(self, e):
        print(type(self._view.ddCodins.value)) #oggetto stringa


