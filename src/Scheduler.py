import schedule
import time
from datetime import datetime
from ReserveCourts import attempt_reserve_court

# Define the start and end time
start_time = "18:45"
end_time = "19:55"


def job():
    print("Starting to reserve Badminton reservation: invoked at", datetime.now())
    result = attempt_reserve_court()
    # If we succeeed the job, we don't want to trigger it again
    if(result):
        print("Badminton reservation succeeded! ", datetime.now())
        time.sleep(2400)
    else:
        print("Badminton reservation failed! ", datetime.now())


def main():
    # Schedule job to run every 2 minutes
    schedule.every(1).seconds.do(job)

    # Run the scheduler
    while True:
        # Check if the current time is between start and end time on Saturday
        if datetime.now().strftime("%A") == "Tuesday" and start_time <= datetime.now().strftime("%H:%M") <= end_time:
            schedule.run_pending()
        time.sleep(10)  # Sleep for 10 seconds before checking again

if __name__ == "__main__":
	main()
