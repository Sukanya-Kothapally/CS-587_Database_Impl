# CS587 Database Implementation Project 

# PART 1 - Goal
Project part1 is generate data according to Wisconsin Benchmark.The benchmark data is loaded into a system(which has sql interface).


## Demonstrate you have loaded data into that system
https://github.com/Sukanya-Kothapally/CS-587_Database_Impl/blob/main/ONEKTUP.png
https://github.com/Sukanya-Kothapally/CS-587_Database_Impl/blob/main/TENKTUP.png
https://github.com/Sukanya-Kothapally/CS-587_Database_Impl/blob/main/Rows.png

## Brief description of your data generation process including what program you used to generate the data.
We generated data using python language. As mentioned in the paper we have generated two csv files named ONEKTUP and TENKTUP and populated the data rowwise as in for each row what are the required values. We initially created two empty tables using pgadmin4 interface and populated the tables with respective data that is generated from a python code.
For populating the empty tables we simply followed the importing csv files option, with that, data from the csv file being imported into the appropriate table.

## Which system you will be working with and why you chose it?
We choose PostgreSQL as we are familiar with it and have some experience from previous terms(used in CS586). We also feel that it has a user friendly interface and convenient to use. Also postgres is free to download and provides a easy way to connect it through pgAdmin.

## Include lessons learned or issues encountered
* We planned to work on a single VM instance and gave owner permission to access the instance for both of us. But, initially only one of us was able to connect to that instance from pgadmin while the other couldn’t. This issue was fixed by adding both of our IP addresses in the firewall rule.
* For generating random data for unique2 attribute we just used a random function from random library. This produced duplicate random numbers. To fix this issue we used sample function from random library to generate random unique numbers. 

## Extra credit for doing the project as a container or VM.
* We implemented this project on a GCP VM.
https://github.com/Sukanya-Kothapally/CS-587_Database_Impl/blob/main/VM.PNG
