import platform
import psutil


def operating_system_info():
    uname = platform.uname()
    print(f"system: {uname.system}")
    print(f"node name: {uname.node}")
    print(f"release: {uname.release}")
    print(f"version: {uname.version}")
    print(f"machine: {uname.machine}")
    print(f"processor: {uname.processor}")

def prosesor():
    print(psutil.cpu_count(logical=False))
    print(psutil.cpu_count(logical=True))

    cpu_freq = psutil.cpu_freq()
    print(cpu_freq.max)
    print(cpu_freq.min)
    print(cpu_freq.current)

    for i , percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"core {i}: {percentage}%")

    print(f"totoal cpu usage: {psutil.cpu_percent()}%")


def memory_details():
    svmem = psutil.virtual_memory()
    print(f"total: {svmem.total}")
    print(f"available: {svmem.available}")
    print(f"used: {svmem.used}")
    print(f"percentage: {svmem.percent}%")

    print(40 * "*")

    swap = psutil.swap_memory()
    print(f"total: {swap.total}")
    print(f"free: {swap.free}")
    print(f"used: {swap.used}")
    print(f"percentage: {swap.percent}%")

def partition_disk():
    partition = psutil.disk_partitions()
    for part in partition:
        print(10 * "-")
        print(f"device: {part.device} -> {part.mountpoint} -> {part.fstype}")
        try:
            partition_usage = psutil.disk_usage(part.mountpoint)
        except PermissionError:
            continue
        print(f"total size: {partition_usage.total}")
        print(f"used: {partition_usage.used}")
        print(f"free: {partition_usage.free}")
        print(f"percentage: {partition_usage.percent}%")

    print(40 * "*")
    disk_io = psutil.disk_io_counters()
    print(f"total read: {disk_io.read_bytes}")
    print(f"total write: {disk_io.write_bytes}")

def network_info():
    if_address = psutil.net_if_addrs()
    for interface_name, interface_address in if_address.items():
        for address in interface_address:
            print(f"---- {interface_name} ----")
            if str(address.family) == 'AddressFamily.AF_INET':
                print(f"ip address: {address.address}")
                print(f"netmask: {address.netmask}")
                print(f"boardcast ip: {address.broadcast}")
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                print(f"mac address: {address.address}")
                print(f"netmask: {address.netmask}")
                print(f"boardcast mac: {address.broadcast}")
    net_io = psutil.net_io_counters()
    print(f"totla bytes sent: {net_io.bytes_sent}")
    print(f"totla bytes received: {net_io.bytes_recv}")

print(psutil.sensors_battery().percent)

operating_system_info()
print(10 * '=')
memory_details()
print(10 * '=')
partition_disk()
print(10 * '=')
network_info()

