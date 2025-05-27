from slack_sdk import WebClient
import os

SLACK_TOKEN = os.environ["SLACK_TOKEN"]
CHANNEL = "C04TS7Y82M9"  # ✅ 실제 슬랙 채널 ID로 교체

client = WebClient(token=SLACK_TOKEN)

response = client.chat_postMessage(
    channel=CHANNEL,
    text="📚 *오늘의 수업 쓰레드 시작!*"
)

thread_ts = response["ts"]
with open("thread_ts.txt", "w") as f:
    f.write(thread_ts)

print("✅ 메시지 전송 완료, thread_ts:", thread_ts)
