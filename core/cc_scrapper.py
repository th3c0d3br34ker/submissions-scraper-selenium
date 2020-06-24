from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

from core.constants import CODE_CHEF, CODE_CHEF_DIR
from core.extensions import CODECHEF_EXTENSIONS as extensions

from selenium import webdriver
from time import sleep


class CC_Scrapper():
    def __init__(self, username: str, driver: webdriver, password=None):
        self.username = username
        self.password = password
        self.driver = driver
        self.submissions = {}

    def getResponse(self, url: str) -> str:
        self.driver.get(url)
        return self.driver.page_source

    def getCode(self, url: str) -> str:
        self.driver.get(url)
        return self.driver.find_element(By.TAG_NAME, "body").text

    def LOGIN(self) -> bool:
        from json import loads

        self.driver.get(CODE_CHEF+'login')
        # Since Codechef uses its api for the login process -_- have to do a this shitty thing.
        loginform = self.driver.find_element(
            By.CSS_SELECTOR, "#ajax-login-form")
        loginform.get_property("name").send_keys(self.username)
        loginform.get_property("pass").send_keys(self.password)
        loginform.submit()
        sleep(2)
        response = loads(self.driver.find_element(By.TAG_NAME, "body").text)

        if response.get("status") == "success":
            return True
        else:
            print("Login Failed! Check your username and password")
            return False

    def LOGOUT(self) -> None:
        self.driver.get(CODE_CHEF+'logout')
        sleep(2)

    def getSubmissions(self) -> None:
        url = CODE_CHEF+'users/'+self.username
        response = self.getResponse(url)
        parsed_response = BeautifulSoup(response, 'lxml')
        plist = self.getSubmissionsList(parsed_response)

        for p in plist:
            problem = {}
            uid = p.text
            problem['submissions_link'] = p['href']
            problem['submissions'] = []
            response = self.getResponse(
                CODE_CHEF + problem['submissions_link']+'?status=15')
            parsed_response = BeautifulSoup(response, 'lxml')

            # Getting the first correct submission.
            submissionResponse = parsed_response.find('tbody').findAll('tr')[0]
            submission = {}
            tds = submissionResponse.findAll('td')
            submission['id'] = tds[4].text
            submission['lang'] = tds[10].text

            submission['ext'] = '.txt'

            if submission.get('lang') in extensions.keys():
                submission['ext'] = extensions[submission.get('lang')]
            response = self.getCode(
                CODE_CHEF+'viewplaintext/' + submission['id'])

            problem['code'] = response
            self.writeCodeFile(code=problem.get('code'),
                               file_path=uid+submission.get('ext'))

    def getSubmissionsList(self, parsed_response: BeautifulSoup) -> list:

        problemlist = []
        # Get all the submission sections first.

        submission_section = parsed_response.find(
            'section', {'class': 'rating-data-section problems-solved'})

        # Get all the articles.
        #   1. Fully Solved
        #   2. Partially Solved

        fullySolved = submission_section.findAll('article')[0]

        # Get the sub sections next.
        subSections = fullySolved.findAll('p')

        for subSection in subSections:
            # From each subsection get all the problems
            for problems in subSection.findAll('a'):
                problemlist.append(problems)

        return problemlist

    def writeCodeFile(self, code: str, file_path: str) -> None:

        CODE_CHEF_DIR.mkdir(exist_ok=True)

        file_path = CODE_CHEF_DIR / file_path
        print(code, file=open(str(file_path), 'w+'))
