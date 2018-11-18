#!/usr/bin/env python

import signal
import time
import touchphat
import pychromecast

print("""

Welcome to Music Caster!

Press Ctrl+C to exit!

""")


device_friendly_name = "Chromeblaster"
chromecasts = pychromecast.get_chromecasts()
cast = next(cc for cc in chromecasts if cc.device.friendly_name == device_friendly_name)
cast.wait()
 
# Turns on lights when buttons are pressed

for pad in ['Back','A','B','C','D','Enter']:
    touchphat.set_led(pad, True)
    time.sleep(0.1)
    touchphat.set_led(pad, False)
    time.sleep(0.1)

# Turns volume down withe the press of the back button
    
@touchphat.on_touch(['Back'])
def handle_touch(event):
    cast.volume_down()
    print(cast.volume_down()*100)

#Casts KEXP with the press of button A
    
@touchphat.on_touch(['A']) 
def touch_A(event):
     touchphat.all_off()
     time.sleep(0.25)
     touchphat.led_on('A')
     print("Now playing: KEXP Seattle")
     mc = cast.media_controller
     mc.play_media('http://live-aacplus-64.kexp.org/kexp64.aac', 'audio/mp3')
     mc.pause()
     mc.play()

# Casts WGBO (Jazz) with the press of button B

@touchphat.on_touch(['B'])
def touch_B(event):
    touchphat.all_off()
    time.sleep(0.25)
    touchphat.led_on('B')
    print("Now playing: WBGO")
    jc = cast.media_controller
    jc.play_media('http://wbgo.streamguys.net/wbgo', 'audio/mp3')
    jc.pause()
    jc.play()

# Casts WFPK with the press of button C

@touchphat.on_touch(['C'])
def touch_C(event):
    touchphat.all_off()
    time.sleep(0.25)
    touchphat.led_on('C')
    print("Now playing: WFPK Louisville")
    cc = cast.media_controller
    cc.play_media('http://lpm.streamguys1.com/wfpk-web', 'audio/mp3')
    cc.pause()
    cc.play()
                            
# Turns volume up
    
@touchphat.on_touch(['Enter'])
def touch_Enter(event):
    cast.volume_up()
    print(cast.volume_up()*100)

signal.pause()
