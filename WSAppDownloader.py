from modules.storergadguard import get_files
from modules.dl import download

download(get_files(input("Enter Microsoft Store URL: ")), input("Enter save path: "),
         input("Enter architecture (x64/x86): "))
