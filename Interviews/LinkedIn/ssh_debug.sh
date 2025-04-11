#!/bin/bash

echo "Usage: ./ssh_debug.sh <user> <server_ip_or_host>"

USER=$1
HOST=$2
PORT=22

echo "🔍 Step 1: Checking basic SSH connectivity..."
ssh -p $PORT -v -o ConnectTimeout=5 $USER@$HOST 2>&1 | tee ssh_debug.log

echo -e "\n🌐 Step 2: Checking network reachability..."
ping -c 4 $HOST
nc -zv $HOST $PORT

echo -e "\n🔒 Step 3: Checking if correct SSH key is being used..."
# This assumes the key is set via config or agent
ssh-aad -l || echo "No key added to ssh-agent. Add with: ssh-add /path/to/key"

echo -e "\n🧠 Step 4: Summary of recent SSH log activity on the server (requires access):"
echo "🔹 Run this on the server:"
echo "  sudo journalctl -u sshd --since '10 minutes ago' | tail"
echo "  or"
echo "  sudo tail -n 50 /var/log/auth.log"

echo -e "\n👮‍♂️ Step 5: Review sshd_config for access restrictions:"
echo "🔹 On the server, check:"
echo "  grep -iE 'AllowUsers|DenyUsers|AllowGroups|DenyGroups' /etc/ssh/sshd_config"
echo "  sudo iptables -L -n | grep $HOST"
echo "  sudo ufw status"

echo -e "\n✅ Done! Check 'ssh_debug.log' for detailed SSH verbose output."


