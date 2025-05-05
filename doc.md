# Technical Documentation: Naukri Webscraper

## Table of Contents

- [Function Reference](#function-reference)
- [Extracted Data Schema](#extracted-data-schema)
- [Configuration & Requirements](#configuration--requirements)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)
- [Disclaimer & License](#disclaimer--license)

---

## Function Reference

### `main()`

Entry point. Orchestrates scraping, CSV export, and skill-based filtering.

### `get_job_listings()`

- Launches Selenium in headless mode.
- Navigates to Naukri.com, performs search, paginates, and extracts job data.
- Returns: `List[Dict]` of job listings.

### `get_article(driver)`

- Extracts job data from a single listing/article element.
- Returns: `Dict` with job fields.

### `get_input_url(wait, driver)`

- Prompts user for search keywords.
- Navigates to search results and returns the URL.

### `get_text_or_default(element, selector, default="N/A")`

- Utility: Extracts text from a child element or returns default.

### `write_to_csv(jobs, csv)`

- Writes job listings (list of dicts) to a CSV file.

### `filter_by_skills(df)`

- Prompts user for skills (comma-separated).
- Filters DataFrame rows where 'Skills Required' matches input.

---

## Extracted Data Schema

Each job listing contains:

| Field                | Description                                      |
|----------------------|--------------------------------------------------|
| Job Title            | Title/position                                   |
| Reference            | URL to job listing                               |
| Company              | Employer name                                    |
| Experience           | Min/max years required                           |
| Salary               | Salary info (if available)                       |
| Location             | City/region                                      |
| Job Description      | Responsibilities, qualifications, requirements   |
| Skills Required      | List of required skills                          |
| Posting Date         | Date posted                                      |

---

## Configuration & Requirements

- **Python 3.x**
- **Chrome Browser** and **Chrome WebDriver** (matching version)
- **Python libraries**: `pandas`, `selenium`
- Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

- **WebDriver**: Place in PATH or let Selenium 4.6+ auto-manage.

---

## Testing

Automated tests are in `test_project.py` (uses `pytest`).

- Install pytest:

    ```bash
    pip install pytest
    ```

- Run tests:

    ```bash
    pytest test_project.py
    ```

Some tests require live access to Naukri.com and may fail if the site structure changes.

---

## Troubleshooting

- **Selectors break:** If scraping fails or data is missing, update CSS selectors/XPaths in `project.py` to match the current site.
- **WebDriver errors:** Ensure ChromeDriver matches your Chrome version.
- **Blocked by site:** Use reasonable pause times and avoid scraping too many pages at once.

---

## Disclaimer & License

- For educational use only. Respect Naukri.com's terms.
- Licensed under MIT. See [LICENSE](LICENSE).
