#!/bin/bash
#
# notifications-common.sh
#
# author: deardooley@gmail.com
#
# URL filter for notifications services
#

filter_service_url() {
	if [[ -z $hosturl ]]; then
		if ((development)); then
			hosturl="$devurl/notifications/"
		else
			hosturl="$baseurl/notifications/$version/"
		fi
	fi
}
