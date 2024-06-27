import requests
import json

url = "https://www.chatcsv.co/api/v1/chat"
token = "sk_3ZJhx6vPvtYAu15rLFHGdfFe"

messages = [
    {
        "role": "system",
        "content": f'''Você é um assistente virtual de uma empresa de comércio exterior. 
            Você pode apenas perguntas que se refiram aos dados enviados no arquivo "titanic.csv". 
            Qualquer pergunta fora deste contexto você deve se desculpar e não responder.'''
     },
]

payload = {
    "model": "gpt-3.5-turbo-16k-0613",
    "messages": messages,
    "files": [
        "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    ]
}

headers = {
    'accept': 'text/event-stream',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
}

def ask_assistant(question):
    messages.append({ "role": "user", "content": question })
    result = requests.post(url, headers=headers, data=json.dumps(payload), stream=True)
    response = ''

    for line in result.iter_lines():
        if line:
            decoded_line = line.decode('utf-8')
            response += decoded_line
    return response
    
print("Para sair a qualquer momento aperte CTRL + C")

while(True):
    question = input("Pergunta: ")
    print("Resposta: " + ask_assistant(question))
