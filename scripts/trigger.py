#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import rospy
import gpio
import time

# for astro
#gpio 0 = sysfs GPIO 388 = pin 1
#gpio 1 = sysfs GPIO 298 = pin 3
#gpio 2 = sysfs GPIO 480 = pin 5
#gpio 3 = sysfs GPIO 486 = pin 7


# for orbitty
#gpio 0 = sysfs GPIO 388 = pin 7
#gpio 1 = sysfs GPIO 298 = pin 8
#gpio 2 = sysfs GPIO 480 = pin 9
#igpio 3 = sysfs GPIO 486 = pin 10

def trigger(target_gpio_number, trigger_per_second):
    print "Trigger set to: " + str(target_gpio_number)
    rospy.init_node('trigger', anonymous=True)
    rate = rospy.Rate(trigger_per_second)
    try:
        gpio.set(target_gpio_number,0)
    except IOError:
        print("No gpio present")

    while not rospy.is_shutdown():
        try:
            gpio.set(target_gpio_number,1)
            time.sleep(1)
            gpio.set(target_gpio_number,0)
        except IOError:
            print("No gpio present")
        rate.sleep()

if __name__ == '__main__':
    try:
        trigger(486, 0.25)
    except rospy.ROSInterruptException:
        pass






