from bs4 import BeautifulSoup
import requests

url = "https://..."
img = requests.get(url).content

saveFile = "./images/aaa.png"
with open(saveFile, mode="wb") as file:
    file.write(img)

print("OK!")
