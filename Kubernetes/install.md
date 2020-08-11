+ pac kubectl minikube libvirt qemu dnsmasq ebtables
+ sudo systemctl start libvirtd.socket
+ sudo usermod -aG kvm $USER
+ sudo usermod -aG libvirt $USER
+ minikube start --driver=kvm2
+ kubectl cluster-info
