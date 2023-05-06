from pyshark import FileCapture
from dds_traffic_analysis.rtps import RtpsPackets


    
class Analyzer:
    def __init__(self, pcap_path: str) -> None:
        network_capture = FileCapture(pcap_path)
        initial_timestamp = network_capture[0].sniff_timestamp
        RtpsPackets(network_capture, float(initial_timestamp))
        
        
if __name__ == '__main__':
    Analyzer('./example2.pcapng')
        