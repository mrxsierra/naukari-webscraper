# Job Listings Web Scraper

#### Video Demo: <https://youtu.be/ls_uxjfADN4?si=MVFuRLyLIclpeeel>

#### Description

This is a Python script that scrapes job listings from Naukri.com and allows you to filter and analyze them based on skills.

## Overview

This project is a Python-based web scraping application that extracts job listings from naukri.com and allow user to anlyse them. The project consists of several essential files:

- **project.py**: The core script responsible for web scraping job listings, processing data, and providing user-friendly filtering options. It employs Selenium to perform web scraping on Naukri.com, extracting details such as job title, reference, company, experience requirements, salary, location, job description, skills required, posting date, and duration. It also allows you to export data to a CSV file and filter job listings according to desired skills.
- **requirements.txt**: Lists the required Python packages and their versions.
- **test_project.py**: Contains unit tests to ensure the functions' correctness.
- **README.md**: The comprehensive project description.

## Features

- Search for job listings based on skills or job titles.
- Filter search results to include zero experience and posts posted within the last three days.
- Provide information about the total number of pages available to scrape for a given search query.
- Allow users to specify the number of pages to scrape for enhanced flexibility.
- Efficiently scrape job listings data from Naukri.com using Selenium.
- Save job listings data to a CSV file.
- Display the total number of job posts scraped.
- Filter job listings based on user-input skills.

## Documentation

### *Program Functions*

The `project.py` script uses several functions to scrape job listings from Naukri.com, process the data, and offer user-friendly filtering options. Below are the key functions of the program:

### `main()`

The `main()` function serves as the entry point of the program. It orchestrates the web scraping and data processing flow. Here's what it does:

- Calls `get_job_listings()` to fetch job listings from Naukri.com.
- Prints the total number of job listings obtained.
- Writes the job listings to a CSV file named "job_listings.csv."
- Reads the CSV file into a pandas DataFrame and displays it.
- Invokes `filter_by_skills()` to filter job listings based on user-defined skills.

### `filter_by_skills(df)`

The `filter_by_skills(df)` function allows users to filter the DataFrame of job listings by specifying desired skills. It prompts the user for input and filters the listings accordingly. Here's how it works:

- Prompts the user to enter one or more skills (comma-separated).
- Filters the DataFrame to include only job listings that match the specified skills.
- Prints the filtered job listings in a user-readable format.

### `get_text_or_default(element, selector, default="N/A")`

The `get_text_or_default(element, selector, default="N/A")` function is a utility function used to extract text content from HTML elements on web pages. It takes three parameters:

- `element`: The parent HTML element to find the child element within.
- `selector`: The CSS selector used to locate the child element.
- `default`: A default value to return if the element is not found.

### `write_to_csv(jobs, csv)`

The `write_to_csv(jobs, csv)` function writes a list of job listings to a CSV file. It takes two parameters:

- `jobs`: A list of dictionaries, where each dictionary represents a job listing.
- `csv`: The path to the CSV file where the job listings will be written.

### `get_job_listings()`

The `get_job_listings()` function is responsible for web scraping job listings from Naukri.com. Here's what it does:

- Configures Selenium to work in headless mode (without a visible browser window).
- Navigates to Naukri.com and searches for job listings based on user input.
- Determines the total number of pages available for the search query.
- Loops through each page, scrapes job listing details using `get_article()`, and accumulates the data in a list of dictionaries.
- Returns the list of job listings.

### `get_article(driver)`

The `get_article(driver)` function extracts job listing data from individual articles on a page. It utilizes Selenium to locate and extract information such as job title, reference, company, experience required, salary, location, job description, skills required, posted date, and duration.

### `get_input_url(wait, driver)`

The `get_input_url(wait, driver)` function retrieves the input URL for web scraping. It prompts the user for job titles or skills, performs a search on Naukri.com, and returns the URL of the search results.

These functions collectively enable the program to scrape, process, and filter job listings effectively.

#### *Extracted Data Features*

The web scraping script extracts various features from job listings on Naukri.com, providing comprehensive information for analysis and decision-making. Here are the key features of the extracted job data:

1. **Job Title:** The job title or position offered by the employer.

2. **Reference:** A reference link to the job listing for further details.

3. **Company:** The name of the company or organization offering the job.

4. **Experience Requirements:** The minimum and maximum years of experience required for the job.

5. **Salary:** Information about the offered salary, if available.

6. **Location:** The geographic location of the job, including city or region.

