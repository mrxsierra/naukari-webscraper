import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import math
import sys
import re


def main():
    """
    Main function to orchestrate the web scraping and data processing.
    """
    jobs = get_job_listings()
    print(f"Total job Post = {len(jobs)}\n 'job_listings.csv' File Saved Sucessfully..")

    csv = "job_listings.csv"
    write_to_csv(jobs, csv)

    read = pd.read_csv(csv)
    print(read)
    while True:
        try:
            filter_by_skills(read)
        except KeyboardInterrupt:
            break


def filter_by_skills(df):
    """
    Filter the DataFrame by desired skills provided by the user (case-insensitive).

    Parameters:
        df (pd.DataFrame): DataFrame containing job listings.

    """
    while True:
        try:
            desired_skills = (
                input("Enter 'Skills' (use ',' for multiple Skills) to Filter: ")
                .strip()
                .split(", ")
            )

            # Remove leading and trailing spaces from each skill and convert to lowercase
            desired_skills = [skill.strip().lower() for skill in desired_skills]

            if all(skill.replace(" ", "").isalpha() for skill in desired_skills):
                break
            else:
                raise ValueError

        except ValueError:
            continue

    # Convert "Skills Required" column in DataFrame to lowercase
    df["Skills Required"] = df["Skills Required"].str.lower()

    # Split multiple skills into a list and check if all skills are required
    filtered_df = df[
        df["Skills Required"].apply(
            lambda skills: all(
                re.search(skill, skills, re.IGNORECASE) for skill in desired_skills
            )
        )
    ]

    # Print the filtered DataFrame in key-value pair format
    print(
        "--------------------------------------------------------------------------\n"
    )
    for index, row in filtered_df.iterrows():
        print(f"Job {index + 1}:")
        for key, value in row.items():
            print(f"{key}: {value}")
        print()
    print("------------------------ Press 'cntrl+c' to exit -----------------------\n")


def get_text_or_default(element, selector, default="N/A"):
    """
    Get the text content of an element using a selector, or return a default value.

    Parameters:
        element (WebElement): The parent element to find the child element in.
        selector (str): CSS selector to locate the child element.
        default (str): Default value to return if the element is not found.

    Returns:
        str: The text content of the element, or the default value if not found.
    """
    try:
        return element.find_element(By.CSS_SELECTOR, selector).text
    except NoSuchElementException:
        return default


def write_to_csv(jobs, csv):
    """
    Write job listings to a CSV file.

    Parameters:
        jobs (list): List of job listing dictionaries.
        csv (str): Path to the CSV file to write to.
    """
    df = pd.DataFrame(jobs)
    df.to_csv(csv, index=False)


def get_job_listings():
    """
    Get job listings from naukri.com using web scraping.

    Returns:
        list: List of dictionaries containing job listing data.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")

    with webdriver.Chrome(options=options) as driver:
        wait = WebDriverWait(driver, 10)
        url = get_input_url(wait, driver)
        res = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "span.fleft.count-string.mr-5.fs12")
            )
        ).text
        page = math.floor(int(res[(res.find("f")) + 2 :]) / 20)
        if page < 1:
            page = 1
        else:
            print(
                f"total number of page for keyword is {page}\n**Note: some keywords may contain less page result or even '0'\n------------------------------------------------------------------"
            )
            while True:
                try:
                    input_page = input(
                        "Input number of page to scrap (Recommend: less than '5'): "
                    )
                    if input_page.isnumeric():
                        break
                    else:
                        continue
                except ValueError:
                    continue
            page = int(input_page)
            while True:
                try:
                    pause_t = int(input("input pause time (in seconds) b/w pages: "))
                    break
                except ValueError:
                    continue
            if pause_t == None or pause_t < 1:
                pause_t = 1

        job_listings = []

        for i in range(page):
            if i != 0:
                place = url.find("?")
                link = url[:place] + "-" + str(i + 1) + url[place:]
                driver.get(link)
                sleep(pause_t)
            print(driver.current_url)
            article_list = get_article(driver)
            job_listings.extend(article_list)

        return job_listings


def get_article(driver):
    """
    Get job listing data from individual articles on a page.

    Parameters:
        driver (webdriver.Chrome): The Chrome WebDriver instance.

    Returns:
        list: List of dictionaries containing job listing data.
    """
    job_article_list = []

    articles = driver.find_elements(By.TAG_NAME, "article")

    for article in articles:
        try:
            title = get_text_or_default(article, "a.title.ellipsis")
            ref = article.find_element(
                By.CSS_SELECTOR, "a.title.ellipsis"
            ).get_attribute("href")
            company = get_text_or_default(article, "a.subTitle.ellipsis.fleft")
            experience = get_text_or_default(
                article, "ul li.fleft.br2.placeHolderLi.experience"
            )
            duration = get_text_or_default(
                article, "ul li.fleft.br2.placeHolderLi.duration"
            )
            salary = get_text_or_default(
                article, "ul li.fleft.br2.placeHolderLi.salary"
            )
            location = get_text_or_default(
                article, "ul li.fleft.br2.placeHolderLi.location"
            )
            job_description = get_text_or_default(
                article, "div.ellipsis.job-description"
            )
            skills_req = get_text_or_default(
                article, "ul.tags.has-description", default=""
            ).split("\n")
            post_date = get_text_or_default(article, "span.fleft.postedDate")

            job_listing = {
                "Title": title,
                "Reference": ref,
                "Company": company,
                "Experience": experience,
                "Salary": salary,
                "Location": location,
                "Job Description": job_description,
                "Skills Required": skills_req,
                "Posted Date": post_date,
                "Duration": duration,
            }
            job_article_list.append(job_listing)

        except NoSuchElementException:
            print("element not found")
    return job_article_list


def get_input_url(wait, driver):
    """
    Get the input URL for the web scraping.

    Parameters:
        wait (WebDriverWait): The WebDriverWait instance.
        driver (webdriver.Chrome): The Chrome WebDriver instance.

    Returns:
        str: The URL to start the web scraping from.
    """
    print(
        "------------------------------------------------------------------\n**Help: If not respond within '30 seconds', Terminate manually by pressing 'ctrl + c'.\n**Note: Make sure internet is working\n------------------------------------------------------------------"
    )
    while True:
        try:
            job = input("Input 'Job' Title/skills = ")
            if job.isnumeric():
                continue
            else:
                break
        except ValueError:
            continue
    print(
        "=================================wait=============================\nMessage: Scraping is in Process...........\nMessage: It may take time based on the number of posts it finds....\n**Note: If you see 'site links and total post', means everything is 'fine', \n   -- other than this, there may be a bug in the code you can start debugging code by first looking into 'webdriver' and 'dependencies'**\n=================================================================="
    )
    driver.get("https://www.naukri.com/")
    search_field = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input.suggestor-input"))
    )
    search_field.send_keys(job)
    search_field.send_keys(Keys.ENTER)
    url = driver.current_url
    driver.get(url + "&jobAge=3&experience=0")
    return driver.current_url


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\nPrograms Forcefully exiting.....")
