import requests

def getListLogApi(urls):
    results = []
    for url in urls:
        try:
            # Fetch data from the API
            response = requests.get(url)
            
            # Check if the request was successful
            if response.status_code == 200:
                # Parse JSON response
                data = response.json()
                results.append((data, None))
            else:
                results.append((None, f"Failed to fetch data from {url}. Status code: {response.status_code}"))
        except requests.RequestException as e:
            results.append((None, f"Error fetching data from {url}: {str(e)}"))
    return results
