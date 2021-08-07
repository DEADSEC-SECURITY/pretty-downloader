'''
    This file contains all functions that make
    this library work :)

    By: Antonio Goncalves -> AKA: DEADSEC-SECURITY
'''

import os
import requests
from tqdm import tqdm

def download(url: str, file_path: str = '',
             file_name=None, name: str = 'Download progress',
             block_size: int = 1024, proxies=None):

    '''
        Download function will process the download
        and display a download bar so its pretty and
        allows the user to see the progress of the download

        A big thanks to TQDM for the library that allows
        this script to have its progress bar:
        https://github.com/tqdm/tqdm

        :param url: str -> Url to download file
        :param file_path: str -> Path to save file
        :param file_name: str -> Name of file with extension
        :param name: str -> Name of tqdm progress bar
        :param block_size: int -> Size of download block
        :param proxies: dict -> Dictionary of proxies
        :return: str -> Saved file path
    '''

    if proxies:
        resp = requests.get(url, stream=True, proxies=proxies)
    else:
        resp = requests.get(url, stream=True)

    total_size_in_bytes = int(resp.headers.get('content-length', 0))

    tqdm_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True, desc=name)

    '''
        Check if a file name is provided if not it will get
        the file name from the url
        Example: http://ipv4.download.thinkbroadband.com/1GB.zip
        The file name would be 1GB.zip
    '''
    if not file_name:
        file_name = url.split('/')[-1]

    '''
        Check if a path was provided if not it
        will use the current path from running the
        script
    '''
    if file_path != '':
        file_path = os.path.join(file_path, file_name)
    else:
        file_path = file_name

    # Start processing the download
    with open(file_path, 'wb') as file:
        for data in resp.iter_content(block_size):
            tqdm_bar.update(len(data))
            file.write(data)
    tqdm_bar.close()

    return file_path
