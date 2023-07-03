import requests
import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
import json
import pandas as pd
load_dotenv()
api = os.getenv('JIRA_API')
username = os.getenv('JIRA_USERNAME')
api_url = "https://agencypmg.atlassian.net/rest/api/2/search"
headers = {
    "Authorization": api,
    "Content-Type": "application/json"
}
payload = {
    "jql": 'project = "ALLI"',
    "maxResults": 1000,
}
auth = HTTPBasicAuth(username,api)
headers = {
  "Accept": "application/json"
}
response = requests.request(
   "GET",
   api_url,
   headers=headers,
   auth=auth,
   params=payload
)
data = json.loads(response.text)
issues = data["issues"]
for issue in issues:
    issue_key = issue["key"]
    issue_summary = issue["fields"]["summary"]
    issue_description = issue["fields"]["description"]
    issue_story = issue["fields"].get("customfield_10023")