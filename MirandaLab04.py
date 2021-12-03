m = int(input(" Please enter number of minutes parked..."))
if (0 < m and m <= 60 ):      	#table 1 minutes
  #  hrs = int(m/60) + 1		# FYI only
    fee = 5
    print("Parking fee for ", m, " minutes is $", fee)
# now for table 2
elif (m > 60 and m <= 300):    	# table 2
    # calculations needed
    fee = int(4*(m/60))
    print('we are in table 2 fee is ', fee)
elif ( m > 300):			# table 3
    #calculations needed
    fee = int(m * (m/60))
    print('we are in table 3 fee == ', fee)
else:
    print("error  negative minutes", m )
