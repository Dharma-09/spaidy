![image](https://user-images.githubusercontent.com/58421062/165298031-f0eb44a6-556b-4991-8045-7c9cded1c299.png)

# Spaidy(Web Crawler) 🕷
For this project, we’ll scrape data from IMDb’s “Top 1,000” movies, specifically the top 50 movies on this page. Here is the information we’ll gather from each movie listing:
* The title
* The year it was released
* How long the movie is
* IMDb’s rating of the movie
* The Metascore of the movie
* How many votes the movie got


# Tools 📌
* BeautifulSoup
* Pandas
* Numpy

# Saving Your Data to a CSV 📽
Below is the code you can add to the bottom of your program to save your data to a CSV file:
```movies.to_csv('movies.csv')```


In order for this code to run successfully, you’ll need to create an empty file and name it whatever you want — making sure it has the ```.csv``` extension. I named mine ```movies.csv```, as you can see above, but feel free to name it whatever you like. Just make sure to change the code above to match it.

# ToDo 🗒
* Scrape other data about each movie — e.g., genre, director, starring, or the summary of the movie
* Find a different website to scrape that interests you
* Grab the movie data for all 1,000 movies on that list
