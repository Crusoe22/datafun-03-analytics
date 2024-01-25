

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
        print(f"Text data saved to {filename}")
    else:
        print(f"Failed to fetch data: {response.status_code}")

# Function created to call and write text file creating data.txt file
def write_txt_file(folder_name, filename, data):
    file_path = Path(folder_name).joinpath(filename)  # use pathlib to join paths

    with file_path.open('w', encoding='utf-8') as file: #, encoding='utf-8-sig'
        file.write(data)
        
# Process Data - text 
def process_txt_file(folder_name, input_filename, output_filename):
    # Fetch the data
    txt_url = 'https://www.gutenberg.org/cache/epub/6130/pg6130.txt' 
    response = requests.get(txt_url)

    if response.status_code == 200:
        data = response.text
        write_txt_file(folder_name, input_filename, data)
        # processed_data = data  
        write_txt_requests_file(folder_name, output_filename, input_filename)

    else:
        print(f"Failed to fetch data: {response.status_code}")

def write_txt_requests_file(txt_folder_name, data_txt_file, input_filename):
    """Function 1. Process Text Data: Process text with lists and sets to demonstrate proficiency in working 
    with text files. Analyze text data to generate statistics like word count, frequency of words, etc., and format 
    these findings into a readable text file."""
    file_path = Path(txt_folder_name).joinpath(input_filename)  # use pathlib to join paths
    file_path_re = Path(txt_folder_name).joinpath(data_txt_file)
    
    with file_path.open('r', encoding='utf-8') as file: 
        content = file.read()
        words = content.split()
        word_count = len(words) 
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

    with file_path_re.open('w', encoding='utf-8') as file:
        file.write(f"\nWord count of file: {word_count}\n")
        file.write(f"\nWord frequency of file: {word_freq}\n")
        print(f"Generated statistics in {data_txt_file}")
          
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



'''Function 2. Process CSV Data: Process CSV files with tuples to demonstrate proficiency in 
working with tabular data. Extract and analyze data from CSV files to produce meaningful statistics, 
summaries, or insights, and save the insights as text files.'''

# Data acquisition - CSV data
def fetch_and_write_csv_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_csv_file(folder_name, filename, response.text)
    else:
        print(f"Failed to fetch data: {response.status_code}")

# Write Data - CSV 
def write_csv_file(folder_name, filename, data):
    file_path = Path(folder_name).joinpath(filename)  # use pathlib to join paths

    # Parse CSV data
    csv_data = parse_csv_data(data)

    with file_path.open('w', newline='', encoding='utf-8') as file: #  
        csv_writer = csv.writer(file)
        csv_writer.writerows(csv_data)
        print(f"CSV data saved to {file_path}")

# function to manipulate the csv data in this example, transforming to a row vs. 1 charac line straight down
def parse_csv_data(csv_text):
    csv_data = []
    csv_reader = csv.reader(StringIO(csv_text))
    for row in csv_reader:
        csv_data.append(row)
    return csv_data

# Process the data - CSV
def process_csv_file(csv_folder_name, input_filename, output_filename):
    # Fetch the data
    csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/Weather%20Data/city_attributes.csv'
    response = requests.get(csv_url)
    
    if response.status_code == 200:
        data = response.text
        write_csv_file(csv_folder_name, input_filename, data)
        # processed_data = data 
        create_data_csv(csv_folder_name, output_filename, input_filename)
    else:
        print(f"Failed to fetch data: {response.status_code}")


def create_data_csv(csv_folder_name, data_csv_file, input_filename):
    
    '''Function 2. Process CSV Data: Process CSV files with tuples to demonstrate proficiency in 
    working with tabular data. Extract and analyze data from CSV files to produce meaningful statistics, 
    summaries, or insights, and save the insights as text files.'''
    
    file_path = Path(csv_folder_name).joinpath(input_filename)  # use pathlib to join paths
    file_path_re = Path(csv_folder_name).joinpath(data_csv_file)
    
    tuple_data = ()
    tuple_list = list(tuple_data)

    us_count = 0
    canada_count = 0
    israel_count = 0

    with file_path.open('r', encoding='utf-8') as file: 
        reader = csv.reader(file)
        for i in reader:
            tuple_list.append(i)
            tuple_data = tuple(tuple_list)

    # Iterate through the data
    for city_data in tuple_data:

        city, country, lat, lon = city_data   
        # Check the country and update the counters
        if country == 'United States':
            us_count += 1
        elif country == 'Canada':
            canada_count += 1
        elif country == 'Israel':
            israel_count += 1
            
    with file_path_re.open('w', encoding='utf-8') as file:
        file.write(f"\nNumber of cities in the United States: {us_count}")
        file.write(f"\nNumber of cities in Canada: {canada_count}")
        file.write(f"\nNumber of cities in Israel: {israel_count}\n")
        file.write(f"\nDisplay tuple in columns:")
        for ii in tuple_data:
           file.write(f"{ii}\n") 
            
        print(f"Displayed csv data in tuple {data_csv_file}")
        



def main():
    ''' Main function to demonstrate module capabilities. '''
   
    print(f"Name: {'datafun-03-analytics-Nolan Moss'}\n")

    txt_url = 'https://www.gutenberg.org/cache/epub/6130/pg6130.txt' 

    csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/Weather%20Data/city_attributes.csv' 

    #excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/raw/master/cattle.xls' 
    
    #json_url = 'https://dog.ceo/api/breeds/image/random'

    txt_folder_name = 'data-txt'
    csv_folder_name = 'data-csv'
    # excel_folder_name = 'data-excel' 
    #json_folder_name = 'data-json' 

    txt_filename = 'data.txt'
    csv_filename = 'data.csv'
    #excel_filename = 'data.xls' 
    #json_filename = 'data.json' 


    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
    fetch_and_write_csv_data(csv_folder_name, csv_filename, csv_url)
    #fetch_and_write_excel_data(excel_folder_name, excel_filename, excel_url)
    #fetch_and_write_json_data(json_folder_name, json_filename, json_url)

    process_txt_file(txt_folder_name,'data.txt', 'results_txt.txt')
    process_csv_file(csv_folder_name,'data.csv', 'results_csv.txt')
    #process_excel_file(excel_folder_name,'data.xls', 'results_xls.txt')
    #process_json_file(json_folder_name,'data.json', 'results_json.txt')
    


if __name__ == "__main__":
    main()