7. **Job Description:** A detailed description of the job responsibilities, qualifications, and requirements.

8. **Skills Required:** A list of skills or qualifications expected from candidates. Skills are extracted as a list, making it easy to analyze and search for specific skills.

9. **Posting Date:** The date when the job listing was posted on Naukri.com.

10. **Duration:** If specified, the duration or contract type of the job.

These extracted data features enable users to explore and filter job listings based on their preferences, skills, and other criteria. Whether you're looking for specific job titles, companies, or skills, this data provides valuable insights into the job market and assists in making informed career decisions.

## Requirements

To run this project, ensure you have the following:

- Python 3.x
- Chrome Browser
- Chrome WebDriver (for Selenium; download the same WebDriver version as your browser [>>Download From Here<<](https://chromedriver.chromium.org/downloads))
- Required Python libraries (install with `pip install -r requirements.txt`):
  - `pandas` library

    ```bash
    pip install pandas
    ```

  - `selenium` library

    ```bash
    pip install selenium
    ```

## Usage

`:: Assuming Chrome Browser is already installed in local machine`

1. Clone this `project folder` from repository to your local machine. `"git clone < repository link >"` will help!

###### Note: Script is only tested in VScode in "Windows 11 local machine" with Chrome Browser installed

2. Install the required libraries by running:

    ```
    pip install -r requirements.txt
    ```

3. (`Only if needed`) Download the Chrome WebDriver and add its executable to your system's PATH.

###### Note: Selenium 4.6x onwards comes with a prebuilt Driver Manager, which automates WebDriver management

4. Run the script using:

    ```
    python project.py
    ```

5. Follow the prompts to input the desired skills and filter job listings.

## Output

The script generates a CSV file named `job_listings.csv` in the project directory, containing the scraped job listings data. Additionally, it displays filtered job listings based on user-provided skills in a well-organized pandas DataFrame.

## Design Choices

- **Web Scraping**: The project utilizes the Selenium library for web scraping Naukri.com, automating the process of retrieving job listings, including essential details such as titles, companies, and required skills.

- **Choice of Selenium**: Selenium was chosen as the web scraping tool for this project due to its robust capabilities in handling dynamic websites with JavaScript-driven content. While other libraries like `requests` and `BeautifulSoup` are suitable for static websites, Naukri.com relies heavily on JavaScript to render job listings. Selenium excels in automating browsers, making it the preferred choice for interacting with the website's dynamic elements and ensuring accurate data extraction. Additionally, using `Scrapy` would have required setting up a separate environment and configuration, adding unnecessary complexity to the project.

- **Data Storage**: Scraped job listings are saved in a CSV file named `job_listings.csv` for further analysis or reference.

- **User Interaction**: The script fosters user interaction by allowing users to input desired skills for filtering job listings, making the experience more customized and user-friendly.

## Example

Here is a brief example of how to use the project:
![Example with Image](Example.jpg)

1. Open your terminal.

2. Run the script by executing the following command:

   ```
   python project.py
   ```

3. When prompted, input the desired job titles or skills. For example:

    - ***"Python"***
    - ***"Data Scientist"***

4. Input the number of pages to scrape from the available `total number of pages for the keyword`.

###### ***For instance, if the `total number of pages for the keyword` is "5", than, enter a `number equal to or less` than `"5"`.***

5. Specify the `pause time` between page requests to efficiently scrape multiple pages (`in seconds`). ***For example, `"2"` seconds.***

6. The script will then fetch job listings, store them in a `CSV file`.

7. Additionally, you can input `specific Skills` to filter the `Required Skills column` and narrow down your search. `For example`, if you initially scraped data for `"Python"` positions but want to filter for those mentioning `"Django"` in the Skills Required column, you can input `"Django"` when prompted.

## Tests

The `test_project.py` file includes unit tests to verify the accuracy of the project's functions. Run the tests using a testing framework like `pytest`:

- Install `pytest`:

    ```
    pip insatll pytest
    ```

- Run `test` script:

    ```
    pytest test_project.py
    ```

## Conclusion

This Python project demonstrates web scraping, data processing, and user interaction. It helps users find job listings based on their skills and provides valuable insights into the job market.

Feel free to explore, modify, or enhance this project for your specific needs!

Note: If you encounter any issues or have questions, please refer to the project's GitHub repository or contact the project's author for support.

## Disclaimer

This script is intended for educational purposes only. Be sure to review and comply with the terms of use of any website you intend to scrape. Use responsibly and ethically.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
