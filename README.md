# Animal Data Website Generator

This project is a Python-based tool that allows users to search for animals and automatically generates a stylish website showcasing their characteristics, such as diet, location, and type. It uses the API Ninjas service to fetch real-time data.

## Features
- **Dynamic Search:** Search for any animal using the API Ninjas database.
- **Automated Web Generation:** Converts API data into a clean, formatted HTML website.
- **Secure Architecture:** Uses environment variables to protect sensitive API keys.
- **Robust Error Handling:** Provides user feedback if an animal is not found or if the input is empty.

## Prerequisites
- Python 3.x
- An API Key from [API Ninjas](https://api-ninjas.com/api/animals)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <"https://github.com/ericbarwinsky/My-Zootopia-with-API">

## Configuration:

Create a .env file in the root directory.
Add your API Key to the file:
Plaintext: API_KEY='YOUR_API_KEY_HERE'

## Usage
1. Run the generator: `py animals_web_generator.py`
2. Enter an animal name when prompted.
3. Open `animals.html` in your browser to view the result.

## Project Structure
- `animals_web_generator.py`: Main entry point; handles user input and HTML logic.
- `data_fetcher.py`: Handles API requests and environment variables.
- `animals_template.html`: The base HTML file with placeholders.
- `.env`: Local storage for your private API key.