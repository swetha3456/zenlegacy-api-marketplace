from langchain import PromptTemplate, LLMChain
from transformers import pipeline
from langchain.llms import HuggingFacePipeline
from langchain.memory import ConversationBufferMemory

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

# Initialize conversation buffer memory to retain context across interactions
memory = ConversationBufferMemory(input_key="project_description", memory_key="history")

# Create a LangChain LLMChain using the prompt, model, and memory
llm_chain = LLMChain(
    prompt=prompt_template,
    llm=llm,
    memory=memory  # Add memory for conversation tracking
)

# Define the input to your model (project description for code generation)
project_description_1 = "Create an API to store, retrieve, update employee data"

# Run the model to generate FastAPI code based on the first description
generated_text_1 = llm_chain.run({
    "project_description": project_description_1
})

print("Generated text for first prompt:\n", generated_text_1)

# Now let's define a second prompt that will leverage the previous context
project_description_2 = "Add functionality to delete employee data"

# Run the model again, and it will keep the previous conversation in memory
generated_text_2 = llm_chain.run({
    "project_description": project_description_2
})

print("Generated text for second prompt (with conversation memory):\n", generated_text_2)

