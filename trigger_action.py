import os
import datetime
import time
from git import Repo
import requests

repo = Repo('.')
headcommit = repo.head.commit
commit_date = time.gmtime(headcommit.committed_date)
today = datetime.datetime.utcnow()
if (commit_date.tm_year, commit_date.tm_mon, commit_date.tm_mday) == (today.year, today.month, today.day):
    print('found commit')
    headers = {
        'Accept': 'application/vnd.github.everest-preview+json',
        'Content-Type': 'application/json',
    }

    data = '{"event_type": "build_application"}'

    USERNAME = os.environ.get('PAT_USERNAME')
    TOKEN = os.environ.get('TOKEN')
    REPO = os.environ.get('REPO')
    response = requests.post(
        'https://api.github.com/repos/{}/{}/dispatches'.format(USERNAME, REPO),
        headers=headers, data=data, auth=(
            USERNAME,
            TOKEN
        )
    )
    print(response.status_code, response.content)
else:
    print('No commit')
