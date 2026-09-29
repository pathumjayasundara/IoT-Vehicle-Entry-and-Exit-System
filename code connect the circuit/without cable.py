from machine import Pin, time_pulse_us
import time

# --- Pin Configuration ---
TRIG_PIN = 5
ECHO_PIN = 4

trig = Pin(TRIG_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)

def measure_distance():
    # 1. Ensure Trig is low to start
    trig.value(0)
    time.sleep_us(2)
    
    # 2. Send a 10 microsecond pulse to Trig
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    
    # 3. Measure the duration of the Echo pulse (in microseconds)
    # timeout is set to 30000us (30ms) which is roughly 5 meters max range
    try:
        duration = time_pulse_us(echo, 1, 30000)
    except OSError as e:
        return None # Timeout error, no echo received
    
    # 4. Calculate distance
    # Speed of sound is ~343 m/s = 0.0343 cm/us
    # Divide by 2 because the sound travels to the object AND back
    distance_cm = (duration * 0.0343) / 2
    return distance_cm

while True:
    dist = measure_distance()
    
    if dist is None:
        print("Out of range or no echo")
    else:
        print("Distance: {:.1f} cm".format(dist))
    
    time.sleep(1)