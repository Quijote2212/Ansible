import AdminConfig
import AdminTask

ldap_settings = AdminConfig.list('LDAPServer')
print(ldap_settings)

ldap_servers = AdminConfig.list('LDAPServer').splitlines()
for ldap_server in ldap_servers:
    server_name = AdminConfig.showAttribute(ldap_server, 'name')
    ldap_host = AdminConfig.showAttribute(ldap_server, 'host')
    ldap_port = AdminConfig.showAttribute(ldap_server, 'port')

    print("LDAP Server: {} - Host: {} - Port: {}".format(server_name, ldap_host, ldap_port))

exit()
