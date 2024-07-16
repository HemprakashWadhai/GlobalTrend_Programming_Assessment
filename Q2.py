#2. Write a Python function that takes a list of URLs, attempts to download their content, and retries up to 3 times if an error occurs. Use appropriate error handling to manage different types of exceptions.
import requests
from time import sleep

def download_content(urls):
    results = {}
    for url in urls:
        attempts = 0
        while attempts < 3:
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
                results[url] = response.content
                break  # Exit the retry loop on successful request
            except requests.exceptions.HTTPError as http_err:
                print(f"HTTP error occurred for {url}: {http_err}")
            except requests.exceptions.ConnectionError as conn_err:
                print(f"Connection error occurred for {url}: {conn_err}")
            except requests.exceptions.Timeout as timeout_err:
                print(f"Timeout error occurred for {url}: {timeout_err}")
            except requests.exceptions.RequestException as req_err:
                print(f"General error occurred for {url}: {req_err}")
            attempts += 1
            print(f"Retrying {url} ({attempts}/3)...")
            sleep(1)  # Optional: wait 1 second before retrying
        else:
            results[url] = None  # If all attempts fail, set result to None
    return results

# Example usage:
urls = [
    "https://example.com",
    "https://invalid-url.com",
    "https://httpbin.org/status/500"  # This URL will return a 500 Internal Server Error
]

downloaded_content = download_content(urls)
for url, content in downloaded_content.items():
    if content:
        print(f"Content downloaded from {url}: {len(content)} bytes")
    else:
        print(f"Failed to download content from {url}")
