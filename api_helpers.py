import requests

# base_url = 'http://localhost:5000'
base_url = 'http://127.0.0.1:5050'


# --------------------------------------------
# Helper function: safe JSON parsing
# --------------------------------------------

def safe_json(response):
    """
    Safely return JSON from a response.
    If response is not JSON, return None.
    """
    try:
        return response.json()
    except ValueError:
        return None


# --------------------------------------------
# Helper: validate response is JSON
# --------------------------------------------


def assert_json_response(response):
    """
    Ensure that response is JSON.
    Raises AssertionError if not JSON.
    """
    if response.headers.get("Content-Type", "").lower() != "application/json" and safe_json(response) is None:
        raise AssertionError(f"Expected JSON response, got:\n{response.text}")
    return safe_json(response)


# GET request
def get_api_data(endpoint, params=None, headers=None):
    if params is None:
        params = {}
    if headers is None:
        headers = {"Accept": "application/json"}  # Force JSON
    response = requests.get(f'{base_url}{endpoint}', params=params, headers=headers)
    return response


# POST request
def post_api_data(endpoint, data, headers=None):
    if headers is None:
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
    response = requests.post(f'{base_url}{endpoint}', json=data, headers=headers)
    return response


# PATCH request
def patch_api_data(endpoint, data, headers=None):
    if headers is None:
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
    response = requests.patch(f'{base_url}{endpoint}', json=data, headers=headers)
    return response
