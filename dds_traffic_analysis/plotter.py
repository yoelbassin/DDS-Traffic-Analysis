from typing import Any, Dict, List
import matplotlib.pyplot as plt
from pyshark.packet.packet import Packet

from dds_traffic_analysis.utils import add_key_to_dict

   


class Plotter:
    def __init__(self) -> None:
        pass
    
    
    def plot_per_node(self, _dict: Dict[str, Dict[str, List[Packet]]], initial_timestamp):
        fig, ax = plt.subplots()
        
        for guid_src, dst in _dict.items():
            packets_per_second: Dict[int, List[int]] = {}
            for packets in dst.values():
                for packet in packets:
                    sniff_time_sec = int(float(packet.sniff_timestamp))
                    add_key_to_dict(packets_per_second, sniff_time_sec, [])
                    packets_per_second[sniff_time_sec].append(int(packet.length))
            
            print(packets_per_second)
                
            ax.plot([x - int(initial_timestamp) for x in sorted(packets_per_second.keys())], [sum(vals) for vals in packets_per_second.values()], label=f'{guid_src}')

        ax.set(xlabel='time (s)', ylabel='bits per second')
        ax.grid()
        ax.legend()
        plt.show()
    
    def plot(self, _dict: Dict[str, Dict[str, List[Packet]]]):
        fig, ax = plt.subplots()
        
        for guid_src, dst in _dict.items():
            for guid_dst, packets in dst.items():
                packets_per_second: Dict[int, List[int]] = {}
                for packet in packets:
                    sniff_time_sec = int(float(packet.sniff_timestamp))
                    add_key_to_dict(packets_per_second, sniff_time_sec, [])
                    packets_per_second[sniff_time_sec].append(int(packet.length))
                    
                
                ax.plot(packets_per_second.keys(), [sum(vals) for vals in packets_per_second.values()], label=f'{guid_src}:{guid_dst}')

        ax.set(xlabel='time (s)', ylabel='bits per second')
        ax.grid()
        ax.legend()
        plt.show()