# QR Code Validator Using Finite Automata

A Python-based project that validates QR code data using Deterministic Finite Automata (DFA).  
The system analyzes QR code bitstreams, verifies their structure, and extracts useful information such as bank payment details or WiFi credentials.

The project also generates visual DFA diagrams to illustrate how QR code validation works using automata theory.

## Features

- QR code structure validation using DFA
- Extraction of encoded QR information
- Supports different QR content types:
  - Bank payment QR codes (account name, account number, account type)
  - WiFi QR codes (SSID and password)
- Automatic generation of DFA state diagrams
- Visualization using Graphviz

## Technologies Used
- Python
- Graphviz
- Finite Automata (Model of Computation concept)
- 
## How It Works

1. The program reads QR code data.
2. The DFA processes the QR bitstream step-by-step.
3. Each state transition validates a part of the QR structure.
4. If the input reaches an **accept state**, the QR code is considered valid.
5. The system extracts encoded information such as:

- Bank account owner name
- Account number
- Account type
- WiFi network name (SSID)
- WiFi password

## Installation

### 1 Install Graphviz

Download and install Graphviz:
https://graphviz.org/download/

### 2 Install Python dependencies
pip install -r requirements.txt

## Run the Project
python qr_dfa_validator.py
After running, the program will generate DFA diagrams:
qr_dfa_full.png
qr_dfa_presentation.png

## Example Output

Example extracted QR information:
QR Type: Bank Payment
Owner Name: John Doe
Account Number: 123456789
Account Type: Savings

Example WiFi QR:
QR Type: WiFi
SSID: MyHomeWifi
Password: mypassword123
Security: WPA2

## DFA Visualization

The project generates DFA diagrams representing the validation process.

Example diagram:

- Start State
- Mode Validation
- Length Validation
- Data Processing
- Accept / Reject State


 Learning Objectives

This project demonstrates:

- Application of **Finite Automata in real-world systems**
- **QR code data structure validation**
- **Graph visualization using Graphviz**
- Integration of **Model of Computation concepts with Python**

  
 Author
Suyog Karki  
BSc Information Technology (Data Science)
