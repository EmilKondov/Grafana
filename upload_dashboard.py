import requests
import json

# Grafana API URL
grafana_url = 'https://ekondov96.grafana.net/api/dashboards/db'

# Grafana API Key
api_key = '2f6093e3-1a52-4024-b3ef-ce96c9e663eb'

# Read the dashboard JSON
with open('dashboard.json', 'r') as f:
    dashboard_json = json.load(f)

# Payload for Grafana API
payload = {
    "dashboard": dashboard_json,
    "overwrite": True,
}

# Headers for Grafana API
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}',
}

# Upload the dashboard
response = requests.post(grafana_url, headers=headers, data=json.dumps(payload))

if response.status_code == 200:
    print('Dashboard uploaded successfully')
else:
    print(f'Failed to upload dashboard: {response.status_code}')
    print(response.json())
