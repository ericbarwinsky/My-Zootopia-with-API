import requests


url_standart = ""
api_key =""


def request_animals():
    pass


import json


def json_load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def cleaned_animal_name(name):
    """ Replace typographic special characters with standard single quotes. """
    return name.replace("’", "'").replace("‘", "'")


def create_animal_data_text(animals_data):
    """
        Parses a list of animal data dictionaries and formats it into a readable string.
        Input: json (list[dict])
        Returns:
        str: A formatted string containing the name, diet, first location, and type
            of each animal found in the input data.
    """
    output_data = ""
    for data in animals_data:
        raw_name = data.get("name", "Unknown")
        animal_name = cleaned_animal_name(raw_name)
        output_data += '<li class="cards__item">'
        output_data += f'<div class="card__title">{animal_name}</div>\n'
        output_data += f'<p class="card__text">\n'

        chars = data.get("characteristics", {})
        if "diet" in chars:
            output_data += f'<strong>Diet:</strong> {chars["diet"]}<br/>\n'
        locs = data.get("locations", [])
        if locs:
            output_data += f'<strong>Location:</strong> {locs[0]}<br/>\n'
        if "type" in chars:
            output_data += f'<strong>Type:</strong> {chars["type"]}<br/>\n'

        output_data += "</p>\n"
        output_data += "</li>"
    return output_data


def website_load_data(file_path):
    """ Loads the HTML Text """
    with open(file_path, "r", encoding="utf-8") as handle:
        html_data = handle.read()
        return html_data


def replace_marker_with_data(website_text_data, formatted_animal_text):
    """ Substitutes the specified placeholder with its formatted string equivalent. """
    new_website_text = website_text_data.replace("__REPLACE_ANIMALS_INFO__", formatted_animal_text)
    return new_website_text


def created_new_html_data(new_website_text_data):
    """ Writes a new HTML file and fills it with content"""
    with open("animals.html", "w") as handle:
        handle.write(new_website_text_data)


def main():
    """Main entry point of the script."""
    animals_data = json_load_data('animals_data.json')
    formatted_animal_text = create_animal_data_text(animals_data)
    website_text_data = website_load_data('animals_template.html')
    new_website_text_data = replace_marker_with_data(website_text_data, formatted_animal_text)
    created_new_html_data(new_website_text_data)
    print("Program completed successfully.")


if __name__ == "__main__":
    main()