#!/usr/bin/env bash
# required arg CN 
# example of execution:
#  ./generate_csr_key_for_certificate.sh mysite.example.com
# useful to generate csr and key for signing certificate by internal CA authority

C="DE"
ST="Berlin"
L="Berlin"
O="Organisation name"
OU="Organization Unit"
MAIL="admin@example.com"
CN="$1"
SUBJ="/C=$C/ST=$ST/L=$L/O=$O/OU=$OU/CN=$CN/emailAddress=$MAIL"
mkdir $CN
openssl req -new -newkey rsa:4096 -keyout $CN/$CN.key -out $CN/$CN.csr -sha512 -subj "$SUBJ" -nodes

