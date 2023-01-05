import os
import openai

openai.api_key = "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"

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