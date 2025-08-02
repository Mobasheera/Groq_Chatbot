from openai import OpenAI

client= OpenAI(
    api_key="GROQ_API_KEY",
    base_url="https://api.groq.com/openai/v1"
)

while True:
    user_input= input("you: ")
    if user_input == "quit":
        print("bot: Goodbye!")
        break
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "you are a career path suggestion bot, provide replies related to career only"}, #You can change this to any role
            {"role": "user", "content": user_input} 
        ]
    )
    print("Bot:, ", response.choices[0].message.content)