# Job Scaper

- Scrap programming jobs using python. 
- If users are searching for python, we will get python jobs from weworkremotely. We will export everything in the single excel file. 


## 1. Introduction

- Use BeautifulSoup to scrap data from the website. 

## 2. Installation

*How do you install beautiful soup?*
- https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup

## 3. Initial request

## 4. Beatiful Soup

- In order to navigate a long string, we are going to use the beautiful soup to filter some data. 
- Search for HTML tags.
Steps:
(Check the doc)
1. Import beautifulsoup
2. Get section with class called jobs

## 5. Job Posts
- There are <section class="jobs">
- What do we use when we like to see the code inside the section. 

# 10. Refactoring

- Refactor data into wwr.py
- There is a function called extract jobs.
- extractor.py with comments
```py
from requests import get
from bs4 import BeautifulSoup


def extract_jobs(keywords):
    base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
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

        # put all job classes into jobs var
        jobs = soup.find_all("section", class_="jobs")

        results = []
        # Iterate each job sections and get li
        for job_section in jobs:
            job_posts = job_section.find_all("li")
            # remove the last index which is the class view_all
            job_posts.pop(-1)
            for post in job_posts:

                # We need to grab the a tag and all other data in a span tag.
                anchors = post.find_all("a")
                anchor = anchors[1]
                # Inside each anchor, there are many data.
                link = anchor["href"]
                anchor.find_all("span", class_="company")
                # Positional assignment(?)
                company, kind, region = anchor.find_all("span", class_="company")
                print(company, kind, region)
                # Get title of the job
                # Find a span with the class called "title"
                title = anchor.find("span", class_="title")
                # string will get the string inside the tags.
                # print(company, kind, region, title)
                # print("//////////////////////")
                # Create a dictionary that stores data.
                job_data = {
                    "company": company.string,
                    "region": region.string,
                    "position": title.string,
                }
                # Put data inside the list
                results.append(job_data)

            # result afterwards store the list of job data.
            for result in results:
                print(result)
                print("/////////////")

```

- put all the code inside the WWR.py.

11. Recursive

- Work on Indeed.com
- First start working on main.py

# 12. Fix bugs

- Indeed.com will check whether you are a bot or not. If you are bot, you cannot request a page.
- Selenium is needed to automate your project.
- Selenium will open the browser and request a page. This way, you are not recognized as a bot.
- If you want to install Selenium from a local environment, you have to do the below:
    local에서 하시는 분들은 참고하세요!! (VS code 등..)

    셀레니움 설치
    pip install selenium (혹은 pip3 install selenium)

    드라이버 설치
    크롬 : https://sites.google.com/a/chromium.org/chromedriver/downloads
    파이어폭스 : https://github.com/mozilla/geckodriver/releases
    사파리 : https://webkit.org/blog/6900/webdriver-support-in-safari-10/
    (mac은 brew가 편해요 brew install chromedriver)
