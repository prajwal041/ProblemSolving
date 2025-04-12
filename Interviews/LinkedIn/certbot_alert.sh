#!/bin/bash
domain="yoursite.com"
expiry_date=$(openssl s_client -connect $domain:443 -servername $domain 2>/dev/null | openssl x509 -noout -enddate | cut -d= -f2)
expiry_seconds=$(date -d "$expiry_date" +%s)
now=$(date +%s)
days_left=$(( ($expiry_seconds - $now) / 86400 ))

if [ $days_left -lt 15 ]; then
  echo "⚠️ TLS certificate for $domain expires in $days_left days!"
fi
