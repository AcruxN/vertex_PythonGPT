# PythonGPT

PythonGPT is an interactive website designed to teach beginners how to code in Python

## Features

- **Python Documentation:** Step-by-step tutorials covering Python basics and fundamentals.
- **Hands-On Exercises:** Practical coding questions on Python programming.
- **AI Chatbot Assistance:** Real-time help and feedback from an embedded AI chatbot.

## Getting Started

### Prerequisites

- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
- [Python 3](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/)

### Installation

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/AcruxN/vertex_PythonGPT
   ```

2. **Install Prerequisites & Backend Dependencies**

    - Install [Python](https://www.python.org/downloads/) and [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
    - Install Dependencies

    ```sh
    pip install -r requirements.txt
    ```

    - Verify installation

    ```sh
    python --version
    gcloud --version
    pip list
    ```

3. **Obtain Google Cloud Service Account's Credential File**

    Follow the documentation to create a service account and download the credential file:
    [Google Cloud IAM Documentation](https://cloud.google.com/iam/docs/service-accounts-create)

    - Provide the IAM role "Vertex AI User" to the service account
    - Export to obtain the JSON file

4. **Apply Credential File**

    ```sh
    export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account-key.json"
    gcloud auth list
    ```

5. **Modify Project Details in vertexFunction.py**
    Rename *google_cloud_platform_project_name* from *line 19* to your google cloud project's name

6. **Run The Program**

    ```sh
    python3 main.py
    ```

### Usage

- Navigate to "<http://localhost:5000>" or "<http://127.0.0.1:5000>" with web browser to access the service
- Follow interactive lessons to learn Python programming
- Use the AI chatbot for assistance whenever needed
