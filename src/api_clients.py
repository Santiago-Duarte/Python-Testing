import requests

def get_location(ip):
    url = f"https://freeipapi.com/api/json/{ip}"
    # Simulamos un navegador web real
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for HTTP errors
    data = response.json()
    return {
        "country": data.get("countryName"),
        "region": data.get("regionName"),
        "city": data.get("cityName"),
    }