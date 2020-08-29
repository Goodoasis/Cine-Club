from PySide2 import QtWidgets, QtCore
from movie import get_movies

class App(QtWidgets.QWidget):
    """
    """

    def __init__(self):
        """ """
        super().__init__()
        self.setWindowTitle("Ciné Club")
        self.setup_ui()
        self.populate_movies()

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

    def populate_movies(self):
        """ """
        for movie in get_movies():
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.lw_movies.addItem(movie.title)




app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()