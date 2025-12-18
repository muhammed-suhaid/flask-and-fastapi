from flask import Flask
app = Flask(__name__)

#----- Home -----#
@app.route('/')
def home():
    return "Welcome"

#----- Get Ping Message -----#
@app.route('/ping')
def ping():
    return "Ping..."

#----- Running the application -----#
if __name__ == '__main__':
    # app.run()
    app.run(debug=True)