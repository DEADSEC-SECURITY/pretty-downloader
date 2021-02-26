import pretty_downloader


def test_download():
    url = 'http://ipv4.download.thinkbroadband.com/1GB.zip'
    pretty_downloader.download(url)

if __name__ == '__main__':
    test_download()