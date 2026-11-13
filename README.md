# API-Sunset-Checker

A Python program that retrieves sunset times for two different locations: Malaga, Spain, and Denpasar, Bali. It uses the `requests` library to send HTTP GET requests to the Sunrise-Sunset API, retrieves the sunset information in JSON format, and displays the results based on the user's selection.

## Features

- **Two Location Support:** Retrieves sunset times for Malaga and Denpasar.
- **Location Selection:** Allows users to check Malaga, Denpasar, or both locations.
- **API Integration:** Uses the Sunrise-Sunset API to retrieve real-time astronomical data.
- **HTTP Requests:** Sends GET requests using Python's `requests` library.
- **JSON Processing:** Extracts sunset information from API responses.
- **Coordinate-Based Search:** Uses latitude and longitude to identify each location.

## Technologies Used

- Python 3
- Requests Library
- Sunrise-Sunset API

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Install the Requests library:

   ```bash
   pip install requests
   ```

3. Save the code in a file named `sunset_checker.py`.
4. Open a terminal or command prompt.
5. Run the program:

   ```bash
   python sunset_checker.py
   ```

6. Choose one of the following options:
   - `malaga` – Check Malaga's sunset time.
   - `denpasar` – Check Denpasar's sunset time.
   - `both` – Check both locations.

## Example

**Example Input:**

```text
Welcome to Sunset Checker for Malaga and Denpasar!

Do you want to check Malaga or Denpasar, or both? both
```

**Example Output:**

```text
Top is Malaga Bottom is Denpasar:

05:45:00 PM
06:30:00 PM
```

*Note: These times are illustrative only. Actual sunset times depend on the date and location.*

## Concepts Practiced

- **API Integration:** Connecting a Python application to an external API.
- **HTTP Requests:** Using `requests.get()` to retrieve information from an API endpoint.
- **Query Parameters:** Passing latitude and longitude through the `params` argument.
- **JSON:** Converting API responses into Python dictionaries using `.json()`.
- **Conditional Statements:** Handling different user selections.
- **Loops:** Iterating through multiple location coordinates.
- **Lists and Dictionaries:** Organizing geographic coordinates and request parameters.
- **String Formatting:** Displaying API results using f-strings.

## Language

Python 3
