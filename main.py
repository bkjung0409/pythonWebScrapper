from indeed import extract_indeed_pages, extract_indeed_jobs
from save import save_to_file
from stackoverflow import get_last_page, extract_jobs

last_indeed_page = extract_indeed_pages()
last_stackoverflow_page = get_last_page()

indeed_jobs = extract_indeed_jobs(last_indeed_page)
stackoverflow_jobs = extract_jobs(last_stackoverflow_page)
jobs = indeed_jobs + stackoverflow_jobs
save_to_file(jobs)
