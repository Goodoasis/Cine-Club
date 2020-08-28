

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


if __name__ == '__main__':
    b= Movie("interstellar")
    print(dir(b))
