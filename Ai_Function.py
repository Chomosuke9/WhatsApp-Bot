from groq import Groq

Model = "llama-3.1-70b-versatile"
pesan_sistem = "You are sarcastic WhatsApp chatbot assistant"
Temperatur = 2
Maksimum_token = 400
Top_P = 1

def gpt(Pertanyaan, pesan_sistem, Temperatur, Model, Maksimum_token, Top_p):
    try:
        client = Groq(
            api_key='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',
        )
        completion = client.chat.completions.create(
            model=Model,
            messages=[
                {
                    "role": "system",
                    "content": pesan_sistem
                },
                {
                    "role": "user",
                    "content": Pertanyaan
                }
            ],
            temperature=Temperatur,
            max_tokens=Maksimum_token,
            top_p=Top_p,
            stream=False,
            stop=None,
        )
        return completion.choices[0].message.content
    except:
        return "Something went wrong, please try again later"
#print(gpt("Hello", pesan_sistem, Temperatur,Model,Maksimum_token,Top_P))