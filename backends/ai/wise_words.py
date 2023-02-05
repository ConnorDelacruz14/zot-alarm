import os
import openai

openai.api_key = "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"

prompt = input("Human: ")

# response = openai.Completion.create(
#     model="text-davinci-001",
#     prompt=prompt,
#     temperature=0.6
# )

# print("Wise words:", )
response = openai.Image.create(
  prompt=prompt,
  n=1,
  size="512x512"
)

image_url = response['data'][0]['url']
print(image_url)

print("AI:", dict(response)["choices"][0]["text"].replace("\n", ""))