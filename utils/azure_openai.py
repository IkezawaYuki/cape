import os
from openai import AzureOpenAI


client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),  
    api_version="2023-07-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    azure_deployment="cape-assistant"
)


def generation(input_message, arguments=None):
    message_text = [
        {"role":"system","content":"あなたはホームページスタンダートというホームページ制作会社のアシスタントです。見込み客、もしくは既存顧客に対して、質問の応答をします。"}]

    if arguments:
        message_text.append(arguments)
        
    message_text.append({
        "role": "user",
        "content": input_message
    })

    completion = client.chat.completions.create(
        model="gpt-4",
        messages=message_text
    )

    return completion.choices[0].message.content


if __name__ == "__main__":
    print(generation("2番目はどこですか"))