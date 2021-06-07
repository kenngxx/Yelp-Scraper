import csv

data = []
data.append(['BUSINESS NAME', 'CATEGORY', 'CUSTOMER/CLIENT AVERAGE STAR RATING', 'NUMBER OF CUSTOMER/CLIENT REVIEWS', 'PRICE RANGE','BUSINESS PHONE NUMBER', 'BUSINESS ADDRESS'])
link = '/html/body/yelp-react-root/div/div/div/div/div/div/div/ul/'

def Scrappy(driver, find, near, start, end, sort):
    if sort == 2:
        fn = 'Highest Rated '
    elif sort == 3:
        fn = 'Most Reviewed '
    else:
        fn = 'Recommended '

    for index in range(start, end):
        try:
            bsName = driver.find_element_by_xpath(link + 'li[{}]/div/div/div/div/div/div/div/div/div[1]/div/div/h4/span/a'.format(index)).get_attribute('textContent')
            print(bsName)
            try:
                cat = driver.find_element_by_xpath(link + 'li[{}]/div/div/div/div/div/div/div[1]/div/div/div/div/div/p'.format(index)).get_attribute('textContent')
                newcat = cat.replace('₱', '')
                print(newcat)
            except:
                newcat = 'CATEGORY UNSPECIFIED'
                print(newcat)

            try:
                ratings = driver.find_element_by_xpath(link + 'li[{}]/div/div/div/div/div/div/div/div/div/div/div/div/span/div'.format(index)).get_attribute('aria-label')
                newrating = ratings.replace('star rating', '')
                print(newrating)

            except:
                newrating = '0'
                print(newrating)

            try:
                reviews = driver.find_element_by_xpath(link + 'li[{}]/div/div/div/div/div/div/div/div/div/div/div/div[2]/span'.format(index)).get_attribute('textContent')
                print(reviews)
            except:
                reviews = '0'
                print(reviews)
            try:
                price = driver.find_element_by_xpath(link + 'li[{}]/div/div/div/div/div/div/div/div/div/div/div/div/p/span[1]/span'.format(index)).get_attribute('textContent')
                if '₱' in price:
                    if price == '₱':
                        newprice = price + ' - Inexpensive'
                    elif price == '₱₱':
                        newprice = price + ' - Moderately Expensive'
                    elif price == '₱₱₱':
                        newprice = price + ' - Expensive'
                    else:
                        newprice = price + ' - Very Expensive'
                else:
                    newprice = 'PRICE RANGE UNSPECIFIED'

            except:
                newprice = 'PRICE RANGE UNSPECIFIED'
            try:
                phone = driver.find_element_by_xpath(link + 'li[{}]/div/div/div/div/div/div/div/div/div/div/div/p'.format(index)).get_attribute('textContent')
                pbool = phone.isalpha()
                if not pbool:
                    print(phone)
                else:
                    phone = 'NO CONTACT NUMBER PROVIDED'
                    print(phone)

            except:
                phone = 'NO CONTACT NUMBER PROVIDED'
                print(phone)

            try:
                address = driver.find_element_by_xpath(link +'li[{}]/div/div/div/div/div/div/div/div/address'.format(index)).get_attribute('textContent')
                print(address)
            except:
                address = 'NO ADDRESS PROVIDED'
                print(address)

        except:
            print('~NO MORE DATA TO SCRAPE~')
            break
            data.pop()

        data.append([bsName, newcat, newrating, reviews, newprice, phone, address])
    with open(fn + find + ' near ' + near + '.csv', 'w', encoding='utf-8') as yelp:
        wr = csv.writer(yelp, lineterminator='\n')
        wr.writerows(data)

def dataClear(dataclear):
    if dataclear == 1:
        data.clear()
    data.append(['BUSINESS NAME', 'CATEGORY', 'CUSTOMER/CLIENT AVERAGE STAR RATING', 'NUMBER OF CUSTOMER/CLIENT REVIEWS','PRICE RANGE', 'BUSINESS PHONE NUMBER', 'BUSINESS ADDRESS'])
