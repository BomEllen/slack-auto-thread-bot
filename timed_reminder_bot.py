# timed_reminder_bot.py (최종본)
from slack_sdk import WebClient
import os
from datetime import datetime, timedelta

# 🔐 슬랙 설정
SLACK_TOKEN = os.environ["SLACK_TOKEN"]
CHANNEL = "C04TS7Y82M9"  # ← 실제 슬랙 채널 ID로 바꿔주세요

# 📁 thread_ts.txt 읽기
try:
    with open("thread_ts.txt", "r") as f:
        THREAD_TS = f.read().strip()
except FileNotFoundError:
    print("❌ thread_ts.txt 파일이 없습니다.")
    exit(1)

# 🕐 현재 시각 (UTC → KST 변환)
now_kst = datetime.utcnow() + timedelta(hours=9)
now = now_kst.strftime("%H:%M")
print(f"🕒 현재 시각 (KST): {now}")

# 시간별 메시지
message_map = {
    "09:50": "쉬는 시간 입니다!!",
    "10:50": "쉬는 시간 입니다!!",
    "11:50": "쉬는 시간 입니다!!",
    "12:50": "점심 시간 입니다!!",
    "14:50": "쉬는 시간 입니다!!",
    "15:50": "쉬는 시간 입니다!!",
    "16:50": "쉬는 시간 입니다!!",
    "테스트": "🧪 테스트용 댓글입니다."  # ← 테스트용 추가
}

# ✅ 테스트를 위해 지금 시각을 '테스트'로 간주
test_mode = True

# 메시지 전송
if test_mode:
    client = WebClient(token=SLACK_TOKEN)
    client.chat_postMessage(
        channel=CHANNEL,
        thread_ts=THREAD_TS,
        text=message_map["테스트"]
    )
    print("✅ 테스트 메시지 전송 완료")
elif now in message_map:
    client = WebClient(token=SLACK_TOKEN)
    client.chat_postMessage(
        channel=CHANNEL,
        thread_ts=THREAD_TS,
        text=message_map[now]
    )
    print(f"✅ {now} - 메시지 전송 완료")
else:
    print("⏸️ 전송할 메시지 없음 (시간 조건 불일치)")
