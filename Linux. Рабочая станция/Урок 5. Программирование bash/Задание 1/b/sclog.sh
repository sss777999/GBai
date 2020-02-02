#!/bin/bash
trap "echo ' Scrip is DONE. God bye .....'" SIGINT
echo this is
echo Script is running ... 
tail -f /var/log/auth.log | grep failure
