from bs4 import BeautifulSoup
import urllib2
import pandas as pd
import matplotlib.pyplot as plt
# import numpy as np


def main():
    print("**======  Data Extracter  =====**")
    testUrl = "http://www.imdb.com/search/title?at=0&count=500&groups=top_1000&release_date=2000,2017&sort=moviemeter"
    pageSource = urllib2.urlopen(testUrl).read()
    soupPKG = BeautifulSoup(pageSource, 'lxml')
    # print soupPKG
    titles = soupPKG.findAll("div",class_='lister-item mode-advanced')
    mymovieslist = []

    # print titles[0]
    for t in titles:
        mymovies = {}
        mymovies['name'] = t.findAll("a")[1].text
        mymovies['year'] = str(t.find("span", "lister-item-year").text).replace('', '').encode('utf-8').strip()
        mymovies['rating'] = float(str(t.find("strong").text))
        mymovies['runtime'] = str(t.find("span", "runtime").text)
        mymovieslist.append(mymovies)

    # print mymovieslist
    df = pd.DataFrame.from_dict(mymovieslist)
    # df.plot()
    # plt.show()

    # Setting up the nw Index
    # df =df.set_index('rating')

    # df.to_csv('movies2k-2k17.csv')
    #print df

    # Filling data with avg rating
    # df[1].fillna(7, inplace=True)

    # Graph
    # df.columns = ['rating', 'name', 'runtime', 'year']

    df.plot(x='year', y='rating')
    plt.title('Rating Vs Year', color='black')
    plt.show()



    #Movie with High Rating
    print df.sort_values(['rating'],ascending=[False])



if __name__=="__main__":
    main()