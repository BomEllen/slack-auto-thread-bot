# post_to_thread.py
from slack_sdk import WebClient
import os
from datetime import datetime

SLACK_TOKEN = os.environ["SLACK_TOKEN"]
CHANNEL = "#일반반"  # 슬랙 채널 ID

# thread_ts 파일에서 읽기
with open("thread_ts.txt", "r") as f:
    THREAD_TS = f.read().strip()

# 현재 시간
now = datetime.now().strftime("%H:%M")

message_map = {
    "09:50": "쉬는 시간 입니다!!",
    "10:50": "쉬는 시간 입니다!!",
    "11:50": "쉬는 시간 입니다!!",
    "12:50": "점심 시간 입니다!!",
    "14:50": "쉬는 시간 입니다!!",
    "15:50": "쉬는 시간 입니다!!",
    "16:50": "쉬는 시간 입니다!!"
}

message = message_map.get(now)
if message:
    client = WebClient(token=SLACK_TOKEN)
    client.chat_postMessage(
        channel=CHANNEL,
        thread_ts=THREAD_TS,
        text=message
    )
    print(f"✅ {now} - 메시지 전송 완료")
else:
    print(f"⏱️ {now} - 전송할 메시지 없음")
