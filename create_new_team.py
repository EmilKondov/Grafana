import requests
import json
import re

#Email validation
def is_valid_email(email):
    #Regular expression for validating an email address
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Function to create a new team
def create_team(team_name, team_email, grafana_url, api_key):
    # Team details
    team_details = {
        "name": team_name,
        "email": team_email
    }

    # Headers for Grafana API
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }

    # Create the new team
    response = requests.post(grafana_url, headers=headers, data=json.dumps(team_details))

    if response.status_code == 200:
        print('Team created successfully')
    else:
        print(f'Failed to create team: {response.status_code}')
        print(response.json())

def main():
    # User input for team details
    team_name = input("Enter the team name: ")
    while True:
        team_email = input("Enter the team email: ")
        if is_valid_email(team_email):
            break
        else:
            print("Invalid email format. Please try again.")

    # Grafana API URL for creating teams
    grafana_url = 'https://ekondov96.grafana.net/org/teams'

    # Grafana API Key
    api_key = 'sa-1-emil-kondov-c438accd-e7b6-436b-9287-cf2f6a0b05ad'

    # Create the team
    create_team(team_name, team_email, grafana_url, api_key)

if __name__ == "__main__":
    main()
