# post_to_thread.py (테스트용)

from slack_sdk import WebClient
import os

# 슬랙 설정
SLACK_TOKEN = os.environ["SLACK_TOKEN"]
CHANNEL = "#일반"  # 슬랙 채널 ID

# thread_ts 불러오기
with open("thread_ts.txt", "r") as f:
    THREAD_TS = f.read().strip()

# 슬랙 클라이언트 생성
client = WebClient(token=SLACK_TOKEN)

# 테스트용 메시지 전송
client.chat_postMessage(
    channel=CHANNEL,
    thread_ts=THREAD_TS,
    text="🧪 테스트용 메시지입니다 (댓글 전송)"
)

print("✅ 테스트 메시지 전송 완료!")
