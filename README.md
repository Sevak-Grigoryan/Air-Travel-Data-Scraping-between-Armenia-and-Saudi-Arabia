# Air Travel Data Scraping from Armenia to Saudi Arabia

## Project Overview
This project aims to scrape data from [Kiwi.com](https://www.kiwi.com) to gather detailed information about air travel options between Yerevan, Armenia, and Riyadh, Saudi Arabia. The project uses Selenium to navigate the website, extract flight details, and handle dynamic content such as modals and cookies.

## Features
- Automated extraction of flight information, including:
  - Departure and destination cities
  - Airports and airlines
  - Flight durations and layover details
  - Prices and wait times
- Handling dynamic elements and pop-ups using Selenium’s explicit waits.
- Efficient navigation through multiple search results.

## Technologies Used
- **Python:** Core language for automation
- **Selenium:** Web scraping and browser automation
- **Fake UserAgent:** For setting a random user agent

## Prerequisites
Before running the project, ensure you have the following installed:

1. Python 3.x
2. Google Chrome and ChromeDriver
3. Required Python packages:
   ```bash
   pip install selenium fake-useragent
   ```

## How to Run
1. Clone the repository or download the project files.
2. Open a terminal and navigate to the project directory.
3. Run the script:
   ```bash
   python main.py
   ```

## Important Notes
- Ensure that the version of ChromeDriver matches your installed version of Google Chrome.
- The script waits for dynamic elements to load, but website updates may require future adjustments to selectors.
- Handle the extracted data (`info` list) as needed.

## Project Structure
- `main.py`: Main script for scraping flight data

## Potential Enhancements
- Improve error handling and logging
- Save extracted data to a structured format (CSV, JSON)
- Implement headless browsing for better performance
- Add retry logic for better reliability

## Disclaimer
This project is intended for educational purposes only. Ensure compliance with the website’s terms of service before scraping data.

