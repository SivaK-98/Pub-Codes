

echo "AKAMAI PURGE BY URL/CPCODE SRARTED FOR PROD"
cd /opt/apps/scripts/Akamai_Url
choice = $1
echo "The Purge Choice you gave: $choice"
python Akamai_Purge_Url.py $choice

disList="sivasubramaniyan.k@hp.com,sathyaseelan.t@hp.com,karthikeyan.p@hp.com"
#disList="pdl-et-ops-support@hp.com,vyasapavan.mukthevi@hp.com"
#disList="sivasubramaniyan.k@hp.com"
log='/opt/apps/scripts/Akamai_Url/Akamai_Purge.log'
url_status=$(egrep -o  "Success|Failed" URL_Status.txt)
if [[ `echo $url_status` == "Success" ]]
then
        echo -e "Hi All, \n\nAkamai URL Purge is  $url_status in Prod.\n\n" >$log
else
        echo -e "Hi All, \n\nAkamai URL Purge  is $url_stauts in Prod.\n\n" >$log
fi

cp_code_status=$(egrep -o  "Success|Failed" CPCODE_Status.txt)
if [[ `echo $cp_code_status` == "Success" ]]
then
        echo -e "Hi All, \n\nAkamai URL Purge is  $cp_code_status in Prod.\n\n" >$log
else
        echo -e "Hi All, \n\nAkamai URL Purge  is $cp_code_stauts in Prod.\n\n" >$log
fi

cat mailing.json >>$log
echo -e "\nRegards,\nETR Support" >>$log

cat $log | mail -s "V9 PROD AKAMAI CACHE CLEAR" -r pdl-et-ops-support@hp.com $disList

cd /opt/apps/scripts/Akamai_Url/
rm Akamai_Purge.log
rm mailing.json
