import os
import json
import logging

CUR_DIR = os.path.dirname(__file__)
DATA_FILE =  os.path.join(CUR_DIR, "data", "movies.json")


class Movie():
    """  """
    def __init__(self, title):
        """[Class constructor]

        Args:
            title ([string]): [movie title]
        """
        self.title = title.title()
    
    def __str__(self):
        """[objet to string]

        Returns:
            [str]: [return a printable of Movie object]
        """
        return self.title

    def _get_movies(self):
        with open(DATA_FILE, "r") as f:
            return json.load(f)

    def _write_movies(self, movies):
        with open(DATA_FILE, "w") as f:
            json.dump(movies, f, indent=4)
        
    def add_to_movies(self):
        # recuperer la liste
        movies = self._get_movies()

        # verifier si le film est deja dans la liste
        if self.title not in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        # sînon on log un message pour dire a luser
        # que le films'est deja dans la liste
        else:
            logging.warning(f"  Le film: '{self.title}' est déjà dans la liste.")
            return False


if __name__ == '__main__':
    b= Movie("interstellar")
    print(b.add_to_movies())
