from storage import StorageJson
from app.movie_app import MovieApp
from MoviesApp_VO3.app.movie_app import  MovieApp
from storage import StorageCsv


def main():
    # Step 1: Create a StorageJson object with a file path (adjust the path if needed)
    storage = StorageJson('db/db.json')  # Replace "movies.json" with the path to your JSON file
    storage2 = StorageCsv('db/db.csv')


    app = MovieApp(storage)
    app.run()


if __name__ == "__main__":
    main()
