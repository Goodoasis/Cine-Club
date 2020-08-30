import os
import json
import logging

# Creation du chemin d'acces au Json.
CUR_DIR = os.path.dirname(__file__)
DATA_FILE =  os.path.join(CUR_DIR, "data", "movies.json")

def get_movies():
    """ Fonction récuperant la liste des films de Json. """
    with open(DATA_FILE, "r") as f:
        movies_title = json.load(f)
    movies = [Movie(movie_title) for movie_title in movies_title]
    return movies


class Movie():
    """
    Classe movie qui formatte un titre d'un film.
    avec des méthodes permettant d'enregistrer le titre
    dans un fichier json.
    """

    def __init__(self, title):
        """
        Constructeur de classe ne prenant q'un
        argument de type str puis le formate.
        """
        self.title = title.title()
    
    def __str__(self):
        """Méthode retournant une version str de l'obj."""
        return self.title

    def _get_movies(self):
        """Méthode privé; retourne le contenue du Json."""
        with open(DATA_FILE, "r") as f:
            return json.load(f)

    def _write_movies(self, movies):
        """Méthode privé; enregistre arg dans le Json."""
        with open(DATA_FILE, "w") as f:
            json.dump(movies, f, indent=4)

    def add_to_movies(self):
        """
        Méthode qui enregistre le film dans le json en
        verifiant au préalable de ne pas faire de doubon.
        """
        movies = self._get_movies()
        
        if self.title not in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"  Le film: '{self.title}' est enregistré.")
            return False

    def remove_from_movies(self):
        """Méthode qui supprime le film si il existe."""
        movies = self._get_movies()

        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"  Suppression impossible:  '{self.title}' n'est pas enregistré.")
            return False            

