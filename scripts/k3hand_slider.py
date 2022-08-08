#!/usr/bin/env python2
# coding=utf-8


import rospy
import time
from sensor_msgs.msg import JointState

from k3hand import k3hand


k3 = None
last_data = None
"""
def callback(data):
    # rospy.loginfo(rospy.get_caller_id() + "%s", data.position)
    print(data.position)
    data_list = []
    for index, value in enumerate(data.position):
        data_list.append(value)
   
    k3.send_radians(data_list)#mycobotに角度を送る（pymycobotで設定した関数）
    #time.sleep(0.5)
"""
def callback(data):
    global last_data
    last_data = data
"""
def callback(data):
    global last
    now=rospy.Time.now()
    dt = now.to_sec() - last.to_sec()
    print(data.position)
    if dt > 0.5:
        print(data.position)
        data_list = []
        for index, value in enumerate(data.position):
            data_list.append(value)
        k3.send_radians(data_list)#mycobotに角度を送る（pymycobotで設定した関数）
        last = now
"""        

def listener():
    global k3

    port = rospy.get_param("~port", "/dev/ttyUSB0")#port のdefault値のjoint_s設定
    baud = rospy.get_param("~baud", 115200)
    print(port, baud)
    k3 = k3hand(port)
    k3.set_speed(100)
    start = k3.get_angles()
    k3.send_angles(start)
    k3.enable_all()
    print("enabled")
#    print(k3.speeds)
 
    rospy.init_node("control_slider", anonymous=True)
#    r = rospy.Rate(5)
    while not rospy.is_shutdown():
        if not last_data is None:
            print(last_data.position)
            data_list = []
            for index, value in enumerate(last_data.position):
                data_list.append(value)
            k3.send_radians(data_list)#mycobotに角度を送る（pymycobotで設定した関数）
        #r.sleep()
        rospy.Subscriber("joint_states", JointState, callback)#JointStateをsubscribe        
    k3.disconnect()
    

if __name__ == "__main__":
    listener()
