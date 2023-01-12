from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

# creating driver with chrome, maximize window, clear cooky
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.delete_all_cookies()

# opening main page in chrome using driver.get()
url="https://www.tuttitalia.it/scuole/"
driver.get(url)
sleep(3)

# try to accept cooky
try:
    cooky=driver.find_element(By.XPATH,'//a[@id="cookieChoiceDismiss"]')
    cooky.click()
    sleep(1)
except: pass

# declearation of lists
all_links,all_school_link=[],[]

# getting the all ~20 links of region and adding in list (all_links)
all_tag=driver.find_elements(By.XPATH,'//table[@class="ct"]//td/a')
for one_tag in all_tag:
    href=one_tag.get_attribute("href")
    all_links.append(href)

# length of outer and inner links before collection
print(len(all_links),len(all_school_link),"------------------length before")

# opening links in list (all_lisnks)
# getting sublinks and adding in list (all_school_link)
for link in all_links:
    driver.get(link)
    sleep(1)
    try:
        if driver.find_element(By.XPATH,'//table[@class="ct"]//td/a'):
            all_tag=driver.find_elements(By.XPATH,'//table[@class="ct"]//td/a')
            for one_tag in all_tag:
                href=one_tag.get_attribute("href")
                all_school_link.append(href)
            print(len(all_school_link),"----------------no. of href")

    except Exception as e:
        print(e,"---------------------in except")

# length of outer and inner links after collection
print(len(all_links),len(all_school_link),"------------------length-after")

# creating dataframe of list (all_school_link)
data1={
    "Page Link":all_school_link
}
df1=pd.DataFrame(data1)
sleep(0.5)


# making csv
df1.to_csv('tuttitalia_links.csv',index=False)

# quit driver and close/stop all process
driver.quit()
