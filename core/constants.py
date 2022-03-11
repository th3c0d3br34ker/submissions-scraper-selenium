from pathlib import Path

WEBDRIVER_DIR = Path("Requirements\chromedriver.exe")

# CodeChef
CODE_CHEF = "https://www.codechef.com/"
CODE_CHEF_DIR = Path("../CodeChef Submissions")

# Hackerrank
HACKERRANK = "https://www.hackerrank.com/rest/contests/master/"
HACKERRANK_BASE = "https://www.hackerrank.com/"
HACKERRANK_DIR = Path("../Hackerank Solutions")

SUPPORTED = ['CodeChef', 'Hackerrank']

# Skip solutions that have already been downloaded (speed up re-downloads)
SKIP_DOWNLOADED = True

# Configure Wait and Retry to circumvent HackerRank's rate limit
MAX_RETRIES = 10
WAIT_SECONDS = 30