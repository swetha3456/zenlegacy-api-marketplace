# import streamlit as st
# import dotenv
# from langchain_openai.llms import OpenAI
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain, SequentialChain
# import os

# os.environ["OPENAI_API_KEY"] = 'sk--fTvpu69QVyjA24KVnSqPDphPNY3JwYuF2Gp4rTZilT3BlbkFJnKX6hBiDdvbhn4TlJNqi7J0WHf-g31m0DqNYPaI-4A'

# # Load environment variables
# dotenv.load_dotenv()

# # Initialize the LLM
# llm = OpenAI()

# code_prompt = PromptTemplate(
#     input_variables=["task", "language"],
#     template="Write a very short {language} function that will {task}"
# )

# test_prompt = PromptTemplate(
#     input_variables=["language", "task", "code"],
#     template="Write a test for the following {language} function, and check if it will {task} :\n{code}"
# )

# explain_prompt = PromptTemplate(
#     input_variables=["language", "task", "code"],
#     template="Explain very briefly how the following {language} function will {task} :\n{code}"
# )
# code_chain = LLMChain(llm=llm, prompt=code_prompt, output_key="code")
# test_chain = LLMChain(llm=llm, prompt=test_prompt, output_key="test")
# explain_chain = LLMChain(llm=llm, prompt=explain_prompt, output_key="explanation")

# chain = SequentialChain(
#     input_variables=["task", "language"],
#     output_variables=["code", "test", "explanation"],
#     chains=[code_chain, test_chain, explain_chain])

# st.title('Code Generator')

# task = st.text_input('Task', 'print hello world')
# language = st.selectbox('Language', ['Python', 'Javascript', 'Java', 'C', 'C++'])

# if st.button('Generate Code'):
#     result = chain({"task": task, "language": language})
#     st.subheader('Generated Code')
#     st.code(result['code'], language=language.lower())

#     st.subheader('Generated Test')
#     st.code(result['test'], language=language.lower())

#     st.subheader('Explanation of Code')
#     st.markdown(result['explanation'])

import streamlit as st

# Define the function to generate the API code based on a prompt
def create_api(prompt: str) -> str:
    # Simulate API generation logic
    return f"Generated API code for: {prompt}"

# Set the title of the Streamlit app
st.title("API Marketplace")

# Add a text input field with the heading
api_prompt = st.text_area("Enter API Generation Prompt")

# Add a button that generates the API
if st.button("Generate API"):
    if api_prompt:
        # Call the create_api function when the button is pressed
        generated_api = create_api(api_prompt)
        # Display the generated API code
        st.code(generated_api)
    else:
        st.warning("Please enter a prompt to generate an API.")

