import os
import openai

openai.api_key = "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"


def generateWiseWords():
  words = openai.Completion.create(
    model="text-davinci-003",
    prompt="I miss my lecture today, give me quote to motivate me not to be late again.",
    temperature=1,
    max_tokens = 200
  )
  return dict(words)["choices"][0]["text"].replace("\n", "")


def generateMotivationalImageLink():
  image = openai.Image.create(
    prompt="person encouraging face",
    size="1024x1024",
  )
  image_url = image['data'][0]['url']
  return image_url