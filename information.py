from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pandas as pd

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.delete_all_cookies()


data1={
    "Region":[''],
    "Provincia":"",
    "City":"",
    "Grade":"",
    "Name Of School":"",
    "Address":"",
    "Type":"",
    "Code":""
}

df1=pd.DataFrame(data1)

# all_links=[]df=pd.read_csv('tuttitalia_School_links.csv')
# all_links=df['School Link']
# print(len(all_links),"*****")
all_links=['https://www.tuttitalia.it/abruzzo/58-altino/89-scuole/','https://www.tuttitalia.it/abruzzo/61-frisa/76-scuole/','https://www.tuttitalia.it/abruzzo/41-rapino/66-scuole/']
for url in all_links:
    driver.get(url)
    sleep(2)
    try:
        cooky=driver.find_element_by_xpath('//a[@id="cookieChoiceDismiss"]')
        cooky.click()
        sleep(1)
    except Exception as e: pass
    region=[]
    rgn=driver.find_element_by_xpath('//div[@id="ic"]/a[3]').text
    region.append(rgn)
    provincia=driver.find_element_by_xpath('//div[@id="ic"]/a[4]').text
    city=driver.find_element_by_xpath('//div[@id="ic"]/a[5]').text
    outer_box=driver.find_elements_by_xpath('//div[@class="aj"]')
    for one_outer in outer_box:
        grade=one_outer.find_element_by_xpath('./div[1]/h2').text
        try:
            box_in_otr=one_outer.find_elements_by_xpath('./div[@class="if"]')
            for one_box in box_in_otr:
                action=ActionChains(driver)
                action.move_to_element(one_box)
                sleep(0.5)
                try:
                    sch_name=one_box.find_element_by_xpath('./div[2]/h3').text
                    addr=one_box.find_element_by_xpath('./div[2]').text
                    type=one_box.find_element_by_xpath('./div[3]/i').text
                    code=one_box.find_element_by_xpath('./div[3]/code').text
                    sleep(0.5)
                except Exception as e:
                    print(e)
                try:
                    data2={
                            "Region":region,
                            "Provincia":provincia,
                            "City":city,
                            "Grade":grade,
                            "Name Of School":sch_name,
                            "Address":addr,
                            "Type":type,
                            "Code":code
                        }
                    df2=pd.DataFrame(data2)
                    df1=df1.append(df2, ignore_index = True)
                except Exception as e:
                        print(e)
        except Exception as e:
            print(e)
df1.to_csv("Inform.csv")


