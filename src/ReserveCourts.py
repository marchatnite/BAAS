from playwright.sync_api import sync_playwright

from datetime import datetime, timedelta
from ConfigParser import parse_config

loginUrl = "https://northwestbadmintonclub.sites.zenplanner.com/login.cfm"


def perform_login_and_res(page, username, password, day_of_week, timeslot):

	formatted_date = generate_date_string_for_selected_weekday(day_of_week)
	# Step 1: Attempt to login,
	perform_login(page, username, password)
	# Step 2: Attempt to go to Calendar
	navigate_to_calendar(page)
	# Step 3: Attempt to click on the correct time slot
	find_and_click_timeslot(page, formatted_date, timeslot)
	# Step 4: Attempt to Reserve slot
	reserve_slot(page)


def attempt_reserve_court():

	with sync_playwright() as p:
		# Launch the browser
		browser = p.chromium.launch(headless=False)

		# Create a new browser context
		context = browser.new_context()

		# Open a new page within the context
		page = context.new_page()

		# Parse the config
		try:
			config = parse_config()
			username = config["USERNAME"]
			password = config["PASSWORD"]
			day_of_week = int(config["DAYOFWEEK"])
			time_slot = config["TIMESLOT"]

			perform_login_and_res(page, username, password, day_of_week, time_slot)
			return True
		except Exception as e:
			print(f"attempt_reserve_court job failed because error : {e}")
			browser.close()
			return False


def generate_date_string_for_selected_weekday(dayOfWeekIndex):
	# Get today's date
	today = datetime.now()

	# Calculate the number of days until next Wednesday (0: Monday, 1: Tuesday, ..., 6: Sunday)
	days_until_wednesday = (dayOfWeekIndex - today.weekday() + 7) % 7

	# Calculate the date of next Wednesday
	next_wednesday = today + timedelta(days=days_until_wednesday)

	# Extract year, month, and day from the date of next Wednesday
	year = str(next_wednesday.year)
	month = str(next_wednesday.month).zfill(2)
	day = str(next_wednesday.day)
	return f"{year}-{month}-{day}"


def perform_login(page, username, password):
	# Navigate to the login page
	page.goto(loginUrl)

	# Fill in the username and password fields
	page.fill('input[name="username"]', username)
	page.fill('input[name="password"]', password)

	# Locate and click the login button
	button = page.query_selector('input[type="SUBMIT"][value="Log In"]')
	button.click()

	# Capture a screenshot (optional)
	page.screenshot(path="Step 1 Login Attempt.png")
	print("Step 1 Login completed")


def navigate_to_calendar(page):
	page.click(".block >> text=Calendar")
	page.screenshot(path="Step 2 Go To Calendar.png")
	print("Step 2 Go to Calender/move to next page completed")


def find_and_click_timeslot(page, dateString, timeslotString):

	print(timeslotString)
	print(f"div[date='{dateString}']")
	print(f'div:has-text("{timeslotString}")')
	try:
		container = page.locator(f"div[date='{dateString}']")
		container.wait_for(timeout=5000)
	except Exception as e:
		print(
			f"Expected Exception occurred because timeslot not on page, will navigate to next one: {str(e)}"
		)

		# if we can't find it then we need to move to next page since it's not present currently
		print(container)
		nextPageIcon = page.locator("i.icon-chevron-right")
		nextPageIcon.click()
		page.screenshot(path="Step 2.5 Click Next Page.png")
		container = page.locator(f"div[date='{dateString}']")
		container.wait_for(timeout=5000)

	# Find elements with text containing "8:00 PM - 9:00 PM"
	time_slot = container.locator(f'div:has-text("{timeslotString}")').nth(1)
	time_slot.click()

	page.screenshot(path="Step 3 Click on Timeslot.png")
	print("Step 3 Click on timeslot completed")


def reserve_slot(page):
	reserve_button = page.locator('a:has-text("Reserve")')
	reserve_button.click()
	page.screenshot(path="Step 4 Click Reserve.png")
	print("Step 4 Clicked on Reserve completed")


if __name__ == "__main__":
	attempt_reserve_court()
