import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "TdP Baseball Manager 2024"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        self._page.bgcolor = "#ebf4f4"
        self._page.window_height = 800
        page.window_center()
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._txt_name = None
        self._txt_result = None

    def load_interface(self):
        # title
        self._title = ft.Text("TdP Baseball Manager 2024", color="blue", size=24)
        # self._page.controls.append(self._title)

        self._ddAnno = ft.Dropdown(label="Anno", width=200, alignment=ft.alignment.top_left)
        self._controller.fill_DD()

        row1 = ft.Row([ft.Container(self._title, width=500),
                       ft.Container(None, width=0),
                       ft.Container(self._ddAnno, width=250)], alignment=ft.MainAxisAlignment.CENTER)
        self._txtOutSquadre = ft.ListView(expand=1, spacing=10, padding=20)
        cont = ft.Container(self._txtOutSquadre, width=300, height= 200, alignment=ft.alignment.top_left, bgcolor="#deeded")
        self._btnCreaGrafo = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handleCreaGrafo)
        row2 = ft.Row([cont, self._btnCreaGrafo], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.END)

        self._ddSquadra = ft.Dropdown(label="Squadra")
        self._btnDettagli = ft.ElevatedButton(text="Dettagli", on_click=self._controller.handleDettagli)
        self._btnPercorso = ft.ElevatedButton(text="Percorso", on_click=self._controller.handlePercorso)
        row3 = ft.Row([ft.Container(self._ddSquadra, width=250),
                       ft.Container(self._btnDettagli, width=250),
                       ft.Container(self._btnPercorso, width=250)], alignment=ft.MainAxisAlignment.CENTER)

        self._page.controls.append(row1)
        self._page.controls.append(row2)
        self._page.controls.append(row3)

        self._txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(ft.Container(self._txt_result, bgcolor="#deeded", height=350))
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def update_page(self):
        self._page.update()

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()