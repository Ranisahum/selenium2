#!/usr/bin/env python
# coding: utf-8

# # 1. Write a python program which searches all the product under a particular product from www.amazon.in. The 
# product to be searched will be taken as input from user. For e.g. If user input is ‘guitar’. Then search for 
# guitars

# In[47]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import requests
import time
from selenium.common.exceptions import NoSuchElementException


# In[57]:


product=input("Enter product name : ")


# In[58]:


driver=webdriver.Chrome(r'chromedriver.exe')


# In[59]:


driver.get("https://www.amazon.in")


# In[60]:


try:
    search_product=driver.find_element(By.ID,"twotabsearchtextbox")
    search_product.send_keys(product)
except NoSuchElementException as e:
        print("Exception raised :",e)
        element=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
        element.text


# In[62]:


search=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input")
search.click()


# In[64]:


driver.close()


# #  In the above question, now scrape the following details of each product listed in first 3 pages of your search 
# results and save it in a data frame and csv. In case if any product has less than 3 pages in search results then 
# scrape all the products available under that product name. Details to be scraped are: "Brand 
# Name", "Name of the Product", "Price", "Return/Exchange", "Expected Delivery", "Availability" and 
# “Product URL”. In case, if any of the details are missing for any of the product then replace it by “-“. 

# In[37]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import requests
import time
from selenium.common.exceptions import NoSuchElementException


# In[38]:


product=input("Enter product name : ")


# In[46]:


driver=webdriver.Chrome(r'chromedriver.exe')


# In[47]:


driver.get("https://www.amazon.in")


# In[48]:


search_product=driver.find_element(By.ID,"twotabsearchtextbox")
search_product.send_keys(product)
search=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input")
search.click()


# In[49]:


brand_name=[]
product_name=[]
price=[]
return_exchange=[]
expected_delivery=[]
availability=[]
product_url=[]


# In[50]:


