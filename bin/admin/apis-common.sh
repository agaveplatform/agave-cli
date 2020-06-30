#!/bin/bash
# 
# apis-common.sh
# 
# author: deardooley@gmail.com
#
# URL filter for apps services
#

filter_service_url() {
	if [[ -z $hosturl ]]; then
		if ((development)); then
			hosturl="$devurl/admin/apis/"
		else
			hosturl="$baseurl/admin/$version/apis/"
		fi
	fi
}

