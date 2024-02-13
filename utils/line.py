from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os


line_bot_api = LineBotApi(os.environ["LINE_CHANNEL_ACCESS_TOKEN"])
handler = WebhookHandler(os.environ["LINE_CHANNEL_SECRET"])


def line_handler(signature, body):
    handler.handle(body, signature)


@handler.add(MessageEvent, message=TextMessage)
def return_message(event):

    # lineの送り主とメッセージを取得する

    # cosmosdbを呼び出し、会話履歴を取得する

    # azure ai search で回答の単語を検索する

    # プロンプトを作成する

    # azure openaiで処理を投げ、responseを受け取る

    # lineで返答する。

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
    
