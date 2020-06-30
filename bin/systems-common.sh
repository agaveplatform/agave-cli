#!/bin/bash
# 
# systems-common.sh
# 
# author: deardooley@gmail.com
#
# URL filter for systems services
#

filter_service_url() {
	if [[ -z $hosturl ]]; then
		if ((development)); then 
			hosturl="$devurl/systems"
		else
			hosturl="$baseurl/systems/$version/"
		fi
	fi
}

