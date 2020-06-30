#!/bin/bash
# 
# jobs-common.sh
# 
# author: deardooley@gmail.com
#
# URL filter for jobs services
#

filter_service_url() {
	if [[ -z $hosturl ]]; then
		if ((development)); then 
			hosturl="$devurl/jobs/"
		else
			hosturl="$baseurl/jobs/$version/"
		fi
	fi
}

