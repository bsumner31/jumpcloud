import requests
from requests.structures import CaseInsensitiveDict

url = "https://1df32474-ea60-4742-8cb9-a424d74647c0.mock.pstmn.io/manage_file"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/json"

read_data = """
{
  "action":"read"
}
"""

download_data = """
{
  "action":"download"
}
"""

read_resp = requests.post(url, headers=headers, data=read_data)
download_resp = requests.post(url, headers=headers, data=download_data)

def check_status_codes():
  if read_resp.status_code != 200:
    print("could not return request for read payload, status code: " + str(read_resp.status_code))

  if download_resp.status_code != 200:
    print("could not return request for download payload, status code: " + str(read_resp.status_code))

def display_payload_request():
  print(f"The request body for the read payload located at {url} is: \n" + read_resp.request.body)
  print(f"The request body for the download payload located at {url} is: \n" + download_resp.request.body)

def validate_and_return_read_payload():
  if read_resp.request.body == read_data :
    print("read_data payload confirmed...")
    print("Returning file contents: " + str(read_resp.content))
  else:
    print("read_data payload does not match request")

def validate_and_return_download_payload():
  if download_resp.request.body == download_data :
    print("download_data payload confirmed")
    content_url = "https://www.learningcontainer.com/wp-content/uploads/2020/04/sample-text-file.txt"
    r = requests.get(content_url, allow_redirects=True)
    open('sample-text-file.txt', 'wb').write(r.content)
    print("Saved file: 'sample-text-file.txt' to current working directory")
  else:
    print("download_data payload does not match request")
  
check_status_codes()
display_payload_request()
validate_and_return_read_payload()
validate_and_return_download_payload()
