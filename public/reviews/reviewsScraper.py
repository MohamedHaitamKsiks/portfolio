
import json
from random import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

import undetected_chromedriver as uc


url = "https://www.fiverr.com/haitamksiks/do-a-prototype-of-your-game-in-godot"
#start firefox headless browser
firefoxOptions = Options()
#firefoxOptions.headless = True

driver = uc.Chrome()

#load data
driver.get(url)
sleep(20.0 + 3.0 * random())
#
while len(driver.find_elements(By.CLASS_NAME, "see-more-button")):
    moreButton = driver.find_element(By.CLASS_NAME, "see-more-button")
    moreButton.click()
    sleep(1.0 + 2.0 * random())

sleep(10.0 + 3.0 * random())

#get all elemets
reviewElements = driver.find_elements(By.CLASS_NAME, "review-item")

#init reviews list
reviews = []

#go throw all elements 
for reviewElement in reviewElements:
    #review header
    reviewHeader = reviewElement.find_element(By.TAG_NAME, "header")
    reviewDescription = reviewElement.find_element(By.CLASS_NAME, "review-description")
    #init review dict
    review = {}
    #get client info
    client = {}
    client["name"] = reviewHeader.find_element(By.TAG_NAME, "h5").text
    client["country"] = reviewHeader.find_element(By.CLASS_NAME, "country-name").text
    #get profile picture
    reviewImages = reviewElement.find_elements(By.CLASS_NAME, "profile-pict-img")
    if len(reviewImages):
        client["picture"] = reviewImages[0].get_attribute("src")
    else:
        client["picture"] = "/icons/profile.png"
    review["client"] = client
    
    #get stars
    review["stars"] = reviewHeader.find_element(By.CLASS_NAME, "rating-score").text
    #get comment
    review["comment"] = reviewDescription.find_element(By.CLASS_NAME, "text-body-2").text
    #append to list
    reviews.append(review)

#convert to json and write
jsonReviews = json.dumps(reviews, indent=4, sort_keys=True)
with open("public/reviews/fiverrReviews.json", "w") as file:
    file.write(jsonReviews)
