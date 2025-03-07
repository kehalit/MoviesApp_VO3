# Movies App Reloaded

This project is a web application built using **Object-Oriented Programming (OOP)** principles. The app allows users to search for movies by title, fetching information about the movies from the OMDB API.
It dynamically displays movie details, such as the title, poster, and other information, using Python and JavaScript. The project also manages data storage and API calls efficiently through the use of
classes and objects.

## Features

- **Movie Search**: Users can input a movie title to search for related movie information.
- **OMDB API Integration**: The app fetches movie data (title, poster, etc.) from the OMDB API using OOP principles.
- **Dynamic Website Generation**: The website dynamically displays movie data based on user input, with a clean, responsive layout.
- **Storage Manager**: A class-based storage manager is used to handle movie data and API responses efficiently.

## Project Structure

### Classes & Objects

1. **MovieSearch**: This class manages API requests to the OMDB API and stores the response data (movie title, poster, etc.).
2. **StorageManager**: A class that handles the storage of movie data, allowing data to be fetched and saved efficiently, supporting future improvements like saving to a local database.
3. **WebsiteGenerator**: This class generates the HTML and styles for displaying movie information dynamically based on user input.

### Installation

#### Backend Setup (Python 3.x)

1. Clone the repository:

     git clone https://github.com/kehalit/OOP_Movie_Project.git

2. Navigate to the project directory:
  cd movie-search-app

3. Create a virtual environment (optional but recommended):
   python3 -m venv venv

4. Activate the virtual environment:
   On macOS/Linux: source venv/bin/activate
   On Windows: .\venv\Scripts\activate
5. Install the required Python libraries:
   pip install -r requirements.txt
   
## Frontend Setup (HTML, CSS, JavaScript)
Open the index.html file in your browser to run the app.

## Required Libraries
This project uses the following Python libraries:

requests: To make HTTP requests to the OMDB API.
python-dotenv: To manage environment variables securely, such as your OMDB API key.
Install them by running: pip install requests python-dotenv

## OMDB API Key
To use the OMDB API, you'll need to obtain an API key. Follow these steps:

Go to OMDB API and sign up for an API key.

Once you have the key, create a .env file in the root directory of the project.

Add your OMDB API key to the .env file: OMDB_API_KEY=your_api_key_here
The .env file should be added to your .gitignore to keep your API key secure.

## Technologies Used

- **Python 3.x**: The backend language used to handle API requests and responses using classes.
- **requests**: Python library used for making HTTP requests to the OMDB API.
- **python-dotenv**: Used to securely load the OMDB API key from the '.env' file.
- **HTML**: For structuring the content.
- **CSS**: For styling the movie details and ensuring a responsive layout.
- **OMDB API**: A free API providing movie data.


## Acknowledgements
OMDB API: http://www.omdbapi.com/



















