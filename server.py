from flask import Flask, request
app = Flask(__name__)
@app.route('/') 
def index():
   headers = request.headers
   return "Request headers:\n" + str(headers)
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=80)