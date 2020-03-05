from pulsesensor import Pulsesensor #import pulse sensor library
import time #import time library

p = Pulsesensor() #store pulse sensor in variable p (tidies code up)
p.startAsyncBPM() #starts the BPM (beats per minute) monitoring

try: #allows you to cancel with Ctrl-C
    while True: #loops forever
        bpm = p.BPM #stores BPM in bpm variable
        if bpm > 0: #checks for pulse
            print("BPM: " + str(bpm)) #this prints the BPM to screen
        else: #this happens if no beats per minute register
            print("No Heartbeat found") 
        time.sleep(1) #waits for 1 second
except:
    p.stopAsyncBPM() #stops BPM monitoring if Ctrl-C is pressed
