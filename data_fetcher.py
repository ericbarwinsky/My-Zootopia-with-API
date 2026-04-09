import requests

API_URL = "https://api.api-ninjas.com/v1/animals?name="
API_KEY = "DEIN_API_KEY_HIER"

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary.
    """
    headers = {'X-Api-Key': API_KEY}
    try:
        response = requests.get(f"{API_URL}{animal_name}", headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return []