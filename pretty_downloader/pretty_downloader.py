from tqdm import tqdm
import requests

# Notice: This script is possible because of the library TQDM
# https://github.com/tqdm/tqdm

# Download function will process the download and display a download bar so its pretty
# and allows the user to see the progress of the download

# Variables available
# url: Url to download the file from
# file_path: Path to save the file
# file_name: Name of the file with extension
# name: Name to display in the download bar
# block_size: The size of each block

def download(url, file_path='', file_name=None, name='Download progress', block_size=1024):
    resp = requests.get(url, stream=True)
    total_size_in_bytes = int(resp.headers.get('content-length', 0))

    bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True, desc=name)

    # Check if a file name is provided if not it will get
    # the file name from the url
    # Example: http://ipv4.download.thinkbroadband.com/1GB.zip
    # The file name would be 1GB.zip
    if not file_name:
        file_name = url.split('/')[-1]

    # Check if a path was provided if not it
    # will use the current path from running the
    # script
    if file_path != '':
        if file_path[-1] == '/':
            file_path = file_path + file_name
        else:
            file_path = file_path + '/' + file_name
    else:
        file_path = file_name

    # Start processing the download
    with open(file_path, 'wb') as file:
        for data in resp.iter_content(block_size):
            bar.update(len(data))
            file.write(data)
    bar.close()
    return True
