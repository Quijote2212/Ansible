# Importar módulos necesarios
import sys
import java

# Establecer las variables de entorno
was_home = "/ruta/a/tu/instalacion/de/WebSphere"
node_name = "nombre_del_nodo"
server_name = "nombre_del_servidor"
new_ldap_port = "nuevo_puerto_ldap"

# Conectar al servidor WebSphere
cell_name = "nombre_de_la_celda"
server_type = "APPLICATION_SERVER"  # Cambiar a "DEPLOYMENT_MANAGER" si es necesario
host_name = "nombre_del_host"
dmgr_port = "puerto_del_DMGRR"
username = "nombre_de_usuario"
password = "contraseña"

try:
    print "Conectando a WebSphere..."
    AdminTask.listServers()

    server_obj = AdminConfig.getid("/Node:%s/Server:%s/" % (node_name, server_name))
    ldap_obj = AdminConfig.list("LDAPServer", server_obj)

    # Actualizar el puerto LDAP
    AdminConfig.modify(ldap_obj, [['ldapPort', new_ldap_port]])

    # Guardar los cambios
    AdminConfig.save()

    # Sincronizar las configuraciones
    AdminNodeManagement.syncActiveNodes()

    # Reiniciar el servidor (si es necesario)
    # AdminControl.invoke(AdminControl.queryNames('cell=%s,node=%s,process=%s,*' % (cell_name, node_name, server_name)), 'restart')

    print "Los cambios se aplicaron correctamente."

except Exception, e:
    print "Error: %s" % e

