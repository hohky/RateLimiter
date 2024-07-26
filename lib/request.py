import requests
import time
import threading
import sys

from lib.log import *


url = input('URL -> ').strip() or None
requests_per_second = int(input('Requests per second -> ').strip()) or 5
interval = 1 / requests_per_second


stop_execution = threading.Event()


def send_request():
    try:
        response = requests.get(url)
        if response.status_code in [429, 403]:
            print(warning(f"Rate limit hit in {c.LIGHTGREEN_EX}{requests_per_second}/requests per second{c.RESET} with {c.LIGHTBLUE_EX}{interval}{c.RESET} of interval"), end="\r")
            stop_execution.set()
        elif response.status_code == 200:
            print(sending(f"Sending {c.BLUE}{requests_per_second}{c.RESET} requests/s with interval {c.LIGHTBLUE_EX}{interval}{c.RESET}"), end="\r")
            # animation_wait(f"Sending {c.BLUE}{requests_per_second}{c.RESET} requests/s with interval {c.LIGHTBLUE_EX}{interval}{c.RESET}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")


def main():
    while not stop_execution.is_set():
        threads = []
        for _ in range(requests_per_second):
            thread = threading.Thread(target=send_request)
            thread.start()
            threads.append(thread)
        
        for thread in threads:
            thread.join()
        
        if stop_execution.is_set():
            break
        
        time.sleep(interval)

