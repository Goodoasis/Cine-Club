from PySide2 import QtWidgets


class App(QtWidgets.QWidget):
    """
    """

    def __init__(self):
        """ """
        super().__init__()
        self.setWindowTitle("Ciné Club")
        self.setup_ui()

    def setup_ui(self):
        """ """
        # Creation du layout
        self.layout = QtWidgets.QVBoxLayout(self)
        # Creation des widgets
        self.le_movieTitle = QtWidgets.QLineEdit()
        self.btn_addMovie = QtWidgets.QPushButton("Ajouter un film")
        self.lw_movies = QtWidgets.QListWidget()
        self.btn_removeMovies = QtWidgets.QPushButton("Supprimer le(s) film(s)")
        # Ajout des widgets dans le layout
        self.layout.addWidget(self.le_movieTitle)
        self.layout.addWidget(self.btn_addMovie)
        self.layout.addWidget(self.lw_movies)
        self.layout.addWidget(self.btn_removeMovies)




app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()