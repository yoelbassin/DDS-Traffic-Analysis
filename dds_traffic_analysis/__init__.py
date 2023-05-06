from pyshark import FileCapture
from dds_traffic_analysis.rtps import RtpsPackets


    
class Analyzer:
    def __init__(self, pcap_path: str) -> None:
        network_capture = FileCapture(pcap_path)
        RtpsPackets(network_capture)
        
        
if __name__ == '__main__':
    Analyzer('./example.pcapng')
        