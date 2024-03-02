import requests,os,csv,re
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
driver = webdriver.Chrome()

proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "https://10.10.1.10:1080",
}

def erase_file_content(file_path):
    with open(file_path, 'w'):
        pass

def extractinfo(inputpath,outputpath):
    dates = []
    likes_counts = []
    image_urls = []
    blog_titles = []
    
    s = ""
    with open(inputpath,"r",encoding="utf-8") as f:
        for x in f:
            s=s+x
    
    soup = BeautifulSoup(s, 'html.parser')

    # Extract information from each article
    for article in soup.find_all('article', class_='blog-item'):
        
        # Extract date
        date_element = article.find('div', class_='bd-item').find('span')
        dates.append(date_element.get_text(strip=True) if date_element else 'N/A')

        # Extract likes count
        likes_element = article.find('a', class_='zilla-likes').find('span')
        if (likes_element):
            temp = likes_element.get_text()
            likes_counts.append(int(re.search(r'\d+', temp).group()))
        else:
            likes_counts.append('N/A')

        # Extract image URL
        try:
            img_element = article.find('div', class_='img').find('a')
            image_url = img_element['data-bg'] if img_element and 'data-bg' in img_element.attrs else 'N/A'
            image_urls.append(image_url)
        except:
            image_urls.append('N/A')

        # Extract blog title
        title_element = article.find('h6').find('a')
        blog_title = title_element.get_text(strip=True).replace('\n', ' ').strip()
        blog_title = ' '.join(blog_title.split())  # Reduce consecutive spaces to a single space
        blog_titles.append(blog_title)

    # Add the data to CSV File
    with open(outputpath, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for data in zip(blog_titles, dates, image_urls, likes_counts):
            writer.writerow(data)

def writeblogcontenttofile(url,inputpath,outputpath):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find elements whose class names point to the blogs
        substring = 'blog-item category-blog'
        matching_elements = soup.find_all(lambda tag: tag.has_attr('class') and " ".join(tag['class']).find(substring) >= 0)
        # print(matching_elements)

        # Print the found elements
        for element in matching_elements:
            with open(inputpath,"a",encoding="utf-8") as f:
                f.write(str(element))
        
        extractinfo(inputpath,outputpath)   
        erase_file_content(inputpath)


# Navigate to the URL
url = 'https://rategain.com/blog/'
driver.get(url)
next_button = driver.find_element(By.CLASS_NAME,'next')
directory_name = os.getcwd()
html_file_name = "temp.html"
cdt = datetime.today()
currentdate = cdt.date()
now = datetime.now()
currenttime = now.strftime("%H_%M_%S")
csv_file_name = f"Data_date_{currentdate}_time_{currenttime}.csv"

header = ['Blog Title', 'Blog Date', 'Blog Image URL', 'Blog Likes Count']

with open(os.path.join(directory_name,csv_file_name), mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    
if (os.path.exists(directory_name)):
    pass
else:
    os.makedirs(directory_name)
        
# Loop through the pages
while (1):
    time.sleep(7)
    current_url = driver.current_url
    print(current_url)
    writeblogcontenttofile(current_url,os.path.join(directory_name,html_file_name),os.path.join(directory_name,csv_file_name))
    try:
        driver.execute_script("""document.getElementsByClassName("next")[0].click()""")
    except:
        print("All blog pages rendered")
        break

# Remove the buffer file and close the browser window
os.remove(os.path.join(directory_name,html_file_name)) 
driver.quit()