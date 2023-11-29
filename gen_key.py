from cryptography.fernet import Fernet
from dotenv import dotenv_values, set_key

# Load current .env file into a dictionary
config = dotenv_values(".env")

# Generate a key and print it
key = Fernet.generate_key()
print(key.decode())

# Add the key to the config dictionary
config["ENCRYPTION_KEY"] = key.decode()

# Write changes back to .env file
for key, value in config.items():
    set_key(".env", key, value)

print("Saved to .env file as ENCRYPTION_KEY")