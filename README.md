To run the application, do the following steps:

- Clone or download the repository
- Open a terminal in the repository folder
- Download the needed libraries:
```
pip install Flask python-dotenv cryptography
```
- Run the script to generate an encryption key in a .env file
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