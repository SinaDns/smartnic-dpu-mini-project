/* xdp_simple.c -- tiny XDP program (drops ICMP packets)
 * Build with: clang -O2 -target bpf -c xdp_simple.c -o xdp_simple.o
 * Attach with: ip link set dev <iface> xdp obj xdp_simple.o sec xdp
 * Requires Linux (root) and iproute2 with XDP support.
 */
#include <linux/bpf.h>
#include <bpf/bpf_helpers.h>
#include <linux/if_ether.h>
#include <linux/ip.h>

SEC("xdp")
int xdp_prog(struct xdp_md *ctx) {
    void *data = (void *)(long)ctx->data;
    void *data_end = (void *)(long)ctx->data_end;

    struct ethhdr *eth = data;
    if ((void*)(eth + 1) > data_end) return XDP_PASS;

    if (eth->h_proto == __constant_htons(ETH_P_IP)) {
        struct iphdr *ip = data + sizeof(struct ethhdr);
        if ((void*)(ip + 1) > data_end) return XDP_PASS;
        if (ip->protocol == IPPROTO_ICMP) {
            // drop ICMP packets (educational example)
            return XDP_DROP;
        }
    }
    return XDP_PASS;
}

char _license[] SEC("license") = "GPL";