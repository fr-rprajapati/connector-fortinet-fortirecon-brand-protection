# Edit the config_and_params.json file and add the necessary parameter values.
# Ensure that the provided input_params yield the correct output schema.
# Add logic for validating conditional_output_schema or if schema is other than dict.
# Add any specific assertions in each test case, based on the expected response.

"""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""

import pytest
from testframework.conftest import valid_configuration, invalid_configuration, valid_configuration_with_token,\
    connector_id, connector_details, info_json, params_json
from testframework.helpers.test_helpers import run_health_check_success, run_invalid_config_test, run_success_test,\
    run_output_schema_validation, run_invalid_param_test, set_report_metadata


def run_invalid_param_test_wrapper(connector_details, operation_name, param_name, param_type, action_params):
    result = run_invalid_param_test(connector_details, operation_name, param_name,
                                    param_type, action_params)
    assert result.get('data', {}).get('hits') == []
    assert result.get('status') == 'Success'


@pytest.mark.check_health
def test_check_health_success(valid_configuration, connector_details):
    set_report_metadata(connector_details, "Health Check", "Verify with valid Configuration")
    result = run_health_check_success(valid_configuration, connector_details)
    assert result.get('status') == 'Available'
    

@pytest.mark.check_health
def test_check_health_invalid_org_id(invalid_configuration, connector_id, connector_details, params_json):
    set_report_metadata(connector_details, "Health Check", "Verify with invalid Organization ID")
    result = run_invalid_config_test(invalid_configuration, connector_id, connector_details, param_name='org_id',
                                     param_type='text', config=params_json['config'])
    assert result.get('status') == "Disconnected"
    

@pytest.mark.check_health
def test_check_health_invalid_api_key(invalid_configuration, connector_id, connector_details, params_json):
    set_report_metadata(connector_details, "Health Check", "Verify with invalid API Key")
    result = run_invalid_config_test(invalid_configuration, connector_id, connector_details, param_name='api_key',
                                     param_type='password', config=params_json['config'])
    assert result.get('status') == "Disconnected"
    

@pytest.mark.check_health
def test_check_health_invalid_server_url(invalid_configuration, connector_id, connector_details, params_json):
    set_report_metadata(connector_details, "Health Check", "Verify with invalid Server URL")
    result = run_invalid_config_test(invalid_configuration, connector_id, connector_details, param_name='server_url',
                                     param_type='text', config=params_json['config'])
    assert result.get('status') == "Disconnected"
    

@pytest.mark.get_code_repo_exposures
def test_get_code_repo_exposures_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Code Repo Exposures", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_code_repo_exposures',
                                   action_params=params_json['get_code_repo_exposures']):
        assert result.get('status') == "Success"


@pytest.mark.get_code_repo_exposures
def test_validate_get_code_repo_exposures_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Code Repo Exposures", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_code_repo_exposures', info_json, params_json['get_code_repo_exposures'])
    

@pytest.mark.get_code_repo_exposures
def test_get_code_repo_exposures_invalid_q(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Code Repo Exposures", "Verify with invalid Search By Keyword")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_code_repo_exposures', param_name='q',
                                    param_type='text', action_params=params_json['get_code_repo_exposures'])


@pytest.mark.get_code_repo_exposures
def test_get_code_repo_exposures_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Code Repo Exposures", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_code_repo_exposures', param_name='page',
                                    param_type='integer', action_params=params_json['get_code_repo_exposures'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_code_repo_exposures
def test_get_code_repo_exposures_invalid_matched_domain(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Code Repo Exposures", "Verify with invalid Matched Domain")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_code_repo_exposures', param_name='matched_domain',
                                    param_type='text', action_params=params_json['get_code_repo_exposures'])
    

@pytest.mark.get_code_repo_exposures
def test_get_code_repo_exposures_invalid_attribute_type(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Code Repo Exposures", "Verify with invalid Attribute Type")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_code_repo_exposures', param_name='attribute_type',
                                    param_type='text', action_params=params_json['get_code_repo_exposures'])
    

@pytest.mark.get_code_repo_exposures
def test_get_code_repo_exposures_invalid_risk_level(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Code Repo Exposures", "Verify with invalid Risk Level")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_code_repo_exposures', param_name='risk_level',
                                    param_type='text', action_params=params_json['get_code_repo_exposures'])
    

@pytest.mark.get_code_repo_exposures
def test_get_code_repo_exposures_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Code Repo Exposures", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_code_repo_exposures', param_name='size',
                                    param_type='integer', action_params=params_json['get_code_repo_exposures'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_code_repos
def test_get_code_repos_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Code Repositories", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_code_repos',
                                   action_params=params_json['get_code_repos']):
        assert result.get('status') == "Success"


@pytest.mark.get_code_repos
def test_validate_get_code_repos_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Code Repositories", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_code_repos', info_json, params_json['get_code_repos'])
    

@pytest.mark.get_code_repos
def test_get_code_repos_invalid_q(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Code Repositories", "Verify with invalid Search By Keyword")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_code_repos', param_name='q',
                                    param_type='text', action_params=params_json['get_code_repos'])
    

@pytest.mark.get_code_repos
def test_get_code_repos_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Code Repositories", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_code_repos', param_name='page',
                                    param_type='integer', action_params=params_json['get_code_repos'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_code_repos
def test_get_code_repos_invalid_matched_domain(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Code Repositories", "Verify with invalid Matched Domain")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_code_repos', param_name='matched_domain',
                                    param_type='text', action_params=params_json['get_code_repos'])


@pytest.mark.get_code_repos
def test_get_code_repos_invalid_attribute_type(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Code Repositories", "Verify with invalid Attribute Type")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_code_repos', param_name='attribute_type',
                                    param_type='text', action_params=params_json['get_code_repos'])
    

@pytest.mark.get_code_repos
def test_get_code_repos_invalid_risk_level(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Code Repositories", "Verify with invalid Risk Level")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_code_repos', param_name='risk_level',
                                    param_type='text', action_params=params_json['get_code_repos'])
    

@pytest.mark.get_code_repos
def test_get_code_repos_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Code Repositories", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_code_repos', param_name='size',
                                    param_type='integer', action_params=params_json['get_code_repos'])
    assert result.get('status') == "failed"


@pytest.mark.get_code_repos_stats
def test_get_code_repos_stats_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Code Repos Statistics", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_code_repos_stats',
                                   action_params=params_json['get_code_repos_stats']):
        assert result.get('status') == "Success"


@pytest.mark.get_code_repos_stats
def test_validate_get_code_repos_stats_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Code Repos Statistics", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_code_repos_stats', info_json, params_json['get_code_repos_stats'])
    

@pytest.mark.get_code_repo_matched_domains_stats
def test_get_code_repo_matched_domains_stats_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Code Repo Matched Domains Statistics", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_code_repo_matched_domains_stats',
                                   action_params=params_json['get_code_repo_matched_domains_stats']):
        assert result.get('status') == "Success"


@pytest.mark.get_code_repo_matched_domains_stats
def test_validate_get_code_repo_matched_domains_stats_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Code Repo Matched Domains Statistics", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_code_repo_matched_domains_stats', info_json, params_json['get_code_repo_matched_domains_stats'])
    

@pytest.mark.get_domain_threats
def test_get_domain_threats_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Domain Threats", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_domain_threats',
                                   action_params=params_json['get_domain_threats']):
        assert result.get('status') == "Success"


@pytest.mark.get_domain_threats
def test_validate_get_domain_threats_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Domain Threats", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_domain_threats', info_json, params_json['get_domain_threats'])
    

@pytest.mark.get_domain_threats
def test_get_domain_threats_invalid_q(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Domain Threats", "Verify with invalid Search By Keyword")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_domain_threats', param_name='q',
                                    param_type='text', action_params=params_json['get_domain_threats'])
    

@pytest.mark.get_domain_threats
def test_get_domain_threats_invalid_tags(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Domain Threats", "Verify with invalid Tags")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_domain_threats', param_name='tags',
                                    param_type='text', action_params=params_json['get_domain_threats'])
    

@pytest.mark.get_domain_threats
def test_get_domain_threats_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Domain Threats", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_domain_threats', param_name='page',
                                    param_type='integer', action_params=params_json['get_domain_threats'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_domain_threats
def test_get_domain_threats_invalid_original_domain(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Domain Threats", "Verify with invalid Original Domain")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_domain_threats', param_name='original_domain',
                                    param_type='text', action_params=params_json['get_domain_threats'])
    

@pytest.mark.get_domain_threats
def test_get_domain_threats_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Domain Threats", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_domain_threats', param_name='size',
                                    param_type='integer', action_params=params_json['get_domain_threats'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_domain_threats_by_id
def test_get_domain_threats_by_id_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Domain Threats By ID", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_domain_threats_by_id',
                                   action_params=params_json['get_domain_threats_by_id']):
        assert result.get('status') == "Success"


@pytest.mark.get_domain_threats_by_id
def test_validate_get_domain_threats_by_id_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Domain Threats By ID", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_domain_threats_by_id', info_json, params_json['get_domain_threats_by_id'])
    

@pytest.mark.get_domain_threats_by_id
def test_get_domain_threats_by_id_invalid_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Domain Threats By ID", "Verify with invalid Domain Threat ID")
    result = run_invalid_param_test(connector_details, operation_name='get_domain_threats_by_id', param_name='id',
                                    param_type='text', action_params=params_json['get_domain_threats_by_id'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_executive_exposures
def test_get_executive_exposures_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Executive Exposures", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_executive_exposures',
                                   action_params=params_json['get_executive_exposures']):
        assert result.get('status') == "Success"


@pytest.mark.get_executive_exposures
def test_validate_get_executive_exposures_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Executive Exposures", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_executive_exposures', info_json, params_json['get_executive_exposures'])
    

@pytest.mark.get_executive_exposures
def test_get_executive_exposures_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Executive Exposures", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_executive_exposures', param_name='page',
                                    param_type='integer', action_params=params_json['get_executive_exposures'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_executive_exposures
def test_get_executive_exposures_invalid_executive_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Executive Exposures", "Verify with invalid Executive ID")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_executive_exposures', param_name='executive_id',
                                    param_type='text', action_params=params_json['get_executive_exposures'])
    

@pytest.mark.get_executive_exposures
def test_get_executive_exposures_invalid_source_type(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Executive Exposures", "Verify with invalid Source Type")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_executive_exposures', param_name='source_type',
                                    param_type='text', action_params=params_json['get_executive_exposures'])
    

@pytest.mark.get_executive_exposures
def test_get_executive_exposures_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Executive Exposures", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_executive_exposures', param_name='size',
                                    param_type='integer', action_params=params_json['get_executive_exposures'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_executive_profiles
def test_get_executive_profiles_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Executive Profiles", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_executive_profiles',
                                   action_params=params_json['get_executive_profiles']):
        assert result.get('status') == "Success"


@pytest.mark.get_executive_profiles
def test_validate_get_executive_profiles_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Executive Profiles", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_executive_profiles', info_json, params_json['get_executive_profiles'])
    

@pytest.mark.get_executive_profiles
def test_get_executive_profiles_invalid_name(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Executive Profiles", "Verify with invalid Executive Name")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_executive_profiles', param_name='name',
                                    param_type='text', action_params=params_json['get_executive_profiles'])
    

@pytest.mark.get_executive_profiles
def test_get_executive_profiles_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Executive Profiles", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_executive_profiles', param_name='page',
                                    param_type='integer', action_params=params_json['get_executive_profiles'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_executive_profiles
def test_get_executive_profiles_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Executive Profiles", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_executive_profiles', param_name='size',
                                    param_type='integer', action_params=params_json['get_executive_profiles'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_open_bucket_exposures
def test_get_open_bucket_exposures_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Open Bucket Exposures", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_open_bucket_exposures',
                                   action_params=params_json['get_open_bucket_exposures']):
        assert result.get('status') == "Success"


@pytest.mark.get_open_bucket_exposures
def test_validate_get_open_bucket_exposures_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Open Bucket Exposures", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_open_bucket_exposures', info_json, params_json['get_open_bucket_exposures'])
    

@pytest.mark.get_open_bucket_exposures
def test_get_open_bucket_exposures_invalid_q(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Open Bucket Exposures", "Verify with invalid Search By Keyword")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_open_bucket_exposures', param_name='q',
                                    param_type='text', action_params=params_json['get_open_bucket_exposures'])
    

@pytest.mark.get_open_bucket_exposures
def test_get_open_bucket_exposures_invalid_bucket_type(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Open Bucket Exposures", "Verify with invalid Bucket Type")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_open_bucket_exposures', param_name='bucket_type',
                                    param_type='text', action_params=params_json['get_open_bucket_exposures'])
    

@pytest.mark.get_open_bucket_exposures
def test_get_open_bucket_exposures_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Open Bucket Exposures", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_open_bucket_exposures', param_name='page',
                                    param_type='integer', action_params=params_json['get_open_bucket_exposures'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_open_bucket_exposures
def test_get_open_bucket_exposures_invalid_file_type(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Open Bucket Exposures", "Verify with invalid File Type")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_open_bucket_exposures', param_name='file_type',
                                    param_type='text', action_params=params_json['get_open_bucket_exposures'])
    

@pytest.mark.get_open_bucket_exposures
def test_get_open_bucket_exposures_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Open Bucket Exposures", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_open_bucket_exposures', param_name='size',
                                    param_type='integer', action_params=params_json['get_open_bucket_exposures'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_rogue_apps
def test_get_rogue_apps_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Rogue Apps", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_rogue_apps',
                                   action_params=params_json['get_rogue_apps']):
        assert result.get('status') == "Success"


@pytest.mark.get_rogue_apps
def test_validate_get_rogue_apps_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Rogue Apps", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_rogue_apps', info_json, params_json['get_rogue_apps'])
    

@pytest.mark.get_rogue_apps
def test_get_rogue_apps_invalid_q(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Rogue Apps", "Verify with invalid Search By Keyword")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_rogue_apps', param_name='q',
                                    param_type='text', action_params=params_json['get_rogue_apps'])
    

@pytest.mark.get_rogue_apps
def test_get_rogue_apps_invalid_appstore(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Rogue Apps", "Verify with invalid App Store Name")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_rogue_apps', param_name='appstore',
                                    param_type='text', action_params=params_json['get_rogue_apps'])
    

@pytest.mark.get_rogue_apps
def test_get_rogue_apps_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Rogue Apps", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_rogue_apps', param_name='page',
                                    param_type='integer', action_params=params_json['get_rogue_apps'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_rogue_apps
def test_get_rogue_apps_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Rogue Apps", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_rogue_apps', param_name='size',
                                    param_type='integer', action_params=params_json['get_rogue_apps'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_rogue_app_by_id
def test_get_rogue_app_by_id_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Rogue App By ID", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_rogue_app_by_id',
                                   action_params=params_json['get_rogue_app_by_id']):
        assert result.get('status') == "Success"


@pytest.mark.get_rogue_app_by_id
def test_validate_get_rogue_app_by_id_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Rogue App By ID", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_rogue_app_by_id', info_json, params_json['get_rogue_app_by_id'])
    

@pytest.mark.get_rogue_app_by_id
def test_get_rogue_app_by_id_invalid_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Rogue App By ID", "Verify with invalid Rogue App ID")
    result = run_invalid_param_test(connector_details, operation_name='get_rogue_app_by_id', param_name='id',
                                    param_type='text', action_params=params_json['get_rogue_app_by_id'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_social_media_threats
def test_get_social_media_threats_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Social Media Threats", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_social_media_threats',
                                   action_params=params_json['get_social_media_threats']):
        assert result.get('status') == "Success"


@pytest.mark.get_social_media_threats
def test_validate_get_social_media_threats_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Social Media Threats", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_social_media_threats', info_json, params_json['get_social_media_threats'])
    

@pytest.mark.get_social_media_threats
def test_get_social_media_threats_invalid_q(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Social Media Threats", "Verify with invalid Search By Keyword")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_social_media_threats', param_name='q',
                                    param_type='text', action_params=params_json['get_social_media_threats'])
    

@pytest.mark.get_social_media_threats
def test_get_social_media_threats_invalid_size(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Social Media Threats", "Verify with invalid Size")
    result = run_invalid_param_test(connector_details, operation_name='get_social_media_threats', param_name='size',
                                    param_type='integer', action_params=params_json['get_social_media_threats'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_social_media_threats
def test_get_social_media_threats_invalid_handle_name(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Social Media Threats", "Verify with invalid Handle Name")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_social_media_threats', param_name='handle_name',
                                    param_type='text', action_params=params_json['get_social_media_threats'])
    

@pytest.mark.get_social_media_threats
def test_get_social_media_threats_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Social Media Threats", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_social_media_threats', param_name='page',
                                    param_type='integer', action_params=params_json['get_social_media_threats'])
    assert result.get('status') == "failed"
    

@pytest.mark.get_social_media_threats
def test_get_social_media_threats_invalid_profile_name(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Social Media Threats", "Verify with invalid Profile Name")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_social_media_threats', param_name='profile_name',
                                    param_type='text', action_params=params_json['get_social_media_threats'])
    

@pytest.mark.get_social_media_threats
def test_get_social_media_threats_invalid_media_type(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Social Media Threats", "Verify with invalid Media Type")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_social_media_threats', param_name='media_type',
                                    param_type='text', action_params=params_json['get_social_media_threats'])
    

@pytest.mark.get_domain_threats_stats
def test_get_domain_threats_stats_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Domain Threats Statistics", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_domain_threats_stats',
                                   action_params=params_json['get_domain_threats_stats']):
        assert result.get('status') == "Success"


@pytest.mark.get_domain_threats_stats
def test_validate_get_domain_threats_stats_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Domain Threats Statistics", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_domain_threats_stats', info_json, params_json['get_domain_threats_stats'])
    

@pytest.mark.get_original_domains_stats
def test_get_original_domains_stats_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Original Domains Statistics", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_original_domains_stats',
                                   action_params=params_json['get_original_domains_stats']):
        assert result.get('status') == "Success"


@pytest.mark.get_original_domains_stats
def test_validate_get_original_domains_stats_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Original Domains Statistics", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_original_domains_stats', info_json, params_json['get_original_domains_stats'])
    

@pytest.mark.get_open_bucket_exposures_stats
def test_get_open_bucket_exposures_stats_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Open Bucket Exposures Statistics", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_open_bucket_exposures_stats',
                                   action_params=params_json['get_open_bucket_exposures_stats']):
        assert result.get('status') == "Success"


@pytest.mark.get_open_bucket_exposures_stats
def test_validate_get_open_bucket_exposures_stats_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Open Bucket Exposures Statistics", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_open_bucket_exposures_stats', info_json, params_json['get_open_bucket_exposures_stats'])
    

@pytest.mark.get_social_media_threats_stats
def test_get_social_media_threats_stats_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Social Media Threats Statistics", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_social_media_threats_stats',
                                   action_params=params_json['get_social_media_threats_stats']):
        assert result.get('status') == "Success"


@pytest.mark.get_social_media_threats_stats
def test_validate_get_social_media_threats_stats_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Social Media Threats Statistics", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_social_media_threats_stats', info_json, params_json['get_social_media_threats_stats'])
    

@pytest.mark.get_tags
def test_get_tags_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Tags", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_tags',
                                   action_params=params_json['get_tags']):
        assert result.get('status') == "Success"


@pytest.mark.get_tags
def test_validate_get_tags_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Tags", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_tags', info_json, params_json['get_tags'])
    

@pytest.mark.get_takedown_requests
def test_get_takedown_requests_success(cache, valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Takedown Requests", "Verify with valid Input Parameters")
    for result in run_success_test(cache, connector_details, operation_name='get_takedown_requests',
                                   action_params=params_json['get_takedown_requests']):
        assert result.get('status') == "Success"


@pytest.mark.get_takedown_requests
def test_validate_get_takedown_requests_output_schema(cache, valid_configuration_with_token, connector_details,
                                                 info_json, params_json):
    set_report_metadata(connector_details, "Get Takedown Requests", "Validate Output Schema")
    run_output_schema_validation(cache, 'get_takedown_requests', info_json, params_json['get_takedown_requests'])
    

@pytest.mark.get_takedown_requests
def test_get_takedown_requests_invalid_q(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Takedown Requests", "Verify with invalid Search By Keyword")
    run_invalid_param_test_wrapper(connector_details, operation_name='get_takedown_requests', param_name='q',
                                    param_type='text', action_params=params_json['get_takedown_requests'])
    

@pytest.mark.get_takedown_requests
def test_get_takedown_requests_invalid_page(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Get Takedown Requests", "Verify with invalid Page")
    result = run_invalid_param_test(connector_details, operation_name='get_takedown_requests', param_name='page',
                                    param_type='integer', action_params=params_json['get_takedown_requests'])
    assert result.get('status') == "failed"


@pytest.mark.update_code_repo_status
def test_update_code_repo_status_invalid_repo_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Update Code Repo Status", "Verify with invalid Code Repo ID")
    result = run_invalid_param_test(connector_details, operation_name='update_code_repo_status', param_name='repo_id',
                                    param_type='text', action_params=params_json['update_code_repo_status'])
    assert result.get('status') == "failed"


@pytest.mark.update_domain_threat_status
def test_update_domain_threat_status_invalid_domain_threat_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Update Domain Threat Status", "Verify with invalid Domain Threat ID")
    result = run_invalid_param_test(connector_details, operation_name='update_domain_threat_status', param_name='domain_threat_id',
                                    param_type='text', action_params=params_json['update_domain_threat_status'])
    assert result.get('status') == "failed"
    

@pytest.mark.update_open_bucket_exposure_status
def test_update_open_bucket_exposure_status_invalid_open_bucket_exposure_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Update Open Bucket Exposure Status", "Verify with invalid Open Bucket Exposure ID")
    result = run_invalid_param_test(connector_details, operation_name='update_open_bucket_exposure_status', param_name='open_bucket_exposure_id',
                                    param_type='text', action_params=params_json['update_open_bucket_exposure_status'])
    assert result.get('status') == "failed"
    

@pytest.mark.update_rogue_app_exposure_status
def test_update_rogue_app_exposure_status_invalid_rogue_app_exposure_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Update Rogue App Status", "Verify with invalid Rogue App ID")
    result = run_invalid_param_test(connector_details, operation_name='update_rogue_app_exposure_status', param_name='rogue_app_exposure_id',
                                    param_type='text', action_params=params_json['update_rogue_app_exposure_status'])
    assert result.get('status') == "failed"


@pytest.mark.update_social_media_threat_status
def test_update_social_media_threat_status_invalid_social_media_threat_id(valid_configuration_with_token, connector_details, params_json):
    set_report_metadata(connector_details, "Update Social Media Threat Status", "Verify with invalid Social Media Threat ID")
    result = run_invalid_param_test(connector_details, operation_name='update_social_media_threat_status', param_name='social_media_threat_id',
                                    param_type='text', action_params=params_json['update_social_media_threat_status'])
    assert result.get('status') == "failed"
