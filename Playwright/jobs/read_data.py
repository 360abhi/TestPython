from configparser import ConfigParser

con = ConfigParser()
con.read('Playwright/jobs/app.properties')

class Read:

    URL = con.get('URL','app_url')
    JOB_TITLE = con.get('JOB','python_job')