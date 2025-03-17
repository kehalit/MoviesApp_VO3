from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def list_movies(self):
        """
               Retrieve a list of all movies stored.

               Returns:
                   list: A list of dictionaries or objects representing movies.
        """
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster):
        """
            Add a new movie to the storage.

            Args:
                title (str): The title of the movie.
                 year (int): The release year of the movie.
                rating (float): The rating of the movie.
                poster (str): The URL or path to the movie's poster image.
        """
        pass

    @abstractmethod
    def delete_movie(self, title):
        """
             Delete a movie from the storage by its title.

            Args:
                title (str): The title of the movie to delete.
        """
        pass

    @abstractmethod
    def update_movie(self, title, rating):
        """
            Update the rating of an existing movie.

            Args:
                 title (str): The title of the movie to update.
                rating (float): The new rating to assign to the movie.
        """
        pass
