# Pretty Downloader ![Version](https://img.shields.io/badge/Version-v0.1.0-orange?style=flat-square&url=https://github.com/DEADSEC-SECURITY/pretty-downloader/blob/main/CHANGELOG.md) ![Python_Version](https://img.shields.io/badge/Python-3.7%2B-blue?style=flat-square) ![License](https://img.shields.io/badge/License-MIT-red?style=flat-square) ![Donate](https://img.shields.io/badge/Donate-Crypto-yellow?style=flat-square)

## 📝 CONTRIBUTIONS

Before doing any contribution read <a href="https://github.com/DEADSEC-SECURITY/pretty-downloader/blob/main/CONTRIBUTING.md">CONTRIBUTING</a>.

## 📧 CONTACT

Email: amng835@gmail.com

General Discord: https://discord.gg/dFD5HHa

Developer Discord: https://discord.gg/rxNNHYN9EQ

## 📥 INSTALLING
<a href="https://pypi.org/project/Pretty-Downloader">Latest PyPI stable release</a>
```bash
pip install pretty-downloader
```

## ⚙ HOW TO USE
```python
import pretty_downloader
pretty_downloader.download(<YOUR URL>)
```
OR
```python
from pretty_downloader import download
download(<YOUR URL>)
```

## 🤝 PARAMETERS
- url : str, required
  - This should be the url of the file you wish to download
- file_path : str, optional
  - The path to save the file (Default: "")
- file_name : str, optional 
  - The file name you want the file to be saved with. Should include file extension (Default: None)
- name : str, optional
  - The name you want to appear in the progress bar (default: 'Download progress')
- block_size : int, optional
  - The size of the download block (Default: 1024)
- proxies : dict, optional
  - Dictionary of proxies to be used (Default: None)
  - Example: {'http': 'http://135.125.218.47:8080'}
  
- RETURNS: Path of file downloaded


## 🖼️ SCRIPT SCREENSHOTS & VIDEOS

  ![alt text](https://s4.gifyu.com/images/New-video.gif)
