from selenium.webdriver.common.keys import Keys

def Sorter(driver, actions, sort, filter):
    try:
        driver.find_element_by_xpath('//span[@class=" css-n6i4z7"]//a[@class="css-1joxor6"]').click()
    except:
        print("ERROR! NO SEARCH RESULTS!")
    if sort == 2:
        print('Highest Rated Selected.')
        actions.send_keys(Keys.ARROW_DOWN).perform()
        actions.send_keys(Keys.ARROW_DOWN).perform()
        actions.send_keys(Keys.ENTER).perform()
    elif sort == 3:
        print('Most Reviewed Selected.')
        actions.send_keys(Keys.ARROW_DOWN).perform()
        actions.send_keys(Keys.ARROW_DOWN).perform()
        actions.send_keys(Keys.ARROW_DOWN).perform()
        actions.send_keys(Keys.ENTER).perform()
    else:
        print('Recommended (Default) selected.')
        actions.send_keys(Keys.ENTER).perform()

    if filter < 2 or filter > 5:
        filter = 1

    try:
        if filter == 2:
            print("Driving Distance Selected.")
            driver.find_element_by_xpath('//div[2]/label/div/div/input[@class="input__09f24__30UUZ"][@type="radio"]').click()
        elif filter == 3:
            print("Biking Distance Selected.")
            driver.find_element_by_xpath('//div[3]/label/div/div/input[@class="input__09f24__30UUZ"][@type="radio"]').click()
        elif filter == 4:
            print("Walking Distance Selected.")
            driver.find_element_by_xpath('//div[4]/label/div/div/input[@class="input__09f24__30UUZ"][@type="radio"]').click()
        elif filter == 5:
            print("Within 4 Blocks Distance Selected.")
            driver.find_element_by_xpath('//div[5]/label/div/div/input[@class="input__09f24__30UUZ"][@type="radio"]').click()
        else:
            print("Bird's-eye View Distance Selected.")
            driver.find_element_by_xpath('//div[1]/label/div/div/input[@class="input__09f24__30UUZ"][@type="radio"]').click()
    except:
        print("ERROR! DISTANCE FILTER NOT FOUND!")
