"""Project 3 emphasizes skills in using Git for version control, 
creating and managing Python virtual environments, and handling different
types of data. The project involves fetching data from the web,
processing it using appropriate Python collections, and writing
the processed data to files."""

# Standard library imports
import csv
from io import StringIO 
from pathlib import Path

# External import
import requests 
import pandas as pd
import json

#Local module imports 
import Nolan_utils


# Fetch and manipulate txt data.
def fetch_and_write_txt_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        # Call function to save content 
        write_txt_file(folder_name, filename, response.text) 
        print(f"Text data saved to {filename}")
    else:
        print(f"Failed to fetch data: {response.status_code}")

# Function created to call and write text file creating data.txt file
def write_txt_file(folder_name, filename, data): 
    # Create path
    file_path = Path(folder_name).joinpath(filename)

    with file_path.open('w', encoding='utf-8') as file: 
        file.write(data)
        
# Process Data - text 
def process_txt_file(folder_name, input_filename, output_filename):
    # Fetch the data
    txt_url = 'https://www.gutenberg.org/cache/epub/6130/pg6130.txt' 
    response = requests.get(txt_url)

    if response.status_code == 200:
        data = response.text
        write_txt_file(folder_name, input_filename, data)
        write_txt_requests_file(folder_name, output_filename, input_filename)

    else:
        print(f"Failed to fetch data: {response.status_code}")

#Analyze text data to generate statistics
def write_txt_requests_file(txt_folder_name, data_txt_file, input_filename):
    # Create path
    file_path = Path(txt_folder_name).joinpath(input_filename)
    file_path_re = Path(txt_folder_name).joinpath(data_txt_file)
    
    with file_path.open('r', encoding='utf-8') as file: 
        content = file.read()
        words = content.split()
        word_count = len(words) 
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

    with file_path_re.open('w', encoding='utf-8') as file:
        file.write(f"\nWord count of file: {word_count}\n"
                   f"\nWord frequency of file: {word_freq}\n")
        print(f"Generated statistics in {data_txt_file}")
          
# Exception reporting
def fetch_txt_data(folder_name, url):
    try:
        response = requests.get(url)
        response.raise_for_status()  

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

# Fetch CSV data
def fetch_and_write_csv_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_csv_file(folder_name, filename, response.text)
    else:
        print(f"Failed to fetch data: {response.status_code}")

# Write CSV data
def write_csv_file(folder_name, filename, data):
    # Create path
    file_path = Path(folder_name).joinpath(filename)

    # Parse CSV data
    csv_data = parse_csv_data(data)

    with file_path.open('w', newline='', encoding='utf-8') as file: #  
        csv_writer = csv.writer(file)
        csv_writer.writerows(csv_data)
        print(f"CSV data saved to {file_path}")

# Function to manipulate the CSV data
def parse_csv_data(csv_text):
    csv_data = []
    csv_reader = csv.reader(StringIO(csv_text))
    for row in csv_reader:
        csv_data.append(row)
    return csv_data

# Process CSV Data
def process_csv_file(csv_folder_name, input_filename, output_filename):
    # Fetch the data
    csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/Weather%20Data/city_attributes.csv'
    response = requests.get(csv_url)
    
    if response.status_code == 200:
        data = response.text
        write_csv_file(csv_folder_name, input_filename, data)
        create_data_csv(csv_folder_name, output_filename, input_filename)
    else:
        print(f"Failed to fetch data: {response.status_code}")

# Extract and analyze data from CSV files
def create_data_csv(csv_folder_name, data_csv_file, input_filename):
    # Create path
    file_path = Path(csv_folder_name).joinpath(input_filename)
    file_path_re = Path(csv_folder_name).joinpath(data_csv_file)
    
    tuple_data = ()
    tuple_list = list(tuple_data)

    # Variables for counter
    us_count = 0
    canada_count = 0
    israel_count = 0

    # Read from path
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
        file.write(f"\nNumber of cities in the United States: {us_count}"
                   f"\nNumber of cities in Canada: {canada_count}"
                   f"\nNumber of cities in Israel: {israel_count}\n")
        
        file.write(f"\nDisplay tuple in columns:")
        for ii in tuple_data:
           file.write(f"{ii}\n") 
            
        print(f"Displayed csv data in tuple {data_csv_file}")

# Data acquisition - excel data
def fetch_and_write_excel_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_excel_file(folder_name, filename, response.content)
    else:
        print(f"Failed to fetch Excel data: {response.status_code}")

# Write Excel data
def write_excel_file(folder_name, filename, data):
    file_path = Path(folder_name).joinpath(filename)

    with open(file_path, 'wb') as file:
        file.write(data)
        print(f"Excel data saved to {file_path}")

# Process Excel data
def process_excel_file(excel_folder_name, input_filename, output_filename):
    # Fetch the data
    excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/raw/master/airline.xls'
    response = requests.get(excel_url)
    
    if response.status_code == 200:
        data = response.content
        write_excel_file(excel_folder_name, input_filename, data)
        excel_data_file(excel_folder_name, input_filename, output_filename)
        
    else:
        print(f"Failed to fetch data: {response.status_code}")

