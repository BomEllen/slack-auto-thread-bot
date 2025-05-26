from slack_sdk import WebClient
import os
from datetime import datetime

SLACK_TOKEN = os.environ.get("SLACK_TOKEN")
CHANNEL = "#일반"  # ✅ 실제 슬랙 채널 ID

# thread_ts.txt 읽기
try:
    with open("thread_ts.txt", "r") as f:
        THREAD_TS = f.read().strip()
except FileNotFoundError:
    print("❌ thread_ts.txt 없음")
    exit(1)

now = datetime.now().strftime("%H:%M")
print(f"🕒 현재 시각: {now}")

message_map = {
    "09:50": "쉬는 시간 입니다!!",
    "10:50": "쉬는 시간 입니다!!",
    "11:50": "쉬는 시간 입니다!!",
    "12:50": "점심 시간 입니다!!",
    "14:50": "쉬는 시간 입니다!!",
    "15:50": "쉬는 시간 입니다!!",
    "16:50": "쉬는 시간 입니다!!",
}

if now in message_map:
    client = WebClient(token=SLACK_TOKEN)
    client.chat_postMessage(
        channel=CHANNEL,
        thread_ts=THREAD_TS,
        text=message_map[now]
    )
    print(f"✅ 메시지 전송 완료: {message_map[now]}")
else:
    print("⏸️ 전송할 메시지 없음")
