from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

startUrl = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome(
    "C:/Users/Wyatt/Downloads/chromedriver_win32/chromedriver")

browser.get(startUrl)

print("this part is running")

def ScrapeData():
    print("function running")
    headers = ["name", "lightyears", "planet mass",
               "stellar magnitude", "discovery year"]
    planetdata = []
    for i in range(0, 15):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        allULtags = soup.find_all("ul",attrs = {"class","exoplant"})
        for eachUl in allULtags:
            allLItags = eachUl.find_all("li")
            tempList = []
            for index,eachLi in enumerate(allLItags):
                if index == 0:
                    tempList.append(eachLi.find_all("a")[0].contents[0])
                else:
                    tempList.append(eachLi.contents[0])
            planetdata.append(tempList)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
        print(planetdata)
    with open ("exoplanetScraping.csv","w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planetdata)

ScrapeData()



