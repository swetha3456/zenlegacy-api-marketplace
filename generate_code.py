from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import re

def get_api_code(user_input):
    code_template = r"""from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

# FastAPI app initialization
app = FastAPI()

# SQLAlchemy database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Database URL from input
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# SQLAlchemy model dynamically generated based on input
{% for model in models %}
class {{ model.name }}(Base):
    __tablename__ = "{{ model.table_name }}"
    id = Column(Integer, primary_key=True, index=True)
    {% for field in model.fields %}
    {{ field.name }} = Column({{ field.type }}, index=True)
    {% endfor %}
{% endfor %}

# Create the database tables
Base.metadata.create_all(bind=engine)

# Pydantic schemas for validation dynamically generated based on input
{% for schema in schemas %}
class {{ schema.name }}(BaseModel):
    {% for field in schema.fields %}
    {{ field.name }}: {{ field.type }}
    {% endfor %}

    class Config:
        orm_mode = True
{% endfor %}

# CRUD operations dynamically generated based on input
{% for operation in operations %}
@app.{{ operation.method }}("{{ operation.path }}", response_model={{ operation.response_model }})
def {{ operation.function_name }}({% if operation.body %}{{ operation.body }}: {{ operation.body_model }}, {% endif %}db: Session = Depends(get_db)):
    {% for line in operation.logic %}
    {{ line }}
    {% endfor %}
    return {{ operation.return_value }}
{% endfor %}
    """

    question_template = f"""
    You are an expert Python API developer. The user needs an API with the following requirements: {user_input}. 
    Generate the complete FastAPI code and nothing else. Ensure there are no syntax errors. Ensure to use double underscores for __tablename__. Do not use "Depends". Here is the code template you need to follow: {code_template}"""

    template = """Question: {question}

    Answer: Let's think step by step."""

    prompt = ChatPromptTemplate.from_template(template)
    model = OllamaLLM(model="llama3")
    chain = prompt | model
    result = chain.invoke({"question": question_template})
    print(result)

    return result

def extract_code(text):
    # Regular expression to capture code between triple backticks
    text = text[text.find("from"):]
    text = text[:text.find("`")]

    return text

if __name__ == "__main__":
    print(extract_code(get_api_code("API for storing and retrieving employee data")))