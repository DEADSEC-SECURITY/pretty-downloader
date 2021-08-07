from setuptools import find_packages, setup
import pathlib

README = (pathlib.Path(__file__).parent / "README.md").read_text(encoding='utf8')

setup(
    name='pretty-downloader',
    packages=find_packages(),
    version='0.1.0',
    description='This is a simple python pretty downloader for your projects.',
    long_description=README,
    long_description_content_type='text/markdown',
    author='DeadSec-Security',
    author_email='amng835@gmail.com',
    url='https://github.com/DEADSEC-SECURITY/pretty-downloader',
    keywords=[
        'progressbar',
        'downloader',
        'download',
        'console',
        'bar',
        'progress',
        'download-bar'
    ],
    license='MIT',
    install_requires=[
        'tqdm==4.57.0',
        'requests==2.25.1'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==6.2.2'],
    python_requires='>=3.7'
)
