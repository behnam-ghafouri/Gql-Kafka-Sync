import requests

def fetch_company_data(company_id):
    try:
        response = requests.get(f"http://identity-service:8000/api/companies/{company_id}/")
        if response.status_code == 200:
            return response.json() # Return the whole dictionary
    except Exception:
        return None
    return None