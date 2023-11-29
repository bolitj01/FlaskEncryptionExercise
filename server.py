from flask import Flask, request, jsonify
from cryptography.fernet import Fernet

app = Flask(__name__)

# Generate a key for encryption
# In a production application, save this in a secure location
key = Fernet.generate_key()
cipher_suite = Fernet(key)

@app.route('/signup', methods=['POST'])
def signup():
    try:
        # Get data from request
        data = request.json
        username = data['username']
        password = data['password']

        # Encrypt the username and password
        encrypted_username = cipher_suite.encrypt(username.encode())
        encrypted_password = cipher_suite.encrypt(password.encode())

        # Save the encrypted data to a file
        with open('users.txt', 'a') as file:
            file.write(f'{encrypted_username.decode()} {encrypted_password.decode()}\n')

        return jsonify({'status': 'success'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)