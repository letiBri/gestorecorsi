import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._ddCodinsValue = None




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

        if len(corsiPD) == 0:
            self._view.lvTxtOut.controls.append(ft.Text("nessun corso trovato in questo periodo"))
            self._view.update_page()
            return

        self._view.lvTxtOut.controls.append(ft.Text(f"Corsi del {pd} periodo didattico:"))
        for c in corsiPD:
            self._view.lvTxtOut.controls.append(ft.Text(c))
        self._view.update_page()
        return

    def handlePrintIscrittiCorsiPD(self, e):
        self._view.lvTxtOut.controls.clear()
        pd = self._view.ddPD.value
        if pd is None:
            self._view.create_alert("Attenzione: selezionare un periodo didattico!")
            self._view.update_page()
            return
        # a questo punto pd="I" o pd="II"
        if pd == "I":
            pdInt = 1
        else:
            pdInt = 2
        corsiPDwI = self._model.getCorsiPDwithIscritti(pdInt) #in questa variabile abbiamo la lista di tuple
        if len(corsiPDwI) == 0:
            self._view.lvTxtOut.controls.append(ft.Text("nessuno corso trovato in questo periodo"))
            self._view.update_page()
            return
        self._view.lvTxtOut.controls.append(ft.Text(f"Dettagli corsi del {pd} periodo didattico:"))
        for c in corsiPDwI:
            self._view.lvTxtOut.controls.append(ft.Text(f"{c[0]} - N Iscritti: {c[1]}"))
        self._view.update_page()
        return

    def handlePrintIscrittiCodins(self, e):
        self._view.lvTxtOut.controls.clear()
        #codins = self._view.ddCodins.value #ho la stringa così
        if self._ddCodinsValue is None: # ho l'oggetto Corso
            self._view.create_alert("Attenzione: selezionare un corso di interesse")
            self._view.update_page()
            return
        #procediamo a stampare gli studenti
        students = self._model.getStudentiCorso(self._ddCodinsValue.codins) #restituisce lista di studenti ordinata per cognome
        if len(students) == 0:
            self._view.lvTxtOut.controls.append(ft.Text("nessuno studente iscritto a questo corso"))
            self._view.update_page()
            return
        self._view.lvTxtOut.controls.append(ft.Text(f"Studenti iscritti al corso {self._ddCodinsValue}"))
        for s in students:
            self._view.lvTxtOut.controls.append(ft.Text(s)) #lo studente ha già un metodo str
        self._view.update_page()
        return

    def handlePrintCDSCodins(self, e):
        self._view.lvTxtOut.controls.clear()
        if self._ddCodinsValue is None:  # ho l'oggetto Corso
            self._view.create_alert("Attenzione: selezionare un corso di interesse")
            self._view.update_page()
            return

        cds = self._model.getCDSofCorso(self._ddCodinsValue.codins) #restituisce una lista di tuple
        if len(cds) == 0:
            self._view.lvTxtOut.controls.append(ft.Text("nessun CDS offe questo corso"))
            self._view.update_page()
            return
        self._view.lvTxtOut.controls.append(ft.Text(f"CDS che frequentano il corso {self._ddCodinsValue}:"))
        for c in cds:
            self._view.lvTxtOut.controls.append(ft.Text(f"CDS: {c[0]} - N iscritti: {c[1]}"))
        self._view.update_page()
        return


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


