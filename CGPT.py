import openai
openai.api_key = "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"

prompt = "Hello, ChatGPT!"
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=50,
    n=1,
    stop=None,
    temperature=0.5,
)

print(response.choices[0].text)
