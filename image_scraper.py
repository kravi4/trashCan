import json
import requests
from base64 import b64encode
from os import makedirs
from os.path import join, basename
import googleapiclient
from googleapiclient.discovery import build
import urllib
from bs4 import BeautifulSoup
import urllib.request
import os
import ssl
import http
import shutil

ssl._create_default_https_context = ssl._create_unverified_context

# Google search api info
goog_search_API="AIzaSyA1SnhpLfHa9Cz36rs4Hz6J3n1TryYJpZw"
cse_id="013600959693809398287:wjmd99g5gpa"


# In order to change the type of things search and the number of results adjust the parameters
def google_search(q="Recyclable goods", start_val=1):
	try:
		service = build("customsearch", "v1", developerKey=goog_search_API)
		res = service.cse().list(q=q,cx=cse_id, searchType='image', num=10,fileType='jpg', safe= 'off', start=start_val).execute()
		return res['items']
	except googleapiclient.errors.HttpError as e:
		return -1


# Creates the recycling directory if it does not exist
def create_recycle_dir():
	if not os.path.exists("./recycle_data"):
		os.makedirs("./recycle_data")
	else:
		shutil.rmtree("./recycle_data")
		os.makedirs("./recycle_data")


# Creates the trash directory if it does not exist
def create_trash_dir():
	if not os.path.exists("./trash_data"):
		os.makedirs("./trash_data")
	else:
		shutil.rmtree("./trash_data")
		os.makedirs("./trash_data")

# Generates the recycling images
def recycle_gen(rec_terms):
	iterval=1
	for search in rec_terms:
		for i in list(range(100)):
			results=google_search(search, i+1)
			print(results)
			if (results!=-1):
				for item in results:
					file_name="./recycle_data/Recycle"+"-"+str(iterval)+".jpg"
					print("hi")
					try:
						urllib.request.urlretrieve(item["link"], file_name)
						iterval+=1
					except urllib.error.HTTPError as e:
						continue
					except ConnectionResetError:
						continue
					except http.client.HTTPException as e:
						continue
			else:
				continue

# Generates the trash images
def trash_gen(trash_terms):
	iterval=1
	for search in trash_terms:
		for i in list(range(100)):
			results=google_search(search, i+1)
			if (results!=-1):
				for item in results:
					file_name="./trash_data/Trash"+"-"+str(iterval)+".jpg"
					try:
						urllib.request.urlretrieve(item["link"], file_name)
						iterval+=1
					except urllib.error.HTTPError as e:
						continue
					except ConnectionResetError:
						continue
					except http.client.HTTPException as e:
						continue
			else:
				continue



recycle_search_terms=["Tin cans", "aluminum cans", "Glass Containers", "Cardboard", "Paper", "Plastic Bottles", "Phonebooks", "Magazines", "pictures of mail", "Office Paper", "newspaper", "steel cans", "soft drink glass bottles", "beer bottles", "wine bottles", "liquor bottles", "Paper Egg Cartons"]
trash_search_terms=["Plastic shopping bags", "plastic stretch wrap", "Styrofoam Egg Cartons", "styrofoam drinking cups", "paper receipts", "Food soiled containers", "greasy pizza boxes", "paper plates with food", "food", "plastic utensils"]

def main():
	create_recycle_dir()
	create_trash_dir()
	recycle_gen(recycle_search_terms)
	trash_gen(trash_search_terms)

if __name__=="__main__":
	main()


