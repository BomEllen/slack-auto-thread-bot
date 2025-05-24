from slack_sdk import WebClient
import os

SLACK_TOKEN = os.environ["SLACK_TOKEN"]
CHANNEL = "#일반"  # 슬랙 채널 ID

client = WebClient(token=SLACK_TOKEN)

response = client.chat_postMessage(
    channel=CHANNEL,
    text="📚 *오늘의 수업 쓰레드 시작!*"
)

# thread_ts 파일로 저장
with open("thread_ts.txt", "w") as f:
    f.write(response["ts"])

print("✅ 메시지 전송 완료")
