To run the application, do the following steps:

- Clone or download the repository
- Open a terminal in the repository folder
- Download the needed libraries:
```
pip install Flask python-dotenv cryptography
```
- Run the script to generate an encryption key in a .env file
    - Note: You only need to run this once. If you run it again, please delete all existing users from users.txt as they cannot be decrypted with the new encryption key.
```
python ./gen_key.py
```
- Run the server
```
python ./server.py
```
- Test the server endpoint /signup using the test.rest file
    - Download the [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) VSCode extension
    - Open the test.rest file
    - Click "Send Request" above the example HTTP requests
        - 200 Status means the request worked as intended

The main branch needs user login info to be encrypted. There are comments in the code starting with 
```
# TODO: ...
```
to give hints where to add or modify the code. To see the solution, look at the solution branch.