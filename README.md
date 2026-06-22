# Snapchat Data Tools

A set of Python tools for parsing and filtering Snapchat data exports.

## Tools

### `Snapshi.py`
Parses a Snapchat HTML data export file (`friends.html`) and extracts usernames and display names into a clean formatted table. Exports usernames to a text file for further processing.

### `Filtering.py`
A generic text-file line filter — prompts for a source `.txt` file and a search keyword, then exports all matching lines to a new file. Useful for filtering through extracted Snapchat username lists.

## Usage

### Extract usernames from Snapchat export
```bash
python Snapshi.py
```
This reads `friends.html` and outputs `snapchat_usernames_list.txt`.

### Filter usernames
```bash
python Filtering.py
```
Follow the interactive prompts to specify a source file and search keyword.

## Requirements
- Python 3.x
- BeautifulSoup4 (`pip install beautifulsoup4`)
