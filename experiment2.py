from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pandas as pd


driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.delete_all_cookies()


# url="https://www.tuttitalia.it/abruzzo/58-altino/89-scuole/"
url="https://www.tuttitalia.it/abruzzo/provincia-di-chieti/12-scuole/"


driver.get(url)
sleep(2)


df1=pd.read_csv('Inform_1000.csv')


all_link=[]
links=driver.find_elements_by_xpath('//table[@class="ct"]//td/a')
for link in links:
    href=link.get_attribute("href")
    all_link.append(href)
print(len(all_link))


for url in all_link:
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
                try:
                    sch_name=one_box.find_element_by_xpath('./div[2]/h3').text
                    addr=one_box.find_element_by_xpath('./div[2]').text
                    type=one_box.find_element_by_xpath('./div[3]/i').text
                    code=one_box.find_element_by_xpath('./div[3]/code').text
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
df1.to_csv("Inform_1000.csv")


driver.quit()
