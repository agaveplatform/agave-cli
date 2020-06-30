#!/bin/bash
# 
# headers-common.sh
# 
# author: deardooley@gmail.com
#
# URL filter for headers services
#

filter_service_url() {
	if [[ -z $hosturl ]]; then
		if ((development)); then
			hosturl="$devurl/headers/v0.1"
		else
			hosturl="$baseurl/headers/v0.1"
		fi
	fi
}

