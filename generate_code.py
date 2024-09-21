from langchain import PromptTemplate, LLMChain
from transformers import pipeline
from langchain.llms import HuggingFacePipeline

# Load the Hugging Face model using a text-generation pipeline
generator = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B", max_new_tokens=1500)

# Wrap the Hugging Face pipeline into LangChain's LLM interface
llm = HuggingFacePipeline(pipeline=generator)

# Define the prompt template for LangChain
prompt_template = PromptTemplate(
    input_variables=["project_description"],
    template="""
You are an expert Python API developer. The user needs an API with the following requirements: {project_description}. 
Generate the complete FastAPI code, including authentication and pagination. Return only code and nothing else.
"""
)

# Create a LangChain LLMChain using the prompt and the model
llm_chain = LLMChain(
    prompt=prompt_template,
    llm=llm
)

# Define the input to your model (topic for text generation)
prompt = "Create an API to store, retrieve, update employee data"

# Run the model to generate FastAPI code based on the description
generated_text = llm_chain.run({
    "project_description": prompt
})

print("Generated text:\n", generated_text)
