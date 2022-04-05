#!/bin/bash
echo "starting tcp experiment"

python tcp.py --bw-host 1000\
          --bw-net 2 \
          --delay 50 \
          --dir ./ \
          --time 30 \
          --maxq 100 \
#         --cong cubic \
#         --cong bbr \
#         --qman fq \

echo "done computations starting plots"
python plot_queue.py -f $dir./q.txt -o $dir./queue.png
python plot_ping.py -f $dir./ping.txt -o $dir./ping.png

echo "plots are complete"
echo "end"
