#!/usr/bin/env python3
"""
Script to print the location of a GitHub user
"""

import requests
import sys
import time


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    # حالة: المستخدم غير موجود
    if response.status_code == 404:
        print("Not found")

    # حالة: rate limit exceeded
    elif response.status_code == 403:
        reset_time = response.headers.get("X-RateLimit-Reset")

        if reset_time:
            current_time = int(time.time())
            reset_time = int(reset_time)

            minutes = (reset_time - current_time) // 60
            print("Reset in {} min".format(minutes))
        else:
            print("Forbidden")

    # الحالة الطبيعية
    else:
        data = response.json()
        print(data.get("location"))
