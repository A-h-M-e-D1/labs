from flask import request,Flask

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def main():
    if request.method == 'GET':
        return 'welcome to my server'
    elif request.method == 'POST':
        data = request.get_json()
    return {'message': 'Received your request!', 'data': data}

if __name__ == '__main__':
    app.run(debug=True)