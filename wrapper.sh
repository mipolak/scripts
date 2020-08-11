#!/bin/bash
#
configfile=$1
conffile=/srv/home/user/scripts/${configfile}
[ ! -f $conffile ] \
&& echo "Could not find config file $configfile" \
&& exit 1

. $conffile
[ -z "${a_sources[*]}" ] \
&& echo "No a_sources array found in config file $configfile" \
&& exit 1

for source in ${a_sources[@]}
do
# do something  ${source}"

done
