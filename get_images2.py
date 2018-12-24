from google_images_download import google_images_download   #importing the library
import sys

busca = sys.argv[1]
limit = sys.argv[2]

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":busca,"limit":limit,"print_urls":True, "delay":1, "output_directory":"train", "prefix":busca}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images