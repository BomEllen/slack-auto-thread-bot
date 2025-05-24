# slack_class_bot.py

from slack_sdk import WebClient
import os

SLACK_TOKEN = os.environ["SLACK_TOKEN"]
CHANNEL = "#일반"  # 슬랙 채널 ID

client = WebClient(token=SLACK_TOKEN)

# 슬랙에 스레드 시작 메시지 전송
response = client.chat_postMessage(
    channel=CHANNEL,
    text="📚 *오늘의 수업 쓰레드 시작!*"
)

# 받은 thread_ts 값을 파일로 저장
thread_ts = response["ts"]
with open("thread_ts.txt", "w") as f:
    f.write(thread_ts)

print("✅ 메시지 전송 완료, thread_ts:", thread_ts)
