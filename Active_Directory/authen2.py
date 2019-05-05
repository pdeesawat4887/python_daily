import ldap

if __name__ == "__main__":
    ldap_server = "192.168.8.134"
    username = "Administrator"
    password = "P@ssw0rd"
    # the following is the user_dn format provided by the ldap server
    user_dn = "uid=" + username + ",dc=itsupport,dc=local"
    # adjust this to your base dn for searching
    base_dn = "dc=itsupport,dc=local"
    connect = ldap.initialize('ldap://' + ldap_server)
    search_filter = "uid=" + username
    try:
        # if authentication successful, get the full user data
        connect.bind_s(user_dn, password)
        result = connect.search_s(base_dn, ldap.SCOPE_SUBTREE, search_filter)
        # return all user data results
        connect.unbind_s()
        print(result)
    except ldap.LDAPError as error:
        connect.unbind_s()
        print(error)
        print("authentication error")
