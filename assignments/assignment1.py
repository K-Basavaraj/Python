"""
1) There are 60sec per minute, write a program that caculate how many seconds 
will be there in an hour? 
"""
# There are 60 seconds in a minute and 60 minutes in an hour
seconds = 60
minutes = 60
hour_in_seconds = seconds * minutes

print("There are", hour_in_seconds, "seconds in an hour.") #There are 3600 seconds in an hour.

"""
2) The Market is 6 miles away from your home, The School is two miles away from your home 
calculate how much further the market is from your home Than the school(in mile)/(wich means 
extra distance comapred to the school)
"""
market_distance = 6
school_distance = 2

extra_distance = market_distance - school_distance

print("The market is", extra_distance, "miles further from your home than the school.")
#The market is 4 miles further from your home than the school.

"""
3) There are 200 remote computers that must be download 200mb updates each month 
there are 1024kb in 1MB.
The total Number of KB downloaded by all computers from remote update server each month.
"""
# Number of remote computers
computers = 200

# Download size in MB per computer
update_size_mb = 200

# Conversion factor: 1 MB = 1024 KB
kb_in_one_mb = 1024

# Convert the update size to KB
update_size_kb = update_size_mb * kb_in_one_mb

# Calculate total KB downloaded by all computers
total_kb = computers * update_size_kb

print(f"Total data downloaded: {total_kb} KB") #Total data downloaded: 40960000 KB
