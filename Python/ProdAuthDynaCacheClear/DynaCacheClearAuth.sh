echo "Clearing Dyna Cache for Prod Auth"

python DynaCacheClear.py

disList="sivasubramaniyan.k@hp.com,sathyaseelan.t@hp.com"
log='/opt/apps/scripts/ProdAuthDynaCacheClear/Dyna_cache.log'
mailing='/opt/apps/scripts/PartnerFeedValidation/mailing.txt'
#Mail
echo -e "Hi All, \n\nHourly Dyna Cache Clear completed in Prod Auth.\n\nPlease find the Cache counts post cache clearance.\n\n" >$log
cat $mailing >>$log
echo -e "\n\nRegards,\nETR Support" >>$log
cat $log | mail -s "V9 Prod Stage Hourly Dyna Cache Clear" -r ETR-Support-Stream@hp.com $disList

cd /opt/apps/scripts/ProdAuthDynaCacheClear/
rm Dyna_cache.log
