import unittest, requests
from src.api_clients import get_location
from unittest.mock import patch

class ApiClientTestCase(unittest.TestCase):

    @patch('src.api_clients.requests.get')
    def test_get_location_returns_expected_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "countryName": "USA",
            "regionName": "FLORIDA",
            "cityName": "MIAMI"
        }
        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "USA")
        self.assertEqual(result.get("region"), "FLORIDA")
        self.assertEqual(result.get("city"), "MIAMI")
        
        # En tests/test_api_client.py (Línea 20)
        mock_get.assert_called_once_with(
            "https://freeipapi.com/api/json/8.8.8.8",
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
        )


    @patch('src.api_clients.requests.get')
    def test_get_location_returns_side_effect(self, mock_get):
        mock_get.side_effect = [
            requests.exceptions.RequestException("API request failed"),
            unittest.mock.Mock(
                status_code=200,
                json=lambda: {
                    "countryName": "USA",
                    "regionName": "FLORIDA",
                    "cityName": "MIAMI"
                }
            )
        ]


        with self.assertRaises(requests.exceptions.RequestException):
            result = get_location("8.8.8.8")

        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "USA")
        self.assertEqual(result.get("region"), "FLORIDA")
        self.assertEqual(result.get("city"), "MIAMI")