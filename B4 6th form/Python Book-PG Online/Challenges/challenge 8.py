import datetime
import time
year = datetime.timedelta(days=365)
voteAge = 18 * year
year = input("\nIn which year were you born? ")
month = input("In which month were you born? ")
date = input("On what date were you born? ")
dateOfBirth = datetime.date(int(year), int(month), int(date))
dateOfVote = datetime.date(int(year)+18, int(month), int(date))
dateToday = datetime.date.today()
if dateOfVote <= dateToday:
    print("\nCongratulations, you can vote.\n")
else:
    print("\nI am sorry you are not old enough to vote.\n")
