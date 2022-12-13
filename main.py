from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
search_term = "python"

response = get(f"{base_url}{search_term}")
# print(response)
# You get response: <Response [200]>
# print(response.text)
# response.text will get all htmls that consist a website.

# Create an error handling flow
if response.status_code != 200:
    print("Can't request website")
else:
    # Handle the returned data w/ a beautiful soup.
    soup = BeautifulSoup(response.text, "html.parser")
    # Find title tags: success!
    # print(soup.find_all("title"))
    # Find sections with a class jobs: success!
    print(soup.find_all("section", class_="jobs"))


def say_hellp(name, age):
    print(f"Hello {name} you are {age} years old")


# Find sections with class jobs.
