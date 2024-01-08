import requests
from bs4 import BeautifulSoup
import json

def scrape_table_to_json(url, table_index, json_filename):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        tables = soup.find_all('table')
        
        if table_index < len(tables):
            table = tables[table_index]
            table_data = []
            
            for row in table.find_all('tr'):
                row_data = [cell.text.strip() for cell in row.find_all(['th', 'td'])]
                table_data.append(row_data)
            
            with open(json_filename, 'w') as json_file:
                json.dump(table_data, json_file, indent=2)
                
            print(f"Table data scraped successfully and saved to {json_filename}")
        else:
            print(f"Error: Table index {table_index} out of range.")
    else:
        print(f"Error: Failed to fetch data from {url}")

# Example usage for the first table on the UCI Machine Learning Repository website
uci_url = 'https://archive.ics.uci.edu/ml/datasets.php'
uci_json_filename = 'uci_table_data.json'
scrape_table_to_json(uci_url, 0, uci_json_filename)