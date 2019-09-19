import requests
from bs4 import BeautifulSoup 

page_url = 'https://www.livejournal.com/media'
 
lj_request = requests.get(page_url) 

lj_content = lj_request.text 

if lj_request.status_code == 200:
    
    print('Yay! We performed a successful request!')
else:
    print('Oops...')  
 
parsed_page = BeautifulSoup(lj_content)

print(type(parsed_page))

print(parsed_page.title)