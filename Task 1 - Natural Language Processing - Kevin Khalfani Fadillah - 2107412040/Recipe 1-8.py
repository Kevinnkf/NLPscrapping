from bs4 import BeautifulSoup
import requests
import pandas as pd
from pandas import Series, DataFrame
from ipywidgets import FloatProgress
from time import sleep
from IPython.display import display
import re
import pickle

url = 'http://www.imdb.com/chart/top?ref_=nv_mv_250_6'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
result = requests.get(url, headers=headers)
c = result.content
soup = BeautifulSoup(c,"lxml")

summary = soup.find('ul',{'class':'ipc-metadata-list'})


# Create empty lists to append the extracted data.
moviename = []
cast = []
description = []
rating = []
ratingoutof = []
year = []
genre = []
movielength = []
rot_audscore = []
rot_avgrating = []
rot_users = []

#regular expression to remove parentheses from the year
rgx = re.compile('[%s]' % '()')

#create a progress bar widget
f = FloatProgress(min=0, max=250)
display(f)

#iterate through each row in IMDb top 250 table 
for i, row in enumerate(summary.findAll('li')):
    for itemTitle in row.findAll('h3', {'class': 'ipc-title__text'}):
        number, title = itemTitle.text.split('.', 1)
        moviename.append(title)

    for yearLengthRated in row.findAll('div', {'class': 'cli-title-metadata'}):
        spans = yearLengthRated.findAll('span')
        year.append(spans[0].text)
        movielength.append(spans[1].text)
        rating.append("No Data")
        if len(spans) == 3:
            rating.append(spans[2].text)

    for ratingContainer in row.findAll('div', {'class': 'cli-ratings-container'}):
        raw = ratingContainer.find('span', {'class': 'ipc-rating-star--imdb'})
        parts = raw.text.split()
        rating.append(parts[0])
        ratingoutof.append(parts[1].replace('(', '').replace(')', ''))

    # Update the progress bar value
    f.value = i
    #sleep so it does not overwhelmed the server
    sleep(0.1)  

  
# List to pandas series
moviename = Series(moviename)
cast = Series(cast)
description = Series(description)
rating = Series(rating)
ratingoutof = Series(ratingoutof)
year = Series(year)
genre = Series(genre)
movielength = Series(movielength)
rot_audscore = Series(rot_audscore)
rot_avgrating = Series(rot_avgrating)
rot_users = Series(rot_users)

# creating dataframe and doing analysis
imdb_df = pd.concat([moviename,year,description,genre,
                    movielength,cast,rating,ratingoutof, rot_audscore,
                    rot_avgrating,rot_users],axis=1)
imdb_df.columns = ['moviename','year','description','genre',
                   'movielength','cast','imdb_rating',
                   'imdb_ratingbasedon','tomatoes_audscore',
                   'tomatoes_rating','tomatoes_ratingbasedon']
imdb_df['rank'] = imdb_df.index + 1
imdb_df.head(1)
imdb_df.to_csv("imdbdataexport.csv", index = False)

print(imdb_df)