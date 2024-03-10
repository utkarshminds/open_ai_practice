from openai import OpenAI

#get from platform.openai.com
client = OpenAI(api_key='ENTER API KEY HERE')



response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "Write a poem in english on the subject given in the chat. Not more than 100 words. If you are not familiar with the subject you can mention."
    },
    {
      "role": "user",
      "content": "Santa claus"
    },
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)


answers = response.choices[0].message.content

print(answers)