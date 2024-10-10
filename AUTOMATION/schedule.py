import schedule
import time
from report_generation import generate_daily_report
from datetime import datetime

# Schedule the daily report task
schedule.every().day.at("23:59").do(lambda: generate_daily_report(datetime.now().strftime('%Y-%m-%d')))

while True:
    schedule.run_pending()
    time.sleep(60)