import requests
from bs4 import BeautifulSoup

limit = "50"
url = f"https://www.indeed.com/jobs?q=python&limit={limit}"


def extract_job(html):
    title = html.find("h2", {
        "class": "title"
    }).find("a", {"class": "jobtitle"})["title"]
    company = html.find("div", {
        "class": "sjcl"
    }).find("span", {
        "class": "company"
    }).text.strip()
    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    return {
        "title": title,
        "company": company,
        "location": location,
        "link": f"https://www.indeed.com//viewjob?jk={job_id}"
    }


def extract_indeed_pages():
    result = requests.get(url)

    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all("a")
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page


def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{url}&start={page*limit}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})

        for result in results:
            job = extract_job(result)
            jobs.append(job)

    return jobs
