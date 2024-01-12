 
# Import necessary libraries
from flask import Flask, render_template, request
import requests

# Create a Flask app
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Define the route for the search results page
@app.route('/search', methods=['POST'])
def search():
    # Get the search term from the request
    search_term = request.form['search_term']

    # Perform a web search for relevant risks
    url = 'https://www.google.com/search'
    params = {'q': search_term + ' risks'}
    response = requests.get(url, params=params)

    # Parse the search results and extract relevant risks
    risks = []
    for result in response.json()['items']:
        risks.append({
            'title': result['title'],
            'description': result['snippet']
        })

    # Render the results page with the extracted risks
    return render_template('results.html', risks=risks)

# Run the app
if __name__ == '__main__':
    app.run()
