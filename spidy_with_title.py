import requests                 # It is a package use to request data from the website.
from bs4 import BeautifulSoup   # It is used to parse HTML and XML documents. We use it to extract data from HTML. you can read more about it in documentation.

# Define a method for crawling through a website and collect its title.

def spidy(url):                     # This method we take the url address as parameter.

    get_url = requests.get(url)     # We collect the data from url

    plain_text = get_url.text       # Convert into text format

    soup = BeautifulSoup(plain_text)   # Create a data structutre of parsed document

    title = soup.select('title')        # Get the title

    print(title)                    # Print the title

spidy('paste web adress')
