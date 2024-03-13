# BAAS
Welcome to Badminton As A Service (BAAS)! Developed exclusively in Notepad because I was too lazy to reinstall VSCode. 

### Requirements!
Requirements:
1. Have Python Installed
2. Clone/Copy the src folder from this repo onto your computer
3. Go to the src folder and do `pip install -r requirements.txt`
4. Run `playwright install` 

Now you are done with Requirements!

---
### Configuration!
Once you are done installing requirements, please go to the config.txt file and fill out the needed fields.
1. Put your username in the username field,
2. Put your password in the password field,
3. You don't need to change DayOfTheWeek or Timeslot if you are fine with our usual time of Wed at 8PM

Once this is done, you are all good! Let's do a little bit of testing.

### Testing! 
Edit the config file to select a date and timeslot that is currently available. For example if its tuesday, I could use Sunday at 6-7PM. 

```
DAYOFWEEK = 6
TIMESLOT = "6:00 PM - 7:00 PM"
```

Run `python ReserveCourts.py` and check to see if it attempts to reserve the correct timeslot. If it works, then everything is configured correctly!


### Using BAAS!
All you need to do to use BAAS is just run `python Scheduler.py`. That's it. As long as you keep it running, it will schedule itself to sign you up for your preferred timeslot on 
Saturday morning when reservations open to ensure that we keep our slots! 

Screenshots will be taken to monitor the progress of the App in the src folder. 

### Demo: 
https://drive.google.com/file/d/1i4CzX5Ar4ekHA3GhQfsFE3Aa59kyfBh1/view?usp=drive_link


```
PS C:\Users\jeffr\Documents\BadmintonAsAService\src> python Scheduler.py
Starting to reserve Badminton reservation: invoked at 2024-03-12 23:14:04.516599
DAYOFWEEK: 6
TIMESLOT: 8:00 PM - 9:00 PM
USERNAME: jeffreyzhang1999@gmail.com
PASSWORD: Hidden
Step 1 Login completed
Step 2 Go to Calender/move to next page completed
8:00 PM - 9:00 PM
div[date='2024-03-17']
div:has-text("8:00 PM - 9:00 PM")
Expected Exception occurred because timeslot not on page, will navigate to next one: Timeout 5000ms exceeded.
<Locator frame=<Frame name= url='https://northwestbadmintonclub.sites.zenplanner.com/calendar.cfm?calendarType=PERSON:CCF7BAB4-9EF3-4AE3-AD3D-CC7754C12770'> selector="div[date='2024-03-17']">
Step 3 Click on timeslot completed
Step 4 Clicked on Reserve completed
Badminton reservation succeeded!  2024-03-12 23:14:16.571129 
```
