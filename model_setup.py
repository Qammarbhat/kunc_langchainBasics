import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Importing langchain_openai 
from langchain_openai import ChatOpenAI

# import output parser
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate

from operator import itemgetter

# Context provided for answering questions
context = """
CQAI and Kashmir University has collaborated and held a workshop about Gen AI. 
In the workshop CQAI (Chainar Quantum AI), founded by Dr. Rukhsan Ul Haq, 
sessions were held with CS students about python, numpy, pandas, PCA, ML, AI, gen AI
"""

# Template for the chatbot's behavior and response structure
template = """
You are a fun chatbot, whenever you are asked any question you answer it properly from the given context and in a very funny way. 
If you cannot answer it from the given context reply with 'ME CHANNE PAYYE'

Context: {context}
Question: {question}
"""

def llm_setup(question: str, context: str, language: str):
    # Initializing ChatOpenAI model
    model = ChatOpenAI(model="gpt-3.5-turbo")

    # Initializing output parser
    parser = StrOutputParser()

    # Setting up the prompt template for the chatbot
    prompt = ChatPromptTemplate.from_template(template)

    # Defining the processing chain
    chain = prompt | model | parser

    # Setting up a translation prompt for language translation
    translation_prompt = ChatPromptTemplate.from_template(
        "translate {answer} to {language}"
    )

    # Defining a translation chain for handling language translation requests
    translation_chain = (
        {
            "answer": chain,  # Output from the main chain
            "language": itemgetter("language"),  # Target language for translation
        } | translation_prompt | model | parser
    )
    
    # Invoking the translation chain with provided context, question, and target language
    response = translation_chain.invoke({
        "context": context,
        "question": question,
        "language": language
    })

    return response

if __name__ == "__main__":
    # Example usage if this script is run directly
    context = """
    CQAI and Kashmir University has collaborated and held a workshop about Gen AI. 
    In the workshop CQAI (Chainar Quantum AI), founded by Dr. Rukhsan Ul Haq, 
    sessions were held with CS students about python, numpy, pandas, PCA, ML, AI, gen AI
    """

    # Example usage: asking a question about Dr. Rukhsan Ul Haq in "pirated English"
    print(llm_setup("Who is Dr Rukhsan Ul Haq", context, "pirated English"))
