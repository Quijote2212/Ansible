# Import the necessary modules
import sys
import os
import re

# Define the function to list all running JVMs
def list_running_jvms():
    # Get the running JVMs using AdminControl
    jvms = AdminControl.queryNames('type=JVM,*').splitlines()

    # Print the names of the running JVMs
    if len(jvms) > 0:
        print("Running JVMs:")
        for jvm in jvms:
            jvm_name = AdminControl.getAttribute(jvm, 'name')
            print("  " + jvm_name)
    else:
        print("No running JVMs found")

# Define the function to stop a JVM
def stop_jvm(jvm_name):
    # Stop the JVM using AdminControl
    print("Stopping JVM: " + jvm_name)
    AdminControl.invoke(AdminControl.queryNames('type=JVM,name=' + jvm_name), 'stop')

# Check if this script is being run with wsadmin
if 'AdminConfig' not in globals():
    print("Error: This script should be run using wsadmin")
    sys.exit(1)

# List all running JVMs
list_running_jvms()

# Ask the user if they want to stop all running JVMs
response = input("Do you want to stop all running JVMs? (y/n): ")
if response.lower() == 'y':
    # Get the running JVMs again
    jvms = AdminControl.queryNames('type=JVM,*').splitlines()

    # Stop each running JVM
    for jvm in jvms:
        jvm_name = AdminControl.getAttribute(jvm, 'name')
        stop_jvm(jvm_name)
