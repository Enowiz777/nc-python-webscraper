from requests import get
from bs4 import BeautifulSoup


def extract_wwr_jobs(keywords):
    base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
    response = get(f"{base_url}{keywords}")

    # Create an error handling flow
    if response.status_code != 200:
        print("Can't request website")
    else:
        soup = BeautifulSoup(response.text, "html.parser")

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
                link = anchor["href"]
                anchor.find_all("span", class_="company")

                company, kind, region = anchor.find_all("span", class_="company")
                title = anchor.find("span", class_="title")
                job_data = {
                    "company": company.string,
                    "region": region.string,
                    "position": title.string,
                }
                # Put data inside the list
                results.append(job_data)

            # result afterwards store the list of job data.
            return results
