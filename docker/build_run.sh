#!/bin/bash
docker build . -t phishytics
./run.sh https://www.google.com
./run.sh http://fb-recovery-100033988317-it.tk/update_security.htm