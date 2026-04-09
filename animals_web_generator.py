import json
import os

import data_fetcher  # Importiert dein neues Modul


def save_data_to_json(data, animal_name):
	"""Saves the fetched animal data into a JSON file."""
	file_name = f"{animal_name}_data.json"
	try:
		with open(file_name, "w", encoding="utf-8") as handle:
			json.dump(data, handle, indent=4)
		return file_name
	except IOError as e:
		print(f"Error saving JSON file: {e}")
		return None


def delete_temporary_file(file_path):
	"""Removes the specified file from the file system."""
	if file_path and os.path.exists(file_path):
		try:
			os.remove(file_path)
		except OSError as e:
			print(f"Error deleting temporary file: {e}")


def cleaned_animal_name(name):
	"""Normalizes typographic special characters."""
	return name.replace("’", "'").replace("‘", "'")


def serialize_animal(animal_obj):
	"""Serializes a single animal dictionary into an HTML list item string."""
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
	output += '  </p>\n</li>'
	return output


def create_animal_data_text(animals_data, target_animal):
	"""Aggregates HTML strings or returns a funny error message."""
	if not animals_data:
		return f'<h2>The animal "{target_animal}" doesn\'t exist. Maybe it\'s hiding in another dimension? 🦄</h2>'
	return "\n".join([serialize_animal(animal) for animal in animals_data])


def load_file_content(file_path):
	"""Reads file content with error handling."""
	try:
		with open(file_path, "r", encoding="utf-8") as handle:
			return handle.read()
	except FileNotFoundError:
		print(f"Error: Template file '{file_path}' not found.")
		return ""


def write_html_to_file(file_content, output_path):
	"""Writes the final HTML content."""
	try:
		with open(output_path, "w", encoding="utf-8") as handle:
			handle.write(file_content)
		return True
	except IOError as e:
		print(f"Error writing HTML file: {e}")
		return False


def main():
	"""Main orchestration logic using the data_fetcher module."""
	while True:
		target_animal = input("Please enter the animal's name for the website: ").strip()
		if target_animal:
			break
		print("Input cannot be empty. Please enter a valid name.")

	target_animal_lower = target_animal.lower()

	# Hier wird das neue Modul genutzt:
	animals_data = data_fetcher.fetch_data(target_animal_lower)

	json_file = None
	if animals_data:
		json_file = save_data_to_json(animals_data, target_animal_lower)

	formatted_animal_text = create_animal_data_text(animals_data, target_animal)
	template_content = load_file_content('animals_template.html')

	if not template_content:
		return

	final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", formatted_animal_text)

	if write_html_to_file(final_html, "animals.html"):
		print(f"Success: 'animals.html' has been updated for '{target_animal}'.")

	if json_file:
		delete_temporary_file(json_file)


if __name__ == "__main__":
	main()