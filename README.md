[![Codacy Badge](https://app.codacy.com/project/badge/Grade/8318552df2264bac9b2f7248b60588cf)](https://www.codacy.com/manual/th3c0d3br34ker/submissions-scraper-selenium?utm_source=github.com&utm_medium=referral&utm_content=th3c0d3br34ker/submissions-scraper-selenium&utm_campaign=Badge_Grade)

# Submissions Scraper

[Hackerrank Scraper](#Hackerrank-Scraper)

[Codacy Scraper](#Codechef-Scraper)

### Setup

This tools works with selenium webdriver. Download and store it in the Requirements Folder. Make sure you download the webdriver accoriding to the version of your chrome browser. This code currently only supports Google Chrome. If you want to contribute, I am always open for collaborations.

1.  Setup requirements for python (>=3.x) using the requirements.txt. Don't forget to setup a virtual environment first.

```bash
pip install -r requirements.txt
```

2.  Setup your credentials in the credentials.py file. Don't worry your password is safe as `credentials.py` is added in `.gitignore`. Add your tracks as per you requirements.

3.  Run `scraper.py`.

```bash
python scraper.py
```

### Requirements

<h3 id="selenium-webdriver">Selenium Webdriver</h3>
<p>Currently Working with chromedriver.exe.</p>
<p>Download the lastest version as per you browser from <a href="https://chromedriver.storage.googleapis.com/index.html">here</a></p>
<blockquote>
<p>Note: Currently working with chrome version 83.0</p>
</blockquote>

---

## Hackerrank Scraper	

<p align="center">
	<a href="https://www.hackerrank.com/jainamd"><img src="assets/title-hackerrank.jpg"></a>
</p>

Get your Hackerrank solutions of problems you have solved in an easy and quick way.

```python
self.Hackerrank = {
	"username": "username",
	"password": "password",
	"tracks":  ["java", "python", "c", "cpp"]
	# Available (add as per your requirements):
	# Languages: "ruby", "shell", "sql", "fp",
	# Domians: "algorithms", "data-structures", "mathematics", "ai", "databases", "regex", "tutorials"
}
```
---

## Codechef Scraper

<p align="center">
	<a href="https://www.codechef.com/jainam_d"><img src="assets/title-codechef.jpg"></a>
</p>

This gets your "Fully Solved" submissions and saves them into a folder on your local machine.

CodeChef is not fond of scraping. It limits the amount of requests one can make. If you have a lot of submissions (>100) to scrape, then I would suggest a naive way to do it. 

```python
self.CodeChef = {
	"username": "username",
	"password": "passwords"
}
```

Ran into an ISSUE? Feel free to open an [issue](https://github.com/th3c0d3br34ker/submissions-scraper-selenium/issues/new). Enjoy!
