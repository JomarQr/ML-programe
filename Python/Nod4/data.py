import requests

def fetch_data():
    PARAMETRS = {"amount": 3, "type": "boolean", "category": 18}
    url = "https://opentdb.com/api.php"
    response = requests.get(url, params=PARAMETRS)
    response.raise_for_status()
    data = response.json()
    return data["results"]

if __name__ == "__main__":
  data = fetch_data()
  print("Dati no API: ")
  print(data)
