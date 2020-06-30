#!/bin/bash
# 
# apps-common.sh
# 
# author: deardooley@gmail.com
#
# URL filter for apps services
#

filter_service_url() {
	if [[ -z $hosturl ]]; then
		if ((development)); then
			hosturl="$devurl/apps/"
		else
			hosturl="$baseurl/apps/$version/"
		fi
	fi
}

