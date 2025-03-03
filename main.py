
from storage_json import StorageJson
from movie_app import MovieApp


def main():
    # Step 1: Create a StorageJson object with a file path (adjust the path if needed)
    storage = StorageJson("movies.json")  # Replace "movies.json" with the path to your JSON file

    # Step 2: Create a MovieApp object and pass the StorageJson object
    app = MovieApp(storage)
    app.run()


if __name__ == "__main__":
    main()
