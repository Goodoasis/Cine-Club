import os
import json
import logging

CUR_DIR = os.path.dirname(__file__)
DATA_FILE =  os.path.join(CUR_DIR, "data", "movies.json")

def get_movies():
        with open(DATA_FILE, "r") as f:
            movies_title = json.load(f)
        movies = [Movie(movie_title) for movie_title in movies_title]
        return movies


class Movie():

    """ 
    """

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
        """ """
        with open(DATA_FILE, "r") as f:
            return json.load(f)

    def _write_movies(self, movies):
        """ """
        with open(DATA_FILE, "w") as f:
            json.dump(movies, f, indent=4)

    def add_to_movies(self):
        """ """
        movies = self._get_movies()
        
        if self.title not in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"  Le film: '{self.title}' est enregistré.")
            return False

    def remove_to_movies(self):
        """ """
        movies = self._get_movies()

        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"  Suppression impossible:  '{self.title}' n'est pas enregistré.")
            return False            

if __name__ == '__main__':
    b= Movie("interstellar")
    print(b.add_to_movies())
    m = Movie("Harry potter")
    c = Movie("matrix")
    print(c.add_to_movies())
    print(m.add_to_movies())
    u = Movie("Arthur et les minimoys")
    print(u.add_to_movies())
    T = Movie("Avengers")
    T.remove_to_movies()
    listy = get_movies()
    print(listy)