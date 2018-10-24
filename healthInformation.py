user_age_years = int(input('enter your age in years:\n'))

user_age_days = user_age_years * 365
user_age_hours = user_age_years * 365 * 24
user_age_minutes = user_age_years * 365 * 24 * 60
user_age_seconds = user_age_years * 365 * 24 * 60 * 60

user_heartrate = user_age_minutes * 72
user_sneeze = user_age_days * 4
user_calories_burn = user_age_days * 2200
user_sandwiches = user_age_days * 6
user_sleep = user_age_days * 8


print('You are at least %d days old' % user_age_days)
print('You are at least %d minutes old.' % user_age_minutes)
print('You are at least %d seconds old.' % user_age_seconds)
print('Your heart has beat %d times, at the average heart rate of 72 beats per minute.' % user_heartrate)
print('You have sneezed an estimated %d times.' % user_sneeze)
print('You have burned an estimated %d calories.' % user_calories_burn)
print('     That is an estimated %d sandwiches!' % user_sandwiches)
print('You have slept an estimated %d hours.' % user_sleep)
