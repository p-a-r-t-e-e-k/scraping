from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pandas as pd

# url="https://www.tuttitalia.it/scuole/"
# url="https://www.tuttitalia.it/abruzzo/58-altino/89-scuole/"

# url="https://www.tuttitalia.it/abruzzo/provincia-di-chieti/12-scuole/"
# url="https://www.tuttitalia.it/abruzzo/provincia-di-pescara/95-scuole/"
# url="https://www.tuttitalia.it/abruzzo/provincia-dell-aquila/80-scuole/"
# url='https://www.tuttitalia.it/abruzzo/provincia-di-teramo/45-scuole/'
# url="https://www.tuttitalia.it/basilicata/provincia-di-matera/14-scuole/"
# url='https://www.tuttitalia.it/basilicata/provincia-di-potenza/86-scuole/'
# url="https://www.tuttitalia.it/calabria/provincia-di-catanzaro/68-scuole/"
# url="https://www.tuttitalia.it/calabria/provincia-di-reggio-calabria/88-scuole/"
# url="https://www.tuttitalia.it/calabria/provincia-di-cosenza/79-scuole/"
# url="https://www.tuttitalia.it/calabria/provincia-di-vibo-valentia/25-scuole/"
# url="https://www.tuttitalia.it/calabria/provincia-di-crotone/16-scuole/"
# url="https://www.tuttitalia.it/campania/provincia-di-avellino/49-scuole/"
# url="https://www.tuttitalia.it/campania/provincia-di-napoli/43-scuole/"
url=''


driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.delete_all_cookies()
driver.get(url)
sleep(2)

# data1={
#     "Region":[''],
#     "Provincia":"",
#     "City":"",
#     "Grade":"",
#     "Name Of School":"",
#     "Address":"",
#     "Type":"",
#     "Code":""
# }

# df1=pd.DataFrame(data1)

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





# jhskjh


# a=driver.find_element_by_xpath('//div[@class="aj"]//h2').text
# print(a)
# a=driver.find_element_by_xpath('//div[@class="aj"]/div[@class="if"]/div[2]').text
# print(a)
# a=driver.find_element_by_xpath('//div[@class="aj"]/div[@class="if"]/div[2]/h3 ').text
# print(a)
# a=driver.find_element_by_xpath('//div[@class="aj"]/div[@class="if"]/div[3]/i').text
# print(a)
# a=driver.find_element_by_xpath('//div[@class="aj"]/div[@class="if"]/div[3]/code').text
# print(a)

# get_url = driver.current_url
# print(get_url,"0000000000000")
#   //table[@class="ct"]//td/a     school by region
#   //table[@class="ct"]//td/a     schools in the provinces 
#   //table[@class="ct"]//td/a     Schools in the city
#   //div[@class="aj"]            school info outer box   all

#   //div[@class="aj"]/div[1]/h2                                                     grade in loop
#   //div[@class="aj"]/div[@class="if"]/div[3]                                  class if  1 2 3
#   //div[@class="aj"]/div[@class="if"]/div[2]/h3                               school name
#   //div[@class="aj"]/div[@class="if"]/div[3]/i                                type
#   //div[@class="aj"]/div[@class="if"]/div[3]/code                             code



#   //table[@class="ct"]//td/a     school by region
#   //table[@class="ct"]//td/a     schools in the provinces 
#   //table[@class="ct"]//td/a     Schools in the city
#   //div[@class="aj"]            school info outer box   all

#   //div[@class="aj"]/div[1]/h2                                                grade in loop
#   //div[@class="aj"]/div[@class="if"]/div[3]                                  class if  1 2 3
#   //div[@class="aj"]/div[@class="if"]/div[2]/h3                               school name
#   //div[@class="aj"]/div[@class="if"]/div[3]/i                                type
#   //div[@class="aj"]/div[@class="if"]/div[3]/code                             code
