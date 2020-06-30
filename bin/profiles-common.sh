#!/bin/bash
# 
# profiles-common.sh
# 
# author: deardooley@gmail.com
#
# URL filter for profiles services
#

filter_service_url() {
	if [[ -z $hosturl ]]; then
		if ((development)); then 
			hosturl="$devurl/profiles/"
		else
			hosturl="$baseurl/profiles/$version/"
		fi
	fi
}

