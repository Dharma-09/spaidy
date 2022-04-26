from email import header
from turtle import title
from unicodedata import name
from unittest import result
from wsgiref import headers
import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

url="https://www.imdb.com/serach/title/?group=top_1000?ref_=adv_prv"
headers={"Accept-Language":"en-US,en=0.5"}
results=requests.get(url,headers=headers)

soup=BeautifulSoup(results.txt,"html.parser")

titles=[]
years=[]
time=[]
imdb_ratings=[]
metascores=[]
votes=[]
us_gross=[]

movie_div=soup.find_all('div',class_='lister-item mode-advanced')

for container in movie_div:

    #name
    name=container.h3.a.text
    titles.append(name)

    #year
    year=container.h3.find('span',class_='lister-item-year').text
    years.append(year)

    #time
    runtime=container.h3.find('span',class_='runtime').text if container.p.find('span',class_='runtime').text else '-'
    time.append(runtime)

    #IMDb_rating
    imdb=float(container.strong.text)
    imdb_ratings.append(imdb)

    #metascore
    m_score=container.find('span',class_='metascore').text if container.find('span',class_='metascore') else '-'

    #There are two nv containers,gran both of them as hey hold both are votes and the grosses
    nv=container.find_all('span',attrs={'name':'nv'})

    #filter nv for votes
    vote=nv[0].text
    votes.append(vote)

    #filter nv for gross
    grosses=nv[1].text if len(nv) > 1 else '-'
    us_gross.append(grosses)

#building Pandas dataframe
movies=pd.DataFrame({
    'movie':titles,
    'year':years,
    'timeMin':time,
    'imdb':imdb_ratings,
    'metascore':metascores,
    'votes':votes,
    'us_grossMillions':us_gross,
})

#cleaning data with Pandas
movies['year']=movies['year'].str.extract('(\d+)').astype(int)
movies['timeMin']=movies['timeMin'].str.extract('(\d+)').astype(int)
movies['metascore']=movies['metascore'].astype(int)
movies['votes']=movies['votes'].str.replace(',','').astype(int)
movies['us_grossMillions']=movies['us_grossMillions'].map(lambda x:x.lstrip('$')).rstrip('M')
movies['us_grossMillions']=pd.to_numeric(movies['us_grossMillions'],errors='coerce')

#save output
movies.to_csv('movies.csv')