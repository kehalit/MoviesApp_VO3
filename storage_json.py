import json
from istorage import IStorage


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path
        self._load_data()


    def _load_data(self):
        """ load data from the json file."""
        try:
            with open(self.file_path, "r") as file:
                self.movies = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.movies = {}


    def _save_data(self):
        with open(self.file_path, "w") as file:
            json.dump(self.movies, file, indent= 4)

    def list_movies(self):
        return self.movies


    def add_movie(self, title, year, rating, poster):
        self.movies[title] = {"year": year, "rating": rating, "poster": poster}
        self._save_data()


    def delete_movie(self, title):
        if title in self.movies:
            del self.movies[title]
            self._save_data()
            print(f" '{title}' has been deleted.")
        else:
            print(f" '{title}' not found in storage. ")


    def update_movie(self, title, rating):
        if title in self.movies:
            self.movies[title]["rating"]= rating
            self._save_data()