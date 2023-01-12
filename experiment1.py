from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pandas as pd

url="https://www.tuttitalia.it/scuole/"
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.delete_all_cookies()
driver.get(url)
sleep(3)

try:
    cooky=driver.find_element_by_xpath('//a[@id="cookieChoiceDismiss"]')
    cooky.click()
    sleep(1)
except: pass


all_links=[]
all_school_link=[]
all_tag=driver.find_elements_by_xpath('//table[@class="ct"]//td/a')
for one_tag in all_tag:
    href=one_tag.get_attribute("href")
    all_links.append(href)
print(len(all_links),len(all_school_link))

for link in all_links:
    driver.get(link)
    sleep(1)
    try:
        if driver.find_element_by_xpath('//table[@class="ct"]//td/a'):
            all_tag=driver.find_elements_by_xpath('//table[@class="ct"]//td/a')
            for one_tag in all_tag:
                href=one_tag.get_attribute("href")
                all_links.append(href)
            print(len(all_links),".......")

    except Exception as e:
        sch_url = driver.current_url
        all_school_link.append(sch_url)
        print(len(all_school_link),"*******")
        # print(e)

data1={
    "Page Link":all_links
}
df1=pd.DataFrame(data1)
sleep(0.5)

data2={
    "School Link":all_school_link
}
df2=pd.DataFrame(data2)
sleep(0.5)

df1.to_csv('tuttitalia_links.csv',index=False)
df2.to_csv('tuttitalia_School_links.csv',index=False)



driver.quit()

#   //table[@class="ct"]//td/a     school by region
#   //table[@class="ct"]//td/a     schools in the provinces 
#   //table[@class="ct"]//td/a     Schools in the city
#   //div[@class="aj"]            school info outer box   all

#   //div[@class="aj"]//h2                                                      grade in loop
#   //div[@class="aj"]/div[@class="if"]/div[3]                                  class if  1 2 3
#   //div[@class="aj"]/div[@class="if"]/div[2]/h3                               school name
#   //div[@class="aj"]/div[@class="if"]/div[3]/i                                type
#   //div[@class="aj"]/div[@class="if"]/div[3]/code                             code