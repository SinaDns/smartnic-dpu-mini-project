// basic_l2.p4 -- minimal P4_16 L2 forwarding example (educational)
#include <core.p4>

typedef bit<48> mac_t;

header ethernet_t {
    mac_t dstAddr;
    mac_t srcAddr;
    bit<16> ethType;
}

struct headers {
    ethernet_t ethernet;
}

parser MyParser(packet_in packet, out headers hdr, inout standard_metadata_t meta) {
    state start {
        packet.extract(hdr.ethernet);
        transition accept;
    }
}

control Ingress(inout headers hdr, inout standard_metadata_t meta) {
    // simple exact-match table: forward based on dst MAC -> port
    action forward(bit<9> port) {
        meta.egress_spec = port;
    }

    action drop() {
        meta.egress_spec = 0; // 0 usually means DROP in simple setups
    }

    table mac_forwarding {
        key = {
            hdr.ethernet.dstAddr: exact;
        }
        actions = { forward; drop; }
        size = 1024;
        default_action = drop();
    }

    apply {
        if (hdr.ethernet.isValid()) {
            mac_forwarding.apply();
        }
    }
}

control Egress(inout headers hdr, inout standard_metadata_t meta) { apply { } }
control Deparser(packet_out packet, in headers hdr) { apply { packet.emit(hdr.ethernet); } }

V1Switch(MyParser(), Ingress(), Egress(), Deparser()) main;