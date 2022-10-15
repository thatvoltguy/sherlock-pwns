from xml.etree import ElementTree as ET
import subprocess

def nmap_scan(ip, options, port_selector, ports):
    ret_bytes = subprocess.check_output(["sudo", "nmap", options, ip, port_selector, ports, "-oX", f"{ip}_nmap.xml"])
    return ret_bytes.decode
