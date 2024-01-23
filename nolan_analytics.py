
'''Organize your project imports following
 conventions. For example, standard library 
 imports first, then external library imports,
then local module imports. Continue to
practice importing your own modules 
and reuse your prior code when building your 
project folders.'''

# Standard library imports
import csv
import pathlib 

# External library imports (requires virtual environment)
import requests  

# Local module imports
# import yourname_attr      
# import yourname_projsetup 

'''4. Data Acquisition
Use the requests library to fetch data from 
specified web APIs or online data sources. This 
will include JSON, CSV, and plain text data. 
After a successful fetch, call the appropriate 
write function to save the data to a file'''

import requests

def fetch_and_write_txt_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        # Call your write function to save the response content
    else:
        print(f"Failed to fetch data: {response.status_code}")

def fetch_and_write_excel_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        # Call your write function to save the response content
    else:
        print(f"Failed to fetch Excel data: {response.status_code}")

'''5. Write Data
Write functions to save content to different 
file types (e.g., text, CSV, JSON).'''

from pathlib import Path

def write_txt_file(folder_name, filename, data):
    file_path = Path(folder_name).join_path(filename) # use pathlib to join paths
    with file_path.open('w') as file:
        file.write(data)
        print(f"Text data saved to {file_path}")


def write_excel_file(folder_name, filename, data):
    file_path = Path(folder_name).join_path(filename) # use pathlib to join paths
    with open(file_path, 'wb') as file:
        file.write(response.content)
        print(f"Excel data saved to {file_path}")