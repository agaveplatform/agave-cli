#!/bin/bash
# 
# uuid-common.sh
# 
# author: deardooley@gmail.com
#
# URL filter for uuid lookup services
#
filter_service_url() {
	if [[ -z $hosturl ]]; then
		if ((development)); then
			hosturl="$devurl/uuids"
		else
			hosturl="$baseurl/uuids/$version/"
		fi
	fi
}

