from pretty_downloader import download

url = 'http://ipv4.download.thinkbroadband.com/1GB.zip'

def basic_download():
    print(download(url))

def path_download():
    print(download(url, file_path=r'C:\Users\amng8\Downloads'))

def name_download():
    print(download(url, file_name='NAME-TEST.zip'))

def progress_download():
    print(download(url, name='Download name test'))

def block_download():
    print(download(url, block_size=2048))

def full_download():
    print(download(url, file_path=r'C:\Users\amng8\Downloads',
                   file_name='NAME-TEST.zip', name='Download name test'
                   , block_size=2048))

if __name__ == '__main__':
    basic_download()
    path_download()
    name_download()
    progress_download()
    block_download()
    full_download()