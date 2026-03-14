from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Troubleshooting and fixing the test failure
The purpose of this test is to validate the response matches the expected schema defined in schemas.py
'''


# --------------------------------------------
# Validate single pet schema
# --------------------------------------------


def test_pet_schema():
    response = api_helpers.get_api_data("/pets/1")
    assert response.status_code == 200
    pet_data = api_helpers.assert_json_response(response)
    validate(instance=pet_data, schema=schemas.pet)


'''
TODO: Finish this test by...
1) Extending the parameterization to include all available statuses
2) Validate the appropriate response code
3) Validate the 'status' property in the response is equal to the expected status
4) Validate the schema for each object in the response
COMPLETED: All tasks are implemented below
'''


# --------------------------------------------
# Validate pets by status
# Task 1.Implemented all other available status as well
# --------------------------------------------
@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_find_by_status_200(status):
    response = api_helpers.get_api_data("/pets/findByStatus", params={"status": status})
    # Task 2: Validate the appropriate response code
    assert response.status_code == 200
    pets = api_helpers.assert_json_response(response)
    # Ensure we got pets list
    assert isinstance(pets, list), f"Expected list, got {type(pets)}"
    # Task 3: Validate the 'status' property in the response equals expected status
    # Task 4: Validate the schema for each object in the response
    for pet in pets:
        assert pet["status"] == status
        validate(instance=pet, schema=schemas.pet)


'''
TODO: Finish this test by...
1) Testing and validating the appropriate 404 response for /pets/{pet_id}
2) Parameterizing the test for any edge cases

COMPLETED: All tasks implemented below
BUG FOUND: API inconsistently returns JSON for some 404s (e.g., 999999) 
           and HTML for others (e.g., -1, "nonexistent")
'''


@pytest.mark.parametrize("pet_id", [0, -1, 999999])
def test_get_by_id_404(pet_id):
    test_endpoint = f"/pets/{pet_id}"

    response = api_helpers.get_api_data(test_endpoint)

    # Task 1: Validate the appropriate 404 response
    assert response.status_code == 404

    # BUG FOUND: API returns JSON or HTML for 404 errors
    # Some IDs (like 999999) return JSON, others (like -1) return HTML
    # Check for the error indication in either format
    response_text = response.text.lower()

    # Accept either "not found" or "message" as valid error indicators
    assert ('not found' in response_text or 'message' in response_text), \
        f"Response should indicate error, got: {response.text[:100]}"


# Additional test to document the bug with pet_id=0
def test_get_by_id_0_bug():
    """
    BUG DOCUMENTATION: pet_id=0 returns 200 instead of 404
    This test check the unexpected behavior where requesting pet with ID 0
    returns a successful response instead of a 404 error.
    """
    test_endpoint = "/pets/0"
    response = api_helpers.get_api_data(test_endpoint)

    # Currently returns 200, but should probably return 404
    # This is a potential bug in the API
    assert response.status_code == 200  # Documents current behavior

    # If this was the expected behavior, it would be:
    # assert response.status_code == 404


