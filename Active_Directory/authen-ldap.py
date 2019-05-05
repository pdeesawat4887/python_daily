#!/usr/bin/env python

import ldap
def authenticate(address, username, password):
    domain_name = 'itupport'
    conn = ldap.initialize('ldap://' + address)
    conn.protocol_version = 3
    conn.set_option(ldap.OPT_REFERRALS, 0)
    # conn.search('dc={},dc=local'.format(domain_name), '(objectclass=person)',attributes=[ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES])
    # base_dn = "dc=itsupport,dc=local"
    # search_filter = "uid=" + username
    # e = conn.search(base_dn, ldap.SCOPE_SUBTREE, search_filter)
    # print(e)
    return conn.simple_bind_s(username, password)

print(authenticate('192.168.8.134', 'pacharapold@itsupport.local', 'Thailand4887'))
print(authenticate('192.168.8.134', 'linuxos@itsupport.local', 'Thailand4887'))