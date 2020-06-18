import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/jobs?q=python"


def get_last_page():
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "s-pagination"})
    pagination = pagination.find_all("a")
    last_page = pagination[-2].text.strip()
    return int(last_page)


def extract_jobs(last_page):
    jobs = []
    # for page in range(1,last_page+1):
    result = requests.get(f"{url}&pg=1")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "-job"})

    for result in results:
        title = result.find("a", {"class": "s-link"})["title"]
        company = result.find(
            "h3", {"class": "fc-black-700"}).find("span").text
        location = result.find("span", {"class": "fc-black-500"}).text
        link = "https://www.stackoverflow.com"+result["data-preview-url"]
        jobs.append({"title": title, "company": company,
                     "location": location, "link": link})

    return jobs


last_page = get_last_page()
extract_jobs(last_page)
