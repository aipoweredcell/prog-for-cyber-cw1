# prog-for-cyber-cw1

# program overview

i made task 4 as a python script to manage and update security incident records using dictionaries. i implemented an incident_manager() function that handles dictionary creation, updates, deletions and loops through remaining data inside a main() block.

## code features

i set up i dictionary containing username, ip address, event type and risk level. u extracted and displayed specific fields at the start (username and ip address). i added a bew status field to "under investigation". i updated risk level to critical. i deleted event type using del. i used a for loop with .items() to print all remaining keys and values. i also used a len(incident) tp count and print the total number if key value pairs left.i structures the program with main() and if __name__ == "__main__":.

### how to run

open terminal in the repo folder and make sure you are on the correct branch. type in the gitbash terminal: py security_incident_manager.py

# image

![alt text](image.png)