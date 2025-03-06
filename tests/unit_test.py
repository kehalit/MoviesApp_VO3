from Movie_project_OOP.storage.storage_json import StorageJson


storage = StorageJson("movies.json")

print("Initial movies:", storage.list_movies())

# Add a movie
#storage.add_movie("The Matrix", 1999, 8.0)
print("After adding The Matrix:", storage.list_movies())

# Update movie rating
storage.update_movie("The Matrix", 9.5)
print("After updating The Matrix rating:", storage.list_movies())

# Delete movie and verify
storage.delete_movie("The Matrix")
print("After deleting The Matrix:", storage.list_movies())

# Check if the movie is really gone
if "The Matrix" not in storage.list_movies():
    print("✅ The Matrix successfully deleted!")
else:
    print("❌ Delete operation failed!")
