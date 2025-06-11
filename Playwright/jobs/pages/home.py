from playwright.sync_api import Page 
import time

class Home:

    search_field = "(//input[@class='suggestor-input '])[1]"
    find_jobs_btn = "//div[.='Search']"
    next_page = "//span[.='Next']"
    page_count = "//div[@id='jobs-list-header']/div/span"

    def __init__(self,page:Page):
        self.page = page

    def goto_url(self,url:str) -> None:
        self.page.goto(url)

    def search_job(self,job_title:str) -> None:
        self.page.fill(self.search_field,value=job_title)
        self.page.click(self.find_jobs_btn)

    def get_jobs(self,num_jobs:int):
        jobs = []
        count = 0
        for x in range(num_jobs):
            if x+1 in [20,40,60,80,100]:
                self.page.click(self.next_page)
                count = 0
                while True:
                    page_count_text = self.page.inner_text(self.page_count)[:2]
                    if page_count_text == str(x+2):
                        break
            job = self.page.inner_text(f"(//div[@class='srp-jobtuple-wrapper']/div/div/h2/a)[{count+1}]")
            count += 1
            jobs.append(job)
        return jobs
    

            


        