import matplotlib.pyplot as plt 
import numpy as np

def plot_cpu(cpu_data_filtered):
    time_range = np.arange(0,(len(cpu_data_filtered)+1)*0.2-0.2,0.2)
    # print(time_range)
    print(len(time_range), len(cpu_data_filtered))
    # plt.plot(ram_data_filtered, color='magenta', marker='o',mfc='pink' )
    # plt.plot(time_range, cpu_data_filtered)
    plt.plot(cpu_data_filtered, label= "% CPU")
    plt.xlabel("Time")
    plt.ylabel("% CPU")
    plt.title('CPU logging')
    plt.legend()
    plt.savefig("cpu_usage.png")
    plt.clf()

def plot_ram(ram_data_filtered, avg_ram):
    
    time_range = np.arange(0,(len(ram_data_filtered)+1)*0.2-0.2,0.2)
    # print(time_range)
    print(len(time_range), len(ram_data_filtered))
    # plt.plot(ram_data_filtered, color='magenta', marker='o',mfc='pink' )
    plt.plot(ram_data_filtered, label= "Ram (MB)")
    plt.axhline(y = avg_ram, color = 'r', linestyle = '-')
    plt.xlabel("Time (x0.2s)")
    # plt.ylabel("")
    plt.title('Ram logging')
    plt.legend()
    plt.savefig("ram_usage.png")
    plt.clf()


cpu_data = []
ram_data = []
with open('logging/cpu_logging.txt') as f:
    cpu_data = []
    for line in f:
        # print(line.rstrip())
        cpu_data.insert(0, line.rstrip())

with open('logging/ram_logging.txt') as f:
    ram_data = []
    for line in f:
        ram_data.insert(0, line.rstrip())
print(len(cpu_data))


# filter latest data
cpu_data_filtered = []
ram_data_filtered = []
for line in cpu_data:
    if line[0:2] == "--":
        break
    cpu_data_filtered.append(line)
    

for line in ram_data:
    if line[0:2] == "--":
        break
    ram_data_filtered.append(line)
    


cpu_data_filtered_np = np.asarray(cpu_data_filtered, dtype=np.float)
plot_cpu(cpu_data_filtered_np[cpu_data_filtered_np>2])

# Get Average Ram usage during training
ram_data_filtered_np = np.asarray(ram_data_filtered, dtype=np.int)
avg_ram  = ram_data_filtered_np[ram_data_filtered_np>463].mean()
print(type(ram_data_filtered_np))
print("Average Ram usage",avg_ram)

plot_ram(ram_data_filtered_np[ram_data_filtered_np>463],avg_ram)






