from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <body style="font-family: Arial; text-align: center; background-color: #f4f4f4;">
        <h1>Payment System - Version 1</h1>
        <div style="background: white; padding: 20px; display: inline-block; border-radius: 10px;">
            <p>Feature: Enter Payment</p>
            <input type="number" placeholder="Enter Amount ($)">
            <button style="background: blue; color: white;">Submit</button>
        </div>
    </body>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)