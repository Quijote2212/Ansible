# Import the necessary modules
import sys
import os
import re

# Define the function to stop a JVM
def stop_jvm(jvm_name):
    # Stop the JVM using AdminControl
    print("Stopping JVM: " + jvm_name)
    AdminControl.invoke(AdminControl.queryNames('type=JVM,name=' + jvm_name), 'stop')

# Check if this script is being run with wsadmin
if 'AdminConfig' not in globals():
    print("Error: This script should be run using wsadmin")
    sys.exit(1)

# Get the cell name using AdminConfig
cell_name = AdminControl.getCell()

# Get all server names in the cell using AdminConfig
servers = AdminConfig.list('ServerEntry').splitlines()
server_names = [re.findall('name=([^,]+)', s)[0] for s in servers]

# Get all JVM names in the cell using AdminControl
jvms = []
for server_name in server_names:
    server_id = AdminConfig.getid('/Server:' + server_name + '/')
    jvm_ids = AdminConfig.list('JavaVirtualMachine', server_id).splitlines()
    jvms.extend([re.findall('name=([^,]+)', jvm_id)[0] for jvm_id in jvm_ids])

# Stop each JVM in the cell
for jvm_name in jvms:
    stop_jvm(jvm_name)
