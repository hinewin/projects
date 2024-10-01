import requests
import os
from bs4 import BeautifulSoup

# Replace these with your actual login details and URLs
login_url = 'https://www.udemy.com/join/login-popup/'
login_payload = {
    'email': os.environ.get("SITE_EMAIL"),
    'password': os.environ.get("SITE_PASSWORD"),
    'csrfmiddlewaretoken': 'YOUR_CSRF_TOKEN'  # You might need to get this dynamically
}

video_url = 'https://www.udemy.com/course/terraform-beginner-to-advanced/learn/lecture/42537366?start=15#overview'

# Start a session
with requests.Session() as session:
    # Get the login page to get the CSRF token
    response = session.get(login_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract CSRF token if required (this example assumes a CSRF token is needed)
    csrf_token = soup.find('input', attrs={'name': 'csrfmiddlewaretoken'})['value']
    login_payload['csrfmiddlewaretoken'] = csrf_token

    # Perform login
    session.post(login_url, data=login_payload)

    # Fetch the video page
    response = session.get(video_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Assuming the title of the video is within a <title> tag
        title = soup.title.string
        print(f"Video Title: {title}")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")