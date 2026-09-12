import requests
from bs4 import BeautifulSoup

def decode_secret_message(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    rows = soup.find_all("tr")[1:]
    
    grid = {}
    max_x = 0
    max_y = 0
    
    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 3:
            continue
        
        x = int(cols[0].text.strip())
        char = cols[1].text.strip()
        y = int(cols[2].text.strip())
        
        grid[(x, y)] = char
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    
    # print from max_y to 0 — y increases upward
    for y in range(max_y, -1, -1):
        line = ""
        for x in range(max_x + 1):
            line += grid.get((x, y), " ")
        print(line)



decode_secret_message("https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub")