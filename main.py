from storage import StorageJson
from App.movie_app import MovieApp
from MoviesApp_VO3.App.movie_app import  MovieApp
from storage import StorageCsv


def main():
    # Step 1: Create a StorageJson object with a file path (adjust the path if needed)
    storage = StorageJson('DB/db.json')  # Replace "movies.json" with the path to your JSON file
    storage2 = StorageCsv('DB/db.csv')



    app = MovieApp(storage2)
    app.run()


if __name__ == "__main__":
    main()