# Extract and analyze data from Excel file
def excel_data_file(folder_name, filename, output_filename):
    # Load the Excel file into a pandas DataFrame
    file_path = Path(folder_name).joinpath(filename)  
    file_txt_path = Path(folder_name).joinpath(output_filename)  
    df = pd.read_excel(file_path)

    # Column names in Execl sheet
    columns_to_process = ['Y', 'W', 'R', 'L', 'K']

    with file_txt_path.open('w', encoding='utf-8') as file:
        file.write(f"\nThese are some insightful statistics from the xls data.\n")

    for column_name in columns_to_process:
        # Extract values from column B
        column_values = df.loc[2:33, column_name]

        # Calculate sum, min, max, and mean
        total_sum = column_values.sum()
        min_value = column_values.min()
        max_value = column_values.max()
        mean_value = column_values.mean()

       
        with file_txt_path.open('a', encoding='utf-8') as file:
            file.write(f"\nThe sum of all values in column {column_name} is: {total_sum}"
                       f"\nThe minimum value in column {column_name} is: {min_value}"
                       f"\nThe maximum value in column {column_name} is: {max_value}"
                       f"\nThe mean of all values in column {column_name} is: {mean_value}\n")

# Fetch JSON data
def fetch_and_write_json_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_json_file(folder_name, filename, response.content)
    else:
        print(f"Failed to fetch json data: {response.status_code}")

# Write JSON data
def write_json_file(folder_name, filename, data):
    file_path = Path(folder_name).joinpath(filename)  # use pathlib to join paths

    with file_path.open('wb') as file:
        file.write(data)
        print(f"Binary data saved to {file_path}")

# Process JSON data
def process_json_file(json_folder_name, input_filename, output_filename):
    # Fetch the data
    json_url = 'https://gist.githubusercontent.com/saltukalakus/124bba04327d8e5eab605d4fb66c53b8/raw/1043e2e62df1bb6118f0d8d1b81881fa45b46cbd/sample_users_with_id.json'
    response = requests.get(json_url)
    
    if response.status_code == 200:
        data = response.content
        write_json_file(json_folder_name, input_filename, data)
        dict_json(json_folder_name, input_filename, output_filename)
       
    else:
        print(f"Failed to fetch data: {response.status_code}")

# Analyze and format JSON data
def dict_json(folder_name, filename, output_filename):
    """Function 4. Process JSON Data: Process JSON data with dictionaries to demonstrate proficiency in working with labeled data. 
    Parse the JSON data to extract relevant information and present it in a simplified, human-readable text format."""
    file_path = Path(folder_name).joinpath(filename)  
    file_txt_path = Path(folder_name).joinpath(output_filename) 

    with file_path.open('r', encoding='utf-8') as file:
        json_data = file.read()

    # Parse JSON data
    user_data = json.loads(json_data)
    
    with file_txt_path.open('w', encoding='utf-8') as file:
        for i in user_data:
        # Extract relevant information
            user_id = i["user_id"] if "user_id" in i else None
            email = i["email"] if "email" in i else None
            name = i["name"] if "name" in i else None
            given_name = i["given_name"] if "given_name" in i else None
            family_name = i["family_name"] if "family_name" in i else None
            nickname = i["nickname"] if "nickname" in i else None
            last_ip = i["last_ip"] if "last_ip" in i else None
            logins_count = i["logins_count"] if "logins_count" in i else None
            created_at = i["created_at"] if "created_at" in i else None
            updated_at = i["updated_at"] if "updated_at" in i else None
            last_login = i["last_login"] if "last_login" in i else None
            email_verified = i["email_verified"] if "email_verified" in i else None


            file.write(f"User ID: {user_id}\nEmail: {email}\nName: {name}\nGiven Name: {given_name}\nFamily Name:"
                    f"{family_name}\nNickname: {nickname}\nLast IP: {last_ip}\nLogins Count: {logins_count}\nCreated At:"
                    f"{created_at}\nUpdated At: {updated_at}\nLast Login: {last_login}\nEmail Verified: {email_verified}\n\n")

# Main finction
def main():
    ''' Main function to demonstrate module capabilities. '''
   
    print(f"Name: {'datafun-03-analytics-Nolan Moss'}\n")

    # Url variables
    txt_url = 'https://www.gutenberg.org/cache/epub/6130/pg6130.txt' 
    csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/Weather%20Data/city_attributes.csv' 
    excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/raw/master/airline.xls' 
    json_url = 'https://gist.githubusercontent.com/saltukalakus/124bba04327d8e5eab605d4fb66c53b8/raw/1043e2e62df1bb6118f0d8d1b81881fa45b46cbd/sample_users_with_id.json'

    # Data folder variables
    txt_folder_name = 'data-txt'
    csv_folder_name = 'data-csv'
    excel_folder_name = 'data-excel' 
    json_folder_name = 'data-json' 

    # Data file variables
    txt_filename = 'data.txt'
    csv_filename = 'data.csv'
    excel_filename = 'data.xls' 
    json_filename = 'data.json' 

    # Call fetch functions
    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
    fetch_and_write_csv_data(csv_folder_name, csv_filename, csv_url)
    fetch_and_write_excel_data(excel_folder_name, excel_filename, excel_url)
    fetch_and_write_json_data(json_folder_name, json_filename, json_url)

    # Call process function
    process_txt_file(txt_folder_name,'data.txt', 'results_txt.txt')
    process_csv_file(csv_folder_name,'data.csv', 'results_csv.txt')
    process_excel_file(excel_folder_name,'data.xls', 'results_xls.txt')
    process_json_file(json_folder_name,'data.json', 'results_json.txt')    

if __name__ == "__main__":
    main()