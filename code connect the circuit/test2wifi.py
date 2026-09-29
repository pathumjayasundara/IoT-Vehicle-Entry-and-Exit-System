import network
import time

SSID = "ESP32_TEST"
PASSWORD = "12345678"

wlan = network.WLAN(network.STA_IF)

wlan.active(False)
time.sleep(2)

wlan.active(True)
time.sleep(2)

print("Connecting to:", SSID)

wlan.connect(SSID, PASSWORD)

for i in range(20):

    print("Status:", wlan.status())

    if wlan.isconnected():
        break

    time.sleep(1)

print()

if wlan.isconnected():

    print("================================")
    print("WIFI CONNECTED!")
    print("IP:", wlan.ifconfig()[0])
    print("================================")

else:

    print("================================")
    print("WIFI FAILED")
    print("Status:", wlan.status())
    print("================================")