from service import *
import pytest

def test_status_codes():
  assert read_resp.status_code == 200, "Status code should be 200"
  assert download_resp.status_code == 200, "Status code should be 200"

def test_verify_api_endpoint():
  assert requests.get(url).content == b'Everything is working!', "Should return b'Everything is working!'"

def test_verify_requests():
  assert download_resp.request.body == download_data, "Should return {action:download}"
  assert read_resp.request.body == read_data, "Should return {action:read}"


if __name__ == "__main__":
  test_status_codes()
  test_verify_api_endpoint()
  test_verify_requests()
  