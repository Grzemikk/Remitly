# JSON IAM Policy Verifier

## Description
This tool verifies AWS IAM Role policy JSON files, ensuring they don't grant overly broad permissions by checking if any policy's `Resource` field contains a single asterisk (`'*'`).

## Setup
1. Clone this repository:
   ```bash
    git clone https://github.com/Grzemikk/Remitly.git

## Usage
To verify a JSON file, navigate to the project directory and run:
python verify_json_policy.py <path_to_json_file>

## Running Tests
To ensure the program operates correctly, run the provided tests:
python -m unittest discover
