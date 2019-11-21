from flask import Flask, render_template, request, jsonify
import time
import solenoid
from flask_basicauth import BasicAuth

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'greenhouse'
app.config['BASIC_AUTH_PASSWORD'] = 'uofdjesuit'

basic_auth = BasicAuth(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Encrypt') == 'Encrypt':
            # pass
            print("Encrypted")
        elif  request.form.get('Decrypt') == 'Decrypt':
            # pass # do something else
            print("Decrypted")
        else:
            # pass # unknown
            return render_template("index.html")
    elif request.method == 'GET':
        # return render_template("index.html")
        print("No Post Back Call")
    return render_template('index.html')
   
@app.route("/settings", methods=['GET', 'POST'])
def settings():
    return render_template("settings.html")
    
@app.route("/api/info")
def api_info():
    info = {
        "time": time.time()
    }
    return jsonify(info)
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')