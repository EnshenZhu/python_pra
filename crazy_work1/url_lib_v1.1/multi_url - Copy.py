import webbrowser
import os
from pathlib import Path

data_folder=Path(os.path.abspath('multi_url.exe').strip('multi_url.exe'))

file_to_open=data_folder/"url.txt"

print(data_folder)

with open(file_to_open) as source:
  for webpage in source:
    url = webpage.strip()   # remove leading and trailing characters
    webbrowser.open(url)    # command to open webpages
    
os.system("pause")