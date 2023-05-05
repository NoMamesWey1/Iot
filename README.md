# IoT

Description: Created a Server that will connect to a MongoDB database and will download some data and parse it, and created a Client to query the server for the resulting data in real time. Used MongoDB, Dataniz, and Google Cloud VM to be able to run the code Locally and on the Cloud.

The program execution:

Step 1: The Client establishes the port and IP address of your Server

Step 2: Your Client sends a packet of data to query the Server

Step 3: Your Server connects to and downloads the current data from your MongoDB Server

Step 4: Your Server figures out which sensor has the best average time, and sends the name of the associated road to the Client

Step 5: Your Client prints out which road is the best one to take given your current data
