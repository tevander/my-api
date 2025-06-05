import requests

def call_llm(prompt):
    # eventually call llm
    print("calling llm with prompt:", prompt)
    response = "here is the AI response: ..."
    #response = requests.post("http://localhost:5000/llm", json={"prompt": prompt})
    return response