service-check
=============

Python script for checking and restarting Windows services

## Setup

Batch file calls the function in python file. Add service names as arguments to the batch file.
Python file needs sender, receiver, and smtp server configured.

## Use

Run the batch file to check the service. Or setup batch file in scheduled task.
This file only check locally

## To Run from Remote computer alter the following lines:
    myserver = sys.argv[1]
    service = ServiceToCheck
    command = 'SC ' + myserver + ' query '+ service +' | find "STATE"'
    restart = 'SC ' + myserver + ' start '+ service
    
    for s in sys.argv[2:]:
    ServiceCheck(s)
    
Batch file would take the first argument as the remote server