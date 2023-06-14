import openai

openai.api_key = "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"

response = openai.ChatCompletion.create(
  model = "gpt-3.5-turbo",
  temperature = 0.2,
  max_tokens = 100,
  messages = [
    {"role": "user", "content": "Who won the 2018 FIFA world cup?"}
  ]
)

print(response['choices'][0]['message']['content'])

if response.status_code == 200:
    # Successful response
    data = response.json()
    # Process the data returned by the API
    generated_text = data['choices'][0]['text']
    print("Generated Text:", generated_text)

else:
    # Handle error cases
    print("Error:", response.status_code)