import openai
from dotenv import dotenv_values

config = dotenv_values(".env")

openai.api_key = config["OPENAI_KEY"]

messages = []
while True:
    try:
        user_input = input("You: ")
        messages.append({"role": "user", "content": user_input})
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=200,
        )
        print(res["choices"][0].message.content)
        messages.append(
            {"role": "assistant", "content": res["choices"][0].message.content}
        )
        # print(messages)

    except KeyboardInterrupt:
        print("Exiting...")
        break

print(res.choices[0].message.content)
