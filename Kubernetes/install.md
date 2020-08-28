+ pac kubectl minikube libvirt qemu dnsmasq ebtables
+ sudo systemctl start libvirtd.socket
+ sudo usermod -aG kvm $USER
+ sudo usermod -aG libvirt $USER
+ minikube start --driver=kvm2
+ kubectl cluster-info

+ on reboot we need to start minikube but before that 
+ we also need to start service as `sudo systemctl start libv**** something like that`
+ 