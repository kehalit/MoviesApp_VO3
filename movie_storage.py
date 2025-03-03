import json
import random


"""This script is responsible for storing and managing movie data in a JSON file (movies.json)."""
def load_movies():
    """The function ensures the program gracefully handles missing files, invalid JSON, or incorrect formats."""
    try:
        with open('movies.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Movies file not found. Starting with an empty database.")
        return {}
    except json.JSONDecodeError:
        print("Error reading the movies file. Starting with an empty database.")
        return {}


def save_movies(movies_db):
    with open('movies.json', 'w') as file:
        json.dump(movies_db, file, indent=4)


def add_movie_to_db(movies_db, title, year, rating):
    if not title.strip():
        return "Movie title cannot be empty."

    if title in movies_db:
        return f'Movie "{title}" already exists in the database.'

    movies_db[title] = {"rating": rating, "year": year}
    save_movies(movies_db)
    return f'Movie "{title}" successfully added.'


def delete_movie(movies_db):
    movie_to_be_deleted = input('Enter movie name to delete: ')
    if movie_to_be_deleted in movies_db:
        del movies_db[movie_to_be_deleted]
        save_movies(movies_db)
        print(f'Movie {movie_to_be_deleted} successfully deleted')
    else:
        print(f"Movie {movie_to_be_deleted} doesn't exist!")
    input("\nPress Enter to continue ")


def update_movie(movies_db):
    movie_name = input('Enter movie name: ')
    if movie_name in movies_db:
        try:
            new_rating = float(input('Enter new movie rating (0-10): '))
            new_year = int(input('Enter new year of release: '))
            if 0 <= new_rating <= 10:
                movies_db[movie_name] = {"rating": new_rating, "year": new_year}
                save_movies(movies_db)
                print(f'Movie {movie_name} successfully updated')
            else:
                print('Rating must be between 0 and 10.')
        except ValueError:
            print('Invalid input! Please ensure rating is a number (0-10) and year is an integer.')
    else:
        print(f"Movie {movie_name} doesn't exist!")
    input("\nPress Enter to continue ")


def search_movie(movies_db):
    movie_to_search = input('Enter part of movie name: ').lower()
    results = [(key, value) for key, value in movies_db.items() if movie_to_search in key.lower()]
    if results:
        for key, value in results:
            print(f'{key}: {value}')
    else:
        print(f'{movie_to_search} not found in the database.')
    input("\nPress Enter to continue ")


def sorted_movie(movies_db):
    # Sort by the "rating" value inside the nested dictionary
    sorted_items = sorted(movies_db.items(), key=lambda item: item[1]["rating"], reverse=True)
    for title, details in sorted_items:
        print(f'{title}: Rating: {details["rating"]}, Year: {details["year"]}')
    input("\nPress Enter to continue ")

