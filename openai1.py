import os
import openai
import ignore

openai.api_key = ignore.openai_apikey

while True:
    ask = input("問題[Q:結束]:")
    if ask == "Q":
        break
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=ask,
        temperature=1,
        max_tokens=512,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\"\"\""]
    )

    print(response["choices"][0]["text"].strip())
    
    