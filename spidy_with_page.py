import requests                 # It is a package use to request data from the website.
from bs4 import BeautifulSoup   # It is used to parse HTML and XML documents. We use it to extract data from HTML. you can read more about it in documentation.

# Define a method for crawling through a website with pages.
def spider(maximum_pages):
    page = 1
    while page <= maximum_pages:
        url = 'paste your web address here' + str(page)    # Paste address of the website to be crawled

        source_code = requests.get(url)     # source_code is a variable which will store the scrapped information from the url. requests.get() will collect all the information.

        plain_text = source_code.text       # source_code will be in html formt for our sake we will convert it into txt format.

        soup = BeautifulSoup(plain_text)    # BeautifulSoup constructor takes the document in the form dtring and parses the document and creates a corresponding data structure.

        for link in soup.findall('a', {'': ''}):    # This for loop will run until the crawler collects all the href from the class. The tag for links is " 'a' ". In the other colons you can add more details like class and sub class.

            href = "paste your web address here" + link.get('href')  # Here we connects the web address to href to create a complete link of that object.

            title = link.string   # It collects the title of the href .

            print(href)

            print(title)
        pages += 1          # Incrementing the page number.

# Calling our Spidy :) :) .

spider(1)
