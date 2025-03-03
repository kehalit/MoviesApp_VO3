class MovieApp:
    """A simple application for managing movies."""

    def __init__(self, storage):
        """
        Initializes the MovieApp with the given storage system.

        Args:
            storage (IStorage): An object that implements the IStorage interface for movie storage.
        """
        self._storage = storage


    def _command_list_movies(self):
        """Displays a list of all movies in the storage."""
        movies = self._storage.list_movies()
        if not movies:
            print("No movies found in storage.")
        else:
            for title, details in movies.items():
                print(f"{title} ({details['year']}) - Rating: {details['rating']}")


    def _command_movie_stats(self):
        """Displays the movie statistics like average rating and movie count."""
        movies = self._storage.list_movies()
        if not movies:
            print("No movies found in storage.")
        else:
            total_movies = len(movies)
            total_rating = sum(movie['rating'] for movie in movies.values())
            avg_rating = total_rating / total_movies if total_movies > 0 else 0
            print(f"Total Movies: {total_movies}")
            print(f"Average Rating: {avg_rating:.2f}")


    def _generate_website(self):
        """Generates a basic HTML page displaying the movies."""
        movies = self._storage.list_movies()
        html_content = "<html><body><h1>Movie List</h1><ul>"

        for title, details in movies.items():
            html_content += f"<li>{title} ({details['year']}) - Rating: {details['rating']}</li>"

        html_content += "</ul></body></html>"

        with open("movies.html", "w") as file:
            file.write(html_content)
        print("Website generated as 'movies.html'.")


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
                    self._command_add_movie()
                elif choice == 3:
                    self._command_delete_movie()
                elif choice == 4:
                    self._command_update_movie()
                elif choice == 5:
                    self._command_movie_stats()
                elif choice == 6:
                     self._command_random_movie()
                elif choice == 7:
                    self._command_search_movie()
                elif choice == 8:
                    self._command_movies_sorted_by_rating()
                elif choice == 9:
                    self._generate_website()
                else:
                    print('Invalid choice. Please select between 1 and 8.')
            except ValueError:
                    print('Invalid input! Please enter a number between 1 and 9.')