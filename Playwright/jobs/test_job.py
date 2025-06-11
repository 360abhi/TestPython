import sys
from pathlib import Path
root_path = Path(__file__).parent.parent.parent
sys.path.append(str(root_path))

from Playwright.jobs.pages.home import Home
from playwright.sync_api import sync_playwright
from Playwright.jobs.read_data import Read

def getJobs():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        home = Home(page)
        home.goto_url(Read.URL)
        home.search_job(Read.JOB_TITLE)
        jobs = home.get_jobs(num_jobs=45)
        for i in range(len(jobs)):
            print(f"{i+1} : {jobs[i]}")
        browser.close()

getJobs()