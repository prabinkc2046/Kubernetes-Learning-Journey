#!/usr/bin/python3
import requests
import time
import random
import string
from concurrent.futures import ThreadPoolExecutor

def generate_random_username():
    return "user" + ''.join(random.choices(string.ascii_lowercase, k=4))

def generate_random_password():
    return "pass" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))

def submit_form_to_localhost(username, password, result_list):
    try:
        data = {
            "existing_user": "no",
            "username": username,
            "password": password
        }

        response = requests.post('http://192.168.49.2:30080', data=data)
        status_code = response.status_code
        print(f"Request Status Code: {status_code}")

        # Append the result to the result_list
        result_list.append(status_code)

    except requests.RequestException as e:
        print(f"Request to localhost failed: {e}")
        result_list.append(None)

if __name__ == "__main__":
    try:
        num_requests = 5
        total_requests = 0
        successful_requests = 0
        result_list = []

        while True:
            total_requests += num_requests
            with ThreadPoolExecutor(max_workers=num_requests) as executor:
                usernames = [generate_random_username() for _ in range(num_requests)]
                passwords = [generate_random_password() for _ in range(num_requests)]
                executor.map(submit_form_to_localhost, usernames, passwords, [result_list] * num_requests)

            # Count the number of successful requests
            successful_requests += result_list.count(200)

            print(f"Success Rate: {successful_requests}/{total_requests}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nRequest loop stopped.")
