from groq import Groq
from Configs import Api_key

Model = "llama-3.1-70b-versatile"
pesan_sistem = ""
Temperatur = 2
Maksimum_token = 400
Top_P = 1

msgs = [{"role": "system","content": pesan_sistem}]

def gpt(messages, Temperatur, Model, Maksimum_token, Top_p):
    try:
        client = Groq(
            api_key=Api_key,
        )
        completion = client.chat.completions.create(
            model=Model,
            messages=messages,
            temperature=Temperatur,
            max_tokens=Maksimum_token,
            top_p=Top_p,
            stream=False,
            stop=None,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return e
