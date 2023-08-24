#!/bin/bash

while true; do
    # Stop the message flow
    mqsistopmsgflow IF21P01MQ_SFDCCRM01_PROD -e SFDCCRM_EXEC1
    
    # Rotate the log file /var/log/messages
    mv /var/log/messages /var/log/messages.old
    touch /var/log/messages
    
    # Start the message flow
    mqsistartmsgflow IF21P01MQ_SFDCCRM01_PROD -e SFDCCRM_EXEC1
    
    # Wait for a moment to stabilize the flow
    sleep 10
    
    # Look for the "INVALID_SESSION_ID" error in the log file
    if grep -q "INVALID_SESSION_ID" /var/log/messages; then
        echo "INVALID_SESSION_ID error found. Re-running from the beginning."
    else
        echo "INVALID_SESSION_ID error not found. The process is complete."
        break
    fi
done
