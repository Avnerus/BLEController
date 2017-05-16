import bluepy.btle

class MyDelegate(bluepy.btle.DefaultDelegate):
    def __init__(self, params):
        bluepy.btle.DefaultDelegate.__init__(self)
        # ... initialise here

    def handleNotification(self, cHandle, data):
        print("Notification!!")
        print(data)
        # ... perhaps check cHandle
        # ... process 'data'


# Initialisation  -------

print("Connecting to BTLE device")
p = bluepy.btle.Peripheral( "00:1E:C0:46:2F:2F")
p.setDelegate( MyDelegate(params=None) )

# Setup to turn notifications on, e.g.
print("Getting characteristics")
ch = p.readCharacteristic(0x000b)
print(ch)
#ch.write( setup_data )

# Main loop --------

while True:
    if p.waitForNotifications(1.0):
        #handleNotification() was called
        continue

    print ("Waiting...")
    # Perhaps do something else here
