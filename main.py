import streamlit as st

# Importing necessary functions and variables from model_setup module
from model_setup import llm_setup, context

# Streamlit app function
def main():
    # Setting the title of the Streamlit app
    st.title('CQAI_KUNC Langchain Basics')
    
    # User input fields for question and language
    question = st.text_input('Enter your question:')
    language = st.text_input('Enter language (e.g., English, German, Pirated English etc.):')
    
    # Button to trigger the response generation
    if st.button('Generate Response'):
        # Checking if both question and language inputs are provided
        if question and language:
            # Calling llm_setup function with provided inputs to generate output
            output = llm_setup(question, context, language)
            # Displaying a heading for the output
            st.write('Output from LLM Setup:')
            # Displaying the generated output from llm_setup function
            st.write(output)
        else:
            # Warning message if inputs are missing
            st.warning('Please enter both question and language.')

if __name__ == '__main__':
    # Calling the main function when the script is executed
    main()
