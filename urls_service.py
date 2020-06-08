from constants import BASE_URL
from json import loads


class URL_Service:

    def __init__(self):
        return

    def get_track_request(self, track, driver):
        FILTERS = "?status=solved"
        LIMIT = "?limit=500"
        OFFSET = "?offset=0"

        URL = BASE_URL + "tracks/" + track + "/challenges" + LIMIT + OFFSET + FILTERS

        try:
            driver.get(URL)
            get_track = loads(driver.find_element_by_tag_name("body").text)
        except Exception as e:
            e.track = track
            raise e
        return get_track

    def get_submissions_request(self, chal_slug, driver):

        LIMIT = "?limit=20"
        OFFSET = "?offset=0"

        URL = BASE_URL + "challenges/" + chal_slug + "/submissions/" + OFFSET + LIMIT
        try:
            driver.get(URL)
            submissions = loads(driver.find_element_by_tag_name("body").text)
        except Exception as e:
            e.track = chal_slug
            raise e
        return submissions

    def get_particular_submission(self, chal_slug, sub_id, driver):
        URL = BASE_URL + "challenges/" + \
            chal_slug + "/submissions/" + str(sub_id)
        try:
            driver.get(URL)
            code_res = loads(driver.find_element_by_tag_name("body").text)
        except Exception as e:
            e.track = chal_slug
            raise e
        return code_res
