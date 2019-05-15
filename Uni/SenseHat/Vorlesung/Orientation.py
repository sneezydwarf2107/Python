from sense_hat import SenseHat
import numpy as np

def angle2pixel(pitchIndex, rollIndex, yawIndex):
    sense = SenseHat()

    a = [0, 0, 0]
    b = [255, 0, 0]

    if yawIndex > 0:
        b[1] = yawIndex
    else:
        b[2] = yawIndex * (-1)

    rollIndex = rollIndex * 8

    pixel = [
        a, a, a, a, a, a, a, a,
        a, a, a, a, a, a, a, a,
        a, a, a, a, a, a, a, a,
        a, a, a, b, b, a, a, a,
        a, a, a, b, b, a, a, a,
        a, a, a, a, a, a, a, a,
        a, a, a, a, a, a, a, a,
        a, a, a, a, a, a, a, a,
    ]

    p = np.array(pixel)

    if pitchIndex != 0:
        p = np.roll(p, pitchIndex, axis=0)

    if rollIndex != 0:
        p = np.roll(p, rollIndex, axis=0)

    sense.clear()
    sense.set_pixels(p)

sense = SenseHat()


range = 20

while True:
    orientation = sense.get_orientation_degrees()

    pitch = orientation["pitch"]
    roll = orientation["roll"]
    yaw = orientation["yaw"]

    if pitch >= 180:
        pitch = pitch-360

    if roll >= 180:
        roll = roll-360

    if yaw >= 180:
        yaw = yaw-360

    pitchIndex = round(pitch / (range / 3), 0)
    rollIndex = round(roll / (range / 3), 0)
    yawIndex = round(yaw / (180.00 / 255.00), 0)


    if pitchIndex > 3:
        pitchIndex = 3

    if pitchIndex < -3:
        pitchIndex = -3

    if rollIndex > 3:
        rollIndex = 3

    if rollIndex < -3:
        rollIndex = -3

    if yawIndex > 255:
        yawIndex = 255

    if yawIndex < -255:
        yawIndex = -255


    print(pitchIndex, rollIndex)
    angle2pixel(int(pitchIndex * (-1)), int(rollIndex), int(yawIndex))





