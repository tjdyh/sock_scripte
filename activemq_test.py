# -*- coding:utf-8 -*-
import stomp
import threading
import time

#推送到主题
__topic_name = '/topic/FirstTopic'
__queue_name = 'test_aaa'
__host = '192.168.88.71'
__port = 61613

# 发送消息到主题
def send_to_topic(__host,__port,topic, msg):
    conn = stomp.Connection10([(__host,__port)])
    conn.start()
    conn.connect()
    conn.send(topic,msg)
    conn.disconnect()

# 发送消息到队列
def send_to_queue(__host,__port,SampleQueue,msg):
    conn = stomp.Connection10([(__host,__port)])
    conn.start()
    conn.connect()
    conn.send(SampleQueue,msg)
    conn.disconnect()




if __name__ == '__main__':
    for i in range(1000):
        send_to_queue(__host,__port,__queue_name, 'queue:测试信息1...')
        # send_to_topic(__host,__port,__topic_name, 'topic:测试信息2...')
        # time.sleep(3)