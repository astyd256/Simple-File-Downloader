# Simple File Downloader

This script provides a simple way to download files from the internet. It prompts the user for a URL and then downloads the file, displaying a progress bar during the download.

## Features

- Download files from a provided URL.
- Display a progress bar with percentage and bytes downloaded.

## Requirements

- Python 3.x
- `requests` library

## Usage

1. Run the script:

        `python SFD.py`

2. Enter the desired URL to download the file. The file will be saved with the same name as in the URL in the directory where the script is run.

3. The file will start downloading and a progress bar will be displayed.

4. If you wish to quit without downloading, simply type `q` and press enter.


## Note

- The downloaded file will be saved in the current directory with the same name as in the URL.
- The default chunk size for downloading is set to 2048 bytes. This can be adjusted if needed.

## Contributions

Feel free to contribute to this script by submitting pull requests or opening issues.

