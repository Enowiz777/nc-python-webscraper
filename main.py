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


def say_hellp(name, age):
    print(f"Hello {name} you are {age} years old")


# Find sections with class jobs.
