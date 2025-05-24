import os
import time
from datetime import datetime
from slack_sdk import WebClient

# 환경변수에서 토큰과 채널 설정
SLACK_TOKEN = os.environ["SLACK_TOKEN"]
CHANNEL = "#일반"  # ⚠️ 실제 슬랙 채널 ID로 변경하세요!

# thread_ts 불러오기
with open("thread_ts.txt", "r") as f:
    THREAD_TS = f.read().strip()

# 슬랙 클라이언트 생성
client = WebClient(token=SLACK_TOKEN)

# 1분 동안 10초 간격으로 메시지 전송 (총 6회)
for i in range(6):
    now = datetime.now().strftime("%H:%M:%S")
    response = client.chat_postMessage(
        channel=CHANNEL,
        thread_ts=THREAD_TS,
        text=f":test_tube: 현재 시각 {now} - 테스트 메시지 {i+1}/6"
    )
    print(f"✅ {now} - 댓글 {i+1} 전송 완료")
    time.sleep(10)  # 10초 대기
