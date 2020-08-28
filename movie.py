import os
import json

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

if __name__ == '__main__':
    b= Movie("interstellar")
    print(dir(b))
