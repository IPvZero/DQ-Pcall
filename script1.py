from pyats.async_ import pcall
from genie.conf import Genie
from genie.utils import Dq
from genie.testbed import load
from rich import print

def get_ospf(hostname, dev):
    #get show output from routing table
    parsed = dev.parse('show ip route')
    #use DQ to parse the OSPF routes from the routing table
    get_routes = (Dq(parsed).contains('O').get_values('routes'))
    #count the number of those OSPF entries
    num_routes = len(get_routes)
    print(f"{hostname} has {num_routes} OSPF routes in its routing table")

def main():
    #load testbed
    testbed = load('testbed.yaml')
    #connect and suppress output
    testbed.connect(log_stdout=False)
    #use pcall to execute on all devices in parallel
    pcall(get_ospf, hostname=testbed.devices, dev=testbed.devices.values())

if __name__ == "__main__":
    main()
