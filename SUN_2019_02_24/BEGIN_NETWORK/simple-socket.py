import socket
name = "www.python.org"
try:
    host = socket.gethostbyname(name)
    print(host)
except socket.gaierror as err:
    print("cannot resolve hostname: ", name, err)


print(socket.getfqdn("171.6.148.252"))
print(socket.getfqdn("8.8.4.4"))
print(socket.getfqdn("115.87.234.160"))
print(socket.getfqdn("1.1.1.1"))
print(socket.getfqdn("9.9.9.9"))

print(socket.gethostname())