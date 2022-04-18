# eee4121f-b-lab2

#author nathanael Thomas THMNAT011
For this lab we will be testing effect of hosts blocked to the % of packets dropped 

to execute the file the following command will be run the program the command is
 	sudo ./run.sh

The following three experiments will be run 
	Experiment 1
	no packets dropped 

	Experiment 2
	adding an additional host to the listed of blocked host. The following commands will be run 
		micro firewall.py 
		uncomment the following commands 
			h8 = '00:00:00:00:00:08'
			address.append(h8)

	Experiment 3
	Removing hosts from the blocked list. Run the following commands
		micro firewall.py
		uncomment the following 
			address = address[:-2]

	Experiment 4
	when no hosts have been blocked on start up run the following command 
		sudo ~/pox/pox.py forwarding.l2_learning
		cd into the firewall folder and run the command 
		sudo python sdn.py
