# REST API Test Framework with Pytest
#AUTHOR : BIVASH NAYAK
#EMAIL : iambivash.bn@gmail.com
## Overview
This is a lightweight and extensible test framework built with `pytest` to validate REST API endpoints. It supports common HTTP methods (GET, POST, PUT, DELETE) and includes reusable fixtures for API client setup and test data. The framework is designed to be easily customized for testing any RESTful API by adjusting the base URL and test cases.

- **Language**: Python
- **Dependencies**: `pytest`, `requests`
- **License**: MIT License

## Features
- Supports testing GET, POST, PUT, and DELETE requests.
- Reusable fixtures for API client and test data.
- Assertions for HTTP status codes and response JSON.
- Extensible for custom endpoints and scenarios.
- Verbose test output with `pytest -v`.

## Prerequisites
- Python 3.8 or higher.
- `pip` for package installation.

## Installation
1. Clone the repository or copy the `test_api_framework.py` file:
   ```bash
   git clone <repository-url>  # Replace with actual URL if hosted
   cd <repository-directory>
   ```
2. Install dependencies:
   ```bash
   pip install pytest requests
   ```

## Configuration
- Update the `BASE_URL` variable in `test_api_framework.py` with your API's base URL (e.g., `https://api.example.com` or `http://localhost:5000`).
- Modify `HEADERS` if your API requires specific headers (e.g., authentication tokens).
- Adjust `test_data` in the fixture to match your API's expected payload.

## Usage
1. Save the test script as `test_api_framework.py`.
2. Run the tests:
   ```bash
   pytest test_api_framework.py -v
   ```
   - `-v`: Enables verbose output.
   - `-s`: Shows print statements (if added).
3. Example output:
   ```
   ============================= test session starts =============================
   collected 5 items

   test_api_framework.py::test_get_endpoint PASSED
   test_api_framework.py::test_post_endpoint PASSED
   test_api_framework.py::test_put_endpoint PASSED
   test_api_framework.py::test_delete_endpoint PASSED
   test_api_framework.py::test_invalid_endpoint PASSED

   =========================== 5 passed in 0.12s =================================
   ```

## Test Cases
- `test_get_endpoint`: Verifies a GET request returns a 200 status and expected data.
- `test_post_endpoint`: Tests a POST request with a 201 status and validates the response.
- `test_put_endpoint`: Checks a PUT request updates data with a 200 status.
- `test_delete_endpoint`: Confirms a DELETE request returns 204 and subsequent GET returns 404.
- `test_invalid_endpoint`: Ensures a 404 is returned for an invalid endpoint.

## Extending the Framework
- **Add New Test Cases**: Create functions prefixed with `test_` for additional endpoints or scenarios.
- **Mock Server**: Use `pytest-mock` to simulate API responses for isolated testing.
- **Environment Variables**: Store `BASE_URL` and `HEADERS` in a `.env` file using `python-dotenv`.
- **Custom Assertions**: Add specific checks for your API's response structure.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support
- **Issues**: Report bugs or suggest features at [issue tracker](https://cyberdudebivash.com/issues) (replace with actual URL if hosted).
- **Contact**: For questions, reach out via [example@email.com](mailto:iambivash.bn@gmail.com).

## Acknowledgments
- Built with `pytest` and `requests` for robust testing.
- Inspired by best practices in API testing and automation.



*Last Updated: 01:23 PM IST, Tuesday, July 08, 2025*