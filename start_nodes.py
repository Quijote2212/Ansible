# Import the necessary modules
import sys

# Check if this script is being run with wsadmin
if 'AdminConfig' not in globals():
    print("Error: This script should be run using wsadmin")
    sys.exit(1)

# Get the cell name using AdminConfig
cell_name = AdminControl.getCell()

# Get the list of nodes using AdminTask
node_list = AdminTask.listNodes().splitlines()

# Start each node in the cell using AdminControl
for node_name in node_list:
    node_agent_object_name = AdminControl.completeObjectName('type=NodeAgent,node=' + node_name + ',*')
    if node_agent_object_name:
        AdminControl.invoke(node_agent_object_name, 'start', '[]')
        print("Started node: " + node_name)
    else:
        print("Node agent object not found for node: " + node_name)
