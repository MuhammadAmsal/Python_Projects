import requests
from bs4 import BeautifulSoup as bs

github_user=input("Input github user: ")
url=f'https://github.com/{github_user}'

r=requests.get(url)
soup= bs(r.content,'html.parser')
profile_img=soup.find('img',{"class":"avatar"})['src']
profile_title=soup.find('div',{"class":"p-note"})
inner_div = profile_title.find('div')
print(profile_img)
print(inner_div.text)