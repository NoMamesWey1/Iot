# IoT Data Analysis

This project focuses on creating a server-client architecture for IoT data analysis. The server connects to a MongoDB database, downloads data, and performs analysis on the data. The client can query the server in real-time to retrieve the analyzed results.

## Description

The program execution follows the following steps:

**Step 1:** The client establishes the port and IP address of the server.

**Step 2:** The client sends a packet of data to query the server.

**Step 3:** The server connects to the MongoDB server and downloads the latest data.

**Step 4:** The server analyzes the data and determines which sensor has the best average time. It then sends the name of the associated road to the client.

**Step 5:** The client receives the response from the server and prints out the best road to take based on the current data.

## Technologies Used

The project utilizes the following technologies:

- MongoDB: A NoSQL database used to store and retrieve the IoT data.
- Dataniz: A data analysis library used to analyze the downloaded data.
- Google Cloud VM: A virtual machine platform used to run the code both locally and on the cloud.

## Execution

To run the program:

1. Set up a MongoDB database and ensure it is accessible.
2. Configure the server with the appropriate MongoDB connection settings.
3. Start the server program on the desired machine or cloud VM.
4. Set up the client program with the server's IP address and port.
5. Run the client program to send queries to the server and receive the analyzed results.
