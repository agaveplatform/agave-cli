#!/bin/bash
#
# clients-common.sh
#
# author: deardooley@gmail.com
#
# URL filter for client registration services
#

filter_service_url() {
	if [[ -z $hosturl ]]; then
		if ((development)); then
			hosturl="$devurl/clients/v2"
		else
			hosturl="$baseurl/clients/v2"
		fi
	fi
}
