from flask import Flask, request, jsonify
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

# Generate a key for encryption
# In a production application, save this in a secure location
# Use the key from the environment variable
key = os.getenv("ENCRYPTION_KEY").encode()
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

        # Decrypt and print all user data from the file
        print_users()

        return jsonify({'status': 'success'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400

def print_users():
    print('User List:')
    try:
        with open('users.txt', 'r') as file:
            for line in file:
                encrypted_username, encrypted_password = line.strip().split()
                decrypted_username = cipher_suite.decrypt(encrypted_username.encode()).decode()
                decrypted_password = cipher_suite.decrypt(encrypted_password.encode()).decode()
                print(f'Username: {decrypted_username}, Password: {decrypted_password}')
    except FileNotFoundError:
        print("The 'users.txt' file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    app.run(debug=True)