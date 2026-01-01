import requests

def fetch_osm_data(query: str, url: str) -> dict:
    """
    Fetch open geospatial data from Overpass API.
    """
    response = requests.post(url, data={"data": query}, timeout=120)
    response.raise_for_status()
    return response.json()
