#!/bin/bash

set -o errexit -o nounset -o xtrace

echo 'LXC_DOMAIN="lxc"' >> /etc/default/lxc
/usr/lib/x86_64-linux-gnu/lxc/lxc-net restart
source /etc/default/lxc-net && echo "server=/lxc/${LXC_ADDR}" >> /etc/dnsmasq.d/lxc
awk '/nameserver/{print "server=" $2}' /etc/resolv.conf >> /etc/dnsmasq.conf
echo "nameserver 127.0.0.1" > /etc/resolv.conf
/etc/init.d/dnsmasq restart
echo "lxc.apparmor.allow_incomplete = 1" >> /etc/lxc/default.conf # required on Debian unstable
