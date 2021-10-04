

echo "Clearing Redis Cache for Prod Auth"
cd /opt/apps/scripts/ProdAuthDynaCacheClear/
python DynaRedisCache.py

disList="sivasubramaniyan.k@hp.com,rajkumar.sundararajan@hp.com,pdl-et-ops-support@hp.com,vyasapavan.mukthevi@hp.com"
#disList="sivasubramaniyan.k@hp.com"
log='/opt/apps/scripts/ProdAuthDynaCacheClear/Dyna_cache.log'
status=$(egrep -o  "Success|Failed" status.txt)
if [[ `echo $status` == "Success" ]]
then
	echo -e "Hi All, \n\nHourly Redis Dyna Cache Clear is $status in Prod Auth.\n\n" >$log
else
	echo -e "Hi All, \n\nHourly Redis Dyna Cache Clear is $stauts in Prod Auth.\n\n" >$log
fi
echo -e "\nRegards,\nETR Support" >>$log
cat $log | mail -s "V9 Prod Stage Hourly Dyna Cache Clear - $status" -r pdl-et-ops-support@hp.com $disList

cd /opt/apps/scripts/ProdAuthDynaCacheClear/
rm Dyna_cache.log

