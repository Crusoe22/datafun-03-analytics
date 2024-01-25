"""Function 1. Process Text Data: Process text with lists and sets to demonstrate proficiency in working 
with text files. Analyze text data to generate statistics like word count, frequency of words, etc., and format 
these findings into a readable text file."""

# Project Module 3 
"""Python module that demonstrates skills in fetching data from the web, 
processing it using Python collections, and writing the processed data 
to different file formats."""

# Standard library imports
import csv
from io import StringIO #Check this
from pathlib import Path
import io #CHECK

# External import
import requests 
import pandas as pd

#Local module imports 

#Add local imports


# Data acquisition - text data
def fetch_and_write_txt_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_txt_file(folder_name, filename, response.text) # Call function to save content
    else:
        print(f"Failed to fetch data: {response.status_code}")

# Function created to call and write text file creating data.txt file
def write_txt_file(folder_name, filename, data):
    file_path = Path(folder_name).joinpath(filename)  # use pathlib to join paths

    # Create the folder if it doesn't exist
    #file_path.parent.mkdir(parents=True, exist_ok=True) #CHECK

    with file_path.open('w', encoding='utf-8') as file: #, encoding='utf-8-sig'
        file.write(data)
        print(f"Text data saved to {file_path}")

# Process Data - text 
def process_txt_file(folder_name, input_filename, output_filename):
    # Fetch the data
    txt_url = 'https://www.gutenberg.org/cache/epub/6130/pg6130.txt' 
    response = requests.get(txt_url)
    
    if response.status_code == 200:
        data = response.text
        write_txt_file(folder_name, input_filename, data)
        processed_data = data  
        write_txt_file(folder_name, output_filename, processed_data)
    else:
        print(f"Failed to fetch data: {response.status_code}")


# Exception reporting
def fetch_txt_data(folder_name, url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        # Will raise an HTTPError 
        # if the HTTP request returns an unsuccessful status code

        # Assuming the response content is text data
        file_path = Path(folder_name) / 'data.txt'
        with open(file_path, 'w') as file:
            file.write(response.text)
        print(f"Text data saved to {file_path}")

    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Oops: Something Else: {err}")
    except IOError as e:
        print(f"I/O error({e.errno}): {e.strerror}")


def main():
    ''' Main function to demonstrate module capabilities. '''
   
    print(f"Name: {'datafun-03-analytics-Nolan Moss'}")

    txt_url = 'https://www.gutenberg.org/cache/epub/6130/pg6130.txt' 

    csv_url = 'https://raw.githubusercontent.com/FoamyGuy/CSVListExample/master/assets/states.csv' 

    excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/raw/master/cattle.xls' 
    
    json_url = 'https://dog.ceo/api/breeds/image/random'

    txt_folder_name = 'data-txt'
    csv_folder_name = 'data-csv'
    excel_folder_name = 'data-excel' 
    json_folder_name = 'data-json' 

    txt_filename = 'data.txt'
    csv_filename = 'data.csv'
    excel_filename = 'data.xls' 
    json_filename = 'data.json' 

    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
    fetch_and_write_csv_data(csv_folder_name, csv_filename, csv_url)
    fetch_and_write_excel_data(excel_folder_name, excel_filename, excel_url)
    fetch_and_write_json_data(json_folder_name, json_filename, json_url)

    process_txt_file(txt_folder_name,'data.txt', 'results_txt.txt')
    process_csv_file(csv_folder_name,'data.csv', 'results_csv.txt')
    process_excel_file(excel_folder_name,'data.xls', 'results_xls.txt')
    process_json_file(json_folder_name,'data.json', 'results_json.txt')

if __name__ == "__main__":
    main()