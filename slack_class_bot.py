from slack_sdk import WebClient
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import os

# 슬랙 봇 토큰과 채널명
SLACK_TOKEN = os.environ["SLACK_TOKEN"]
CHANNEL = "C04TS7Y82M9"  # 실제 채널 이름이나 ID 입력

client = WebClient(token=SLACK_TOKEN)
scheduler = BlockingScheduler()
thread_ts_holder = {}

# 매일 8:50에 스레드 생성
@scheduler.scheduled_job('cron', hour=8, minute=50)
def create_daily_thread():
    response = client.chat_postMessage(
        channel=CHANNEL,
        text="📚 *오늘의 수업 쓰레드*",
    )
    thread_ts_holder["ts"] = response["ts"]
    print("✅ 스레드 생성 완료")

# 메시지 전송 함수
def post_message_to_thread(text):
    thread_ts = thread_ts_holder.get("ts")
    if not thread_ts:
        print("❌ 스레드 없음")
        return
    client.chat_postMessage(
        channel=CHANNEL,
        thread_ts=thread_ts,
        text=text
    )
    print(f"✅ 메시지 전송: {text}")

# 쉬는 시간
for t in ['09:50', '10:50', '11:50', '14:50', '15:50', '16:50']:
    h, m = map(int, t.split(':'))
    scheduler.add_job(post_message_to_thread, 'cron', hour=h, minute=m, args=["🎉쉬는 시간 입니다!!🎉"])

# 점심 시간
scheduler.add_job(post_message_to_thread, 'cron', hour=12, minute=50, args=["🍘점심 시간 입니다!!🍙"])

scheduler.start()
