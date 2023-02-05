import os
import openai

openai.api_key = "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"

prompt = input("Human: ")

response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.6
)

# print("Wise words:", )
# response = openai.Image.create(
#   prompt="an inspirational person",
#   n=1,
#   size="1024x1024"
# )
# image_url = response['data'][0]['url']
# print(image_url)

print("AI:", dict(response)["choices"][0]["text"].replace("\n", ""))