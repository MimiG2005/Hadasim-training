from fastapi import FastAPI
import os
import json
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/addObj")
def add_data(data: dict):
    with open("data.txt", "a",encoding="utf-8") as file:
        json.dump(data, file)
        file.write("\n")

    return {"message": "Data added successfully", "data": data}    

@app.get("/getObj")
def get_data():
    filename = "data.txt"
    
    if not os.path.exists(filename):
        return {"message": "No data found", "data": []}

    with open(filename, "r", encoding="utf-8") as file:
        data = file.readlines()
        last_10 = data[-10:]
    
    return {"message": "Last messages retrieved successfully", "data": last_10}