start=0
end=3
for page in range(start,end):
    url=driver.find_elements(By.XPATH,'//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
    for i in url:
        product_url.append(i.get_attribute('href'))
    next_button=driver.find_element(By.XPATH,'//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]')
    next_button.click()
    time.sleep(5)


# In[51]:


len(product_url)


# In[54]:


for url in product_url[0:10]:
    driver.get(url)
    time.sleep(2)


# In[ ]:


driver.close()


# # 3.Write a python program to access the search bar and search button on images.google.com and scrape 10 
# images each for keywords ‘fruits’, ‘cars’ and ‘Machine Learning’, ‘Guitar’, ‘Cakes’. 

# In[8]:


import selenium
import time
import requests
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# In[9]:


driver=webdriver.Chrome(r'chromedriver.exe')


# In[10]:


driver.get("https://www.google.com/")


# In[11]:


product=driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
product.send_keys("fruits")


# In[12]:


search=driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[1]/div/span')
search.click()


# In[16]:


image=driver.find_element(By.XPATH,'/html/body/div[7]/div/div[4]/div/div[1]/div/div[1]/div/div[2]/a')
image.click()


# In[17]:


for _ in range(20):
    driver.execute_script("window.scrollBy(0,1000)")


# In[18]:


img_url=[]
img_data=[]


# In[19]:


url=driver.find_elements(By.XPATH,'//img[@class="rg_i Q4LuWd"]')


# In[20]:


for i in url:
    source=i.get_attribute('src')
    if source is not None:
        if(source[0:4]=='http'):
            img_url.append(source)
    


# In[21]:


for i in range(len(img_url)):
    if i >10:
        BreakBy.XPATH,
    print('Downloading {0} of {1} images' .format(i,10))
    response=requests.get(img_url[i])
    file=open(r"C:\Users\pihur\OneDrive\Desktop\fliprobo"+str(i)+".jpg","wb")
    file.write(response.content)


# In[22]:


driver.close()


# # 4.rite a python program to search for a smartphone(e.g.: Oneplus Nord, pixel 4A, etc.) on www.flipkart.com
# and scrape following details for all the search results displayed on 1st page. Details to be scraped: “Brand 
# Name”, “Smartphone name”, “Colour”, “RAM”, “Storage(ROM)”, “Primary Camera”, 
# “Secondary Camera”, “Display Size”, “Battery Capacity”, “Price”, “Product URL”. Incase if any of the 
# details is missing then replace it by “- “. Save your results in a dataframe and CSV. 

# In[96]:


import selenium
import warnings
warnings.filterwarnings('ignore')
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


# In[128]:


driver=webdriver.Chrome(r'chromedriver.exe')


# In[129]:


driver.get("https://www.flipkart.com")


# In[130]:


product=driver.find_element(By.CLASS_NAME,"_3704LK")
product.send_keys("Smartphones")


# In[131]:


search=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
search.click()


# In[132]:


link=[]


# In[133]:


url=driver.find_elements(By.XPATH,'//a[@class="_1fQZEK"]')
for i in url:
    link.append(i.get_attribute("href"))


# In[134]:


len(link)


# In[135]:


for r in link:
    driver.get(r)
    time.sleep(2)


# In[136]:


brand_name=[]
smartphone_name=[]
colour=[]
ram=[]
storage=[]
primary_camera=[]
secondary_camera=[]
display_size=[]
battery_capacity=[]
pricce=[]
product_url=[]


# In[137]:


brand=driver.find_elements(By.XPATH,'//span[@class="B_NuCI"]')
for i in brand:
    brand_name.append(i.text.split(" ")[0])


# In[140]:


name=driver.find_elements(By.XPATH,'//span[@class="B_NuCI"]')
for i in name:
    smartphone_name.append(i.text)


# In[142]:


Colour=driver.find_elements(By.XPATH,'//div[@class="_2C41yO"]')
for i in Colour:
    colour.append(i.text)


# In[143]:


Ram=driver.find_elements(By.XPATH,'//a[@class="_1fGeJ5 PP89tw"]')
for i in Ram:
    ram.append(i.text)


# In[145]:


Storage=driver.find_elements(By.XPATH,'//a[@class="_1fGeJ5 PP89tw"]')
for i in Storage:
    storage.append(i.text)


# In[155]:


Primary_camera=driver.find_elements(By.XPATH,'//li[@class="_21Ahn-"]')
for i in Primary_camera:
    primary_camera.append(i.text.split("|")[0])


# In[157]:


Secondary_camera=driver.find_elements(By.XPATH,'//li[@class="_21Ahn-"]')
for i in Secondary_camera:
    secondary_camera.append(i.text)


# In[160]:


Price=driver.find_elements(By.XPATH,'//dic[@class="_30jeq3 _16Jk6d"]')
for i in Price:
    price.append(i.text)


# In[166]:


Btr=driver.find_elements(By.XPATH,'//li[@class="_21Ahn-"]')
for i in Btr:
    battery_capacity.append(i.text)


# # 5.Write a program to scrap geospatial coordinates (latitude, longitude) of a city searched on google maps. 

# In[1]:


import selenium
import time
import requests
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# In[2]:


driver=webdriver.Chrome(r'chromedriver.exe')


# In[3]:


driver.get('https://www.google.co.in/maps/')


# In[4]:


search=driver.find_element(By.CLASS_NAME,'tactile-searchbox-input')
search.send_keys("Bhubaneswar")


# In[5]:


btn=driver.find_element(By.ID,'searchbox-searchbutton')
btn.click()


# In[6]:


try:

    url_string = driver.current_url

    print("URL Extracted: ", url_string)

    lat_lng = re.findall(r'@(.*)data',url_string)

    if len(lat_lng):

        lat_lng_list = lat_lng[0].split(",")

        if len(lat_lng_list)>=2:

            lat = lat_lng_list[0]

            lng = lat_lng_list[1]

        print("Latitude = {}, Longitude = {}".format(lat, lng))



except Exception as e:

        print("Error: ", str(e))


# In[7]:


driver.close()


# # . Write a program to scrap all the available details of best gaming laptops from digit.in.

# In[212]:


import selenium
import time
import requests
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# In[213]:


driver=webdriver.Chrome(r'chromedriver.exe')


# In[214]:


driver.get("https://www.digit.in/")


# In[225]:


top_10=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[4]/ul/li[4]/a')
top_10.click()


# In[226]:


gaming_laptop=driver.find_element(By.XPATH,'/html/body/div[7]/div/div/div[3]/div[2]/ul/li[19]/a').click()


# In[227]:


url=[]


# In[228]:


Url=driver.find_elements(By.XPATH,'//DIV[@class="left_side"]')
for i in Url:
    url.append(i.get_attribute("href"))


# In[219]:


name=[]


# In[220]:


laptop_name=driver.find_elements(By.XPATH,'//DIV[@class="left_side"]')
for i in laptop_name:
    name.append(i.text)


# In[221]:


display=[]


# In[222]:


Dply=driver.find_elements(By.XPATH,'//div[@class="value"]')
for i in Dply:
    display.append(i.text)


# In[ ]:


driver.close()


# # .7. Write a python program to scrape the details for all billionaires from www.forbes.com. Details to be scrapped: 
# “Rank”, “Name”, “Net worth”, “Age”, “Citizenship”, “Source”, “Industry”. 

# In[23]:


import selenium
import time
import requests
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings("ignore")
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# In[33]:


driver=webdriver.Chrome(r'chromerdrriver.exe')


# In[34]:


driver.get("https://www.forbes.com/")


# In[36]:


search=driver.find_element(By.CLASS_NAME,'_69hVhdY4')
search.click()


# In[39]:


click_button=driver.find_element(By.CLASS_NAME,'mpBfVZz3')
click_button.click()


# In[42]:


billonaries=driver.find_element(By.XPATH,'/html/body/div[1]/header/nav/div[1]/div/div/div[2]/ul/li[1]/div[2]/div[3]/ul/li[1]/a').click()


# In[43]:


RANK=[]
NAME=[]
NET_WORTH=[]
AGE=[]
Citizenship=[]
Source=[]
industry=[]


# In[44]:


rank=driver.find_elements(By.XPATH,'//DIV[@class="rank"]')
for i in rank:
    RANK.append(i.text)
name=driver.find_elements(By.XPATH,'//DIV[@class="personName"]')
for i in name:
    NAME.append(i.text)
new_worth=driver.find_elements(By.XPATH,'//DIV[@class="netWorth"]')
for i in new_worth:
    NET_WORTH.append(i.text)
age=driver.find_elements(By.XPATH,'//DIV[@class="age"]')
for i in age:
    AGE.append(i.text)
citizenship=driver.find_elements(By.XPATH,'//DIV[@class="countryOfCitizenship"]')
for i in citizenship:
    Citizenship.append(i.text)

source=driver.find_elements(By.XPATH,'//DIV[@class="source-column"]')
for i in source:
    Source.append(i.text)
Industry=driver.find_elements(By.XPATH,'//DIV[@class="category"]')
for i in Industry:
    industry.append(i.text)


# In[45]:


df=pd.DataFrame({"Rank":RANK,"Name":NAME,'NET_WORTH':NET_WORTH,"AGE":AGE,"Citizenship":Citizenship,"Source":Source,"industry":industry})


# In[46]:


df


# In[47]:


driver.close()


# # 8. Write a program to extract at least 500 Comments, Comment upvote and time when comment was posted 
# from any YouTube Video. 

# In[125]:


import selenium
import time
import requests
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings("ignore")
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# In[126]:


driver=webdriver.Chrome(r'chromerdrriver.exe')


# In[127]:


driver.get("https://www.youtube.com/")


# In[128]:


channel1=driver.find_element(By.CLASS_NAME,'style-scope ytd-rich-grid-media')
channel1.click()


# In[129]:


for _ in range(20):
    driver.execute_script("window.scrollBy(0,1000)")


# In[130]:


comment=[]
Comment_upvote=[]
time=[]


# In[131]:


Comment=driver.find_elements(By.XPATH,'//span[@class="style-scope yt-formatted-string"]')
for i in Comment[0:20]:
    comment.append(i.text)


# In[132]:


comment_upvote=driver.find_elements(By.XPATH,'//span[@class=" style-scope ytd-comment-renderer"]')
for i in comment_upvote[0:20]:
    Comment_upvote.append(i.text)


# In[133]:


Time=driver.find_elements(By.XPATH,'//a[@class="yt-simple-endpoint style-scope yt-formatted-string"]')
for i in Time[0:20]:
    time.append(i.text)


# In[136]:


driver.close()


# # 9. Write a python program to scrape a data for all available Hostels from https://www.hostelworld.com/ in 
# “London” location. You have to scrape hostel name, distance from city centre, ratings, total reviews, overall 
# reviews, privates from price, dorms from price, facilities and property description

# In[157]:


import selenium
import time
import requests
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings("ignore")
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# In[176]:


driver=webdriver.Chrome(r'chromerdrriver.exe')


# In[177]:


driver.get("https://www.hostelworld.com/")


# In[179]:


hostel=driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div[2]/div/div/div[4]/div/div[2]/div/div[1]/div/div/div/input")
hostel.send_keys("London")


# In[180]:


search=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div[2]/div/div/div[4]/div/div[2]/div/div[1]/div/div/ul/li[2]/div')
search.click()


# In[181]:


go=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div[2]/div/div/div[4]/div/div[2]/div/div[5]/button')
go.click()


# In[182]:


name=[]
distance_from_city=[]
ratings=[]
total_review=[]
over_all_review=[]
privates_from_price=[]
dorms_from_price=[]
Facilities=[]
property_description=[]


# In[183]:


Name=driver.find_elements(By.XPATH,'//div[@class="property-name"]')
for i in Name:
    name.append(i.text)


# In[184]:


try:
    distance=driver.find_elements(By.XPATH,'//span[@class="distance-description"]')
    for i in distance:
        distance_from_city.append(i.text)
except NoSuchElementException:
    print("-")   


# In[185]:


Rating=driver.find_elements(By.XPATH,'//div[@class="score"]')
for i in Rating:
    ratings.append(i.text)


# In[186]:


try:
    Total_review=driver.find_elements(By.XPATH,'//div[@class="review"]')
    for i in Total_review:
        total_review.append(i.text)
except NoSuchElementException:
    print("-")


# In[187]:


try:
    Over_all_review=driver.find_elements(By.XPATH,'//div[@class="keyword"]')
    for i in Over_all_review:
        over_all_review.append(i.text)
except NoSuchElementException:
    print("-")


# In[188]:


try:
    Privates_from_price=driver.find_elements(By.XPATH,'//div[@class="accommodation-price"]')
    for i in Privates_from_price[0:31]:
        privates_from_price.append(i.text)
except NoSuchElementException:
    print("-")


# In[189]:


try:
    Dorms_from_price=driver.find_elements(By.XPATH,'//div[@class="accommodation-price"]')
    for i in Dorms_from_price[0:31]:
        dorms_from_price.append(i.text)
except NoSuchElementException:
    print("-")


# In[193]:


try:
    facilities=driver.find_elements(By.XPATH,'//div[@class="has-wifi"]')
    for i in facilities[0:31]:
        Facilities.append(i.text)
except NoSuchElementException:
    print("-")


# In[194]:


try:
    Property_description=driver.find_elements(By.XPATH,'//div[@class="rating-factors prop-card-tablet rating-factors small"]')
    for i in Property_description[0:31]:
        property_description.append(i.text)
except NoSuchElementException:
    print("-")

