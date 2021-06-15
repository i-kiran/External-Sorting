# External-Sorting
## An implementation of external sorting with the N-way merge algorithm covered in the live session.
Dataset creation:
For this question, you would have to create a synthetic table (simulating sales records of department stores) containing
50000 records. Each record in this file contains four fields: (1) Transaction ID (an integer), (2) Transaction sale amount
(an integer), (3) Customer name (string) and, (4) category of item. Transaction ID is an integer to identify each transaction
uniquely in the dataset. You can create this field using a simple “counter” in your code. Transaction sale amount is a
random integer between 1 and 60000. Customer name is a random 3 letter string. You can model this as a character array
of length 3. Category of the item is a random integer between 1 --1500.
After creating this dataset, you need to simulate its storage on a disk. Define a disk block as a file which can store
only B records of the synthetic table. Assume an unspanned organization i.e., records are not allowed to span across two
disk blocks. Following this store your entire synthetic table as a collection of these “disk blocks.” Each disk block
(simulated as a file) should have a unique name, for that you can name them as 1.txt, 2.txt, 3.txt, ..., etc. Basically, your
original synthetic sales table would be stored as a series of files. For e.g., if B=300, then the first disk block (file) would
store Row 1 -- Row 300; the second disk block (second file) would store Row 301 – Row 600. Do not hard code the value
of B. It may be changed during the evaluation.
For sake of simplicity use text files for simulating the disk blocks. Also note that each disk block should have an
entry at its end which stores the file name of the next disk block for the file. Additionally, in your code you should store
the file name of the first disk block of the synthetic sales table. This would be needed at a later stage to perform a linear
scan through the file. You need to sort the file on the transaction sale amount. Note that all the intermediate runs
(created during the sort process) should be managed/stored as “simulated disk blocks” only. Finally, your code
should produce a txt file as output which contains the records in the sorted order.
## Details of Simulated Main Memory:
Assume that you have space for storing only M “simulated disk blocks” in the main memory. In other words, you are
allowed to read/operate on a maximum of M “simulated disk blocks” at a time. Do not hard code the value of M. It may
be changed during the evaluation.
