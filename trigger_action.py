import git
import datetime
import time
from git import Repo

repo = Repo('.')
headcommit = repo.head.commit
commit_date = time.gmtime(headcommit.committed_date)
today = datetime.datetime.today()
if (commit_date.tm_year, commit_date.tm_mon, commit_date.tm_mday) == (today.year, today.month, today.day):
    print("Yep")
