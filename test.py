from service import *

def run_tests():
  assert read_resp.status_code == 200, "Status code should be 200"

  assert download_resp.status_code == 200, "Status code should be 200"

  assert requests.get(url).content == b'Everything is working!', "Should return b'Everything is working!'"

  assert download_resp.request.body == download_data, "Should return {action:download}"

  assert read_resp.request.body == read_data, "Should return {action:read}"


if __name__ == "__main__":
  run_tests()
  