from models import get_code_result_model
from constants import BASE_DIR
from pathlib import Path
from util import get_file_extension
from urls_service import get_track_request, get_submissions_request, get_particular_submission


class HR_Scrapper:

    def __init__(self):
        return

    def get_track(self, track, driver):
        tracks = get_track_request(track, driver)
        models = tracks.get('models')
        for i in models:
            chal_slug = i.get('slug')
            sub_domain = i.get('track').get('slug')
            if chal_slug is None:
                raise Exception("Chal_slug:"+str(chal_slug))

            sub_domain_string = "Domain: "+sub_domain
            print(track + " "+sub_domain_string +
                  chal_slug.rjust(70 - len(sub_domain_string)))

            sub_id = self.get_submissions(chal_slug, driver)
            code = False
            if sub_id:
                result = self.get_code(chal_slug, sub_id, driver)
                code = result.get('code')
                lang = result.get('language')

            if code:
                ext = get_file_extension(track, lang)
                self.create_code_file(track, sub_domain, chal_slug, code, ext)

    def create_code_file(self, track, sub_domain, filename, code, ext):
        folder = Path("..", BASE_DIR, track, sub_domain)

        file_path = folder / (filename+ext)

        if not folder.exists():
            folder.absolute().mkdir(exist_ok=True)
            if not file_path.is_file():
                print(code, file=open(str(file_path), 'w'))
        else:
            print(code, file=open(str(file_path), 'w'))

    def get_submissions(self, chal_slug, driver):
        submissions = get_submissions_request(chal_slug, driver)

        if submissions is None:
            raise Exception("Submissions: "+str(submissions))

        models = submissions.get('models')
        if len(models) > 0:
            sub_id = models[0]['id']
            return sub_id
        else:
            return False

    def get_code(self, chal_slug, sub_id, driver) -> get_code_result_model:
        code_res = get_particular_submission(chal_slug, sub_id, driver)

        if code_res is None:
            raise Exception("Code_res: "+code_res)

        model = code_res.get('model')
        code = model.get('code')
        language = model.get('language')
        result = dict()
        result['code'] = code
        result['language'] = language
        return result
