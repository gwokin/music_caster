# Music Caster
Creates a remote to allow a user to cast internet radio stations to their Chromecast Audio 

### Hardware Requirements

The [Raspberry Pi 3](https://www.raspberrypi.org) is the computer for this project. The Pimoroni [TouchPhat](https://shop.pimoroni.com/products/touch-phat) is used to provide buttons for the remote. 

### Software Requirements

 The necessary dependencies can be installed with the code below.

```
sudo apt install python3 python3-pip python3-touchphat python3-pychromecast
```

This project is not compatible with Python 2 and must be run with Python 3.

### Set Up

The "device\_friendly\_name" line of code in internet\_radio.py will have to be updated with the name of your Chromecast. Additionally, the radio stations can be switched by pasting the internet address of the stream in the play_media block of the appropriate TouchPhat button. 

Once this is done, TouchPhat buttons **A**, **B**, **C**, and **D** will cast four different radio stations and the **Back** and **Enter** buttons will adjust the volume. 

### Thanks

I would like to thank [Balloob](https://github.com/balloob) for the [PyChromecast](https://github.com/balloob/pychromecast) library which made this project possible.