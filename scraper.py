def initialization(platform, credential):
    if (platform == "CodeChef"):
        from core.cc_scrapper import CC_Scrapper
        from core.utils import setupSeleniumDriver

        try:
            driver = setupSeleniumDriver()

            codechef_scraper = CC_Scrapper(
                username=credential.get("username"),
                password=credential.get("password"),
                driver=driver)

            # Login first LOL
            if codechef_scraper.LOGIN():

                # Start the freaking show! :p

                codechef_scraper.getSubmissions()
                codechef_scraper.LOGOUT()

        except Exception as error:
            print(error)
        finally:
            driver.quit()

    elif (platform == "Hackerrank"):
        from core.hr_scrapper import HR_Scrapper
        from core.utils import setupSeleniumDriver

        try:
            driver = setupSeleniumDriver()

            hackerrank_scraper = HR_Scrapper(
                username=credential.get("username"),
                password=credential.get("password"),
                driver=driver)

            # Login first :D
            if hackerrank_scraper.LOGIN():

                # Start the freaking show! :p
                # Hackerrank uses tracks
                for track in credential.get("tracks"):
                    hackerrank_scraper.getTrack(track)

                # Logout :D
                hackerrank_scraper.LOGOUT()

        except Exception as error:
            print(error)
        finally:
            driver.quit()
    else:
        print("Currently supported: ")
        from core.constants import SUPPORTED
        for idx, val in enumerate(SUPPORTED):
            print(f"{idx}. {val}")
        exit()


def main():
    try:
        from credentials import ACCOUNTS
        accounts = ACCOUNTS().getAccounts()
        accountsList = list(accounts)
    except ModuleNotFoundError:
        print("Please setup a credentials.py file!")

    if accountsList:
        print("Found the following Account(s): ")
        for index, account in enumerate(accountsList):
            print(f"{index+1}. {account}")

        option = int(input("Enter your choice: ")) - 1
        initialization(accountsList[option],
                       accounts.get(accountsList[option]))
    else:
        print("Please define accounts in credentials.py")


if __name__ == "__main__":
    main()
