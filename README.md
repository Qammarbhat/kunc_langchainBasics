# kunc_langchainBasics

# Guide for KU NC Students

### Creating a Github Repo
Start by creating a repository in your Github

### Cloning the Repo
Use the following command in your terminal/Powershell to clone the repository in your local machine:

#### For Mac:
```sh
git clone https://github.com/username/repository.git
```
#### For Linux
```sh
git clone https://github.com/username/repository.git
```

### Powershell (Windows)
```sh
git clone https://github.com/username/repository.git
```

**Note:** 
*Replace `https://github.com/username/repository.git` with the actual URL of your repository.

### Setting Up the Environment
1. #### Open the cloned directory in your Favorite IDE (VSCode, PyCharm, or anything else).

2. #### Create a Virtual Environment

    a. Open the terminal
    
    **For Bash (Mac and Linux)**
    ```sh
    python3.10 -m venv venv
    ```

    **For Windows (Powershell)**
    ```powershell
    python -m venv venv
    ```

3. #### Activating the Environment

    **For Mac and Linux**
    ```sh
    source venv/bin/activate
    ```

    **For Powershell (Windows)**
    ```powershell
    .\venv\Scripts\Activate.ps1
    ```


4. #### Create these necessary modules:

    a. `.env`

    a. `main.py`
    
    b. `model_setup.py`
    
    c. `requirements.txt`

## main.py

### Overview
In this module, we will use Streamlit to create a frontend for our service/application.

### Resources
- Streamlit Docs: [https://docs.streamlit.io/](https://docs.streamlit.io/)

## .env

### Purpose
The `.env` file is used to store environment variables that are sensitive or specific to your project. These variables are typically used to configure settings or credentials required by your application.

### What for
- **Sensitive Information**: Store API keys, database credentials, and other sensitive information securely.
- **Configuration**: Customize settings such as debugging flags, development versus production environment settings, etc.
- **Portability**: Facilitate easy configuration management across different environments without hardcoding values in your codebase.

## requirements.txt

### Purpose
The `requirements.txt` file lists the Python packages that are required for your project to run successfully. It helps in managing dependencies and ensuring that all necessary libraries are installed.

### What for
- **Dependency Management**: Specify exact versions or ranges of Python packages required by your project.
- **Reproducibility**: Ensure that others can replicate your development environment with the same dependencies.
- **Virtual Environments**: Facilitate creation of virtual environments with specific package versions using tools like `pip` or `conda`.



## model_setup.py

### Overview
In this module, we will set up an LLM (Large Language Model) using OpenAI's **GPT-3.5-turbo** with Langchain. We'll explore basic Langchain features like integration with OpenAI, standard output parsing, and working with chains.

### Resources
- Langchain Docs: [https://python.langchain.com/v0.2/docs/introduction/](https://python.langchain.com/v0.2/docs/introduction/)
- Build a Chatbot Tutorial: [https://python.langchain.com/v0.2/docs/tutorials/chatbot/](https://python.langchain.com/v0.2/docs/tutorials/chatbot/)
- python-dotenv Docs: [https://pypi.org/project/python-dotenv/](https://pypi.org/project/python-dotenv/)
- OpenAI Platform Playground: [https://platform.openai.com/playground/chat?models=gpt-3.5-turbo-1106](https://platform.openai.com/playground/chat?models=gpt-3.5-turbo-1106)
- Output Parser: [https://api.python.langchain.com/en/latest/output_parsers/langchain_core.output_parsers.string.StrOutputParser.html](https://api.python.langchain.com/en/latest/output_parsers/langchain_core.output_parsers.string.StrOutputParser.html)
- ChatPromptTemplate: [https://python.langchain.com/v0.2/docs/tutorials/chatbot/](https://python.langchain.com/v0.2/docs/tutorials/chatbot/)
- Chains in Langchain: [https://python.langchain.com/v0.1/docs/modules/chains/](https://python.langchain.com/v0.1/docs/modules/chains/), [https://python.langchain.com/v0.2/docs/tutorials/chatbot/](https://python.langchain.com/v0.2/docs/tutorials/chatbot/)
    






