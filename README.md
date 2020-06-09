<p align="center">
	<a href="https://www.hackerrank.com/jainamd"><img src="assets/title-hackerrank.jpg"></a>
</p>

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/eeb5576eb02d4f0e8e8edca5cb3d6024)](https://www.codacy.com/manual/th3c0d3br34ker/hackerrank-scraper-selenium?utm_source=github.com&utm_medium=referral&utm_content=th3c0d3br34ker/hackerrank-scraper-selenium&utm_campaign=Badge_Grade) ![GitHub](https://img.shields.io/github/license/th3c0d3br34ker/hackerrank-scraper-selenium)

# Hackerrank Scraper

Get your Hackerrank solutions of problems you have solved in an easy  and quick way.

## Setup

This tools works with selenium webdriver. Download and store it in the Requirements Folder. Make sure you download the webdriver accorinding to the version of your chrome browser. This code currently only supports Google Chrome. If you want to contribute, I am always open for collaborations.

1.  Setup requirements for python (>=3.x) using the requirements.txt. Don't forget to setup a virtual environment first.

```bash
pip install -r requirements.txt
```

2.  Setup your credentials in the credentials.py file. Don't worry your password is safe as `credentials.py` is added in `.gitignore`.

```python
username="username"
password="password"
```

3.  Add your tracks to tracks to tracks.py.

```python
TRACKS= ["java", "python", "c", "cpp"]
```

4.  Run `scraper.py`.

```bash
python scraper.py
```

Ran into an ISSUE? Feel free to open an issue. Enjoy!
