#!/usr/bin/env python2

import rospy

# some functions

if __name__ == '__main__':
    rospy.init_node('get_int', anonymous=True)
    sim = rospy.get_param( '~int', 10) # <- edit
    print(sim)
