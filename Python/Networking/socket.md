### 1.Socket
- A python module which provides access to BSD Socket interface.
- It is available on all modern Unix systems, Windows, MacOS, and probably additional platforms.
- It is starightforward transliteration of Unix system call and interface for sockets in Python OOP style.

### 2. Functions:
##### 2.1 Creating Socket Object:
- socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
- socketpair([family[, type[, proto]]])
- create_connection(address, timeout= GLOBAL_DEFAULT, source_address=None, '*', all_errors=False)
- create_server(address, *, family=AF_INET, backlog=None, reuse_port=False, dualstack_ipv6=False)
- fromfd(fd, family, type, proto=0)
- fromshare(data)

##### 2.2 Other functions:
- close(fd)
- getaddrinfo(host, port, family=0, type=0, proto=0, flags=0)
- getfqdn([name])
- gethostbyname(hostname)
- gethostbyname_ex(hostname)
- gethostname()
- gethostbyaddr(ip_address)
- getnameinfo(sockaddr, flags)
- getnameinfo(sockaddr, flags)
- getprotobyname(protocolname)
- getservebyname(servicename[, protocolname])
- getservbyport(port,  [, protocolname])
- ntohl(x)
- ntohs(x)
- htonl(x)
- htons(s)
- inte_aton(ip_string)
- inet_ntoa(packed_ip)
- inet_pton(address_family, ip_string)
- inet_atop(address_family, packed_ip)
- CMSG_LEN(length)
- CMSG_SPACE(length)
- getdefaulttimeout()
- setdefaulttimeout(timeout)
- sethostname(name)
- if_nameindex()
- if_nametoindex(if_name)
- if_indextoname(if_index)
- send_fds(sock, buffers, fds[, flags[, address]])
- recv_fds(sock, bufsize, maxfds[, flags])

##### 2.3 Function creating a socket object
+ `socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)`
    - Create a socket Object from given params.
    - Parametes:
        - `family`: Address family
        - `type`:  Socket type
        - `proto`: Protocol number

- `socketpair([family[, type[, proto]]])`
    - Build a pair of socket object from given params
+ `create_connection(address, timeout= GLOBAL_DEFAULT, source_address=None, '*', all_errors=False)`
    - Creates a TCP service listening on the internet address, and returns an Object.
    - Parametes:
        - `address`: A 2-tuple (host, port)
- `create_server(address, *, family=AF_INET, backlog=None, reuse_port=False, dualstack_ipv6=False)`
    - Create a TCP Socket bound to address and returns socket object.
    - Parametes:
        - `address`: A 2-tuple (host, port)
        - `family`: Address family (Either AF_INET or AF_INET6)
        - `backlog`: Queue size passed to socket.listen()
        - `reuse_port`: Sets SO_REUSEPORT socket option
        - `dualstack_ipv6`: Enable use of both IPv4 and IPv6
+ fromfd(fd, family, type, proto=0)
- fromshare(data)
+ has_dualstack_ipv6()
- SocketType



##### Socket object
- Property:
    - family
    - type
    - proto
- Methods:
    - accept()
    - bind(address)
    - close()
    - connect(address)
    - connect_ex(address)
    - detach()
    - dup()
    - fileno()
    - get_inheritable()
    - getpeername()
    - getsockname()
    - getsockopt(level, optname[, buflne])
    - getblocking()
    - gettimeout()
    - ioctl(control, option)
    - listen([backlog])
    - makefile(mode='r', buffering=None, *, encoding=None, errors=None, newline=None)
    - recv(bufsize, [, flags])
    - recvfrom(bufsize, [, flags])
    - recvmsg(bufsize, [, ancbufsize[, flags]])
    - recvmsg_into(bufsize, [, ancbufsize[, flags]])
    - recvfrom_into(buffer[, nbytes[, flags]])
    - recv_into(buffer[, nbytes[, flags]])
    - send(bytes[, flags])
    - sendall(bytes[, flags])
    - sendto(bytes, address)
    - sendto(bytes, flags, address)
    - sendmsg(buffers[, ancdata[, flags[, address]]])
    - sendmsg_afalg([msg, ]*, op[, iv[, assoclen[, flags]]]) 
    - sendfile(file, offset=0, count=None)
    - set_inheritable(inheritable)
    - setblocking(flag)
    - settimeout(value)
    - setsockopt(level, optname, value:int)
    - setsockopt(level, optname, value:buffer)
    - setsockopt(level, optname, None optlen:int)
    - shutdown(how)
    - share(process_id)


#### Some Constanst
##### socket type
- socket.SOCK_STREAM
- socket.SOCK_DGRAM
- socket.SOCK_RAW
- socket.SOCK_RDM
- socket.SOCK_SEQPACKET
- socket.SOCK_CLOEXEC
- socket.SOCK_NONBLOCK


##### socket proto
- socket.CAN_RAW
- socket.CAN_BCM
- socket.CAN_ISOTP 
- socket.CAN_J1939.


##### socket family
- socket.AF_INET
- socket.AF_INET6
- socket.AF_UNIX
- socket.AF_CAN
- socket.AF_PACKET
- socket.AF_RDS



