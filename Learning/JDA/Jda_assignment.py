'''
A python script to download an image provided in the plaintext file
Format: $ python Jda_assignment.py [input_file]
'''
import urllib.request
import argparse
import sys
def download_jpg(url, file_name,count, args):       # function to dowlnload jpg images
    try:                                            # retrieve image
        full_path = file_name + '.jpg'
        urllib.request.urlretrieve(url, full_path)
    except:                                         # image not loading
        print("There is an error in the link. Please check the file ",args," of line no ",count)
    return url, file_name

# args = sys.argv[1]
parser = argparse.ArgumentParser()                  #  full featured commandline parser which generally parses sys.argv and gives you back the data in a much easier to use fashion
parser.add_argument("file", help="plain text file in .txt")
args = parser.parse_args()
file = args.file
lines = [line.rstrip('\n') for line in open(file)]
count = 0                                           # to count error link in the plain text file
for url in lines:
    file_name = input("Enter the file "+url+" to save as: ")
    count += 1
    download_jpg(url, file_name,count, file)
print("Images Successfully saved in current directory")

