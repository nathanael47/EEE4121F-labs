#!/bin/bash

# Note: Mininet must be run as root.  So invoke this shell script
# using sudo.

echo "connecting to controller"
~/pox/pox.py forwarding.l2_learning misc.firewall &


echo "running sdn.py and pinging all hosts"
gnome-terminal --  python sdn.py

echo "done"
