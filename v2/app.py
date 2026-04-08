from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <body style="font-family: Arial; text-align: center; background-color: #e8f4fd;">
        <h1>Payment System - Version 2</h1>
        <div style="background: white; padding: 20px; display: inline-block; border-radius: 10px;">
            <p>Feature: Validation Logic</p>
            <input type="number" id="amt" placeholder="Enter Amount ($)">
            <button onclick="alert('Validating Payment... Verification Successful!')" 
                    style="background: orange; color: white;">Validate & Pay</button>
        </div>
    </body>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)