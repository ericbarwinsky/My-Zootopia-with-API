import requests
import json
import os

API_URL = "https://api.api-ninjas.com/v1/animals?name="
API_KEY = "DEIN_API_KEY_HIER"


def fetch_animal_data(animal_name):
    """
    Fetches animal data from the API Ninjas service using a specific animal name.
    Includes timeout and error handling for network stability.
    """
    headers = {'X-Api-Key': API_KEY}
    try:
        response = requests.get(f"{API_URL}{animal_name}", headers=headers, timeout=10)
        # Raises an HTTPError if the response was an error
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return []


def save_data_to_json(data, animal_name):
    """
    Saves the fetched animal data into a JSON file named after the animal.
    """
    file_name = f"{animal_name}_data.json"
    try:
        with open(file_name, "w", encoding="utf-8") as handle:
            json.dump(data, handle, indent=4)
        return file_name
    except IOError as e:
        print(f"Error saving JSON file: {e}")
        return None


def delete_temporary_file(file_path):
    """
    Removes the specified file from the file system if it exists.
    """
    if file_path and os.path.exists(file_path):
        try:
            os.remove(file_path)
        except OSError as e:
            print(f"Error deleting temporary file {file_path}: {e}")


def cleaned_animal_name(name):
    """
    Normalizes typographic special characters to standard single quotes.
    """
    return name.replace("’", "'").replace("‘", "'")


def serialize_animal(animal_obj):
    """
    Serializes a single animal dictionary into an HTML list item string.
    """
    raw_name = animal_obj.get("name", "Unknown")
    animal_name = cleaned_animal_name(raw_name)
    chars = animal_obj.get("characteristics", {})
    locs = animal_obj.get("locations", [])

    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal_name}</div>\n'
    output += '  <p class="card__text">\n'

    if "diet" in chars:
        output += f'    <strong>Diet:</strong> {chars["diet"]}<br/>\n'
    if locs:
        output += f'    <strong>Location:</strong> {locs[0]}<br/>\n'
    if "type" in chars:
        output += f'    <strong>Type:</strong> {chars["type"]}<br/>\n'

    output += '  </p>\n'
    output += '</li>'
    return output


def create_animal_data_text(animals_data):
    """
    Iterates through a list of animals and aggregates their serialized HTML strings.
    """
    return "\n".join([serialize_animal(animal) for animal in animals_data])


def load_file_content(file_path):
    """
    Reads and returns the content of a file from a given path with error handling.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as handle:
            return handle.read()
    except FileNotFoundError:
        print(f"Error: Template file '{file_path}' not found.")
        return ""
    except IOError as e:
        print(f"Error reading template: {e}")
        return ""


def write_html_to_file(file_content, output_path):
    """
    Writes the final HTML content to a specified file path using UTF-8 encoding.
    """
    try:
        with open(output_path, "w", encoding="utf-8") as handle:
            handle.write(file_content)
        return True
    except IOError as e:
        print(f"Error writing HTML file: {e}")
        return False


def main():
    """
    Main orchestration logic: fetch, save, process, generate website, and cleanup.
    """
    target_animal = input("Please enter the animal´s name for the website: ")
    target_animal = target_animal.lower()

    animals_data = fetch_animal_data(target_animal)

    if not animals_data:
        print(f"No data found or error occurred for {target_animal}.")
        return

    json_file = save_data_to_json(animals_data, target_animal)

    formatted_animal_text = create_animal_data_text(animals_data)
    template_content = load_file_content('animals_template.html')

    if not template_content:
        return

    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", formatted_animal_text)

    if write_html_to_file(final_html, "animals.html"):
        print(f"Success: 'animals.html' has been generated for '{target_animal}'.")

    delete_temporary_file(json_file)


if __name__ == "__main__":
    main()