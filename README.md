# Python API Practice Project (Flask & FastAPI)

This repository contains simple backend API examples built using **Flask** and **FastAPI** for learning and practice purposes.

---

## Tech Stack
- Python
- Flask
- FastAPI
- Uvicorn

---

## Setup Instructions

### 1. Create Virtual Environment
```bash
python -m venv venv
````

### 2. Activate Virtual Environment (Windows)
```bash
venv\Scripts\activate
````

### 3. Install Dependencies

- Flask Installation
```bash
pip install flask
````

- FastAPI Installation
```bash
python -m pip install "fastapi[standard]"
````

---

## Project 

### 1. Ping API

- A simple API used to verify that the server is running correctly and returns 'Welcome' and also 'ping...' message in another URL.
- Framework Used : Flask
- Run the Weather API :
````
    python ping.py
````

### 2. Weather API

- A REST API that performs CRUD operations on weather data.
- Framework Used : FastAPI
- Run the Weather API : 
````
    fastapi dev weather.py
````
or
````
    uvicorn weather:app --reload
````



