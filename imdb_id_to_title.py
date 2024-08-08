# Load the dataset from the uploaded file <rating-short.xlsx>
import pandas as pd
file_path_notitle = '/content/rating-short.xlsx'
imdb_data_notitle = pd.read_excel(file_path_notitle)

import requests
from bs4 import BeautifulSoup

def get_movie_name(imdb_id):
  url = f"https://www.imdb.com/title/{imdb_id}/"
  headers = {'User-Agent': 'Mozilla/5.0'}
# Add a user-agent header
  response = requests.get(url, headers=headers)
  soup = BeautifulSoup(response.content, 'html.parser')
  title = soup.find('h1').text.strip()
  return title
movie_names = []
for imdb_id in imdb_data[' tconst']:
  movie_names.append(get_movie_name(imdb_id))

# Print the list of movie names
print(movie_names)

