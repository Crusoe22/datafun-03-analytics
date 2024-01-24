import requests
import pathlib as Path

def fetch_and_write_txt_data(folder_name, filename, url):
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        # Call your write function to save the response content
        write_txt_file(folder_name, filename, response.text)
        
    else:
        print(f"Failed to fetch data: {response.status_code}")

def write_txt_file(folder_name, filename, data):
    file_path = Path(folder_name).joinpath(filename) # use pathlib to join paths
    with file_path.open('w') as file:
        file.write(data)
        print(f"Text data saved to {file_path}")

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

    txt_url = r'https://shakespeare.mit.edu/romeo_juliet/full.html'
    txt_folder_name = 'data-txt'
    txt_filename = 'data.txt'

    #fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
    fetch_txt_data(txt_folder_name, txt_url)


if __name__ == "__main__":
    main()