import pytest
import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from project import (
    get_job_listings,
    get_input_url,
    get_article,
    write_to_csv,
    filter_by_skills,
)


@pytest.fixture
def mock_input(monkeypatch):
    inputs = iter(
        [
            "python",
            "1",
            "2",
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
        "Duration",
    ]

    assert isinstance(jobs[0], dict)
    assert list(jobs[0].keys()) == expected_keys


@pytest.fixture
def mock_get_text_or_default(monkeypatch):
    def mock_get_text_or_default(element, selector, default="N/A"):
        return "Mocked Text"

    monkeypatch.setattr("project.get_text_or_default", mock_get_text_or_default)


def test_get_article(mock_get_text_or_default):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    with webdriver.Chrome(options=options) as driver:
        driver.get("https://www.naukri.com/python-jobs?k=python")

        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "a.subTitle.ellipsis.fleft")
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
            "Duration",
        ]

        assert isinstance(article_list[0], dict)
        assert list(article_list[0].keys()) == expected_keys


def test_get_input_url(mock_input):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")

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
            "Reference": "https://www.naukri.com/job-listings-backend-developer-python-django-trade-brains-bangalore-bengaluru-0-to-1-years-290623904605",
            "Company": "Pixel Creationz",
            "Experience": "0-1 Yrs",
            "Salary": "Not disclosed",
            "Location": "Bangalore/Bengaluru",
            "Job Description": "Requirements : Proficient understanding in Python, with knowledge of Python web framewo...",
            "Skills Required": "['Python', 'Python web framework', 'Git', 'Django', 'DBMS', 'SQL', 'Web Framework', 'Web technologies']",
            "Posted Date": "1 Day Ago",
            "Duration": None,
        },
        {
            "Title": "Python Developer",
            "Reference": "https://www.naukri.com/job-listings-python-developer-ajobman-ahmedabad-0-to-3-years-300823500154",
            "Company": "Ajobman",
            "Experience": "0-3 Yrs",
            "Salary": "Not disclosed",
            "Location": "Ahmedabad",
            "Job Description": "The developer should have the necessary skills and experience with the Odoo platform, i...",
            "Skills Required": "['ERP', 'GIT', 'Postgresql', 'Debugging', 'Director', 'Troubleshooting', 'Information technology', 'SDLC']",
            "Posted Date": "Few Hours Ago",
            "Duration": None,
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
    filter = filter_by_skills(df)
    assert isinstance(filter, type(None))
