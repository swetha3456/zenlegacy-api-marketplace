import os, random

def generate_code(project_id):
    code = '''from fastapi import FastAPI

app = FastAPI()

@app.get("/1234/")
def read_root():
    return {"Hello": "World"}

@app.get("/1234/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}'''

    return code

def deploy_code():
    project_id = str(random.randint(100000, 999999))
    code = generate_code(project_id)
    os.mkdir(project_id)
    os.chdir(project_id)

    with open("main.py", "w") as f:
        f.write(code)
    
    os.system("uvicorn main:app --host 0.0.0.0 --port 8080 --reload")

if __name__ == "__main__":
    deploy_code()