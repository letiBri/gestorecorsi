import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Gestore corsi edizione 2025"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None

        self.ddPD = None
        self.ddCodins = None
        self.btnPrintCorsiPD = None
        self.btnPrintIscrittiCorsiPD = None
        self.btnPrintIscrittiCodins = None
        self.btnPrintCDSCodins = None

    def load_interface(self):
        # title
        self._title = ft.Text("Hello World", color="blue", size=24)
        self._page.controls.append(self._title)

        self.ddPD = ft.Dropdown(label="Periodo Didattico", options=["I", "II"])
        self.ddCodins = ft.Dropdown(label="Corso")
        self._controller.fillddCodins()

        self.btnPrintCorsiPD = None
        self.btnPrintIscrittiCorsiPD = None
        self.btnPrintIscrittiCodins = None
        self.btnPrintCDSCodins = None


        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
