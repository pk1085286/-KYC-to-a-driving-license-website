from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/verify-kyc', methods=['POST'])
def verify_kyc():
    # Get user details from the request
    user_id = request.form['user_id']
    name = request.form['name']
    dob = request.form['dob']
    mobile_number = request.form['mobile_number']
    
    # Verify user's identity using the mobile KYC API
    mobile_kyc_api_url = "https://example.com/mobile-kyc-api/verify"
    params = {
        "user_id": user_id,
        "name": name,
        "dob": dob,
        "mobile_number": mobile_number
    }
    response = requests.post(mobile_kyc_api_url, json=params)
    
    # Return the verification result to the driving license website
    if response.status_code == 200:
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'failure'})

if __name__ == '__main__':
    app.run(debug=True)
