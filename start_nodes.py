# Import the necessary modules
import sys

# Check if this script is being run with wsadmin
if 'AdminConfig' not in globals():
    print("Error: This script should be run using wsadmin")
    sys.exit(1)

# Get the cell name using AdminControl
cell_name = AdminControl.getCell()

# Get the list of servers using AdminTask
server_list = AdminTask.listServers('[-serverType APPLICATION_SERVER -serverType NODE_AGENT]').splitlines()

# Start each server in the cell using AdminControl
for server_name in server_list:
    server_object_name = AdminControl.completeObjectName('type=Server,node=' + cell_name + ',process=' + server_name + ',*')
    if server_object_name:
        AdminControl.startServer(server_object_name)
        print("Started server: " + server_name)
    else:
        print("Server object not found for server: " + server_name)
