from flask import Flask,request
import requests

app = Flask(__name__)

@app.route('/')
def main():
    return "Hello SSRF"

@app.route('/fetch_url')
def fetch_url():
    url = request.args.get('url')

    if not url:
        return "Plase provide url paramster",400
    try:
        content =request.get(url).text
        return content
    except Exception as e:
        return "Error fetching URL: {e}",500
    
if __name__ == "__main__":
    app.run(debug=True)
    
