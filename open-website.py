import time
import webbrowser

# Run this program and your browser will automatically
# open every 2 hours for 3 times
 
total_break = 3
break_count = 0

print("this program is started on " + time.ctime())
while(break_count < total_break):

	# every 2 Hours
	time.sleep(2 * 60 * 60)
	webbrowser.open("https://www.youtube.com/watch?v=lFGnsdV-sR4")
	break_count += 1