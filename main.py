from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import Sorter
import Scraper

programloop = True
while programloop:
    dataclear = 0
    print("Program Starting...")
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("--allow-running-insecure-content")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    print("Headless Browser Initialized.")
    print("Loading Website...")
    driver.get("https://www.yelp.com/")
    find = input("FIND (Restaurants, Resorts, Hotel, Lawyers, Accountants, etc.): ")
    near = input("Near (Location): ")
    sort = int(input("Sort List By (Input: 1- Recommended (Default), 2- Highest Rated, 3- Most Reviewed) : "))
    print("Filter Search Results by Distance")
    print("Input 1 for Bird's-eye View Distance (Wide Range) (Default)")
    print("Input 2 for Driving Distance (Within 8 kms)")
    print("Input 3 for Biking Distance (Within 4 kms)")
    print("Input 4 for Walking Distance (Within 2 kms)")
    print("Input 5 for Within 4 Blocks (Fewer Search Results & Sometimes, none)")
    filter = int(input("Input: "))
    print("Searching...")
    search_box = driver.find_element_by_id('find_desc')
    search_box.send_keys(find)
    location_box = driver.find_element_by_id('dropperText_Mast')
    location_box.clear()
    location_box.send_keys(near)
    location_box.send_keys(Keys.ENTER)
    actions = ActionChains(driver)
    wait = WebDriverWait(driver, 10)
    Sorter.Sorter(driver, actions, sort, filter)
    sleep(3)
    start = 3
    end = 13
    try:
        if driver.find_element_by_xpath('//button[@class=" css-y1jj6m"]').is_displayed():
            start = 4
            end = 14
    except:
        pass
    try:
        nxtBtn = driver.find_element_by_xpath('//*[@class="next-link navigation-button__09f24__3F7Pt css-166la90"]')
        while nxtBtn.is_enabled():
            Scraper.Scrappy(driver, find, near, start, end, sort)
            if nxtBtn.is_enabled():
                nxtBtnclk = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="next-link navigation-button__09f24__3F7Pt css-166la90"]'))).click()
                print("Next Page...")
                sleep(3)
        driver.close()
        driver.quit()
    except:
        try:
            try:
                if driver.find_element_by_xpath('//*[contains(text(), "No results")]').is_displayed():
                    print("ERROR! NO SEARCH RESULTS!")
            except:
                Scraper.Scrappy(driver, find, near, start, end, sort)
                dataclear = 1
                Scraper.dataClear(dataclear)
                driver.close()
                driver.quit()
        except:
            driver.close()
            driver.quit()
    print("Scraping Finished...")
    wannaloop = 'yes'
    while wannaloop == 'yes':
        wannaloop = input('Do You want to Scrape again? (Yes or No): ')
        wannaloop.lower()
        if wannaloop == 'yes':
            programloop = True
            wannaloop = 'no'
        elif wannaloop == 'no':
            programloop = False
            wannaloop = 'no'
            print("Saving Scraped Data to a Csv File...")
            sleep(1)
            print("Program Closing...")
            sleep(3)
            break
        else:
            print("Invalid Input! Please Input Again.")
            wannaloop = 'yes'
