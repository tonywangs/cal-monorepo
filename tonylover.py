from flask import Flask, request, jsonify
from langchain.chains import ConversationChain
from langchain.llms import OpenAI  # Correct import for OpenAI LLM

app = Flask(__name__)

def read_text_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

# Load mental health advice from the text file
text_file_path = 'data/mental_health_advice.txt'
mental_health_advice = read_text_file(text_file_path)

# Initialize LangChain components
llm = OpenAI(api_key='sk-proj-azhfDUS19t7tBfeCIVWoT3BlbkFJ6Z5fQZXGy0lCquKpuZyk')  # Replace with your OpenAI API key
conversation = ConversationChain(llm=llm)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    
    # Incorporate mental health advice into the context
    context = mental_health_advice
    
    # Generate response using LangChain
    response = conversation.run(input=user_message, context=context)
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
