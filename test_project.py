import os

import pandas as pd
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from project import (
    filter_by_skills,
    get_article,
    get_input_url,
    get_job_listings,
    write_to_csv,
)


@pytest.fixture
def mock_input(monkeypatch):
    inputs = iter(
        [
            "python",
            "1",
            "5",
        ]
    )
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))


def test_get_job_listings(mock_input):
    jobs = get_job_listings()

    expected_keys = [
        "Title",
        "Reference",
        "Company",
        "Experience",
        "Salary",
        "Location",
        "Job Description",
        "Skills Required",
        "Posted Date",
        # "Duration",
    ]
    assert isinstance(jobs, list)
    if len(jobs) > 0:
        assert isinstance(jobs[0], dict)
        assert list(jobs[0].keys()) == expected_keys
    else:
        pytest.skip(f"No jobs returned; likely due to anti-bot or site change. {jobs}")


@pytest.fixture
def mock_get_text_or_default(monkeypatch):
    def mock_get_text_or_default(element, selector, default="N/A"):
        return "Mocked Text"

    monkeypatch.setattr("project.get_text_or_default", mock_get_text_or_default)


@pytest.mark.skip(
    reason="Requires live website access; may fail due to anti-bot measures."
)
def test_get_article(mock_get_text_or_default):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    )
    with webdriver.Chrome(options=options) as driver:
        driver.get("https://www.naukri.com/python-jobs?k=python")

        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (
                    By.XPATH,
                    "//div[contains(@class, 'srp-jobtuple-wrapper')]",
                )
            )
        )
        article_list = get_article(driver)
        expected_keys = [
            "Title",
            "Reference",
            "Company",
            "Experience",
            "Salary",
            "Location",
            "Job Description",
            "Skills Required",
            "Posted Date",
            # "Duration",
        ]

        assert isinstance(article_list[0], dict)
        assert list(article_list[0].keys()) == expected_keys


@pytest.mark.skip(
    reason="Requires live website access; may fail due to anti-bot measures."
)
def test_get_input_url(mock_input):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    )
    with webdriver.Chrome(options=options) as driver:
        wait = WebDriverWait(driver, 10)
        url = get_input_url(wait, driver)
        expected_url = (
            "https://www.naukri.com/python-jobs?k=python&jobAge=3&experience=0"
        )
        assert url == expected_url


def test_write_to_csv():
    df = [
        {
            "Title": "Backend Developer (Python/Django)",
            "Reference": "https://www.naukri.com/job-listings-backend-developer-python-django-trade-brains-bangalore-bengaluru-0-to-1-years-290623904605",  # noqa: E501
            "Company": "Pixel Creationz",
            "Experience": "0-1 Yrs",
            "Salary": "Not disclosed",
            "Location": "Bangalore/Bengaluru",
            "Job Description": "Requirements : Proficient understanding in Python, with knowledge of Python web framewo...",  # noqa: E501
            "Skills Required": "['Python', 'Python web framework', 'Git', 'Django', 'DBMS', 'SQL', 'Web Framework', 'Web technologies']",  # noqa: E501
            "Posted Date": "1 Day Ago",
            # "Duration": None,
        },
        {
            "Title": "Python Developer",
            "Reference": "https://www.naukri.com/job-listings-python-developer-ajobman-ahmedabad-0-to-3-years-300823500154",
            "Company": "Ajobman",
            "Experience": "0-3 Yrs",
            "Salary": "Not disclosed",
            "Location": "Ahmedabad",
            "Job Description": "The developer should have the necessary skills and experience with the Odoo platform, i...",  # noqa: E501
            "Skills Required": "['ERP', 'GIT', 'Postgresql', 'Debugging', 'Director', 'Troubleshooting', 'Information technology', 'SDLC']",  # noqa: E501
            "Posted Date": "Few Hours Ago",
            # "Duration": None,
        },
    ]
    csv = "test.csv"
    write_to_csv(df, csv)
    assert os.path.exists(csv)


@pytest.fixture
def mock_input_f(monkeypatch):
    inputs = iter(
        [
            "Git",
        ]
    )
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))


def test_filter_by_skills(mock_input_f):
    df = pd.DataFrame(
        {
            "Job Title": ["Data Analyst", "Data Scientist", "Software Engineer"],
            "Skills Required": [
                "Python, SQL, Excel",
                "Python, R, Machine Learning",
                "Java, C++, Git",
            ],
        }
    )
    result = filter_by_skills(df)
    assert result is None
