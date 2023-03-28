# Import the necessary modules
import sys

# Check if this script is being run with wsadmin
if 'AdminConfig' not in globals():
    print("Error: This script should be run using wsadmin")
    sys.exit(1)

# Get the cell name using AdminConfig
cell_name = AdminControl.getCell()

# Get all server names in the cell using AdminConfig
servers = AdminConfig.list('ServerEntry').splitlines()
server_names = [server.split('name=')[1].split(',')[0] for server in servers]

# Get all JVM names in the cell using AdminControl
jvms = []
for server_name in server_names:
    server_id = AdminConfig.getid('/Server:' + server_name + '/')
    jvm_ids = AdminConfig.list('JavaVirtualMachine', server_id).splitlines()
    jvms.extend([jvm.split('name=')[1].split(',')[0] for jvm in jvm_ids])

# Stop each JVM in the cell using AdminControl
for jvm_name in jvms:
    jvm_object_name = AdminControl.queryNames('type=JVM,name=' + jvm_name)
    if jvm_object_name:
        AdminControl.invoke(jvm_object_name, 'stop')
        print("Stopped JVM: " + jvm_name)
