from json import loads
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from core.constants import HACKERRANK, HACKERRANK_BASE, HACKERRANK_DIR, SKIP_DOWNLOADED, WAIT_SECONDS, MAX_RETRIES
from core.extensions import HACKERRANK_EXTENSIONS


class HR_Scrapper():

    def __init__(self, username: str, password: str, driver: webdriver):
        """
        Hackerrank Scrapper Class

        This class handles all the methods for scraping the Hackerrank website.
        """
        self.username = username
        self.password = password
        self.driver = driver

    def LOGIN(self):

        self.driver.get(HACKERRANK_BASE+"login")

        # Log in...
        self.driver.find_element(By.NAME, "username").send_keys(self.username)
        self.driver.find_element(By.NAME, "password").send_keys(self.password)
        self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)

        # Wait for a second for the driver to send submit
        sleep(1)
        self.driver.get(HACKERRANK_BASE+self.username)

        try:
            username = self.driver.find_element(By.CLASS_NAME, "username").text
            if username == self.username:
                return True
            else:
                return False
        except NoSuchElementException:
            print("Login Falied! Check your username and password.")
            return False

    def LOGOUT(self):
        self.driver.get(HACKERRANK_BASE+self.username)
        sleep(2)
        self.driver.find_element(By.CLASS_NAME, "username").click()
        self.driver.find_element(By.CLASS_NAME, "logout-button").click()
        sleep(5)

    def getTrack(self, track):
        limit = 50
        offset = 0
        while True:
            tracks = self.getTrackRequest(track, limit, offset)
            models = tracks.get('models')
            for i in models:
                chal_slug = i.get('slug')
                sub_domain = i.get('track').get('slug')
                if chal_slug is None:
                    raise Exception("Chal_slug:"+str(chal_slug))

                sub_domain_string = "Domain: "+sub_domain
                print(track + " "+sub_domain_string +
                    chal_slug.rjust(80 - len(sub_domain_string)))

                if SKIP_DOWNLOADED and self.codeFileExists(track, sub_domain, chal_slug):
                    print("Skipped!")
                    continue

                sub_id = self.getSubmissions(chal_slug)
                code = False
                if sub_id:
                    for attempt in range(1, MAX_RETRIES+1):
                        try:
                            result = self.getCode(chal_slug, sub_id)
                            code = result.get('code')
                            lang = result.get('language')
                            break
                        except WaitAndRetry as error:
                            print(error, "(attempt #"+str(attempt)+", retrying in "+str(WAIT_SECONDS)+" seconds)")
                            if attempt < MAX_RETRIES:
                                sleep(WAIT_SECONDS)
                            else:
                                raise Exception("Max. retries reached. Chal_slug:"+str(chal_slug))

                if code:
                    ext = ''
                    if lang in HACKERRANK_EXTENSIONS.keys():
                        ext = HACKERRANK_EXTENSIONS.get(lang)
                    elif track in HACKERRANK_EXTENSIONS:
                        ext = HACKERRANK_EXTENSIONS.get(track)
                    self.writeCodeFile(track, sub_domain, chal_slug, code, ext)

            # check if more pages available
            if len(models) == limit:
                offset += limit
            else:
                break

    def getTrackRequest(self, track, limit=50, offset=0):

        FILTERS = "?status=solved"
        LIMIT = "&limit="+str(limit)
        OFFSET = "&offset="+str(offset)

        URL = HACKERRANK + "tracks/" + track + "/challenges" + FILTERS + LIMIT + OFFSET

        try:
            self.driver.get(URL)
            get_track = loads(
                self.driver.find_element_by_tag_name("body").text)
        except Exception as error:
            error.track = track
            raise error
        return get_track

    @staticmethod
    def writeCodeFile(track, sub_domain, filename, code, ext):

        folder = HACKERRANK_DIR / track

        HACKERRANK_DIR.mkdir(exist_ok=True)
        folder.mkdir(exist_ok=True)

        folder = folder / sub_domain
        file_path = folder / (filename+ext)

        if not folder.exists():
            folder.absolute().mkdir(exist_ok=True)
            if not file_path.is_file():
                print(code, file=open(str(file_path), 'w'))
        else:
            # Currently using print() to write files to disk.
            print(code, file=open(str(file_path), 'w'))

    @staticmethod
    def codeFileExists(track, sub_domain, filename, ext='*'):
        folder = HACKERRANK_DIR / track
        folder = folder / sub_domain
        if folder.exists():
            for path in folder.glob(filename+ext):
                if path.is_file():
                    return True
        return False

    def getSubmissions(self, chal_slug):

        submissions = self.getSubmissionsRequest(chal_slug)

        if submissions is None:
            raise Exception("Submissions: "+str(submissions))

        models = submissions.get('models')
        if len(models) > 0:
            # Skip MCQ (multiple choice question)
            if 'challenge' in models[0] and 'kind' in models[0]['challenge'] and models[0]['challenge']['kind'] == 'mcq':
                return False
            # models are all the submissions models[0] being the latest
            sub_id = models[0]['id']
            return sub_id
        else:
            return False

    def getCode(self, chal_slug, sub_id) -> dict:
        code_res = self.getSubmission(
            chal_slug, sub_id)

        if code_res is None:
            raise Exception("Code_res: "+code_res)

        model = code_res.get('model')
        if model == False:
            raise WaitAndRetry(code_res.get('message'))

        code = model.get('code')
        language = model.get('language')

        result = dict()
        result['code'] = code
        result['language'] = language
        return result

    def getSubmissionsRequest(self, chal_slug):

        LIMIT = "?limit=20"
        OFFSET = "?offset=0"

        URL = HACKERRANK + "challenges/" + chal_slug + "/submissions/" + OFFSET + LIMIT
        try:
            self.driver.get(URL)
            submissions = loads(
                self.driver.find_element_by_tag_name("body").text)
        except Exception as error:
            error.track = chal_slug
            raise error
        return submissions

    def getSubmission(self, chal_slug, sub_id):
        URL = HACKERRANK + "challenges/" + \
            chal_slug + "/submissions/" + str(sub_id)
        try:
            self.driver.get(URL)
            code_res = loads(self.driver.find_element_by_tag_name("body").text)
        except Exception as e:
            e.track = chal_slug
            raise e
        return code_res

class WaitAndRetry (Exception):
    pass