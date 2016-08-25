# agriculture
 
## HOUSE
committee="agriculture armedservices budget education energy standards financial intrelations homeland judiciary resources ethics govreform science smbusiness transportation va wmcommittee"
 
chamber=house
for committee in ${committee}; do
   echo "${committee}"
for congress in $(seq 101 114); do
   echo ${congress}
   curl "http://www.gpo.gov/fdsys/browse/committeecong.action?collection=CHRG&committee=${committee}&chamber=${chamber}&congressplus=${congress}&ycord=0" | grep ">Text<" | sed 's/\(.*<a href="\)\(.*\)\(" target="_blank".*$\)/\2/g' | xargs wget {}
done
done
 
 
## SENATE
 
committee="agriculture armedservices banking budget commerce energy environment finance foreignrelations health homeland indianaffairs judiciary smbusiness va ethics intelligence aging"
chamber=senate
 
for committee in ${committee}; do
   echo "${committee}"
for congress in $(seq 101 114); do
   echo ${congress}
   curl "http://www.gpo.gov/fdsys/browse/committeecong.action?collection=CHRG&committee=${committee}&chamber=${chamber}&congressplus=${congress}&ycord=0" | grep ">Text<" | sed 's/\(.*<a href="\)\(.*\)\(" target="_blank".*$\)/\2/g' | xargs wget {}
done
done