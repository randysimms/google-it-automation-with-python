#copy files to linux
# scp -i .\qwikLABS-LXXXX-1XXXXXXX.pem .\ticky_check.py student-XX-xxxxxxxxxxxx@XX.XXX.XX.XXX:/home/student-XX-xxxxxxxxxxxx
#
# run python to parse syslog and create reports
python3 ./ticky_check.py

#convert files
./csv_to_html.py error_message.csv /var/www/html/error_message.html

./csv_to_html.py user_statistics.csv /var/www/html/user_statistics.html

#view reports by open any web-browser and enter the following URL in the search bar.
echo open the report by visiting:
#example of ifconfig:  inet 192.168.111.1 netmask 0xffffff00 broadcast 192.168.111.255
ip=$(ifconfig eth0 | grep inet | cut -d ' ' -f6)
echo http://$ip/error_message.html

echo http://$ip/user_statistics.html

