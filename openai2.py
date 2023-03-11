import openai

# 使用 API 密鑰設定 OpenAI API client
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# 設定 GPT-3 模型，並指定使用的模型版本
model_engine = "text-davinci-003"

# 定義函式，輸入上文與使用者輸入的文字，並回傳 GPT-3 產生的回覆
def chat(prompt, model=model_engine):
    completions = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        temperature=0.7,
    )
    return completions.choices[0].text.strip()

while True:
    ask = input("請輸入你的問題[Q:結束]:")
    if ask == "Q":
        break
    print(chat(ask))
