# Importar las clases necesarias
from com.ibm.websphere.management import AdminClient
from com.ibm.websphere.security import SSLConfig
from com.ibm.websphere.security.ssl import SSLConfigHelper
from java.util import HashMap

# Definir la función para cambiar el puerto LDAP y activar SSL
def configureLDAPSSL():
    # Conectar al servidor WebSphere
    hostname = 'localhost'  # Cambia esto al nombre de host adecuado
    port = 8880  # Cambia esto al puerto de administración adecuado
    username = 'admin'  # Cambia esto al nombre de usuario adecuado
    password = 'password'  # Cambia esto a la contraseña adecuada
    client = AdminClient.connect(hostname + ':' + str(port), username, password)

    # Obtener la configuración del servidor LDAP
    ldapServer = AdminConfig.getid('/Cell:DefaultCell/Node:DefaultNode/Server:ldapServer/')
    ldapServerName = AdminConfig.showAttribute(ldapServer, 'name')

    # Cambiar el puerto LDAP a 636
    ldapServerPortProps = AdminConfig.list('Property', ldapServer)
    for prop in ldapServerPortProps.splitlines():
        propName = AdminConfig.showAttribute(prop, 'name')
        if propName == 'sslEnabled':
            AdminConfig.modify(prop, [['value', 'true']])
            print('SSL habilitado en el servidor LDAP ' + ldapServerName)

    # Guardar la configuración
    AdminConfig.save()
    print('Cambios guardados correctamente.')

# Llamar a la función para configurar LDAP con SSL
configureLDAPSSL()
