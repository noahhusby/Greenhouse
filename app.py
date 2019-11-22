from flask import Flask, render_template, request, jsonify
from gpiozero import LED
import time
from solenoid import solenoid
from flask_basicauth import BasicAuth

a=0
solenoid_a= solenoid(4)

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'greenhouse'
app.config['BASIC_AUTH_PASSWORD'] = 'uofdjesuit'

basic_auth = BasicAuth(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    global a
    global solenoid_a
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Encrypt') == 'Encrypt':
            if a==0:
                solenoid_a.enable()
                a=1
            elif a==1:
                solenoid_a.disable()
                a=0
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
