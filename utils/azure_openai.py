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
        {"role":"system","content":"あなたはホームページスタンダートというホームページ制作会社のアシスタントです。見込み客、もしくは既存顧客に対して、質問の応答をします。応答は比較的短めの文章でに端的に、かつ丁寧に回答します。"}]

    if arguments:
        message_text.append(arguments)
        
    message_text.append({
        "role": "user",
        "content": input_message
    })

    completion = client.chat.completions.create(
        model="gpt-4",
        messages=message_text,
        max_tokens=300,
        temperature=0.9,
    )
    # print(completion.choices[0].message)
    # return completion.choices[0].message.content
    return completion.choices[0].message


# if __name__ == "__main__":
#     resp = generation(input_message="こんにちは")
