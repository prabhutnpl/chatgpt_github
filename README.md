# OPENAI GITHUB SEARCH README

This is a Python Flask web application that creates a natural language processing (NLP) search engine for a GitHub repository. The application takes advantage of the OpenAI API to generate text predictions and the llama_index library to create an index of the repository's content, allowing users to search for specific keywords within the repository.

## Libraries used

- os
- dotenv
- llama_index
- langchain
- Flask

The `llama_index` library is used to create an index of the repository's content, while the `langchain` library is used to generate text predictions for the search engine. The `dotenv` library is used to load environment variables from a `.env` file, while `Flask` is used to create the web application.

## Environment variables

The application loads two environment variables from a `.env` file using the `dotenv` library:

- `OPENAI_API_KEY`: The API key for the OpenAI API.
- `GITHUB_TOKEN`: The authentication token for the GitHub API.

## Code explanation

The application imports several Python libraries including `os`, `dotenv`, `llama_index`, `langchain`, and `Flask`. It also imports two classes from `llama_index`: `GPTVectorStoreIndex` and `GithubRepositoryReader`. `GPTVectorStoreIndex` is used to create the index of the repository's content, while `GithubRepositoryReader` is used to read the content from the repository.

The application reads the content of a specific repository, specified by `owner`, `repo`, and `branch` variables using the `GithubRepositoryReader` class. It sets `use_parser` and `verbose` to False to speed up the process.

The application defines a `PromptHelper` object to assist in generating text prompts, setting the maximum input size to 4096 characters, the number of output tokens to 256, and the maximum chunk overlap to 20.

The application defines an `LLMPredictor` object using the OpenAI API, with the temperature set to 0 and the `model_name` set to "text-davinci-002". The `LLMPredictor` is used to generate text predictions for the search engine.

A `ServiceContext` object is created, which contains the `PromptHelper` and `LLMPredictor` objects. This object is used to configure the `GPTVectorStoreIndex`.

Finally, the `GPTVectorStoreIndex` is built from the content of the repository, using the `ServiceContext` to configure the index.

The Flask application defines two routes: `'/'` and `'/query'`. The `'/'` route simply renders a webpage using a template file called `'webpage.html'`. The `'/query'` route is used to handle search queries submitted by the user.

When a search query is submitted, the application parses the JSON request body and extracts the query string. It then queries the `GPTVectorStoreIndex` for documents that match the query string, returning the results as a JSON object.

The application runs on the Flask development server when executed as the main script. It listens on all available network interfaces (`host='0.0.0.0'`).
