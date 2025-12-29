import json
import os
import typer

app = typer.Typer()
FILE_NAME = "data.txt"
@app.command()
def add_obj(data: str):
    """
    Add a JSON object with name, age, and city to the local file.
    Example: '{"name":"Lea","age":25,"city":"Tel Aviv"}'
    """
    try:
        parsed  = json.loads(data)
    except json.JSONDecodeError:
        typer.echo("Invalid JSON")
        raise typer.Exit(code=1)
    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(json.dumps(parsed) + "\n")
    typer.echo("Person added successfully!")

@app.command()
def get_last_ten():
    if not os.path.exists(FILE_NAME):
        typer.echo("File does not exist")
        raise typer.Exit(1)

    with open(FILE_NAME, encoding="utf-8") as f:
        for line in f.readlines()[-10:]:
            try:
                typer.echo(json.loads(line))
            except json.JSONDecodeError:
                typer.echo("Invalid JSON line")

if __name__ == "__main__":
    app()

