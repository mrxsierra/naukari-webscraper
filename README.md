# 🚀 Naukri Webscraper

[![Video Demo](https://img.youtube.com/vi/ls_uxjfADN4/maxresdefault.jpg)](https://www.youtube.com/watch?v=ls_uxjfADN4)

A Python tool to automate job searches on [Naukri.com](https://www.naukri.com/), filter listings by skills, and export structured data for analysis.

---

## 📋 Overview

This project is a Python-based web scraper that extracts job listings from Naukri.com, allowing users to analyze and filter them by skills. It uses Selenium for browser automation and Pandas for data handling. The tool is interactive, robust, and tested with `pytest`.

**Main files:**

- `project.py`: Core scraping, filtering, and CSV export logic.
- `test_project.py`: Automated tests (using `pytest`) for reliability.
- `pyproject.toml`: Project metadata and dependencies.
- `README.md`: Documentation and usage guide.

---

## ✨ Features

- Search and scrape job listings by title or skill.
- Filter results for zero experience and recent postings (last 3 days).
- Choose how many pages to scrape and set pause time between requests.
- Extracts: job title, company, salary, location, description, skills, post date, and reference link.
- Save results to a CSV file.
- Interactive skill-based filtering of results.
- Automated tests for core logic with `pytest`.

---

## 🛠️ Technologies Used

- **Python** (3.13+)
- **Selenium** (browser automation)
- **Pandas** (data manipulation & CSV export)
- **pytest** (testing)
- **Chrome WebDriver** (headless browser)
- **Git** (version control)

---

## ⚡ Quickstart

### 1. Prerequisites

- Python 3.13 or newer
- Google Chrome browser
- Chrome WebDriver (matching your Chrome version, [download here](https://chromedriver.chromium.org/downloads))

### 2. Install Dependencies

```bash
pip install pandas selenium
pip install pytest  # for running tests
```

Or, if using a tool that supports `pyproject.toml`:

```bash
pip install .
```

### 3. Run the Scraper

```bash
python project.py
```

Follow the prompts to:

- Enter job title/skills to search
- Choose number of pages to scrape
- Set pause time between pages
- Filter results by desired skills

### 4. Output

- Results are saved to `job_listings.csv`
- Filtered results are displayed in the terminal

---

## 📝 Usage Example

```text
Input 'Job' Title/skills = Python
Input number of page to scrap (Recommend: less than '5'): 2
input pause time (in seconds) b/w pages: 2
...
Enter 'Skills' (use ',' for multiple Skills) to Filter: Django, SQL
```

---

## 🧩 Project Structure

```sh
workDir
--|--project.py         # Main scraping and filtering logic
  |--test_project.py    # Automated tests (pytest)
  |--pyproject.toml     # Project metadata and dependencies
  |--README.md          # This documentation
  |++job_listings.csv   # Output file (generated)
```

---

## 🧪 Testing

Automated tests are provided in `test_project.py` and use `pytest`.

To run tests:

```bash
pytest test_project.py
```

Some tests require live website access and may be skipped or fail if Naukri.com blocks bots or changes structure.

---

## ⚠️ Note on Site Changes

>***Note :*** `If scraping fails or data is missing...`
    `naukri.com` may update, its HTML structure or class names.
    If you encounter errors or missing data, **update the locators like, CSS selectors/XPaths in `project.py`** to match the new site layout.

---

## 🏆 Key Learnings

- Selenium for dynamic web scraping
- Data wrangling and export with Pandas
- Writing maintainable, testable automation code
- Robust error handling and user interaction
- Automated testing with `pytest`

---

## 📄 License

MIT [License](./LICENSE.txt)

---

## 🙋‍♂️ Support

For questions or issues, open an issue on [GitHub](https://github.com/mrxsierra/naukari-webscraper) or contact the author.

---

## 📢 Disclaimer

This script is for educational purposes. Please respect Naukri.com's terms of use and robots.txt. Use responsibly.
