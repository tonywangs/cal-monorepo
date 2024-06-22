from flask import Flask, request, jsonify
from langchain.chains import ConversationChain
from langchain.llms import OpenAI  # Correct import for OpenAI LLM

app = Flask(__name__)
# Initialize LangChain components
llm = OpenAI(api_key='sk-proj-azhfDUS19t7tBfeCIVWoT3BlbkFJ6Z5fQZXGy0lCquKpuZyk')  # Replace with your OpenAI API key
conversation = ConversationChain(llm=llm)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    
    # Generate response using LangChain
    response = conversation.run(input=user_message, context=company_policies)
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
