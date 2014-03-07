num = 14
num_display = str(num)
print "The num is", num_display

# display with decimal point, but not really there yet
decimal_point = "."
num_display = (str(num) + str(decimal_point))
print "The num with . is", num_display

# if there's a decimal point in the display, add behind that
for button in range(4):
	# add numbers after decimal
	if (num_display.find('.') > 0):
		# decimal point at the end and no numbers following
		if (num_display.find('.') == num_display.__len__()-1):
			num = float(str(num) + decimal_point + str(button))
		# already numbers after the decimal point so just add to end
		else:
			num = float(str(num) + str(button))
	# if no decimal
	else:
		num = int(str(num) + str(button)) # no decimal point -> make sure its an int
	num_display = str(num)


print "Press a button and concat that to num:", num