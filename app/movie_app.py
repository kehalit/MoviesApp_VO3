import random
import requests
import os
from dotenv import load_dotenv

from MoviesApp_VO3.storage.storage_json import StorageJson
from MoviesApp_VO3.storage.storage_csv import StorageCsv
from MoviesApp_VO3.storage.istorage import IStorage


#from class_zwith_Api.test import API_KEY
load_dotenv()

API_KEY = os.getenv('API_KEY')
URL = "http://www.omdbapi.com/?i=tt3896198"


class MovieApp:
    """A simple application for managing movies."""

    def __init__(self, storage:IStorage):
        """
        Initializes the MovieApp with the given storage system.

        Args:
            storage (IStorage): An object that implements the IStorage interface for movie storage.
        """
        self._storage = storage

    def _add_movie(self):
        title = input('Enter new movie name: ').strip()

        if not title:
            print('Movie name cannot be empty. Please try again.')
            input("\nPress Enter to continue ")
            return

        try:
            # Fetch movie details from OMDb API
            response = requests.get(URL, params={"t": title, "apikey": API_KEY})
            data = response.json()

            # Handle cases where the movie is not found
            if data.get("Response") == "False":
                print(f"Error: {data.get('Error')}")
                input("\nPress Enter to continue ")
                return

            # Extract movie details
            movie_title = data.get("Title")
            year = int(data.get("Year", 0))  # Convert to int, default to 0 if missing
            rating = float(data.get("imdbRating", 0.0))  # Convert to float, default to 0.0
            poster = data.get("Poster")

            # Store the movie details
            self._storage.add_movie(movie_title, year, rating, poster)

            print(f"Movie '{movie_title}' added successfully!")

        except requests.exceptions.RequestException as e:
            print(f"Error: Unable to connect to OMDb API ({e})")

        input("\nPress Enter to continue ")

    def _delete_movie(self):
        movie_to_be_deleted = input('Enter movie name to delete: ')
        self._storage.delete_movie(movie_to_be_deleted)
        input("\nPress Enter to continue ")

    def _update_movie(self):
        movie_name = input('Enter movie name: ')
        if movie_name in self._storage.list_movies():
            try:
                new_rating = float(input('Enter new movie rating (0-10): '))
                if 0 <= new_rating <= 10:
                   self._storage.update_movie(movie_name, new_rating)

            except ValueError:
                print('Invalid input! Please ensure rating is a number (0-10) and year is an integer.')
        else:
            print(f"Movie {movie_name} doesn't exist!")
        input("\nPress Enter to continue ")

    def _command_list_movies(self):
        """Displays a list of all movies in the storage."""
        movies = self._storage.list_movies()
        if not movies:
            print("No movies found in storage.")
        else:
            for title, details in movies.items():
                print(f"{title} ({details['year']}) - Rating: {details['rating']}")


    def _movie_stats(self):
        movies_db = self._storage.list_movies()
        if not movies_db:
            print('No movies in the database to calculate stats.')
            input("\nPress Enter to continue ")
            return
        ratings = [details["rating"] for details in movies_db.values()]
        average = round(sum(ratings) / len(ratings), 2)
        sorted_ratings = sorted(ratings)
        median = sorted_ratings[len(sorted_ratings) // 2] if len(sorted_ratings) % 2 else \
            (sorted_ratings[len(sorted_ratings) // 2 - 1] + sorted_ratings[len(sorted_ratings) // 2]) / 2
        best_movie = max(self._storage.list_movies(), key=lambda k: movies_db[k]["rating"])
        worst_movie = min(movies_db, key=lambda k: movies_db[k]["rating"])

        print(f'Average Rating: {average}')
        print(f'Median Rating: {median}')
        print(f'Best Movie: {best_movie} (Rating: {movies_db[best_movie]["rating"]}, '
              f'Year: {movies_db[best_movie]["year"]})')
        print(f'Worst Movie: {worst_movie} (Rating: {movies_db[worst_movie]["rating"]},'
              f' Year: {movies_db[worst_movie]["year"]})')
        input("\nPress Enter to continue ")


    def _random_movie(self):
        movies= self._storage.list_movies()
        if movies:
            random_key, random_value = random.choice(list(movies.items()))
            print(f"Your movie for tonight: {random_key}, it's rated {random_value['rating']}")
        else:
            print("No movies in the database!")
        input("\nPress Enter to continue ")

    def _search_movie(self):
        movie_to_search = input('Enter part of movie name: ').lower()
        results = [(key, value) for key, value in self._storage.list_movies().items() if movie_to_search in key.lower()]
        if results:
            for key, value in results:
                print(f'{key}: {value['rating']}')
        else:
            print(f'{movie_to_search} not found in the database.')
        input("\nPress Enter to continue ")

    def _movies_sorted_by_rating(self):
        # Sort by the "rating" value inside the nested dictionary
        sorted_items = sorted(self._storage.list_movies().items(), key=lambda item: item[1]["rating"], reverse=True)
        for title, details in sorted_items:
            print(f'{title}: Rating: {details["rating"]}, Year: {details["year"]}')
        input("\nPress Enter to continue ")

    def _generate_website(self):
        """Generates an improved HTML page displaying movies with a responsive grid layout."""
        movies = self._storage.list_movies()

        # Load the HTML template
        template_path = os.path.join("_static", "index_template.html")
        with open(template_path, "r", encoding="utf-8") as file:
            template = file.read()

        # Create movie grid
        movie_grid = '<div class="movie-container">'
        for title, details in movies.items():
            poster_url = details.get("Poster", "").strip()
            if not poster_url or poster_url == "N/A":
                poster_url = "static/default.jpg"  # Placeholder image

            movie_grid += f"""
            <div class="movie">
                <img class="movie-poster" src="{poster_url}" alt="{title}" 
                    onerror="this.onerror=null; this.src='static/default.jpg';">
                <div class="movie-title">{title}</div>
                <div class="movie-year">{details.get('year', 'N/A')}</div>
            </div>
            """
        movie_grid += "</div>"

        # Replace template placeholders
        final_html = template.replace("__TEMPLATE_TITLE__", "Masterschool's Movie app")
        final_html = final_html.replace("__TEMPLATE_MOVIE_GRID__", movie_grid)

        # Save as index.html
        with open("index.html", "w", encoding="utf-8") as file:
            file.write(final_html)

        print("Website was generated successfully as 'index.html'.")

    def run(self):
        """Main method to run the application."""
        while True:
            print('\nMovieApp Menu:')
            print('0. Exit')
            print('1. List movies')
            print('2. Add movie')
            print('3. Delete movie')
            print('4. Update movie')
            print('5. Stats')
            print('6. Random movie')
            print('7. Search movie')
            print('8. Movies sorted by rating')
            print('9. Generate website')

            try:
                choice = int(input('Enter choice (0-8): ').strip())

                if choice == 0:
                    print('Bye')
                    break
                elif choice == 1:
                    self._command_list_movies()
                elif choice == 2:
                    self._add_movie()
                elif choice == 3:
                    self._delete_movie()
                elif choice == 4:
                    self._update_movie()
                elif choice == 5:
                    self._movie_stats()
                elif choice == 6:
                     self._random_movie()
                elif choice == 7:
                    self._search_movie()
                elif choice == 8:
                    self._movies_sorted_by_rating()
                elif choice == 9:
                    self._generate_website()
                else:
                    print('Invalid choice. Please select between 1 and 8.')
            except ValueError:
                    print('Invalid input! Please enter a number between 1 and 9.')