from slack_sdk import WebClient
import os

SLACK_TOKEN = os.environ["SLACK_TOKEN"]
CHANNEL = "#일반"  # 실제 슬랙 채널 ID로 바꾸세요

# thread_ts 불러오기
with open("thread_ts.txt", "r") as f:
    THREAD_TS = f.read().strip()

print("💬 댓글 달 스레드 ts:", THREAD_TS, type(THREAD_TS))

client = WebClient(token=SLACK_TOKEN)

# 메시지 전송
client.chat_postMessage(
    channel=CHANNEL,
    thread_ts=str(THREAD_TS),  # string 타입 보장
    text="🧪 테스트용 메시지입니다 (댓글 전송)"
)

print("✅ 댓글 전송 완료!")
