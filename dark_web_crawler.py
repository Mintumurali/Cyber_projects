import requests
from bs4 import BeautifulSoup
import time

# User-Agent header to simulate a browser request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Example list of dark web URLs (these are placeholders and require Tor network access)
DARK_WEB_SITES = [
    "http://exampledarkweb.onion",  # Replace with actual .onion sites
    "http://anotherdarkweb.onion"
]

# Function to fetch and parse dark web pages
def fetch_dark_web_page(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            return soup.get_text()
        else:
            return f"Error: Status code {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

# Function to scan for leaked credentials
def scan_for_leaks(content):
    keywords = ["password", "email", "leak", "credit card", "SSN", "hacked"]
    found = [keyword for keyword in keywords if keyword in content.lower()]
    return found if found else None

# Main function to run the dark web crawler
def main():
    print("Starting dark web crawler...")
    for site in DARK_WEB_SITES:
        print(f"Scanning: {site}")
        page_content = fetch_dark_web_page(site)
        if page_content:
            leaks = scan_for_leaks(page_content)
            if leaks:
                print(f"Potential leaks found on {site}: {', '.join(leaks)}")
            else:
                print(f"No leaks detected on {site}.")
        time.sleep(5)  # Delay to avoid excessive requests

if __name__ == "__main__":
    main()
