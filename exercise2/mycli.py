import json
import os
import typer

app = typer.Typer()
FILE_NAME = "data.txt"

def add_person_to_file(obj: dict):
    all_data = json.load(open(FILE_NAME)) if os.path.exists(FILE_NAME) else []
    all_data.append(obj)
    with open(FILE_NAME, "w") as f:
        json.dump(all_data, f, indent=4)
    print("Person added successfully!")

@app.command()
def add_obj(person: str):
    """
    Add a JSON object with name, age, and city to the local file.
    Example: '{"name":"Lea","age":25,"city":"Tel Aviv"}'
    """
    person_obj = json.loads(person)
    add_person_to_file(person_obj)

if __name__ == "__main__":
    app()

