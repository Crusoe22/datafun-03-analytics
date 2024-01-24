import requests
import pathlib as Path

def fetch_and_write_txt_data(folder_name, filename, url):
    response = requests.get(url, verify=False)
    if response.status_code == 2:
        # Call your write function to save the response content
        write_txt_file(folder_name, filename, response.text)
        
    else:
        print(f"Failed to fetch data: {response.status_code}")

def write_txt_file(folder_name, filename, data):
    file_path = Path(folder_name).joinpath(filename) # use pathlib to join paths
    with file_path.open('w') as file:
        file.write(data)
        print(f"Text data saved to {file_path}")

def main():

    txt_url = r'https://shakespeare.mit.edu/romeo_juliet/full.html'
    txt_folder_name = 'data-txt'
    txt_filename = 'data.txt'

    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)


if __name__ == "__main__":
    main()