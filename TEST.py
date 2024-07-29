import requests


def test_api_connection():
    url = "https://api.example.com/data"
    headers = {
        'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises a HTTPError if the HTTP request returned an unsuccessful status code

        # If the API call is successful
        print(f"Status Code: {response.status_code}")
        print("Response JSON:")
        print(response.json())
        return True

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return False
    except Exception as err:
        print(f"Other error occurred: {err}")
        return False


if __name__ == "__main__":
    if test_api_connection():
        print("API connection successful.")
    else:
        print("Failed to connect to the API.")
