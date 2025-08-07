import requests
from bs4 import BeautifulSoup

# Step 1: Website URL to scrape
url = 'https://www.bbc.com/news'

# Step 2: Send a request to the website
response = requests.get(url)

# Step 3: Check if the request was successful
if response.status_code == 200:
    # Step 4: Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 5: Find all headlines (h2 and h3 tags)
    headlines = soup.find_all(['h2', 'h3'])

    # Step 6: Open a text file to save the headlines
    file = open("headlines.txt", "w", encoding="utf-8")

    # Step 7: Write each headline to the file
    count = 1
    for tag in headlines:
        headline = tag.get_text().strip()
        if len(headline) > 15:  # Avoid very short or unrelated text
            file.write(str(count) + ". " + headline + "\n")
            count += 1

    file.close()
    print("✅ Headlines saved to headlines.txt")
else:
    print("❌ Failed to retrieve the webpage.")
