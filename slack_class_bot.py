# slack_class_bot.py
from slack_sdk import WebClient
import os

# 슬랙 봇 토큰과 채널 ID
SLACK_TOKEN = os.environ["SLACK_TOKEN"]
CHANNEL = "#일반"  # 여기에 실제 채널 ID 입력

client = WebClient(token=SLACK_TOKEN)

# 슬랙에 메시지 전송
response = client.chat_postMessage(
    channel=CHANNEL,
    text="📚 *오늘의 수업 쓰레드 시작!*"
)

# 생성된 쓰레드 타임스탬프 출력
print("✅ 메시지 전송 완료, thread_ts:", response["ts"])
