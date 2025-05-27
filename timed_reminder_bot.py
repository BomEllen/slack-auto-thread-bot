from slack_sdk import WebClient
import os
from datetime import datetime, timedelta

# 🔐 슬랙 토큰과 채널 설정
SLACK_TOKEN = os.environ["SLACK_TOKEN"]
CHANNEL = "#일반"  # ✅ 실제 슬랙 채널 ID로 바꾸세요

# 📁 thread_ts.txt 읽기
try:
    with open("thread_ts.txt", "r") as f:
        THREAD_TS = f.read().strip()
except FileNotFoundError:
    print("❌ thread_ts.txt 파일이 없습니다.")
    exit(1)

# 🕒 현재 시각을 KST(한국 표준시) 기준으로 변환
now_kst = datetime.utcnow() + timedelta(hours=9)
now = now_kst.strftime("%H:%M")
print(f"🕒 현재 시각 (KST): {now}")

# ⏰ 시간별 자동 댓글 메시지 매핑
message_map = {
    "09:50": "쉬는 시간 입니다!!",
    "10:50": "쉬는 시간 입니다!!",
    "11:50": "쉬는 시간 입니다!!",
    "12:50": "점심 시간 입니다!!",
    "14:50": "쉬는 시간 입니다!!",
    "15:50": "쉬는 시간 입니다!!",
    "16:50": "쉬는 시간 입니다!!",
    "15:430": "쉬는 시간 입니다!!",
}

# ✅ 해당 시간에 맞는 메시지가 있다면 댓글 전송
if now in message_map:
    client = WebClient(token=SLACK_TOKEN)
    client.chat_postMessage(
        channel=CHANNEL,
        thread_ts=THREAD_TS,
        text=message_map[now]
    )
    print(f"✅ 메시지 전송 완료: {message_map[now]}")
else:
    print("⏸️ 전송할 메시지 없음 (조건 불일치)")
