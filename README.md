🚀 Overview

The Movie Recommender System is a web application built using Streamlit. It allows users to select a movie from a dataset and recommends five similar movies along with their posters by leveraging a precomputed similarity matrix. The movie posters are fetched using the TMDb API.

🛠️ Features
Interactive dropdown for selecting a movie.
Personalized recommendations for five similar movies.
Display of movie posters fetched from TMDb API.
📂 Project Structure
├── .venv/              # Virtual environment (ignored by Git)
├── dataset/            # Data files (ignored by Git)
├── .gitignore          # Files and directories to be ignored by Git
├── .env                # Environment variables file (ignored by Git)
├── app.py              # Streamlit application
├── model.ipynb         # Jupyter notebook for model development
├── movie.pkl           # Pickle file containing movie metadata
├── similarity.pkl      # Pickle file for movie similarity matrix
├── README.md           # Project documentation
🔧 Setup Instructions
Prerequisites
Ensure you have the following installed:

Python 3.x
Pip
Installation
Clone the repository:
git clone https://github.com/your-username/your-repo.git
cd your-repo
Set up a virtual environment:

python -m venv .venv
source .venv/bin/activate  # For Linux/Mac
.venv\Scripts\activate     # For Windows
Install the dependencies:

pip install -r requirements.txt
Create a .env file:
Add your TMDb API key as an environment variable:

TMDB_API_KEY=your_api_key_here

🏃 Running the Application
To launch the application, use the following command:

streamlit run app.py
Open the provided URL in your browser to access the app.

🧩 How It Works
Select a movie from the dropdown list.
Click the Recommend button.
The application retrieves five similar movies and displays their titles along with poster images fetched via the TMDb API.
📝 Example API Usage
]
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables
api_key = os.getenv("TMDB_API_KEY")
url = f"https://api.themoviedb.org/3/movie/{{movie_id}}?api_key={api_key}&language=en-US"


📌 Important Notes
Ensure your TMDb API key is valid and added to the .env file.
If a poster is unavailable, a placeholder image will be displayed.
The movie.pkl and similarity.pkl files are essential for the application to function correctly.


📚 Future Enhancements
Display additional metadata, such as genres and ratings.
Implement a search bar for faster movie selection.
Add better error handling for API requests.
