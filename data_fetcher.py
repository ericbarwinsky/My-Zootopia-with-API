import requests
import os
from dotenv import load_dotenv

# Lädt die Variablen aus der .env Datei in das System
load_dotenv()

# Holt den Wert der Variable 'API_KEY' aus dem System
API_KEY = os.getenv('API_KEY')
API_URL = "https://api.api-ninjas.com/v1/animals?name="

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Uses the API key loaded from the environment variables.
    """
    # Sicherheitscheck: Falls der Key nicht geladen werden konnte
    if not API_KEY:
        print("Error: API_KEY not found. Please check your .env file.")
        return []

    headers = {'X-Api-Key': API_KEY}
    try:
        response = requests.get(f"{API_URL}{animal_name}", headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return []