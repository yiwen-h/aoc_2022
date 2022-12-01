import requests
import os

COOKIE = os.environ.get("SESSION")

def get_data(day):
    response = requests.get(f'https://adventofcode.com/2022/day/{day}/input',
                            cookies={'session': COOKIE})
    raw_data = response.content.decode('UTF-8')
    return raw_data
