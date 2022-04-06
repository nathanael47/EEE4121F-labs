# eee4121f-b Lab 1


TCP LAB

In this lab this are the following things that were changed to conduct the experiments 

This lab to run tcp.py and obtaining the plots can be run through the single command 
sudo ./run.sh


Before starting activate the statistics module through the following command 
	- sudo pip install statistics
	
When starting this command train the first step is 
1. sudo mn -c    //this command will clear the network

Then the command to run the programs
2. sudo ./run.sh 

The following changes were made to execute through all the experiments. 
All the changes for the experiments will be made in the file ***run.sh**

Changing the congestion control mechanism 

Congestion Control Mechanisms
	To change the mechanism flags within the run.sh file needs to be changed 
	The flags are:
	
		TCP Reno - nothing needs to be changed as the TCP reno is the default 
				   in run.sh make sure the following are commented out as follows

				
				#--cong bbr \
				#--pman fq \
				
		TCP Cubic - The following flag needs to be changed in run.sh

				uncomment the flag --cong bbr \ 

				and change it as follows

				--cong bbr \ --> --cong cubic \
				
		TCP BBR - The following needs to be changed in run.sh 

			if TCP cubic was used before recomment the flag --cong cubic \ using the # before the flag as follows
				#  --cong bbr \

				if the cong flag was changed to cubic just do this 

				--cong cubic \ --> --cong bbr \
				
				Then uncomment the following flags 
					--cong bbr \
					--pman fq \			 

For the congestion control mechanism TCP Reno 
 
	For experiments 1 - 3, make sure the congestion control is configured as flags for TCP
	Reno as stated above in the congestion control mechansim section 
	
	Experiment 1: queue size - 100 and host link speed - 1 Gbps
	
		For this experiment the following changes need to be made in the run.sh file 
		Make sure the flags are as follows  

		--bw-host 1000 \
		--maxq 100 \

		save and run the following commands 

		sudo mn -c
		sudo ./run.sh

		plots can be used with any linux based image viewer i used fim 
		To view the plots the following commands were used 

		fim ping.png
		fim queue.png 

		To view the average and standard deviation use the following command

		nano answer.txt

		
	Experiment 2: queue size - 20 and host link speed - 1 Gbps
	
		For this experiment the following changes need to be made in the run.sh file 
		Make sure the flags are as follows  

		--bw-host 1000 \
		--maxq 20 \

		save and run the following commands 

		sudo mn -c
		sudo ./run.sh

		plots can be used with any linux based image viewer i used fim 
		To view the plots the following commands were used 

		fim ping.png
		fim queue.png 

		To view the average and standard deviation use the following command

		nano answer.txt

	Experiment 3: queue size - 100 and host link speed - 100 Mbps

		For this experiment the following changes need to be made in the run.sh file 
		Make sure the flags are as follows  

		--bw-host 100 \
		--maxq 100 \

		save and run the following commands 

		sudo mn -c
		sudo ./run.sh

		plots can be used with any linux based image viewer i used fim 
		To view the plots the following commands were used 

		fim ping.png
		fim queue.png 

		To view the average and standard deviation use the following command

		nano answer.txt


For the congestion control mechanism TCP Cubic

	For experiments 4 - 6, make sure the congestion control is configured as flags for TCP
	Cubic as stated above in the congestion control mechansim section 

	Experiment 4: queue size - 100 and host link speed - 1 Gbps
		For this experiment the following changes need to be made in the run.sh file 
		Make sure the flags are as follows 

			--bw-host 1000 \
			--maxq 100 \

		save and run the following commands 

			sudo mn -c
			sudo ./run.sh

		
		plots can be used with any linux based image viewer i used fim 
		To view the plots the following commands were used 

			fim ping.png
			fim queue.png 

		To view the average and standard deviation use the following command

			nano answer.txt
		
	Experiment 5: queue size - 20 and host link speed - 1 Gbps
	
		For this experiment the following changes need to be made in the run.sh file 
		Make sure the flags are as follows  

		--bw-host 1000 \
		--maxq 20 \

		save and run the following commands 

		sudo mn -c
		sudo ./run.sh

		plots can be used with any linux based image viewer i used fim 
		To view the plots the following commands were used 

		fim ping.png
		fim queue.png 

		To view the average and standard deviation use the following command

		nano answer.txt

	Experiment 6: queue size - 100 and host link speed - 100 Mbps

		For this experiment the following changes need to be made in the run.sh file 
		Make sure the flags are as follows  

		--bw-host 100 \
		--maxq 100 \

		save and run the following commands 

		sudo mn -c
		sudo ./run.sh

		plots can be used with any linux based image viewer i used fim 
		To view the plots the following commands were used 

		fim ping.png
		fim queue.png 

		To view the average and standard deviation use the following command

		nano answer.txt

		


Fot the congestion control mechanism TCP BBR

	For experiments 7 - 9, make sure the congestion control is configured as flags for TCP
	BBR as stated above in the congestion control mechansim section 

	Experiment 7: queue size - 100 and host link speed - 1 Gbps
	
		For this experiment the following changes need to be made in the run.sh file 
		Make sure the flags are as follows 

			--bw-host 1000 \
			--maxq 100 \

		save and run the following commands 

			sudo mn -c
			sudo ./run.sh

		
		plots can be used with any linux based image viewer i used fim 
		To view the plots the following commands were used 

			fim ping.png
			fim queue.png 

		To view the average and standard deviation use the following command

			nano answer.txt
		
	Experiment 8: queue size - 20 and host link speed - 1 Gbps
	
		For this experiment the following changes need to be made in the run.sh file 
		Make sure the flags are as follows  

		--bw-host 1000 \
		--maxq 20 \

		save and run the following commands 

		sudo mn -c
		sudo ./run.sh

		plots can be used with any linux based image viewer i used fim 
		To view the plots the following commands were used 

		fim ping.png
		fim queue.png 

		To view the average and standard deviation use the following command

		nano answer.txt

	Experiment 9: queue size - 100 and host link speed - 100 Mbps

	
		For this experiment the following changes need to be made in the run.sh file 
		Make sure the flags are as follows  

		--bw-host 100 \
		--maxq 100 \

		save and run the following commands 

		sudo mn -c
		sudo ./run.sh

		plots can be used with any linux based image viewer i used fim 
		To view the plots the following commands were used 

		fim ping.png
		fim queue.png 

		To view the average and standard deviation use the following command

		nano answer.txt

These were the changes made in order to run through all the experiments for the lab 
