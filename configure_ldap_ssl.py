# Import the necessary classes
from com.ibm.websphere.management import AdminClient
from com.ibm.websphere.security import SSLConfig
from com.ibm.websphere.security.ssl import SSLConfigHelper
from java.util import HashMap

# Define the function to configure LDAP SSL
def configureLDAPSSL():
    # Connect to the WebSphere server
    hostname = 'localhost'  # Change this to the correct hostname
    port = 8880  # Change this to the correct admin port
    username = 'admin'  # Change this to the correct username
    password = 'password'  # Change this to the correct password
    client = AdminClient.connect(hostname + ':' + str(port), username, password)

    # Get the LDAP server configuration
    ldapServer = AdminConfig.getid('/Cell:DefaultCell/Node:DefaultNode/Server:ldapServer/')
    ldapServerName = AdminConfig.showAttribute(ldapServer, 'name')

    # Change the LDAP port to 636
    ldapServerPortProps = AdminConfig.list('Property', ldapServer)
    for prop in ldapServerPortProps.splitlines():
        propName = AdminConfig.showAttribute(prop, 'name')
        if propName == 'sslEnabled':
            AdminConfig.modify(prop, [['value', 'true']])
            print('SSL enabled on LDAP server ' + ldapServerName)

    # Save the configuration
    AdminConfig.save()
    print('Changes saved successfully.')

# Call the function to configure LDAP with SSL
configureLDAPSSL()
