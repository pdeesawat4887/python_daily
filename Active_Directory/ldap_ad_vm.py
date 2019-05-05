import sys
from ldap3 import Server, Connection, ALL, NTLM, ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES, AUTO_BIND_NO_TLS, SUBTREE
from ldap3.core.exceptions import LDAPCursorError

server_name = '192.168.8.134'
domain_name = 'itsupport'
user_name = 'Administrator'
password = 'P@ssw0rd'

format_string = '{:25} {:>6} {:19} {:19} {}'
print(format_string.format('User', 'Logins', 'Last Login', 'Expires', 'Member Of'))

server = Server(server_name, get_info=ALL)
conn = Connection(server, user='{}\\{}'.format(domain_name, user_name), password=password, authentication=NTLM, auto_bind=True)
conn.search('dc={},dc=local'.format(domain_name), '(objectclass=person)', attributes=[ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES])
for e in conn.entries:
    try:
        mem = e.memberOf
    except LDAPCursorError:
        desc = ""
    print(format_string.format(str(e.name), str(e.logonCount), str(e.lastLogon)[:19], str(e.accountExpires)[:19], mem))
print(dir(e))
