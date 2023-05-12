import os
from dotenv import load_dotenv
from llama_index import GPTVectorStoreIndex, GithubRepositoryReader
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

load_dotenv()

openai_api_key = os.environ["OPENAI_API_KEY"]
github_token = os.environ["GITHUB_TOKEN"]

owner = "prabhutnpl"
repo = "chatgpt"
branch = "main"

documents = GithubRepositoryReader(
    github_token=github_token,
    owner=owner,
    repo=repo,
    use_parser=False,
    verbose=False,
).load_data(branch=branch)

my_index = GPTVectorStoreIndex.from_documents(documents)

@app.route('/')
def index():
    welcome_message = "Welcome to ChatGPT bot!"
    question_message = "Ask a question like 'Who is Prabhakaran?'"
    return render_template('webpage.html', welcome=welcome_message, question=question_message)

@app.route('/query', methods=['POST'])
def handle_query():
    query_engine = my_index.as_query_engine()
    # Parse the JSON request body
    data = request.get_json()
    query = data['query']

    # Query the index and return the response
    response = query_engine.query(query)
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0')


