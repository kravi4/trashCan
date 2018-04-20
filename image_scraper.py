import json
import requests
from base64 import b64encode
from os import makedirs
from os.path import join, basename
from googleapiclient.discovery import build
import urllib
from bs4 import BeautifulSoup
import urllib

# Google search api info
goog_search_API="AIzaSyDN4oozjSRo-le_VJSGSV0I6Y5x8zly7VM"
cse_id="013600959693809398287:wjmd99g5gpa"


# In order to change the type of things search and the number of results adjust the parameters
def google_search(q="Recyclable goods", num=3):
	service = build("customsearch", "v1", developerKey=goog_search_API)
	res = service.cse().list(q=q,cx=cse_id, searchType='image', num=3,fileType='jpg', safe= 'off').execute()
	return res['items']


# In order to change the type of things search and the number of results ad
results=google_search()

# opens the file and saves the images
iterval=1
for item in results:
	file_name="Recyclable_goods"+"-"+str(iterval)+".jpg"
	urllib.urlretrieve(item["link"], file_name)

	

