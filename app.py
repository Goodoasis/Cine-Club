from PySide2 import QtWidgets, QtCore

from movie import Movie, get_movies


class App(QtWidgets.QWidget):
    """
    Interface graphique d'une appmication qui permet de lister des
    titres de film, de sauvegarder cette listeet enfin de les
    supprimer.

    """

    def __init__(self):
        """Constructeur de notre interface graphique."""
        super().__init__()
        self.setWindowTitle("Ciné Club")
        self.setup_ui()  # Ajout des Widgets.
        self.populate_movies()
        self.setup_connexions()  # Création des connexion entre widgets.

    def setup_ui(self):
        """Creation et dispositions des widgets."""
        # Creation du layout
        self.layout = QtWidgets.QVBoxLayout(self)
        # Creation des widgets
        self.le_movieTitle = QtWidgets.QLineEdit()
        self.btn_addMovie = QtWidgets.QPushButton("Ajouter un film")
        self.lw_movies = QtWidgets.QListWidget()
        self.lw_movies.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_removeMovies = QtWidgets.QPushButton("Supprimer le(s) film(s)")
        # Ajout des widgets dans le layout
        self.layout.addWidget(self.le_movieTitle)
        self.layout.addWidget(self.btn_addMovie)
        self.layout.addWidget(self.lw_movies)
        self.layout.addWidget(self.btn_removeMovies)

    def populate_movies(self):
        """
        Remplis le ListWidget des films contenus dans data/movies.json.
        """
        self.lw_movies.clear()
        for movie in get_movies():
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            # Methode pour joindre un objet a un str de ListWidget.
            lw_item.setData(QtCore.Qt.UserRole, movie)
            # Ajout du contenu du json dans ListWidget.
            self.lw_movies.addItem(lw_item)

    def setup_connexions(self):
        """Creation des connexions"""
        self.btn_addMovie.clicked.connect(self.add_movie)
        # Reaction du bouton entrée si focus sur le lineEdit.
        self.le_movieTitle.returnPressed.connect(self.add_movie)
        self.btn_removeMovies.clicked.connect(self.remove_movie)

    def add_movie(self):
        """Méthode pour ajouter un film a partir du LineEdit.
        Vérifie si ce film n'existe pas déjà avant de l'enregistrer"""
        # Récupérer le text du lineEdit si non vide.
        movie_title = self.le_movieTitle.text()
        if not movie_title:
            return False

        movie= Movie(movie_title)  #  Creation de l'instance Movie.
        result = movie.add_to_movies()  # Ajout du film dans le Json.

        if result:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            # Ajouter le film dans le ListWidget.
            self.lw_movies.addItem(lw_item)
        
        self.le_movieTitle.setText("")

    def remove_movie(self):
        """Méthode pour supprimer le(s) film(s) selectionnés."""
        for selected_item in self.lw_movies.selectedItems():
            movie = selected_item.data(QtCore.Qt.UserRole)
            movie.remove_from_movies()
            self.lw_movies.takeItem(self.lw_movies.row(selected_item))


app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()