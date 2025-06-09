from copy import copy

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fill_DD(self):
        myValuesDD = list(map(lambda x: ft.dropdown.Option(data=x, key=x, on_click=self.read_year), self._model.getYears()))
        self._view._ddAnno.options = myValuesDD

    def fill_LV(self):
        self._view._txtOutSquadre.controls.clear()
        self._model.getTeams(self.year)
        self._view._txtOutSquadre.controls.append(ft.Text(f"Squadre presenti nell'anno {self.year} = {len(self._model._teams)}"))
        for team in self._model._teams:
            self._view._txtOutSquadre.controls.append(ft.Text(f"{team})"))
            self._view._ddSquadra.options.append(ft.dropdown.Option(data=team, key=team, on_click=self.read_team))
        self._view.update_page()

    def read_year(self, e):
        self.year = e.control.data
        self.fill_LV()

    def read_team(self, e):
        self.team = e.control.data

    def handleCreaGrafo(self, e):
        self._model.buildGraph(copy(self._view._ddAnno.value))

    def handleDettagli(self, e):
        self._view._txt_result.controls.clear()
        res = self._model.getNeighbors(self.team)
        for team in res:
            self._view._txt_result.controls.append(ft.Text(f"{team[0]}          {team[1]}"))
        self._view.update_page()

    def handlePercorso(self, e):
        self._model.getPath(self.team)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"Nodo di partenza {self.team}"))
        for node in self._model._bestPath:
            self._view._txt_result.controls.append(ft.Text(f"{node}"))
        self._view.update_page()