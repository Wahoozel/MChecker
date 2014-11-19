import urllib.request, urllib.error
from bs4 import *

url = "https://minecraft.net/haspaid.jsp?user="
print("=== Minecraft Premium Account Checker ===")


def check(username):
    try:
        html = urllib.request.urlopen(url + username).read()
        soup = BeautifulSoup(html)
        text = soup.findAll(text=True)

        print("Is premium: " + text[0])
        return
    except TimeoutError or urllib.error.URLError or urllib.error.HTTPError:
        print("Could not contact Mojang's servers.")
        return
    except Exception as e:
        print(str(e))
        return

running = True
while running:
    check(input("Enter username: "))