import os
from datetime import datetime
from slack_sdk import WebClient

# 환경변수에서 슬랙 토큰, 채널 ID 불러오기
SLACK_TOKEN = os.environ["SLACK_TOKEN"]
CHANNEL = "C01ABCDEFG"  # ✅ 반드시 실제 슬랙 채널 ID로 바꿔주세요!

# thread_ts.txt에서 thread_ts 불러오기
try:
    with open("thread_ts.txt", "r") as f:
        THREAD_TS = f.read().strip()
except FileNotFoundError:
    print("❌ thread_ts.txt 파일이 없습니다. 먼저 slack_class_bot.py를 실행하세요.")
    exit(1)

# 현재 시각 확인 (HH:MM 형식)
now = datetime.now().strftime("%H:%M")

# 시간별 전송 메시지 정의
message_map = {
    "🎉09:50": "쉬는 시간 입니다!!🎉",
    "🎉10:50": "쉬는 시간 입니다!!🎉",
    "🎉11:50": "쉬는 시간 입니다!!🎉",
    "🍙12:50": "점심 시간 입니다!!🍘",
    "🎉14:50": "쉬는 시간 입니다!!🎉",
    "🎉15:50": "쉬는 시간 입니다!!🎉",
    "🎉16:50": "쉬는 시간 입니다!!🎉",
}

# 현재 시각에 해당하는 메시지가 있으면 전송
if now in message_map:
    client = WebClient(token=SLACK_TOKEN)
    client.chat_postMessage(
        channel=CHANNEL,
        thread_ts=THREAD_TS,
        text=message_map[now]
    )
    print(f"✅ {now} - 메시지 전송 완료: {message_map[now]}")
else:
    print(f"⏱️ {now} - 전송할 메시지 없음")
