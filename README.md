# Nutanix Enterprise AI (NAI) Demo Applications

This repository contains two sample applications for demonstrating Nutanix Enterprise AI (NAI):
1. **Standalone Chatbot**: A GUI-based chatbot application built with `tkinter`.
2. **Web Chatbot**: A web-based chatbot application built with `Flask`.

## Prerequisites

Before running the applications, ensure you have the following:
- Python 3.8 or later installed.
- An active NAI API endpoint and API key.
- Required Python dependencies installed (see the `requirements.txt` files in each directory).

## Setup

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-repo/nai-demo-apps.git
   cd nai-demo-apps
   ```

2. Set up your environment variables:
   ```bash
   export NAI_ENDPOINT=<your_nai_endpoint>
   export NAI_API_KEY=<your_nai_api_key>
   ```

Replace <your_nai_endpoint> and <your_nai_api_key> with your NAI API endpoint and API key.

## Standalone Chatbot
The standalone chatbot is a desktop application built with tkinter.

### Installation
1. Navigate to the standalone directory:
```
cd standalone
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```

### Usage
1. Run the chatbot application:
```
python chatbot.py
```
2. A GUI window will open. Enter your message in the input field and click the "Send" button to interact with the chatbot.

## Web Chatbot
The web chatbot is a web application built with Flask.

### Installation
1. Navigate to the web directory:
```
cd web
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```
### Usage
1. Run the Flask application:
```
python app.py
```
2. Open your web browser and navigate to http://127.0.0.1:5000.
3. Enter your message in the input box and click the "Send" button to interact with the chatbot.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Troubleshooting
* Ensure the .env file is correctly configured with your NAI API endpoint and API key.
* If you encounter SSL verification issues, you can disable SSL verification by modifying the requests.post call in the code (verify=False is already set in the examples).

## Contributing
Feel free to submit issues or pull requests to improve this project.

## Acknowledgments
This project demonstrates the capabilities of Nutanix Enterprise AI (NAI) and is intended for educational and demonstration purposes.