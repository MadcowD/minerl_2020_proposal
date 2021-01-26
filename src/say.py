from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# @app.route('/say', methods=['GET', 'POST']) #allow both GET and POST requests
# def say():
#     if request.method == 'POST':
#         print(request.args)
#     return "sup"
if __name__ == '__main__':
    print("hi")
    app.run(debug=True, host="localhost", port=80) #run app in debug mode on port 5000