# FastAPI Demo

This repository contains a FastAPI demonstration project. Follow the instructions below to set up and run the application.

## Prerequisites

- Python 3.13.3 (latest version)
- Git

## Setup Instructions

### 1. Clone the Repository

Git Bash:
```bash
git clone https://github.com/JinLeeGG/FastAPI.git
```
Command Prompt:
```bash
cd FastAPI
```
### 2. Create a Virtual Environment

Open a Command Prompt and run:

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### On Windows:
```bash
cd venv\Scripts
```
```bash
activate.bat
```

#### On macOS/Linux:
```bash
source venv/bin/
```
```bash
activate.bat
```

### 4. Install Dependencies

With the virtual environment activated, install the required packages:

```bash
pip install fastapi
pip install "uvicorn[standard]"
pip install jinja2
```

## Running the Application

1. Make sure you're in the project directory where `main.py` is located
2. Start the application with:

```bash
uvicorn main:app --reload
```

3. The web application will be available at:
   - Main URL: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Interactive API documentation (Swagger UI): [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Alternative API documentation: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Development

The `--reload` flag enables auto-reload, so the server will restart automatically when you make changes to the code.

## API Documentation

FastAPI automatically generates interactive API documentation:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
