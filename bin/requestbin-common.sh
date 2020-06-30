#!/bin/bash
# 
# requestbin-common.sh
# 
# author: deardooley@gmail.com
#
# URL filter for requestbin services
#

filter_service_url() {
	if [[ -z $hosturl ]]; then
		if ((development)); then 
			hosturl="https://requestbin.agaveplatform.org/"
		else
			hosturl="https://requestbin.agaveplatform.org/"
		fi
	fi
}

