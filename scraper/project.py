from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
#check START_URL
START_URL = "https://en.wikipedia.org/wiki/Lists_of_stars"
browser = webdriver.Chrome("/Users/apoorvelous  /Downloads/chromedriver")
browser.get(START_URL)
time.sleep(10)
def scrape():
    headers = ["name", "Distance", "Mass", "Radius"]
    planet_data = []
    for i in range(0, 428):
        #(what are you reading, how are you reading it; as a html file)
        soup = BeautifulSoup(browser.page_source, "html.parser")
        #ul tags are main and inside those ar li tags
        #attrs = attributes is class and exoplanet
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            #planet name = ul tage
            #discovery date = li tag
            li_tags = ul_tag.find_all("li")
            # temp_list = to store one data information at a time
            temp_list = []
            #enumerate= returns both index and data
            for index, li_tag in enumerate(li_tags):
                #if it is a main tag
                if index == 0:
                    #all the content in the first name will be appended
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                        #when an error occurs
                    except:
                        temp_list.append("")
                        #keep appending values
            planet_data.append(temp_list)
            #path for a forward button
            #.click - when you click the button
            #span 1 - backward arrow; span 2 - forward button } based on web page
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
        #where you are going to read and storing as f
    with open("planet_scraper.csv", "w") as f:
        #writing the file in f - (the file stored)
        csvwriter = csv.writer(f)
        #first thing you are writing is the header, then nect row is planet_data
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
        #GENERAL - reading and storing inside as a csv file
scrape()
