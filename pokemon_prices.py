import csv
import requests
from urllib.parse import quote

API_KEY = "5a2bae51-bcfc-4744-9d81-6fdf712cbf14"  # Replace with your actual API key

def fetch_price(pokemon_name, card_number, year=None):
    url = f"https://api.mavin.io/search"

    query = f"{pokemon_name} {card_number}"
    if year:
        query += f" {year}"
    
    #print(query)

    headers = {
        "accept": "application/json",
        "X-API-KEY": API_KEY
    }

    # Manually format the query parameter
    formatted_query = quote(query, safe="")

    # Pass the formatted query as a string
    url += f"?q={formatted_query}"
    
    response = requests.get(url, headers=headers)
    #print(f"Request URL: {response.url}")  # Debug statement
    #print(f"Response status: {response.status_code}")  # Debug statement

    if response.status_code != 200:
        print(f"Error: {response.text}")  # Debug statement
        return None

    data = response.json()

    if data.get("totalCount", 0) > 0:
        return data["marketValue"]
    else:
        return None



def fetch_prices_from_csv(file_path):
    with open(file_path, "r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            pokemon_name, card_number, *year = row
            year = year[0] if year else None
            price = fetch_price(pokemon_name, card_number, year)
            with open("found.csv", "a", newline='') as found_file:
                found_writer = csv.writer(found_file, lineterminator="\n")
                if price:
                    print(f"{pokemon_name}, {card_number}, {year if year else ''}: ${price}")
                    found_writer.writerow([pokemon_name, card_number, year if year else '', price])
                else:
                    print(f"{pokemon_name}, {card_number}, {year if year else ''}: Price not found")
                    found_writer.writerow([pokemon_name, card_number, year if year else '', "Price not found"])


if __name__ == "__main__":
    file_path = "pokemon_cards.csv"  # Replace with the path to your CSV file
    fetch_prices_from_csv(file_path)
