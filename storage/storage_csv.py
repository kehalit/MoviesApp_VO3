import csv
from os import write

from .istorage import IStorage

class StorageCsv(IStorage):
    def __init__(self, file_path):
        """Initializes the storage with a CSV file path."""
        self.file_path = file_path
        self._load_data()


    def _load_data(self):
        """Loads data from the CSV file into the movies dictionary."""
        self.movies = {}
        try:
            with open(self.file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.movies[row['title']] = {'title': row['title'], 'rating': float(row['rating']), 'year': int(row['year'])}
        except FileNotFoundError:
            self.movies = {}


    def _save_data(self, movies):
        """Saves the current movies data into the CSV file."""
        with open(self.file_path, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['title', 'year', 'rating']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader() # Write header
            for title, details in self.movies.items():
                writer.writerow({
                    'title': title,
                    'rating': details['rating'],
                    'year': details['year']
                })


    def list_movies(self):
        """Returns a dictionary of all movies."""
        return self.movies


    def add_movie(self, title, year, rating, poster):
        """Adds a new movie to the storage."""
        self.movies[title] = {'year': int(year), 'rating': float(rating), 'Poster': poster}
        self._save_data(self.movies)


    def delete_movie(self, title):
        """Deletes a movie from the storage."""
        if title in self.movies:
            del self.movies[title]
            self._save_data(self.movies)
            print(f" '{title}' has been deleted.")
        else:
            print(f" '{title}' not found in storage. ")


    def update_movie(self, title, rating):
        """Updates the rating of an existing movie."""
        if title in self.movies:
            self.movies[title]['rating'] = rating
            self._save_data(self.movies)

