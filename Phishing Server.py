from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

# Route to handle the POST request
@app.route('/updateEmail', methods=['POST'])
def update_email():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        email_or_phone = data.get('newValue')

        # You can process or store the email/phone here
        print(f"Received email/phone: {email_or_phone}")

        # Respond with a success message
        return jsonify({"message": "Data received successfully"}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Something went wrong"}), 400

@app.route('/enterPassword', methods=['GET', 'POST'])
def enter_password():
    if request.method == 'POST':
        password = request.form['password']
        # Process password as needed
        return "Password updated!"
    return render_template('password.html')

if __name__ == '__main__':
    # Run the app on port 5000
    app.run(debug=True, port=5000)