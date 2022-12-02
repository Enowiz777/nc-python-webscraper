from requests import get

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
    print(response.text)
    print("Success!")
