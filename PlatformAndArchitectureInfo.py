import psutil;
import platform;
import datetime;

def CPU_Info_OS():
	print("\nCPU Info OS:");
	if platform.system()=='Windows':
		return platform.processor();
	elif platform.system()=='Darwin':
		command='/usr/sbin/sysctl -n machdep.cpu.brand_string';
		return popen(command).read().strip();	
	elif platform.system()=='Linux':
		command='cat/proc/cpuinfo';
		return popen(command).read().strip();
	return 'Platform not identified';

def get_size(bytes,suffix="B"):
	factor=1024;
	for unit in ["","K","M","G","T","P"]:
		if bytes<factor:
			return f"{bytes:.2f}{unit}{suffix}";
		bytes/=factor;

def Platform_Info():
	print("\nPlatform Info:");
	uname=platform.uname();
	print(f"System:{uname.system}");
	print(f"Node name:{uname.node}");
	print(f"Release:{uname.release}");
	print(f"Version:{uname.version}");
	print(f"Machine:{uname.machine}");
	print(f"Processor:{uname.processor}");

def CPU_Info():
	print("\nCPU Info:");
	print("Physical cores:",psutil.cpu_count(logical=False));
	print("Total cores:",psutil.cpu_count(logical=True));
	print("Therefor number of threads per core can run: ",int(psutil.cpu_count(logical=True)/psutil.cpu_count(logical=False)));

	cpufreq=psutil.cpu_freq();
	print(f"Maximum Frequency: {cpufreq.max:.2f}MHz");
	print(f"Minimum Frequency: {cpufreq.min:.2f}MHz");
	print(f"Current Frequency: {cpufreq.current:.2f}MHz");

	print("CPU usage per core: ");
	for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
		print(f"Core {i}: {percentage}%");
	print(f"Total cpu usage: {psutil.cpu_percent()}%");

def Boot_Info():
	print("\nBoot info:");
	boot_time_timestamp=psutil.boot_time();
	bt=datetime.datetime.fromtimestamp(boot_time_timestamp);
	print(f"Boot time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}");

def RAM_Usage():
	print("\nRAM usage:");

	abc=psutil.virtual_memory();

	print(f"Total: {get_size(abc.total)}");
	print(f"Available: {get_size(abc.available)}");
	print(f"Percentage: {get_size(abc.percent)}%");
