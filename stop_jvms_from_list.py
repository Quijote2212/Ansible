# Import the necessary modules
import sys

# Check if this script is being run with wsadmin
if 'AdminConfig' not in globals():
    print("Error: This script should be run using wsadmin")
    sys.exit(1)

# Get the cell name using AdminConfig
cell_name = AdminControl.getCell()

# Read the list of JVM names from a file
jvm_list_file = "jvm_list.txt"
with open(jvm_list_file) as f:
    jvms = [line.strip() for line in f]

# Stop each JVM in the cell using AdminControl
for jvm_name in jvms:
    jvm_object_name = AdminControl.queryNames('type=JVM,name=' + jvm_name)
    if jvm_object_name:
        AdminControl.invoke(jvm_object_name, 'stop')
        print("Stopped JVM: " + jvm_name)
