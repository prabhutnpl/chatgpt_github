import os
from dotenv import load_dotenv
from llama_index import GPTVectorStoreIndex, GithubRepositoryReader, GPTKeywordTableIndex, SimpleDirectoryReader, LLMPredictor, PromptHelper, ServiceContext
from langchain import OpenAI
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

load_dotenv()

openai_api_key = os.environ["OPENAI_API_KEY"]
github_token = os.environ["GITHUB_TOKEN"]

owner = "prabhutnpl"
repo = "chatgpt_github"
branch = "master"

documents = GithubRepositoryReader(
    github_token=github_token,
    owner=owner,
    repo=repo,
    use_parser=False,
    verbose=False,
).load_data(branch=branch)

# define prompt helper
# set maximum input size
max_input_size = 4096
# set number of output tokens
num_output = 256
# set maximum chunk overlap
max_chunk_overlap = 20
prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap)

# define LLM
llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-davinci-002", max_tokens=num_output))

service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)

# build index
my_index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)


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


