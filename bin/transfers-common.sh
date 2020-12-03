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
			hosturl="$devurl/transfers/"
		else
			hosturl="$baseurl/transfers/$version/"
		fi
	fi
}
