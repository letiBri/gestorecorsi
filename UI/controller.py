import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillddCodins(self):
        for cod in self._model.getCodins():
            self._view.ddCodins.options.append(cod)

