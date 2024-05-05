import requests


def google_api():
    google = requests.get('https://www.google.com/')
    return google.status_code, google.reason, google.url, google.is_redirect, google.is_permanent_redirect


print(google_api())
