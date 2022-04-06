#!/bin/bash
echo "starting tcp experiment"

python tcp.py --bw-host 100 \
          --bw-net 2 \
          --delay 50 \
          --dir ./ \
          --time 30 \
          --maxq 100 \
          --cong bbr \
          --qman fq \
          

echo "done computations starting plots"
echo "plotting the queue graph"
python plot_queue.py -f $dir./q.txt -o $dir./queue.png
echo "done"
echo "plotting the ping graph"
python plot_ping.py -f $dir./ping.txt -o $dir./ping.png
echo "done
"
echo "plots are complete"
echo "end"
