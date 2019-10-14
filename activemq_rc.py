# -*-coding:utf-8-*-
import stomp
import time

__listener_name = 'SampleListener'
__queue_name = 'test_aaa'
__host = '192.168.88.12'
__port = 61613

class SampleListener(object):
    def on_message(self, headers, message):
        print('每5秒发送一次')
        print('headers:%s' % headers['destination'])
        print('message:%s\n' % message)


#从队列接收消息
def receive_from_queue():
    # conn = stomp.Connection10([(__host,__port)])
    conn = stomp.Connection10([('192.168.88.11',61613),('192.168.88.12',61613)])
    conn.set_listener(__listener_name, SampleListener())
    conn.start()
    # conn.connect(wait=True)
    conn.connect()
    conn.subscribe(__queue_name,id=1,ack='auto')
    # time.sleep(1)
    while True:
        pass
    conn.disconnect()



if __name__ == '__main__':
    # receive_from_topic()
    receive_from_queue()