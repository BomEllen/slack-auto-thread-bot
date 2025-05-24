# timed_reminder_bot.py
from slack_sdk import WebClient
import os
from datetime import datetime

SLACK_TOKEN = os.environ.get("SLACK_TOKEN")
CHANNEL = "#일반반"  # 슬랙 채널 ID
THREAD_TS = "슬랙 쓰레드 ts값"  # 아침에 생성된 메시지의 thread_ts 입력

client = WebClient(token=SLACK_TOKEN)

# 현재 시간 확인
now = datetime.now().strftime("%H:%M")

# 시간별 메시지 정의
message_map = {
    "10:50": "쉬는시간 입니다!!",
    "09:50": "쉬는시간 입니다!!",
    "11:50": "쉬는시간 입니다!!",
    "12:50": "점심시간 입니다!!",
    "14:50": "쉬는시간 입니다!!",
    "15:50": "쉬는시간 입니다!!",
    "16:50": "쉬는시간 입니다!!"
}

# 현재 시간에 해당하는 메시지를 전송
if now in message_map:
    client.chat_postMessage(
        channel=CHANNEL,
        thread_ts=THREAD_TS,
        text=message_map[now]
    )
    print(f"✅ {now} - 메시지 전송 완료")
else:
    print(f"⏱️ {now} - 전송할 메시지 없음")
