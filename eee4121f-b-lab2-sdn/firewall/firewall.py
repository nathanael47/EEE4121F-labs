
from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
from collections import namedtuple
import os
# TODO Add your imports here 
# import the csv module 
import csv


log = core.getLogger()
policyFile = "%s/pox/pox/misc/firewall-policies.csv" % os.environ[ 'HOME' ]

#TODO Add your global variables here 
#array to store the addresses of the hosts that need to be blocked 
address = []
#opening the files and address it to a variable 
with open(policyFile) as data:

    #reading in the data 
    read = csv.reader(data)
    #skipping the headers of the file 
    next(read)
    #Running through each line of the csv file and appending the mac addresses and not the IDs
    for r in read:
        address.append(r[1])

   # used to remove the last two elemeents from the array so only two hosts are blocked
   # address = address[:-2]
   # used to add an additional host to the blocked list
   # h8 = '00:00:00:00:00:08'
   # address.append(h8)
   
          
class Firewall (EventMixin):

    def __init__ (self):
        self.listenTo(core.openflow)
        log.debug("Enabling Firewall Module")

    def _handle_ConnectionUp (self, event):
        #TODO Add your logic here 
        #looping therough the address 
        for a in address:            
            b = of.ofp_match()
            b.dl_src = EthAddr(a)
            flow_mod = of.ofp_flow_mod()
            flow_mod.match = b
            event.connection.send(flow_mod)


        log.debug("Firewall rules installed on %s", dpidToStr(event.dpid))

def launch ():
    #    Starting the Firewall module
    
    core.registerNew(Firewall)
