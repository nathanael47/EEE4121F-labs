#!/usr/bin/python

# EEE4121F-B Lab 2
# SDN

# Implementing a Layer-2 Firewall using POX and Mininet


from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.clean import cleanup
import time 

def treeTopo():
    cleanup()
    net = Mininet( controller=RemoteController )
   
    #adding the controller object
    info('*** Adding the controller\n') 
    net.addController('c0')
    #c0 = net.addController('c0')
    #adding the hosts 
    info('*** Adding the Hosts\n')
    h1 = net.addHost('h1', ip = '10.0.0.1', mac='00:00:00:00:00:01')
    h2 = net.addHost('h2', ip = '10.0.0.2', mac='00:00:00:00:00:02')
    h3 = net.addHost('h3', ip = '10.0.0.3', mac='00:00:00:00:00:03')
    h4 = net.addHost('h4', ip = '10.0.0.4', mac='00:00:00:00:00:04')
    h5 = net.addHost('h5', ip = '10.0.0.5', mac='00:00:00:00:00:05')
    h6 = net.addHost('h6', ip = '10.0.0.6', mac='00:00:00:00:00:06')
    h7 = net.addHost('h7', ip = '10.0.0.7', mac='00:00:00:00:00:07')
    h8 = net.addHost('h8', ip = '10.0.0.8', mac='00:00:00:00:00:08')

    #adding the switches 
    info('*** Adding the switches\n')
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    s4 = net.addSwitch('s4')
    s5 = net.addSwitch('s5')
    s6 = net.addSwitch('s6')
    s7 = net.addSwitch('s7')

    #adding the link between s3 with h1 and h2
    net.addLink(h1, s3)
    net.addLink(h2, s3)

    #adding the link between s4 and h3 and h4 
    net.addLink(h3, s4)
    net.addLink(h4, s4)

    #adding the link between h5-s6-h6
    net.addLink(h5, s6)
    net.addLink(h6, s6)

    #adding the link between h7-s7-h8
    net.addLink(h7, s7)
    net.addLink(h8, s7)

    #adding the links between switches 
    root = s1
    layer1 = [s2, s5]
    layer2 = [s3, s4, s6, s7]

    for i, l in  enumerate(layer1):
        net.addLink(root, l)
        net.addLink( l, layer2[2*i])
        net.addLink( l, layer2[2*i+1])
    
    info('*** starting network\n')
    net.start()

    info(' *** running CLI\n')
   # CLI(net)
    net.pingAll()
   
    info('*** Stopping network')
    net.stop()
     #this is to allow the gnome ternimal to remain open for a few seconds before closing 
    time.sleep(30)
    print("Going to start the cleanup")
    cleanup()
if __name__ == '__main__':
    setLogLevel( 'info' )
    treeTopo()
