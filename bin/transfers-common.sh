#!/bin/bash
#
# transfers-common.sh
#
# author: deardooley@gmail.com
#
# URL filter for transfers services
#

filter_service_url() {
	if [[ -z $hosturl ]]; then
		if ((development)); then
			hosturl="$devurl/api/transfers/"
		else
			hosturl="$baseurl/api/transfers/$version/"
		fi
	fi
}
