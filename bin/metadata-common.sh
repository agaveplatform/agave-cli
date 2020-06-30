#!/bin/bash
# 
# metadata-common.sh
# 
# author: deardooley@gmail.com
#
# URL filter for metadata services
#

filter_service_url() {
	if [[ -z $hosturl ]]; then
		if ((development)); then 
			hosturl="$devurl/meta/"
		else
			hosturl="$baseurl/meta/$version/"
		fi
	fi
}

