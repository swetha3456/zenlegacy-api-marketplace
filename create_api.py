import os
from generate_code import *

def get_generated_code(user_prompt):
    return extract_code(get_api_code(user_prompt))

def deploy_code(user_prompt):
    code = get_generated_code(user_prompt)

    with open("main.py", "w") as f:
        f.write(code)
    
    os.system("uvicorn main:app --host 0.0.0.0 --port 8080 --reload")

if __name__ == "__main__":
    deploy_code("create an api for storing and retrieving employee data")
