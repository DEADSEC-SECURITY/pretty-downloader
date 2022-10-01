"""
    This file contains all functions that make
    this library work :)
"""

#  Copyright (c) 2022.
#  All rights reserved to the creator of the following script/program/app, please do not
#  use or distribute without prior authorization from the creator.
#  Creator: Antonio Manuel Nunes Goncalves
#  Email: amng835@gmail.com
#  LinkedIn: https://www.linkedin.com/in/antonio-manuel-goncalves-983926142/
#  Github: https://github.com/DEADSEC-SECURITY

import os
from typing import Optional

import requests
from tqdm import tqdm


DEFAULT_HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.6',
    'accept-encoding': 'gzip, deflate',
    "content-type": "application/json",
}


def _download_with_progress(resp: requests.Response, file_path: str, block_size: int,
                            bar_name: str):
    """
        Downloads the file using tqdm progress bar

        :param resp:
        :return:
    """

    total_size_in_bytes = int(resp.headers.get('content-length', 0))
    tqdm_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True, desc=bar_name)

    with open(file_path, 'wb') as file:
        for data in resp.iter_content(block_size):
            tqdm_bar.update(len(data))
            file.write(data)
    tqdm_bar.close()


def _download_no_progress(resp: requests.Response, file_path: str, block_size: int):
    """
        Downloads the file but without showing a progress bar.

        :param resp:
        :param file_path:
        :param block_size:
        :return:
    """
    with open(file_path, 'wb') as file:
        for data in resp.iter_content(block_size):
            file.write(data)


def download(url: str, file_path: str = '', file_name: Optional[str] = None,
             show_progress: bool = True, bar_name: str = 'Download progress',
             block_size: int = 1024, proxies: Optional[dict] = None, headers: Optional[dict] = None,
             *args, **kwargs):
    """
        Download function will process the download
        and display a download bar so its pretty and
        allows the user to see the progress of the download

        A big thanks to TQDM for the library that allows
        this script to have its progress bar:
        https://github.com/tqdm/tqdm

        :param url: str -> Url to download file
        :param file_path: str -> Path to save file
        :param file_name: str -> Name of file with extension
        :param show_progress: bool -> Display progress bar or not
        :param bar_name: str -> Name of tqdm progress bar
        :param block_size: int -> Size of download block
        :param proxies: dict -> Dictionary of proxies
        :param headers: dict -> Dictionary of headers
        :param args: Extra parameters are passed to request library
        :param kwargs: Extra parameters are passed to request library
        :return: str -> Saved file path
    """

    # Use default headers if none are passed
    if not headers:
        headers = DEFAULT_HEADERS

    # If file_name is not passed it will get it from the url itself
    if not file_name:
        file_name = url.split('/')[-1]

    # If destination path is not passed use current path
    if file_path != '':
        file_path = os.path.join(file_path, file_name)
    else:
        file_path = file_name

    resp = requests.get(url, stream=True, proxies=proxies, headers=headers, *args, **kwargs)

    # Start processing the download
    if show_progress:
        _download_with_progress(resp, file_path, block_size, bar_name)
    else:
        _download_no_progress(resp, file_path, block_size)

    return file_path
