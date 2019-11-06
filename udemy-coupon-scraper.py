# Learn Viral Udemy Coupon Scraper
#Description: This code scrapes the title and coupon of all items
#from learn viral on the number of pages specified by user.
#outputs the scraped items into csv file

#Version 0: By MikeePy



from selenium import webdriver
from bs4 import BeautifulSoup
import time

links = []
title = []
numpages = input("Enter Number of Pages you want to Scrape:   ")

driver = webdriver.Chrome()

pagemax = int(numpages)

page = 0

#start of looping through the pages
while page < pagemax:
    urllink = "https://udemycoupon.learnviral.com/coupon-category/free100-discount/page/" + str(page+1) + "/"
    driver.get(urllink)
    link_list_one_page = []
    soup = BeautifulSoup(driver.page_source, 'lxml')
    divs = soup.find_all('div', class_= 'link-holder')
    divs2 = soup.find_all('h3', class_= 'entry-title')
    #create the lists from beautifulsoup scrape of title and link
    for div in divs:
        links.append(div.find('a')['href'])

    for div in divs2:
        title.append(div.find('a')['title'])

    #wait for a period so not to flood site with request
    time.sleep(3)
    page = page+1
    
driver.quit()

#two lists are complete, checks length of both to see if it matches.
#cleans up strings of each list and output to csv
if len(links) == len(title):
    with open("udemyscrape.csv","w") as f:        
        final_list = zip(title,links)
        for t,l in final_list:
            t = t.replace('View the "','')
            t = t.replace('" coupon page','')
            t = t.strip()
            t = t.replace(',', ' ')
            listt = l.replace('\\','\\')
            f.write(f"{t},{listt},'\n'")
else:
    print("Something is wrong")
print("Scrape complete")