# /bin/bash
route add -net 10.1.2.0 netmask 255.255.255.0 dev thetap gw 10.1.1.2
route add -net 10.1.3.0 netmask 255.255.255.0 dev thetap gw 10.1.1.2
