#!/bin/bash

# 1. Create a new directory in linux and copy first 2000 lines from existing file to new file
mkdir -p ~/install/hdfsusecases
head -2000 ~/pigdata/NYSE_daily.txt >> ~/install/hdfsusecases/NYSE_2020_06_20.txt

# 2. Create another file copying lines 2001 to 3000 from the existing file
head -3000 ~/pigdata/NYSE_daily.txt | tail -1000 >> ~/install/hdfsusecases/NYSE_2020_06_21.txt

# 3. Create a directory in Hadoop
hadoop fs -mkdir -p /user/hduser/tmp/hdfsusecases

# 4. Check if the directory is created in HDFS
hadoop fs -test -d /user/hduser/tmp

# 5. Check status code of the command
echo $?

# 6. Copy file from linux to hdfs
hadoop fs -put ~/install/hdfsusecases/NYSE_2020_06_20.txt /user/hduser/tmp/hdfsusecases/NYSE_2020_06.txt
# Or
hadoop fs -copyFromLocal ~/install/hdfsusecases/NYSE_2020_06_20.txt /user/hduser/tmp/hdfsusecases/NYSE_2020_06.txt

# 7. Check if file is created and create a zero byte file in HDFS
hadoop fs -test -f /user/hduser/tmp/hdfsusecases/NYSE_2020_06.txt
echo $?
hadoop fs -touchz /user/hduser/tmp/hdfsusecases/_SUCCESS

# 8. Append the file generated in step 2 in linux with the file generated in step 6 in the hdfs directory
hadoop fs -appendToFile ~/install/hdfsusecases/NYSE_2020_06_21.txt /user/hduser/tmp/hdfsusecases/NYSE_2020_06_20.txt

# 9. Count the size of the file in HDFS
hadoop fs -du -h /user/hduser/tmp/hdfsusecases/NYSE_2020_06_20.txt

# 10. Count the number of rows in the file
hadoop fs -cat /user/hduser/tmp/hdfsusecases/NYSE_2020_06.txt | wc -l

# 11. Display lines 11 to 20 from the file
hadoop fs -cat /user/hduser/tmp/hdfsusecases/NYSE_2020_06.txt | head -20 | tail -10

# 12. Store lines 11 to 20 into a linux file
hadoop fs -cat /user/hduser/tmp/hdfsusecases/NYSE_2020_06.txt | head -20 | tail -10 >> ~/install/hdfsusecases/NYSE_sampledata1.txt

# 13. Delete the first line from the file
# (This step cannot be performed directly due to the WORM property of HDFS data)

# 14. Copy the file with a new name
hadoop fs -cp /user/hduser/tmp/hdfsusecases/NYSE_2020_06.txt /user/hduser/tmp/hdfsusecases/NYSE_2020_06_bkp.txt

# 15. Merge the files into Linux directory
# (This step is left blank as merging files requires a different approach)

# 16. Set the blocksize to 64MB and check the number of blocks generated
hadoop fs -Ddfs.blocksize=64M -put -f ~/pigdata/NYSE_daily.txt /user/hduser/tmp/hdfsusecases/Orginall/org.txt

# 17. Set the blocksize to 128MB and replace the existing file
hadoop fs -Ddfs.blocksize=128M -put -f ~/pigdata/NYSE_daily.txt /user/hduser/tmp/hdfsusecases/Orginall/org_128mb.txt

# 18. Set the replication to 3 while writing the file in HDFS
hadoop fs -Ddfs.replication=3 -put -f ~/pigdata/NYSE_daily.txt /user/hduser/tmp/hdfsusecases/Orginall/org_3r.txt

# 19. To check the block information
hdfs fsck /user/hduser/tmp/hdfsusecases/Orginall/org_3r.txt -files -blocks -locations

# 20. Important Command DistCp
# (This step is left blank as it requires specific details about the clusters involved)

# 21. Choose to overwrite the target files unconditionally even if it exists using upto 2 mappers depends
# (This step is left blank as it requires specific details about the clusters involved)

# 22. To view the content of editlog file, need to convert into xml file using editlog viewer
# (This step is left blank as it requires specific details about the Hadoop configuration and setup)
