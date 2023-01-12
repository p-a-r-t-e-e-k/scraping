from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pandas as pd

# creating driver with chrome, maximize window, clear cooky
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.delete_all_cookies()

# declaring dictionary for first dataframe-> df1
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

# getting links from tuttitalia_links.csv from getting_links.py
df = pd.read_csv('getting_links.py')
all_links=df['Page Link']
print(len(all_links),"-------------total links in csv/list")

# itrate links
count=1
for url in all_links:
    print(url,"---------------------url-> "+str(count)+"/"+str(len(all_links)))
    count+=1
    driver.get(url)
    sleep(2)

    # try to accept cooky
    try:
        cooky=driver.find_element(By.XPATH,'//a[@id="cookieChoiceDismiss"]')
        cooky.click()
        sleep(1)
    except Exception as e: pass

    # getting region, provincia, city,
    region=[]
    rgn=driver.find_element(By.XPATH,'//div[@id="ic"]/a[3]').text
    region.append(rgn)
    provincia=driver.find_element(By.XPATH,'//div[@id="ic"]/a[4]').text
    city=driver.find_element(By.XPATH,'//div[@id="ic"]/a[5]').text

    # getting grade, school name, address, type, school code
    outer_box=driver.find_elements(By.XPATH,'//div[@class="aj"]')
    for one_outer in outer_box:
        grade=one_outer.find_element(By.XPATH,'./div[1]/h2').text
        try:
            box_in_otr=one_outer.find_elements(By.XPATH,'./div[@class="if"]')
            for one_box in box_in_otr:
                action=ActionChains(driver)
                action.move_to_element(one_box)
                sleep(0.5)
                try:
                    sch_name=one_box.find_element(By.XPATH,'./div[2]/h3').text
                    addr=one_box.find_element(By.XPATH,'./div[2]').text
                    type=one_box.find_element(By.XPATH,'./div[3]/i').text
                    code=one_box.find_element(By.XPATH,'./div[3]/code').text
                    sleep(0.5)
                except Exception as e:
                    print(e)

                # making 2nd dataframe(df2) and append in first dataframe(df1)
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

# making final csv
df1.to_csv("Inform.csv")

# quit driver and close/stop all process
driver.quit()
