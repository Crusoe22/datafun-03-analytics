"""2. Project Start
In your Python file, create a docstring with a brief 
introduction to your project."""


"""3. Import Dependencies"""
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
#import pandas as pd

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
        write_txt_file(folder_name, filename, response.text)
    else:
        print(f"Failed to fetch data: {response.status_code}")

'''def fetch_and_write_excel_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        # Call your write function to save the response content
        dataframe = pd.read_csv(pd.compat.StringIO(response.text))
        write_excel_file(folder_name, filename, dataframe)
    else:
        print(f"Failed to fetch Excel data: {response.status_code}")'''

'''5. Write Data
Write functions to save content to different 
file types (e.g., text, CSV, JSON).'''

from pathlib import Path

def write_txt_file(folder_name, filename, data):
    file_path = Path(folder_name).join_path(filename) # use pathlib to join paths
    with file_path.open('w') as file:
        file.write(data)
        print(f"Text data saved to {file_path}")


'''def write_excel_file(folder_name, filename, data):
    file_path = Path(folder_name).join_path(filename) # use pathlib to join paths
    with open(file_path, 'wb') as file:
        file.write(response.content)
        print(f"Excel data saved to {file_path}")'''

""" 6. Process Data and Generate Output
Write functions to read, process, and write results using 
appropriate Python collections (lists, sets, dictionaries,
 etc.). Demonstrate understanding of each collection data
  type's characteristics and usage.

Process the fetched data using appropriate Python collections 
and generate insightful analytics. The results of the processing 
should be formatted and written into text files.

Function 1. Process Text Data: Process text with lists and sets 
to demonstrate proficiency in working with text files. Analyze 
text data to generate statistics like word count, frequency of 
words, etc., and format these findings into a readable text file.

Function 2. Process CSV Data: Process CSV files with tuples 
to demonstrate proficiency in working with tabular data. Extract
 and analyze data from CSV files to produce meaningful statistics
 , summaries, or insights, and save the insights as text files.

Function 3. Process Excel Data: Extract and analyze data from
 Excel files to produce meaningful statistics, summaries, or 
 insights, and save the insights as text files.

Function 4. Process JSON Data: Process JSON data with 
dictionaries to demonstrate proficiency in working with labeled
 data. Parse the JSON data to extract relevant information and 
 present it in a simplified, human-readable text format."""

"""8. Main Function
Implement a main() function to test the folder creation
 functions and demonstrate the use of imported modules. For 
 example:"""
 
def main():
    ''' Main function to demonstrate module capabilities. '''

    #print(f"Name: {yourname_attr.my_name_string}")

    txt_url = 'https://shakespeare.mit.edu/romeo_juliet/full.html'

    csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/World%20Happiness%20Data/2020.csv' 

    excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/raw/master/cattle.xls' 
    
    json_url = 'http://api.open-notify.org/astros.json'

    txt_folder_name = 'data-txt'
    csv_folder_name = 'data-csv'
    excel_folder_name = 'data-excel' 
    json_folder_name = 'data-json' 

    txt_filename = 'data.txt'
    csv_filename = 'data.csv'
    excel_filename = 'data.xls' 
    json_filename = 'data.json' 

    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
    #fetch_and_write_csv_data(csv_folder_name, csv_filename,csv_url)
    #fetch_and_write_excel_data(excel_folder_name, excel_filename,excel_url)
    #fetch_and_write_json_data(json_folder_name, json_filename,json_url)

    #process_txt_file(txt_folder_name,'data.txt', 'results_txt.txt')
    #process_csv_file(csv_folder_name,'data.csv', 'results_csv.txt')
    #process_excel_file(excel_folder_name,'data.xls', 'results_xls.txt')
    #process_json_file(json_folder_name,'data.json', 'results_json.txt')

    # Find some data you care about. What format is it? How will you ingest the data?
    # What do you want to extract and write? What export format will you use?
    # Process at least TWO unique data sets and describe your work clearly.
    # Use the README.md and your code to showcase your ability to work with data.


"""9. Conditional Script Execution
Ensure the main function only executes when the script is
 run directly, not when imported as a module by using standard 
 boilerplate code."""

if __name__ == "__main__":
    main()