ELAN is deployed in Microsoft Azure and the URL to access is: http://peldaws2.westus.cloudapp.azure.com/

 
If the website is not loading, probably the server is down. Execute the below to restart the server:

1. ssh peldaws2.westus.cloudapp.azure.com
Or with similar programs like putty on Windows.

2. Username: minchen 
   Password:  "Password1212"
 
3. sudo su
 
4. Then execute the commands like:
    ./serverStatus
    ./killServer
    ./runServer