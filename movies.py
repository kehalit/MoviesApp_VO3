import movie_storage
import random
"""This script provides user interface """

def list_movies(movies_db):
    print(f'{len(movies_db)} movies in total')
    for title, details in movies_db.items(): #return as atuple
        print(f'{title}: Rating: {details["rating"]}, Year: {details["year"]}')
    input("\nPress Enter to continue ")


def add_movie(movies_db):
    title = input('Enter new movie name: ').strip() # to remove extra spaces
    # Check if the movie name is empty
    if not title:
        print('Movie name cannot be empty. Please try again.')
        input("\nPress Enter to continue ")
        return

    try:
        rating = float(input('Enter new movie rating (0-10): '))
        if not (0 <= rating <= 10):
            print("rating must be between 0 and 10. ")
            input("\npress Enter to continue")
            # Prompt the user for the year of release
        year = int(input('Enter the year of release: '))

        result = movie_storage.add_movie_to_db(movies_db, title, year, rating) #to store the movie in the database
        print(result)

    except ValueError:
        print('Invalid input! Please enter valid numbers for rating and year.')
    input("\nPress Enter to continue ")


def stats(movies_db):
    if not movies_db:
        print('No movies in the database to calculate stats.')
        input("\nPress Enter to continue ")
        return
    ratings = [details["rating"] for details in movies_db.values()]
    average = round(sum(ratings) / len(ratings), 2)
    sorted_ratings = sorted(ratings)
    median = sorted_ratings[len(sorted_ratings) // 2] if len(sorted_ratings) % 2 else \
        (sorted_ratings[len(sorted_ratings) // 2 - 1] + sorted_ratings[len(sorted_ratings) // 2]) / 2
    best_movie = max(movies_db, key=lambda k: movies_db[k]["rating"])
    worst_movie = min(movies_db, key=lambda k: movies_db[k]["rating"])

    print(f'Average Rating: {average}')
    print(f'Median Rating: {median}')
    print(f'Best Movie: {best_movie} (Rating: {movies_db[best_movie]["rating"]}, '
          f'Year: {movies_db[best_movie]["year"]})')
    print(f'Worst Movie: {worst_movie} (Rating: {movies_db[worst_movie]["rating"]},'
          f' Year: {movies_db[worst_movie]["year"]})')
    input("\nPress Enter to continue ")


def random_movie(movies_db):
    if movies_db:
        random_key, random_value = random.choice(list(movies_db.items()))
        print(f"Your movie for tonight: {random_key}, it's rated {random_value}")
    else:
        print("No movies in the database!")
    input("\nPress Enter to continue ")


def main():
    """the main function controls the menu system and user interachtion """
    print('********** My Movies Database **********')
    movies = movie_storage.load_movies() #loads exting movie data from movie_storage


    while True:
        print('Menu:')
        print('0. Exit')
        print('1. List movies')
        print('2. Add movie')
        print('3. Delete movie')
        print('4. Update movie')
        print('5. Stats')
        print('6. Random movie')
        print('7. Search movie')
        print('8. Movies sorted by rating')

        try:
            choice = int(input('Enter choice (0-8): '))
            if choice == 0:
                print('Bye')
                break
            elif choice == 1:
                list_movies(movies)
            elif choice == 2:
                add_movie(movies)
            elif choice == 3:
                movie_storage.delete_movie(movies)
            elif choice == 4:
                movie_storage.update_movie(movies)
            elif choice == 5:
                stats(movies)
            elif choice == 6:
                random_movie(movies)
            elif choice == 7:
                movie_storage.search_movie(movies)
            elif choice == 8:
                movie_storage.sorted_movie(movies)
            else:
                print('Invalid choice. Please select between 1 and 8.')
        except ValueError:
            print('Invalid input! Please enter a number between 1 and 8.')


if __name__ == "__main__":
    main()
