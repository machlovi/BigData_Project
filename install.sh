#!/bin/sh
cat workers | while read line
do
    if [ "$line" = "-" ]; then
        echo "Skip $line"
    else
        ssh root@$line -n "rm -rf /BigData_Project/ && mkdir /BigData_Project/"
        echo "Copy data to $line"
        scp  /BigData_Project/setup.py root@$line:/BigData_Project/ && scp /BigData_Project/manager root@$line:/BigData_Project/ && scp /BigData_Project/workers root@$line:/BigData_Project/
        echo "Setup $line"
        ssh root@$line -n "cd /BigData_Project/ && python3 setup.py && ntpdate time.nist.gov"
        echo "Finished config node $line"
    fi
done



