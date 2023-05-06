from typing import Any, Dict, Iterable, List, NewType, Set
from pyshark import FileCapture
from pyshark.packet.packet import Packet

from dds_traffic_analysis.plotter import Plotter
from dds_traffic_analysis.utils import add_key_to_dict

GuidPrefix = NewType('GuidPrefix', str)

UNKNOWN_GUID_PREFIX = GuidPrefix('Unknown')


def rtps_filter(packets: Iterable[Packet]):
    return [packet for packet in packets if 'RTPS' in str(packet.layers)]


class RtpsPackets:
    def __init__(self, packets: Iterable[Packet]) -> None:
        self._packets = rtps_filter(packets)
        self._dict: Dict[GuidPrefix, Dict[GuidPrefix, List[Packet]]] = {}
        
        
        for packet in self._packets:
            guid_prefix = GuidPrefix(packet.rtps.guidprefix_src)
            add_key_to_dict(self._dict, guid_prefix, {})
            dst_guid_prefix = packet.rtps.get_field('guidprefix_dst')
            if dst_guid_prefix is None:
                dst_guid_prefix = UNKNOWN_GUID_PREFIX
                
            add_key_to_dict(self._dict[guid_prefix], dst_guid_prefix, [])
            self._dict[guid_prefix][dst_guid_prefix].append(packet)
            
        print(self._dict)
        
        self._plotter = Plotter()
        # self._plotter.plot(self._dict)
        self._plotter.plot_per_node(self._dict)
                
                
        
    def __get_guid_prefixes(self) -> Set[str]:
        guid_prefixes = set()
        for packet in self._packets:
            guid_prefixes.add(packet.rtps.guidprefix)
        return guid_prefixes
    
    
    