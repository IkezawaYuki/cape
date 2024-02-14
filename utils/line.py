from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os
import logging
from utils.azure_openai import generation
from utils.aisearch import retrieval
from utils.cosmosdb import save_chat, get_chat_history


line_bot_api = LineBotApi(os.environ["LINE_CHANNEL_ACCESS_TOKEN"])
handler = WebhookHandler(os.environ["LINE_CHANNEL_SECRET"])


def line_handler(body, signature):
    handler.handle(body, signature)


@handler.add(MessageEvent, message=TextMessage)
def return_message(event):
    logging.info(event)

    # lineの送り主とメッセージを取得する
    text = event.message.text
    logging.info(text)

    user_id = event.source.user_id
    logging.info(user_id)

    # cosmosdbを呼び出し、会話履歴を取得する
    arguments = get_chat_history(user_id)
    logging.info(arguments)

    # azure ai search で回答の単語を検索する
    add_info = retrieval(text)
    logging.info(add_info)

    # プロンプトを作成する
    prompt = f"""{text}
以下、付加情報
```{add_info}```"""

    # azure openaiで処理を投げ、responseを受け取る
    resp_message = generation(prompt, arguments)

    # lineで返答する。
    line_bot_api.push_message(
        user_id,
        TextSendMessage(text=resp_message.content))

    # 返答を保存する
    save_chat(user_id, text, "user")
    save_chat(user_id, resp_message.content, "system")

