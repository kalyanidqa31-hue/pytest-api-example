Assessment completed by Kalyani

Tasks Completed

1.Fix-api_helpers.py
a.I have Updated base url in(api_helpers.py- line 4)
Original base_url = 'http://localhost:5000'
Updated base_url = 'http://127.0.0.1:5050'
b.Added safe_json() Helper Function:Safely attempts to convert the API response to JSON.
Prevents test failures caused by non-JSON responses (HTML, text, or error pages).
c.Added assert_json_response() Validation Function
Verifies that the API response is valid JSON.
Checks both:Content-Type header & JSON parsing result.
d.Added Default Headers to GET Requests:Explicitly requests JSON responses from the API.
e.Added Request Headers for POST and PATCH:
Ensures request body is sent as JSON.
Ensures server returns JSON response.
f.Improved Parameter Handling:Avoids mutable default arguments, which can cause unexpected behavior in Python.

2. Fix – test_pet_schema
Status: Completed
While running the schema validation test, I identified that the name field in schemas.py was incorrectly defined as an integer.
Issue: "type": "integer" used for name
Fix: Updated to "type": "string" (schemas.py – line 12)
Outcome: test_pet_schema now passes successfully

3. Extend – test_find_by_status_200
Status: Completed
Enhanced the existing test to improve validation coverage.
Updates made:
Parameterized test for all statuses:
available
sold
pending
Added response status code validation (200)
Verified each pet object’s status value
Applied schema validation for every record in the response
Result: All parameterized scenarios are passing.


4. Complete – test_get_by_id_404
Status:Completed
Implemented negative testing for invalid pet IDs.
Enhancements include:
404 response validation
Parameterized edge cases:
999999
-1
"nonexistent"
Error message validation supporting both JSON and HTML responses
Additional test created to highlight pet_id = behavior inconsistency
Result:All edge-case tests are passing.


5. PATCH Test – Store Orders
Status:Completed (limitations documented)
Work completed:
Created test_patch_order_by_id
Implemented pytest fixture for order data
Added optionalOrder schema in schemas.py
Designed alternative flow using POST setup before PATCH
Covered negative scenario for non-existent order IDs
Observation:PATCH endpoint is currently not functional; tests are conditionally skipped.

Bugs Identified During Testing
Bug 1 — Schema Type Mismatch (Critical) — Fixed
File: schemas.py (line 12)
Problem: name defined as integer instead of string
Impact: Schema validation failure
Resolution: Corrected data type to string

Bug 2 — Pet ID 0 Returns Incorrect Status
Endpoint: GET /pets/0
Expected: 404 Not Found
Actual: 200 OK with pet data
Indicates ID 0 is treated as valid, which is inconsistent.

Bug 3 — Inconsistent 404 Response Format
Endpoint: GET /pets/{invalid_id}
Observed:
Some IDs return JSON:
{"message": "Pet not found"}
Others return HTML error pages
Impact: Error parsing cannot rely on a consistent structure.

Bug 4 — PATCH Endpoint Not Implemented
Endpoint: PATCH /store/order/{order_id}
Behavior: Returns 404
Possible reasons:
Endpoint not implemented
Requires prior order creation
Tests skip gracefully while documenting expected behavior.

Test Execution Summary
Total Tests: 8+5=13
Passed: 10
Skipped: 2 (PATCH unavailable)
Failed: 1(due to  assertion error : assert 200 == 404)
Coverage Achieved:
Schema validation
Status filtering
404 negative scenarios
Edge-case handling
Response validation
Fixtures & parameterization
Bonus tasks (Order schema, PATCH tests)

Technical Stack Used are
pytest
pytest-html
pyhamcrest
jsonschema
requests
flask_restx

Implementation Notes:
1.Completed all TODO items across test files
2.Tests aligned with actual API behavior
3.Defects documented with expected vs actual results
4.Alternative approaches added where endpoints were unavailable
5.Followed pytest and Python testing best practices

Overall Status:Assessment completed and ready for review.
