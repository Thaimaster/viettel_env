import os, time
import psutil
import numpy as np
from datetime import datetime


def tracking_memory_usage(begin_ram):

    # Getting loadover15 minutes
    # load1, load5, load15 = psutil.getloadavg()

    cpu_usage = psutil.cpu_percent(interval=1)

    print("The CPU usage is : ", cpu_usage)

    # Getting % usage of virtual_memory ( 3rd field)
    ram =  psutil.virtual_memory()[2]
    print('RAM memory % used:', ram)
    # Getting usage of virtual_memory in GB ( 4th field)
    ram_ = psutil.virtual_memory()[3]/1000000000*1024 - begin_ram
    ram_ = int(ram_)
    print('RAM Used (GB):', ram_ )

    return cpu_usage, ram_

def main(output_dir):

    print("wait 10s to check current RAM usage: ")
   # write current date
    current_time = datetime.now()
    current_time= "--------------" + str(current_time) + "--------------"
    with open(f'{output_dir}/ram_logging.txt', 'a') as f:
        f.write(current_time)
        f.write("\n")
    with open(f'{output_dir}/cpu_logging.txt', 'a') as f:
        f.write(current_time)
        f.write("\n")
    
    
     # Get current Ram usage
    begin_ram_list = []
    for i in range(20):
        current_ram = (psutil.virtual_memory()[3]/1000000000)*1024
        begin_ram_list.append(current_ram)
        time.sleep(0.5)
    begin_ram = np.asarray(begin_ram_list).mean()
    print("Check Done ----------------------------")
    print("begin RAM(GB):", begin_ram)

 
    

    while True:
        cpu_usage, ram = tracking_memory_usage(begin_ram)

        with open(f'{output_dir}/ram_logging.txt', 'a') as f:
            f.write(str(ram))
            f.write("\n")
        with open(f'{output_dir}/cpu_logging.txt', 'a') as f:
            f.write(str(cpu_usage))
            f.write("\n")

if __name__ == "__main__":
    output_dir = "logging"
    main(output_dir)

