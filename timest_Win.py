import time as tm

while True:

	try:
		mode = input("M-min, S-sec, H-hour : ").lower()
		if mode == "m":
			min = int( input("Min: ") )

			while min > 0:
				print(f"Min : {min}")
				tm.sleep(60)
				min -= 1
				
		elif mode == "s":
			sec = int( input("Sec: ") )

			while sec > 0:
				print(f"Sec : {sec}")
				tm.sleep(1)
				sec -= 1

		elif mode == "h":
			hour = int( input("Hours: ") )

			while hour > 0:
				print(f"Hour : {hour}")
				tm.sleep(3600)
				hour -= 1
	except:
		input("ERROR!")
	
	else:
		print("\nEND TIMER\n\n")
