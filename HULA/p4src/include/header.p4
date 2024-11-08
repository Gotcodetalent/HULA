/*************************************************************************
*********************** H E A D E R S  ***********************************
*************************************************************************/
const bit<16> TYPE_IPV4 = 0x800;
typedef bit<9> egressSpec_t;
typedef bit<48> macAddr_t;
typedef bit<32> ip4Addr_t;
typedef bit<32> tor_id_t;
header ethernet_t
{
    macAddr_t dstAddr;
    macAddr_t srcAddr;
    bit<16> etherType;
}
header ipv4_t
{
    bit<4> version;
    bit<4> ihl;
    bit<6> dscp;
    bit<2> ecn;
    bit<16> totalLen;
    bit<16> identification;
    
    bit<3> flags;
    bit<13> fragOffset;
    bit<8> ttl;
    bit<8> protocol;
    bit<16> hdrChecksum;
    ip4Addr_t srcAddr;
    ip4Addr_t dstAddr;
}
header probe_t
{
    bit<24> dst_tor;
    bit<8> path_util;
    bit<8> var;
    bit<8> ttl;
}
header tcp_t
{
    bit<16> srcPort;
    bit<16> dstPort;
    bit<32> seqNo;
    bit<32> ackNo;
    bit<4> dataOffset;
    bit<4> res;
    bit<1> cwr;
    bit<1> ece;
    bit<1> urg;
    bit<1> ack;
    bit<1> psh;
    bit<1> rst;
    bit<1> syn;
    bit<1> fin;
    bit<16> window;
    bit<16> checksum;
    bit<16> urgentPtr;
}
struct metadata
{
    bit<1> sfmode;
    bit<9> nxt_hop;
    bit<32> self_id;
    bit<32> dst_tor;
    bit<14> ecmp_hash;
    bit<14> ecmp_group_id;
    
    bit<1> redundancy;
    bit<48> flowlet_last_stamp;
    bit<48> flowlet_time_diff;
    bit<13> flowlet_register_index;
    bit<16> flowlet_id;   
    
    
    bit<16> num_nhops;
    
    
    bit<1> random_path;
}
struct headers
{
    ethernet_t ethernet;
    ipv4_t ipv4;
    tcp_t tcp;
    probe_t probe;
}
