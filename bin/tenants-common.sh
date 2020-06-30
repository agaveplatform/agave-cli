#!/bin/bash
#
# tenants-common.sh
#
# author: deardooley@gmail.com
#
# URL filter for tenants services
#

filter_service_url() {
	if [[ -z $hosturl ]]; then
		if (($development)); then
			if [[ -n "$AGAVE_DEV_TENANTS_API_BASEURL" ]]; then
				hosturl="$AGAVE_DEV_TENANTS_API_BASEURL/tenants/v2"
			elif [[ -n "$devurl" ]]; then
				hosturl="${devurl}/tenants/v2"
			else
				hosturl="https://sandbox.agaveplatform.org/tenants/v2/"
			fi
		else
			if [[ -n "$AGAVE_TENANTS_API_BASEURL" ]]; then
				hosturl="$AGAVE_TENANTS_API_BASEURL"
			else
				hosturl="https://sandbox.agaveplatform.org/tenants/v2/"
			fi
		fi
	fi

	#hosturl="${hosturl%&}"
}
