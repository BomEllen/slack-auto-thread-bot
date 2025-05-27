from slack_sdk import WebClient
import os
from datetime import datetime, timedelta

# 슬랙 설정
SLACK_TOKEN = os.environ["SLACK_TOKEN"]
CHANNEL = "C04TS7Y82M9"  # ← 실제 슬랙 채널 ID로 바꿔주세요

# thread_ts 읽기
try:
    with open("thread_ts.txt", "r") as f:
        THREAD_TS = f.read().strip()
except FileNotFoundError:
    print("❌ thread_ts.txt 파일이 없습니다.")
    exit(1)

# 현재 시각 (KST 기준으로 변환)
now_kst = datetime.utcnow() + timedelta(hours=9)
now = now_kst.strftime("%H:%M")
print(f"🕒 현재 시각 (KST): {now}")

# 현재 시각을 포함한 테스트 메시지 맵
message_map = {
    now: f"✅ 현재 시각 {now} 기준 테스트 메시지입니다.",
    "🎉09:50": "쉬는시간 입니다!!🎉",
    "🎉10:50": "쉬는시간 입니다!!🎉",
    "🎉11:50": "쉬는시간 입니다!!🎉",
    "🍘12:50": "점심시간 입니다!! 맛점하세요!🍙",
    "🎉14:50": "쉬는시간 입니다!!🎉",
    "🎉15:50": "쉬는시간 입니다!!🎉",
    "🎉16:50": "쉬는시간 입니다!!🎉",
}

# 조건 일치 시 메시지 전송
if now in message_map:
    client = WebClient(token=SLACK_TOKEN)
    client.chat_postMessage(
        channel=CHANNEL,
        thread_ts=THREAD_TS,
        text=message_map[now]
    )
    print(f"✅ {now} - 메시지 전송 완료: {message_map[now]}")
else:
    print("⏸️ 현재 시각에 해당하는 메시지가 없습니다.")
