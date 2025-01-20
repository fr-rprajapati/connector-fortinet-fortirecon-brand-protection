"""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""

from datetime import datetime
import requests
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger("fortinet-fortirecon-brand-protection")


class MakeRestApiCall:

    def __init__(self, config):
        self.server_url = config.get('server_url', '').strip().strip('/')
        if not self.server_url.startswith('http') or not self.server_url.startswith('https'):
            self.server_url = 'https://' + self.server_url
        self.org_id = config.get("org_id")
        self.authkey = config.get("api_key", '')
        self.verify_ssl = config.get("verify_ssl", True)

    def make_request(self, method='GET', endpoint='', params=None, data=None):
        try:
            url = self.server_url + f"/bp/{self.org_id}" + endpoint
            headers = {"Content-Type": "application/json",
                       "Authorization": self.authkey}
            logger.debug(f"\n-----------req_start-----------\n{method} - {url}\nparams: {params}\ndata: {data}\n")
            try:
                from connectors.debug_utils.curl_script import make_curl
                make_curl(method, url, headers=headers, params=params, json=data, verify_ssl=self.verify_ssl)
            except Exception as err:
                logger.info(f"Error in curl utils: {str(err)}")
            response = requests.request(method=method, url=url,
                                        headers=headers, json=data, params=params,
                                        verify=self.verify_ssl)

            if response.ok:
                if 'json' in str(response.headers):
                    return response.json()
                else:
                    return response.text
            else:
                logger.error("Error: {0}".format(response.json()))
                raise ConnectorError('{0}:{1}'.format(response.status_code, response.text))
        except requests.exceptions.SSLError as e:
            logger.exception('{0}'.format(e))
            raise ConnectorError('{0}'.format(e))
        except requests.exceptions.ConnectionError as e:
            logger.exception('{0}'.format(e))
            raise ConnectorError('{0}'.format(e))
        except Exception as e:
            logger.error('{0}'.format(e))
            raise ConnectorError('{0}'.format(e))


def build_params(params={}, multiselect=[]):
    new_params = {}
    for key, value in params.items():
        if value is False or value == 0 or value:
            if key in ("start_date", "end_date"):
                value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d")
            elif key in multiselect:
                value = ",".join(value)
            elif key in ("status", "online_status") and isinstance(value, str):
                value = value.upper().replace(" ", "_")
            new_params[key] = value
    return new_params


def get_code_repos(config, params):
    ob = MakeRestApiCall(config)
    new_params = build_params(params)
    return ob.make_request(method="GET", endpoint="/code_repos", params=new_params)


def get_code_repo_exposures(config, params):
    ob = MakeRestApiCall(config)
    new_params = build_params(params)
    return ob.make_request(method="GET", endpoint="/code_repo_exposures", params=new_params)


def get_code_repos_stats(config, params):
    ob = MakeRestApiCall(config)
    return ob.make_request(method="GET", endpoint=f"/stats/code_repos")


def get_code_repo_matched_domains_stats(config, params):
    ob = MakeRestApiCall(config)
    return ob.make_request(method="GET", endpoint="/stats/code_repos/matched_domains")


def get_domain_threats(config, params):
    ob = MakeRestApiCall(config)
    new_params = build_params(params)
    return ob.make_request(method="GET", endpoint="/domain_threats", params=new_params)


def get_domain_threats_by_id(config, params):
    ob = MakeRestApiCall(config)
    _id = params.pop("id")
    return ob.make_request(method="GET", endpoint=f"/domain_threats/{_id}")


def get_executive_exposures(config, params):
    ob = MakeRestApiCall(config)
    new_params = build_params(params)
    return ob.make_request(method="GET", endpoint="/executive_exposures", params=new_params)


def get_executive_profiles(config, params):
    ob = MakeRestApiCall(config)
    new_params = build_params(params)
    return ob.make_request(method="GET", endpoint="/executive_profiles", params=new_params)


def get_open_bucket_exposures(config, params):
    ob = MakeRestApiCall(config)
    new_params = build_params(params)
    return ob.make_request(method="GET", endpoint="/open_bucket_exposures", params=new_params)


def get_rogue_apps(config, params):
    ob = MakeRestApiCall(config)
    new_params = build_params(params, multiselect=["status"])
    return ob.make_request(method="GET", endpoint="/rogue_apps", params=new_params)


def get_rogue_app_by_id(config, params):
    ob = MakeRestApiCall(config)
    _id = params.pop("id")
    return ob.make_request(method="GET", endpoint=f"/rogue_apps/{_id}")


def get_social_media_threats(config, params):
    ob = MakeRestApiCall(config)
    new_params = build_params(params)
    return ob.make_request(method="GET", endpoint="/social_media_threats", params=new_params)


def get_domain_threats_stats(config, params):
    ob = MakeRestApiCall(config)
    return ob.make_request(method="GET", endpoint=f"/stats/domain_threats")


def get_original_domains_stats(config, params):
    ob = MakeRestApiCall(config)
    new_params = build_params(params)
    return ob.make_request(method="GET", endpoint="/stats/domain_threats/original_domains", params=new_params)


def get_open_bucket_exposures_stats(config, params):
    ob = MakeRestApiCall(config)
    return ob.make_request(method="GET", endpoint=f"/stats/open_bucket_exposures")


def get_social_media_threats_stats(config, params):
    ob = MakeRestApiCall(config)
    return ob.make_request(method="GET", endpoint=f"/stats/social_media_threats")


def get_tags(config, params):
    ob = MakeRestApiCall(config)
    return ob.make_request(method="GET", endpoint=f"/tags")


def get_takedown_requests(config, params):
    ob = MakeRestApiCall(config)
    new_params = build_params(params, multiselect=["status", "category"])
    return ob.make_request(method="GET", endpoint="/takedowns", params=new_params)

# Update status
def update_code_repo_status(config, params):
    status = params.pop("status")
    payload = {"status": status}
    MK = MakeRestApiCall(config=config)
    endpoint = "/code_repos/{0}".format(params.pop("repo_id"))
    response = MK.make_request(endpoint=endpoint, method="PATCH", params=params, data=payload)
    return response


def update_domain_threat_status(config, params):
    status = params.pop("status")
    payload = {"status": status}
    MK = MakeRestApiCall(config=config)
    endpoint = "/domain_threats/{0}".format(params.pop("domain_threat_id"))
    response = MK.make_request(endpoint=endpoint, method="PATCH", params=params, data=payload)
    return response


def update_open_bucket_exposure_status(config, params):
    status = params.pop("status")
    payload = {"status": status}
    MK = MakeRestApiCall(config=config)
    endpoint = "/open_bucket_exposures/{0}".format(params.pop("open_bucket_exposure_id"))
    response = MK.make_request(endpoint=endpoint, method="PATCH", params=params, data=payload)
    return response


def update_rogue_app_exposure_status(config, params):
    status = params.pop("status")
    payload = {"status": status}
    MK = MakeRestApiCall(config=config)
    endpoint = "/rogue_apps/{0}".format(params.pop("rogue_app_exposure_id"))
    response = MK.make_request(endpoint=endpoint, method="PATCH", params=params, data=payload)
    return response


def update_social_media_threat_status(config, params):
    status = params.pop("status")
    payload = {"status": status}
    MK = MakeRestApiCall(config=config)
    endpoint = "/social_media_threats/{0}".format(params.pop("social_media_threat_id"))
    response = MK.make_request(endpoint=endpoint, method="PATCH", params=params, data=payload)
    return response


def _check_health(config):
    try:
        get_code_repos_stats(config, {})
        return True
    except Exception as e:
        raise Exception(str(e))


operations = {
    "get_code_repos": get_code_repos,
    "get_code_repo_exposures": get_code_repo_exposures,
    "get_code_repos_stats": get_code_repos_stats,
    "get_code_repo_matched_domains_stats": get_code_repo_matched_domains_stats,
    "get_domain_threats": get_domain_threats,
    "get_domain_threats_by_id": get_domain_threats_by_id,
    "get_executive_exposures": get_executive_exposures,
    "get_executive_profiles": get_executive_profiles,
    "get_open_bucket_exposures": get_open_bucket_exposures,
    "get_rogue_apps": get_rogue_apps,
    "get_rogue_app_by_id": get_rogue_app_by_id,
    "get_social_media_threats": get_social_media_threats,
    "get_domain_threats_stats": get_domain_threats_stats,
    "get_original_domains_stats": get_original_domains_stats,
    "get_open_bucket_exposures_stats": get_open_bucket_exposures_stats,
    "get_social_media_threats_stats": get_social_media_threats_stats,
    "get_tags": get_tags,
    "get_takedown_requests": get_takedown_requests,
    "update_code_repo_status": update_code_repo_status,
    "update_domain_threat_status": update_domain_threat_status,
    "update_open_bucket_exposure_status": update_open_bucket_exposure_status,
    "update_rogue_app_exposure_status": update_rogue_app_exposure_status,
    "update_social_media_threat_status": update_social_media_threat_status
}
