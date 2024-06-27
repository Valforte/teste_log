import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI

openai_api_key  = 'OPEN_AI_API_KEY'
llm = OpenAI(api_token=openai_api_key)

df = pd.read_csv("./moat_202404.csv")

chat_df = SmartDataframe(df, config={"llm": llm})

def ask_assistant(question):
    return chat_df.chat(question)

print("Para sair a qualquer momento aperte CTRL + C")

while(True):
    question = input("Pergunta: ")
    print("Resposta: ")
    print(ask_assistant(question))
