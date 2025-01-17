[日本語](oneview-ansible-ja.md)
# Ansible HPE OneView Modules
### Modules

  * [hpe_icsp_os_deployment - Deploy the operating system on a server using HPE ICsp.](#hpe_icsp_os_deployment)
  * [hpe_icsp_server - Adds, removes and configures servers in ICsp.](#hpe_icsp_server)
  * [image_streamer_artifact_bundle - Manage the Artifact Bundle resource.](#image_streamer_artifact_bundle)
  * [image_streamer_artifact_bundle_facts - Retrieve facts about the Artifact Bundle.](#image_streamer_artifact_bundle_facts)
  * [image_streamer_build_plan - Manages Image Stream OS Build Plan resources.](#image_streamer_build_plan)
  * [image_streamer_build_plan_facts - Retrieve facts about one or more of the Image Streamer Build Plans.](#image_streamer_build_plan_facts)
  * [image_streamer_deployment_group_facts - Retrieve facts about the Image Streamer Deployment Groups.](#image_streamer_deployment_group_facts)
  * [image_streamer_deployment_plan - Manage Image Streamer Deployment Plan resources.](#image_streamer_deployment_plan)
  * [image_streamer_deployment_plan_facts - Retrieve facts about the Image Streamer Deployment Plans.](#image_streamer_deployment_plan_facts)
  * [image_streamer_golden_image - Manage Image Streamer Golden Image resources.](#image_streamer_golden_image)
  * [image_streamer_golden_image_facts - Retrieve facts about one or more of the Image Streamer Golden Image.](#image_streamer_golden_image_facts)
  * [image_streamer_os_volume_facts - Retrieve facts about the Image Streamer OS Volumes.](#image_streamer_os_volume_facts)
  * [image_streamer_plan_script - Manage the Image Streamer Plan Script resources.](#image_streamer_plan_script)
  * [image_streamer_plan_script_facts - Retrieve facts about the Image Streamer Plan Scripts.](#image_streamer_plan_script_facts)
  * [oneview_alert_facts - Retrieve facts about the OneView Alerts.](#oneview_alert_facts)
  * [oneview_appliance_configuration_timeconfig_facts - Retrieve facts about the OneView appliance supported locales.](#oneview_appliance_configuration_timeconfig_facts)
  * [oneview_appliance_device_read_community - Manage the Appliance Device Read Community string.](#oneview_appliance_device_read_community)
  * [oneview_appliance_device_read_community_facts - Retrieve the facts about the OneView appliance device read community.](#oneview_appliance_device_read_community_facts)
  * [oneview_appliance_device_snmp_v1_trap_destinations - Manage the Appliance Device SNMPv1 Trap Destinations.](#oneview_appliance_device_snmp_v1_trap_destinations)
  * [oneview_appliance_device_snmp_v1_trap_destinations_facts - Retrieve the facts about the OneView appliance SNMPv1 trap forwarding destinations.](#oneview_appliance_device_snmp_v1_trap_destinations_facts)
  * [oneview_appliance_device_snmp_v3_trap_destinations - Manage the Appliance Device SNMPv3 Trap Destinations.](#oneview_appliance_device_snmp_v3_trap_destinations)
  * [oneview_appliance_device_snmp_v3_trap_destinations_facts - Retrieve the facts about the OneView appliance SNMPv3 trap forwarding destinations.](#oneview_appliance_device_snmp_v3_trap_destinations_facts)
  * [oneview_appliance_device_snmp_v3_users - Manage the Appliance Device SNMPv3 Users.](#oneview_appliance_device_snmp_v3_users)
  * [oneview_appliance_device_snmp_v3_users_facts - Retrieve the facts about the OneView appliance SNMPv3 users.](#oneview_appliance_device_snmp_v3_users_facts)
  * [oneview_appliance_ssh_access - Manage OneView Appliance SSH Access Configuration.](#oneview_appliance_ssh_access)
  * [oneview_appliance_ssh_access_facts - Retrieve the facts about OneView Appliance SSH Access Configuration.](#oneview_appliance_ssh_access_facts)
  * [oneview_appliance_time_and_locale_configuration - Manage OneView Appliance Locale and Time Configuration.](#oneview_appliance_time_and_locale_configuration)
  * [oneview_appliance_time_and_locale_configuration_facts - Retrieve the facts about the OneView appliance time and locale configuration.](#oneview_appliance_time_and_locale_configuration_facts)
  * [oneview_certificates_server - Manage OneView Certificates Server resources.](#oneview_certificates_server)
  * [oneview_certificates_server_facts - Retrieve the facts about one or more of the OneView Certificates Server.](#oneview_certificates_server_facts)
  * [oneview_connection_template - Manage the OneView Connection Template resources.](#oneview_connection_template)
  * [oneview_connection_template_facts - Retrieve facts about the OneView Connection Templates.](#oneview_connection_template_facts)
  * [oneview_datacenter - Manage OneView Data Center resources.](#oneview_datacenter)
  * [oneview_datacenter_facts - Retrieve facts about the OneView Data Centers.](#oneview_datacenter_facts)
  * [oneview_drive_enclosure - Manage OneView Drive Enclosure resources.](#oneview_drive_enclosure)
  * [oneview_drive_enclosure_facts - Retrieve the facts about one or more of the OneView Drive Enclosures.](#oneview_drive_enclosure_facts)
  * [oneview_enclosure - Manage OneView Enclosure resources.](#oneview_enclosure)
  * [oneview_enclosure_facts - Retrieve facts about one or more Enclosures](#oneview_enclosure_facts)
  * [oneview_enclosure_group - Manage OneView Enclosure Group resources.](#oneview_enclosure_group)
  * [oneview_enclosure_group_facts - Retrieve facts about one or more of the OneView Enclosure Groups.](#oneview_enclosure_group_facts)
  * [oneview_ethernet_network - Manage OneView Ethernet Network resources.](#oneview_ethernet_network)
  * [oneview_ethernet_network_facts - Retrieve the facts about one or more of the OneView Ethernet Networks.](#oneview_ethernet_network_facts)
  * [oneview_event - Manage OneView Events.](#oneview_event)
  * [oneview_event_facts - Retrieve the facts about one or more of the OneView Events.](#oneview_event_facts)
  * [oneview_fabric - Manage OneView Fabric resources.](#oneview_fabric)
  * [oneview_fabric_facts - Retrieve the facts about one or more of the OneView Fabrics.](#oneview_fabric_facts)
  * [oneview_fc_network - Manage OneView Fibre Channel Network resources.](#oneview_fc_network)
  * [oneview_fc_network_facts - Retrieve the facts about one or more of the OneView Fibre Channel Networks](#oneview_fc_network_facts)
  * [oneview_fcoe_network - Manage OneView FCoE Network resources](#oneview_fcoe_network)
  * [oneview_fcoe_network_facts - Retrieve the facts about one or more of the OneView FCoE Networks](#oneview_fcoe_network_facts)
  * [oneview_firmware_bundle - Upload OneView Firmware Bundle resources.](#oneview_firmware_bundle)
  * [oneview_firmware_driver - Provides an interface to remove Firmware Driver resources.](#oneview_firmware_driver)
  * [oneview_firmware_driver_facts - Retrieve the facts about one or more of the OneView Firmware Drivers.](#oneview_firmware_driver_facts)
  * [oneview_hypervisor_cluster_profile - Manage OneView Hypervisor Cluster Profile resources.](#oneview_hypervisor_cluster_profile)
  * [oneview_hypervisor_cluster_profile_facts - Retrieve the facts about one or more of the OneView Hypervisor Cluster Profiles.](#oneview_hypervisor_cluster_profile_facts)
  * [oneview_hypervisor_manager - Manage OneView Hypervisor Manager resources.](#oneview_hypervisor_manager)
  * [oneview_hypervisor_manager_facts - Retrieve the facts about one or more of the OneView Hypervisor Managers.](#oneview_hypervisor_manager_facts)
  * [oneview_id_pools - Manage OneView ID pools resources.](#oneview_id_pools)
  * [oneview_id_pools_facts - Retrieve the facts about OneView ID pools resources.](#oneview_id_pools_ipv4_facts)
  * [oneview_id_pools_ipv4_range - Manage OneView ID pools IPV4 Range resources.](#oneview_id_pools_ipv4_range)
  * [oneview_id_pools_ipv4_range_facts - Retrieve the facts about one or more of the OneView ID Pools IPV4 Ranges.](#oneview_id_pools_ipv4_range_facts)
  * [oneview_id_pools_ipv4_subnet - Manage OneView ID pools IPV4 Subnet resources.](#oneview_id_pools_ipv4_subnet)
  * [oneview_id_pools_ipv4_subnet_facts - Retrieve the facts about one or more of the OneView ID Pools IPV4 Subnets.](#oneview_id_pools_ipv4_subnet_facts)
  * [oneview_interconnect - Manage the OneView Interconnect resources.](#oneview_interconnect)
  * [oneview_interconnect_facts - Retrieve facts about one or more of the OneView Interconnects.](#oneview_interconnect_facts)
  * [oneview_interconnect_link_topology_facts - Retrieve facts about the OneView Interconnect Link Topologies.](#oneview_interconnect_link_topology_facts)
  * [oneview_interconnect_type_facts - Retrieve facts about one or more of the OneView Interconnect Types.](#oneview_interconnect_type_facts)
  * [oneview_internal_link_set_facts - Retrieve facts about the OneView Internal Link Sets.](#oneview_internal_link_set_facts)
  * [oneview_label - Manage Oneview Label Resources.](#oneview_label)
  * [oneview_label_facts - Retrieve facts about Oneview Label Resources.](#oneview_label_facts)
  * [oneview_logical_downlinks_facts - Retrieve facts about one or more of the OneView Logical Downlinks.](#oneview_logical_downlinks_facts)
  * [oneview_logical_enclosure - Manage OneView Logical Enclosure resources.](#oneview_logical_enclosure)
  * [oneview_logical_enclosure_facts - Retrieve facts about one or more of the OneView Logical Enclosures.](#oneview_logical_enclosure_facts)
  * [oneview_logical_interconnect - Manage OneView Logical Interconnect resources.](#oneview_logical_interconnect)
  * [oneview_logical_interconnect_facts - Retrieve facts about one or more of the OneView Logical Interconnects.](#oneview_logical_interconnect_facts)
  * [oneview_logical_interconnect_group - Manage OneView Logical Interconnect Group resources.](#oneview_logical_interconnect_group)
  * [oneview_logical_interconnect_group_facts - Retrieve facts about one or more of the OneView Logical Interconnect Groups](#oneview_logical_interconnect_group_facts)
  * [oneview_logical_switch - Manage OneView Logical Switch resources.](#oneview_logical_switch)
  * [oneview_logical_switch_facts - Retrieve the facts about one or more of the OneView Logical Switches.](#oneview_logical_switch_facts)
  * [oneview_logical_switch_group - Manage OneView Logical Switch Group resources.](#oneview_logical_switch_group)
  * [oneview_logical_switch_group_facts - Retrieve facts about OneView Logical Switch Groups.](#oneview_logical_switch_group_facts)
  * [oneview_login_detail_facts - Retrieve the facts about login details](#oneview_login_detail_facts)
  * [oneview_managed_san - Manage OneView Managed SAN resources.](#oneview_managed_san)
  * [oneview_managed_san_facts - Retrieve facts about the OneView Managed SANs.](#oneview_managed_san_facts)
  * [oneview_network_set - Manage OneView Network Set resources.](#oneview_network_set)
  * [oneview_network_set_facts - Retrieve facts about the OneView Network Sets](#oneview_network_set_facts)
  * [oneview_os_deployment_plan_facts - Retrieve facts about one or more OS Deployment Plans.](#oneview_os_deployment_plan_facts)
  * [oneview_os_deployment_server - Manage OneView Deployment Server resources.](#oneview_os_deployment_server)
  * [oneview_os_deployment_server_facts - Retrieve facts about one or more OS Deployment Servers.](#oneview_os_deployment_server_facts)
  * [oneview_power_device - Manage OneView Power Device resources.](#oneview_power_device)
  * [oneview_power_device_facts - Retrieve facts about the OneView Power Devices.](#oneview_power_device_facts)
  * [oneview_rack - Manage OneView Racks resources.](#oneview_rack)
  * [oneview_rack_facts - Retrieve facts about Rack resources.](#oneview_rack_facts)
  * [oneview_san_manager - Manage OneView SAN Manager resources.](#oneview_san_manager)
  * [oneview_san_manager_facts - Retrieve facts about one or more of the OneView SAN Managers](#oneview_san_manager_facts)
  * [oneview_sas_interconnect - Manage the OneView SAS Interconnect resources.](#oneview_sas_interconnect)
  * [oneview_sas_interconnect_facts - Retrieve facts about the OneView SAS Interconnects.](#oneview_sas_interconnect_facts)
  * [oneview_sas_interconnect_type_facts - Retrieve facts about the OneView SAS Interconnect Types.](#oneview_sas_interconnect_type_facts)
  * [oneview_sas_logical_interconnect - Manage OneView SAS Logical Interconnect resources.](#oneview_sas_logical_interconnect)
  * [oneview_sas_logical_interconnect_facts - Retrieve facts about one or more of the OneView SAS Logical Interconnects.](#oneview_sas_logical_interconnect_facts)
  * [oneview_sas_logical_interconnect_group - Manage OneView SAS Logical Interconnect Group resources.](#oneview_sas_logical_interconnect_group)
  * [oneview_sas_logical_interconnect_group_facts - Retrieve facts about one or more of the OneView SAS Logical Interconnect Groups.](#oneview_sas_logical_interconnect_group_facts)
  * [oneview_sas_logical_jbod_attachment_facts - Retrieve facts about one or more of the OneView SAS Logical JBOD Attachments.](#oneview_sas_logical_jbod_attachment_facts)
  * [oneview_sas_logical_jbod_facts - Retrieve facts about one or more of the OneView SAS Logical JBODs.](#oneview_sas_logical_jbod_facts)
  * [oneview_scope - Manage OneView Scope resources.](#oneview_scope)
  * [oneview_scope_facts - Retrieve facts about one or more of the OneView Scopes.](#oneview_scope_facts)
  * [oneview_server_hardware - Manage OneView Server Hardware resources.](#oneview_server_hardware)
  * [oneview_server_hardware_facts - Retrieve facts about the OneView Server Hardware.](#oneview_server_hardware_facts)
  * [oneview_server_hardware_type - Manage OneView Server Hardware Type resources.](#oneview_server_hardware_type)
  * [oneview_server_hardware_type_facts - Retrieve facts about Server Hardware Types of the OneView.](#oneview_server_hardware_type_facts)
  * [oneview_server_profile - Manage OneView Server Profile resources](#oneview_server_profile)
  * [oneview_server_profile_facts - Retrieve facts about the OneView Server Profiles.](#oneview_server_profile_facts)
  * [oneview_server_profile_template - Manage OneView Server Profile Template resources.](#oneview_server_profile_template)
  * [oneview_server_profile_template_facts - Retrieve facts about the Server Profile Templates from OneView.](#oneview_server_profile_template_facts)
  * [oneview_storage_pool - Manage OneView Storage Pool resources.](#oneview_storage_pool)
  * [oneview_storage_pool_facts - Retrieve facts about one or more Storage Pools.](#oneview_storage_pool_facts)
  * [oneview_storage_system - Manage OneView Storage System resources.](#oneview_storage_system)
  * [oneview_storage_system_facts - Retrieve facts about the OneView Storage Systems](#oneview_storage_system_facts)
  * [oneview_storage_volume_attachment - Provides an interface to remove extra presentations from a specified server profile.](#oneview_storage_volume_attachment)
  * [oneview_storage_volume_attachment_facts - Retrieve facts about the OneView Storage Volume Attachments.](#oneview_storage_volume_attachment_facts)
  * [oneview_storage_volume_template - Manage OneView Storage Volume Template resources.](#oneview_storage_volume_template)
  * [oneview_storage_volume_template_facts - Retrieve facts about Storage Volume Templates of the OneView.](#oneview_storage_volume_template_facts)
  * [oneview_switch - Provides an interface to remove ToR Switch resources.](#oneview_switch)
  * [oneview_switch_facts - Retrieve facts about the OneView Switches.](#oneview_switch_facts)
  * [oneview_switch_type_facts - Retrieve facts about the OneView Switch Types.](#oneview_switch_type_facts)
  * [oneview_task_facts - Retrieve facts about the OneView Tasks.](#oneview_task_facts)
  * [oneview_unmanaged_device - Manage OneView Unmanaged Device resources.](#oneview_unmanaged_device)
  * [oneview_unmanaged_device_facts - Retrieve facts about one or more of the OneView Unmanaged Device.](#oneview_unmanaged_device_facts)
  * [oneview_uplink_set - Manage OneView Uplink Set resources.](#oneview_uplink_set)
  * [oneview_uplink_set_facts - Retrieve facts about one or more of the OneView Uplink Sets.](#oneview_uplink_set_facts)
  * [oneview_user - Manage OneView Users.](#oneview_user)
  * [oneview_user_facts - Retrieve the facts about one or more of the OneView Users.](#oneview_user_facts)
  * [oneview_version_facts - Returns the range of possible API versions supported by the appliance](#oneview_version_facts)
  * [oneview_volume - Manage OneView Volume resources.](#oneview_volume)
  * [oneview_volume_facts - Retrieve facts about the OneView Volumes.](#oneview_volume_facts)

---

## hpe_icsp_os_deployment
Deploy the operating system on a server using HPE ICsp.

#### Synopsis
 Deploy the operating system on a server based on the available ICsp OS build plan.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpICsp >= 1.0.2

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| api_version  |   No  |  300  | |  ICsp API version.  |
| custom_attributes  |   No  |  | |  Custom Attributes.  |
| icsp_host  |   Yes  |  | |  ICsp hostname.  |
| os_build_plan  |   Yes  |  | |  OS Build plan.  |
| password  |   Yes  |  | |  ICsp password.  |
| personality_data  |   No  |  | |  Personality Data.  |
| server_id  |   No  |  | |  Server ID. Deprecated, IP address is preferred (server_ipAddress).  |
| server_ipAddress  |   No  |  | |  The IP address of the iLO of the server.  |
| username  |   Yes  |  | |  ICsp username.  |



#### Examples

```yaml

- name: Deploy OS
  hpe_icsp_os_deployment:
    icsp_host: "{{ icsp }}"
    username: "{{ icsp_username }}"
    password: "{{ icsp_password }}"
    server_id: "{{ server_profile.serialNumber }}"
    server_ipAddress: "{{server_iLO_ip}}"
    os_build_plan: "{{ os_build_plan }}"
    custom_attributes: "{{ osbp_custom_attributes }}"
    personality_data: "{{ network_config }}"
  delegate_to: localhost

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| icsp_server   | Has the facts about the server that was provisioned with ICsp. |  When the module runs successfully, but can be null. |  dict |



---


## hpe_icsp_server
Adds, removes and configures servers in ICsp.

#### Synopsis
 This module allows you to add, remove and configure servers in the Insight Control Server Provisioning (ICsp). In ICsp, a server, often referred to as a Target Server, is a physical ProLiant server or a virtual machine that can have actions taken upon it.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpICsp >= 1.0.2

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| api_version  |   No  |  300  | |  ICsp API version.  |
| icsp_host  |   Yes  |  | |  ICsp hostname.  |
| password  |   Yes  |  | |  ICsp password.  |
| server_ipAddress  |   Yes  |  | |  The IP address of the iLO of the server.  |
| server_password  |   Yes  |  | |  The password required to log into the server's iLO  |
| server_personality_data  |   No  |  | |  Additional data to send to ICsp.  |
| server_port  |   No  |  [443]  | |  The iLO port to use when logging in.  |
| server_username  |   Yes  |  | |  The username required to log into the server's iLO.  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li>  <li>network_configured</li> </ul> |  Indicates the desired state for the ICsp server. 'present' will register the resource on ICsp. 'absent' will remove the resource from ICsp, if it exists. 'network_configured' will set the network configuration.  |
| username  |   Yes  |  | |  ICsp username.  |



#### Examples

```yaml

  - name: Ensure the server is registered in ICsp
    hpe_icsp_server:
      icsp_host: "{{icsp_host}}"
      username: "{{icsp_username}}"
      password: "{{icsp_password}}"
      server_ipAddress: "{{server_iLO_ip}}"
      server_username: "Admin"
      server_password: "admin"
      state: present
    delegate_to: localhost

  - name: Set the network configuration
    hpe_icsp_server:
      icsp_host: "{{ icsp }}"
      username: "{{ icsp_username }}"
      password: "{{ icsp_password }}"
      server_ipAddress: "{{ server_ipAddress }}"
      server_username: "{{ server_username }}"
      server_password: "{{ server_password }}"
      server_personality_data: "{{ network_config }}"
      state: network_configured
    delegate_to: localhost

  - name: Ensure the server is removed from ICsp
    hpe_icsp_server:
      icsp_host: "{{icsp_host}}"
      username: "{{icsp_username}}"
      password: "{{icsp_password}}"
      server_ipAddress: "{{server_iLO_ip}}"
      server_username: "Admin"
      server_password: "admin"
      state: absent
    delegate_to: localhost

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| target_server   | Has the facts about the server that was added to ICsp. |  On states 'present' and 'network_configured' . Can be null. |  dict |



---


## image_streamer_artifact_bundle
Manage the Artifact Bundle resource.

#### Synopsis
 Provides an interface to manage the Artifact Bundle. Can create, update, remove, and download, upload, extract

#### Requirements (on the host that executes the module)
  * python >= 3.4.2
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with Artifact Bundle properties and its associated states.  |
| state  |   Yes  |  | <ul> <li>present</li>  <li>absent</li>  <li>downloaded</li>  <li>archive_downloaded</li>  <li>backup_uploaded</li>  <li>backup_created</li>  <li>extracted</li>  <li>backup_extracted</li> </ul> |  Indicates the desired state for the Artifact Bundle resource. `present` will ensure data properties are compliant with OneView. When the artifact bundle already exists, only the name is updated. Changes in any other attribute value is ignored. `absent` will remove the resource from OneView, if it exists. `downloaded` will download the Artifact Bundle to the file path provided. `archive_downloaded` will download the Artifact Bundle archive to the file path provided. `backup_uploaded` will upload the Backup for the Artifact Bundle from the file path provided. `backup_created` will create a Backup for the Artifact Bundle. `extracted` will extract an Artifact Bundle. `backup_extracted` will extract an Artifact Bundle from the Backup.  |



#### Examples

```yaml

- name: Create an Artifact Bundle
  image_streamer_artifact_bundle:
    config: "{{ config }}"
    state: present
    data:
      name: 'Artifact Bundle'
      description: 'Description of Artifact Bundles Test'
      buildPlans:
        - resourceUri: '/rest/build-plans/ab65bb06-4387-48a0-9a5d-0b0da2888508'
          readOnly: 'false'
  delegate_to: localhost

- name: Download the Artifact Bundle to the file path provided
  image_streamer_artifact_bundle:
    config: "{{ config }}"
    state: downloaded
    data:
      name: 'Artifact Bundle'
      destinationFilePath: '~/downloaded_artifact.zip'
  delegate_to: localhost

- name: Download the Archive for Artifact Bundle to the file path provided
  image_streamer_artifact_bundle:
    config: "{{ config }}"
    state: archive_downloaded
    data:
      name: 'Artifact Bundle'
      destinationFilePath: '~/downloaded_archive.zip'
  delegate_to: localhost

- name: Upload an Artifact Bundle
  image_streamer_artifact_bundle:
    config: "{{ config }}"
    state: present
    data:
      localArtifactBundleFilePath: '~/uploaded_artifact.zip'
  delegate_to: localhost

- name: Upload Backup an Artifact Bundle
  image_streamer_artifact_bundle:
    config: "{{ config }}"
    state: backup_uploaded
    data:
      deploymentGroupURI: '/rest/deployment-groups/c5a727ef-71e9-4154-a512-6655b168c2e3'
      localBackupArtifactBundleFilePath: '~/uploaded_backup.zip'
  delegate_to: localhost

- name: Create Backup for Artifact Bundle
  image_streamer_artifact_bundle:
    config: "{{ config }}"
    state: backup_created
    data:
      deploymentGroupURI: '/rest/deployment-groups/c5a727ef-71e9-4154-a512-6655b168c2e3'
  delegate_to: localhost

- name: Extract an Artifact Bundle
  image_streamer_artifact_bundle:
    config: "{{ config }}"
    state: extracted
    data:
      name: 'Artifact Bundle'
  delegate_to: localhost

- name: Extract Backup an Artifact Bundle
  image_streamer_artifact_bundle:
    config: "{{ config }}"
    state: backup_extracted
    data:
      deploymentGroupURI: '/rest/deployment-groups/c5a727ef-71e9-4154-a512-6655b168c2e3'
  delegate_to: localhost

- name: Update an Artifact Bundle
  image_streamer_artifact_bundle:
    config: "{{ config }}"
    state: present
    data:
      name: 'Artifact Bundle'
      newName: 'Artifact Bundle Updated'
  delegate_to: localhost

- name: Remove an Artifact Bundle
  image_streamer_artifact_bundle:
    config: "{{ config }}"
    state: absent
    data:
      name: 'Artifact Bundle'
  delegate_to: localhost

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| artifact_bundle   | Has the OneView facts about the Artifact Bundles. |  On state 'present' and 'extracted'. |  dict |
| artifact_bundle_deployment_group   | Has the OneView facts about the Deployment Group. |  On state 'backup_extracted', 'backup_uploaded', and 'backup_created'. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## image_streamer_artifact_bundle_facts
Retrieve facts about the Artifact Bundle.

#### Synopsis
 Retrieve facts about the Artifact Bundle.

#### Requirements (on the host that executes the module)
  * python >= 3.4.2
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Name of the Artifact Bundle.  |
| options  |   No  |  | |  List with options to gather additional facts about the Artifact Bundle. Options allowed: `allBackups` gets the list of backups for the Artifact Bundles. `backupForAnArtifactBundle` gets the list of backups for the Artifact Bundle.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Artifact Bundles
  image_streamer_artifact_bundle_facts:
    config: "{{ config }}"
  delegate_to: localhost
- debug: var=artifact_bundles

- name: Gather paginated, filtered and sorted facts about Artifact Bundles
  image_streamer_artifact_bundle_facts:
    config: "{{ config }}"
    params:
      start: 0
      count: 3
      sort: name:ascending
      filter: state=OK
  delegate_to: localhost
- debug: var=artifact_bundles

- name: Gather facts about an Artifact Bundle by name
  image_streamer_artifact_bundle_facts:
    config: "{{ config }}"
    name: "Artifact Bundles Test"
  delegate_to: localhost
- debug: var=artifact_bundles

- name: Gather facts about all Backups for Artifact Bundle
  image_streamer_artifact_bundle_facts:
    config: "{{ config }}"
    name: "Artifact Bundles Test"
    options:
      - allBackups
  delegate_to: localhost
- debug: var=artifact_bundles
- debug: var=artifact_bundle_backups
```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| artifact_bundle_backups   | The list of backups for the Artifact Bundles. |  When requested, but can also be null. |  list |
| artifact_bundles   | The list of Artifact Bundles. |  Always, but can be also null. |  list |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## image_streamer_build_plan
Manages Image Stream OS Build Plan resources.

#### Synopsis
 Provides an interface to manage Image Stream OS Build Plans. Can create, update, and remove.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with OS Build Plan properties and its associated states.  |
| state  |   Yes  |  | <ul> <li>present</li>  <li>absent</li> </ul> |  Indicates the desired state for the OS Build Plan resource. `present` will ensure data properties are compliant with Synergy Image Streamer. `absent` will remove the resource from Synergy Image Streamer, if it exists.  |



#### Examples

```yaml

- name: Create an OS Build Plan
  image_streamer_build_plan:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: 'Demo OS Build Plan'
      description: "oebuildplan"
      oeBuildPlanType: "deploy"
  delegate_to: localhost

- name: Update the OS Build Plan description and name
  image_streamer_build_plan:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: 'Demo OS Build Plan'
      description: "New description"
      newName: 'OS Build Plan Renamed'
  delegate_to: localhost

- name: Remove an OS Build Plan
  image_streamer_build_plan:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: absent
    data:
        name: 'Demo OS Build Plan'
  delegate_to: localhost

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| build_plan   | Has the OneView facts about the OS Build Plan. |  On state 'present'. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## image_streamer_build_plan_facts
Retrieve facts about one or more of the Image Streamer Build Plans.

#### Synopsis
 Retrieve facts about one or more of the Image Streamer Build Plans.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Build Plan name.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Build Plans
  image_streamer_build_plan_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
  delegate_to: localhost
- debug: var=build_plans

- name: Gather paginated, filtered and sorted facts about Build Plans
  image_streamer_build_plan_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 0
      count: 3
      sort: name:ascending
      filter: oeBuildPlanType=capture
  delegate_to: localhost
- debug: var=build_plans

- name: Gather facts about a Build Plan by name
  image_streamer_build_plan_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "{{ name }}"
  delegate_to: localhost
- debug: var=build_plans

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| build_plans   | The list of Build Plans. |  Always, but can be null. |  list |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## image_streamer_deployment_group_facts
Retrieve facts about the Image Streamer Deployment Groups.

#### Synopsis
 Retrieve facts about the Image Streamer Deployment Groups.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Name of the Deployment Group.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Deployment Groups
  image_streamer_deployment_group_facts:
    config: "{{ config }}"
  delegate_to: localhost

- debug: var=deployment_groups

- name: Gather paginated, filtered and sorted facts about Deployment Groups
  image_streamer_deployment_group_facts:
    config: "{{ config }}"
    params:
      start: 0
      count: 3
      sort: name:ascending
      filter: state=OK
  delegate_to: localhost

- debug: var=deployment_groups

- name: Gather facts about a Deployment Group by name
  image_streamer_deployment_group_facts:
    config: "{{ config_path }}"
    name: "OSS"
  delegate_to: localhost

- debug: var=deployment_groups

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| deployment_groups   | The list of Deployment Groups |  Always, but can be empty. |  list |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## image_streamer_deployment_plan
Manage Image Streamer Deployment Plan resources.

#### Synopsis
 Provides an interface to manage Image Streamer Deployment Plans. Can create, update, and remove.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with Deployment Plan properties and its associated states.  |
| state  |   Yes  |  | <ul> <li>present</li>  <li>absent</li> </ul> |  Indicates the desired state for the Deployment Plan resource. `present` will ensure data properties are compliant with Synergy Image Streamer. `absent` will remove the resource from Synergy Image Streamer, if it exists.  |



#### Examples

```yaml

- name: Create a Deployment Plan
  image_streamer_deployment_plan:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      description: "Description of this Deployment Plan"
      name: 'Demo Deployment Plan'
      hpProvided: 'false'
      oeBuildPlanName: "Demo Build Plan"
  delegate_to: localhost

- name: Update the Deployment Plan
  image_streamer_deployment_plan:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: 'Demo Deployment Plan'
      newName:  'Demo Deployment Plan (changed)'
      description: "New description"
  delegate_to: localhost

- name: Remove the Deployment Plan
  image_streamer_deployment_plan:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: absent
    data:
        name: 'Demo Deployment Plan'
  delegate_to: localhost

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| deployment_plan   | Has the facts about the Image Streamer Deployment Plan. |  On state 'present', but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## image_streamer_deployment_plan_facts
Retrieve facts about the Image Streamer Deployment Plans.

#### Synopsis
 Retrieve facts about one or more of the Image Streamer Deployment Plans.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Deployment Plan name.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Deployment Plans
  image_streamer_deployment_plan_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
  delegate_to: localhost
- debug: var=deployment_plans

- name: Gather paginated, filtered and sorted facts about Deployment Plans
  image_streamer_deployment_plan_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 0
      count: 3
      sort: name:ascending
      filter: state=active
  delegate_to: localhost
- debug: var=deployment_plans

- name: Gather facts about a Deployment Plan by name
  image_streamer_deployment_plan_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "Demo Deployment Plan"
  delegate_to: localhost
- debug: var=deployment_plans

- name: Gather facts about Server Profiles and Server Profile Templates that are using Deployment Plan
  image_streamer_deployment_plan_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "Demo Deployment Plan"
    options: "usedby"
  delegate_to: localhost
- debug: var=deployment_plans

- name: Get the OS deployment plan details from OneView for a deployment plan
  image_streamer_deployment_plan_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "Demo Deployment Plan"
    options: "osdp"
  delegate_to: localhost
- debug: var=deployment_plans

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| deployment_plans   | The list of Deployment Plans. |  Always, but can be null. |  list |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## image_streamer_golden_image
Manage Image Streamer Golden Image resources.

#### Synopsis
 Provides an interface to manage Image Streamer Golden Image. Can create, add, update, and remove.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with Golden Image properties and its associated states.  |
| state  |   Yes  |  | <ul> <li>present</li>  <li>absent</li>  <li>downloaded</li>  <li>archive_downloaded</li> </ul> |  Indicates the desired state for the Golden Image resource. `present` will ensure data properties are compliant with Synergy Image Streamer. `absent` will remove the resource from Synergy Image Streamer, if it exists. `downloaded` will download the Golden Image to the file path provided. `archive_downloaded` will download the Golden Image archive to the file path provided.  |



#### Examples

```yaml

- name: Add a Golden Image from OS Volume
  image_streamer_golden_image:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: 'Demo Golden Image creation'
      description: "Test Description"
      imageCapture: "true"
      osVolumeName: 'OSVolume-20'
      buildPlanName: 'Buld Plan name'
  delegate_to: localhost

- name: Create a Golden Image uploading from a local file
  image_streamer_golden_image:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: 'Demo Golden Image upload'
      description: "Test"
      localImageFilePath: '~/image_file.zip'
  delegate_to: localhost

- name: Update the Golden Image description and name
  image_streamer_golden_image:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: 'Demo Golden Image upload'
      description: "New description"
      newName: 'Golden Image Renamed'
  delegate_to: localhost

- name: Download the Golden Image to the file path provided
  image_streamer_golden_image:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: downloaded
    data:
      name: 'Demo Golden Image'
      destination_file_path: '~/downloaded_image.zip'
  delegate_to: localhost

- name: Download the Golden Image archive log to the file path provided
  image_streamer_golden_image:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: archive_downloaded
    data:
      name: 'Demo Golden Image'
      destination_file_path: '~/archive.log'
  delegate_to: localhost

- name: Remove a Golden Image
  image_streamer_golden_image:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: absent
    data:
        name: 'Golden Image name'
  delegate_to: localhost

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| golden_image   | Has the OneView facts about the Golden Image. |  On state 'present'. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## image_streamer_golden_image_facts
Retrieve facts about one or more of the Image Streamer Golden Image.

#### Synopsis
 Retrieve facts about one or more of the Image Streamer Golden Image.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Golden Image name.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Golden Images
  image_streamer_golden_image_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
  delegate_to: localhost
- debug: var=golden_images

- name: Gather paginated, filtered and sorted facts about Golden Images
  image_streamer_golden_image_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 0
      count: 3
      sort: name:ascending
      filter: importedFromBundle=true
  delegate_to: localhost
- debug: var=golden_images

- name: Gather facts about a Golden Image by name
  image_streamer_golden_image_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "{{ name }}"
  delegate_to: localhost
- debug: var=golden_images

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| golden_images   | The list of Golden Images. |  Always, but can be null. |  list |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## image_streamer_os_volume_facts
Retrieve facts about the Image Streamer OS Volumes.

#### Synopsis
 Retrieve facts about the Image Streamer OS Volumes.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Name of the OS Volume.  |
| options  |   No  |  | |  List with options to gather additional facts about OS volumes. Options allowed: `getStorage` gets the storage details of an OS volume `getArchivedLogs` gets the archived logs of an OS volume  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all OS Volumes
  image_streamer_os_volume_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    image_streamer_hostname: 172.16.101.48
  delegate_to: localhost
- debug: var=os_volumes

- name: Gather paginated, filtered and sorted facts about OS Volumes
  image_streamer_os_volume_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    image_streamer_hostname: 172.16.101.48
    params:
      start: 0
      count: 3
      sort: name:ascending
      filter: status=OK
  delegate_to: localhost
- debug: var=os_volumes

- name: Gather facts about an OS Volume by name
  image_streamer_os_volume_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    image_streamer_hostname: 172.16.101.48
    name: "Test Volume"
  delegate_to: localhost
- debug: var=os_volumes

- name: Gather facts about storage of an OS Volume
  image_streamer_os_volume_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    image_streamer_hostname: 172.16.101.48
    name: "Test Volume"
    options:
      - getStorage
  delegate_to: localhost
- debug: var=storage

- name: Get archived logs of the OS volume
  image_streamer_os_volume_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    image_streamer_hostname: 172.16.101.48
    name: "Test Volume"
    options:
      - getArchivedLogs:
          file_path: './archived.logs'
  delegate_to: localhost
- debug: var=log_file_path


```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| log_file_path   | OS volume archived log file path |   |  str |
| os_volumes   | The list of OS Volumes |  Always, but can be empty. |  list |
| storage   | Storage details of an OS volume. |   |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## image_streamer_plan_script
Manage the Image Streamer Plan Script resources.

#### Synopsis
 Provides an interface to manage the Image Streamer Plan Script. Can create, update, and remove.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with Plan Script properties and its associated states.  |
| state  |   Yes  |  | <ul> <li>present</li>  <li>absent</li>  <li>differences_retrieved</li> </ul> |  Indicates the desired state for the Plan Script resource. `present` will ensure data properties are compliant with Synergy Image Streamer. `absent` will remove the resource from Synergy Image Streamer, if it exists. `differences_retrieved` will retrieve the modified contents of the Plan Script as per the selected attributes.  |



#### Examples

```yaml

- name: Create a Plan Script
  image_streamer_plan_script:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    image_streamer_hostname: 172.16.101.48
    state: present
    data:
      description: "Description of this plan script"
      name: 'Demo Plan Script'
      hpProvided: False
      planType: "deploy"
      content: 'echo "test script"'
  delegate_to: localhost

- name: Update the Plan Script
  image_streamer_plan_script:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    image_streamer_hostname: 172.16.101.48
    state: present
    data:
      name: 'Demo Plan Script'
      newName:  'Demo Plan Script new name'
      description: "New description"
      content: 'echo "test script changed"'
  delegate_to: localhost

- name: Retrieve the Plan Script content differences
  image_streamer_plan_script:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    image_streamer_hostname: 172.16.101.48
    state: differences_retrieved
    data:
      name: 'Demo Plan Script'
      content: 'echo "test script changed 2"'
  delegate_to: localhost
- debug: var=plan_script_differences

- name: Remove the Plan Script
  image_streamer_plan_script:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    image_streamer_hostname: 172.16.101.48
    state: absent
    data:
        name: 'Demo Plan Script'
  delegate_to: localhost

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| plan_script   | Has the facts about the Image Streamer Plan Script. |  On state 'present', but can be null. |  dict |
| plan_script_differences   | Has the facts about the modified contents of the Plan Script as per the selected attributes. |  On state 'differences_retrieved'. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## image_streamer_plan_script_facts
Retrieve facts about the Image Streamer Plan Scripts.

#### Synopsis
 Retrieve facts about one or more of the Image Streamer Plan Script.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Plan Script name.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Plan Scripts
  image_streamer_plan_script_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    image_streamer_hostname: 172.16.101.48
  delegate_to: localhost
- debug: var=plan_scripts

- name: Gather paginated, filtered and sorted facts about Plan Scripts
  image_streamer_plan_script_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    image_streamer_hostname: 172.16.101.48
    params:
      start: 0
      count: 3
      sort: name:ascending
      filter: planType=capture
  delegate_to: localhost
- debug: var=plan_scripts

- name: Gather facts about a Plan Script by name
  image_streamer_plan_script_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    image_streamer_hostname: 172.16.101.48
    name: "Demo Plan Script"
  delegate_to: localhost
- debug: var=plan_scripts

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| plan_scripts   | The list of Plan Scripts. |  Always, but can be null. |  list |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_alert_facts
Retrieve facts about the OneView Alerts.

#### Synopsis
 Retrieve facts about the OneView Alerts.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| params  |   No  |  | |  List with parameters to help filter the alerts. Params allowed: `count`, `fields`, `filter`, `query`, `sort`, `start`, and `view`.  |



#### Examples

```yaml

- name: Gather facts about the last 2 alerts
  oneview_alert_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      count: 2

- debug: var=alerts

- name: Gather facts about the alerts with state 'Cleared'
  oneview_alert_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      count: 2
      filter: "alertState='Cleared'"

- debug: var=alerts

- name: Gather facts about the alerts with urgency 'High'
  oneview_alert_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      count: 5
      filter: "urgency='High'"

- debug: var=alerts

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| alerts   | The list of alerts. |  Always, but can be null. |  list |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_appliance_configuration_timeconfig_facts
Retrieve facts about the OneView Time Configuration.

#### Synopsis
 Retrieve facts about the OneView Time Configuration.

#### Requirements (on the host that executes the module)
  * python >= 3.4.2
  * hpeOneView >= 6.0.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |



## Example Playbook

```yaml

- name: Gather Facts about Oneview Appliance time configuration
  oneview_appliance_configuration_timeconfig_facts:
    config: "{{ config }}"
  delegate_to: localhost

- debug: var=appliance_configuration_timeconfig

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| appliance_configuration_timeconfig   | Has all the OneView facts about the supported appliance locales. |  Always. Cannot be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_appliance_device_read_community
Manage the Appliance Device Read Community string.

#### Synopsis
 Provides an interface to manage the Appliance Device Read Community string. It can only update it. This results in an update of the community string on all servers being managed/monitored by this OneView instance. The supported characters for community string are aA-zA, 0-9, !, ",

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with the Appliance Device Read Community.  |
| state  |   |  | <ul> <li>present</li> </ul> |  Indicates the desired state for the Appliance Device Read Community. `present` ensures data properties are compliant with OneView.  |



#### Examples

```yaml

- name: Ensure that the Appliance Device Read Community is present with Community String 'public'
  oneview_appliance_device_read_community:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      communityString: 'public'
  delegate_to: localhost

- debug:
    var: appliance_device_read_community

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| appliance_device_read_community   | Has all the OneView facts about the OneView Appliance Device Read Community. |  Always. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_appliance_device_read_community_facts
Retrieve the facts about the OneView appliance device read community.

#### Synopsis
 Retrieve the facts about the OneView appliance device read community.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |



#### Examples

```yaml

- name: Gather facts about the Appliance snmp configuration
  oneview_appliance_device_read_community_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200

- debug:
    var: appliance_device_read_community

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| appliance_device_read_community   | Has all the OneView facts about the OneView appliance device read community. |  Always. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_appliance_device_snmp_v1_trap_destinations
Manage the Appliance Device SNMPv1 Trap Destinations.

#### Synopsis
 Provides an interface to manage the Appliance Device SNMPv1 Trap Destinations.

#### Requirements (on the host that executes the module)
  * python >= 3.4.2
  * hpeOneView >= 6.0.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   No  |  | |  List with the SNMPv1 Trap Destination properties  |
| name  |   Yes  |  | |  SNMPv1 Trap Destination address  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  Indicates the desired state for the Appliance Device SNMPv1 Trap Destinations. `present` ensures data properties are compliant with OneView. `absent` removes the resource from OneView, if it exists.  |



#### Examples

```yaml

- name: Create or Update an Appliance Device SNMPv1 Trap Destination by Destination Address
  oneview_appliance_device_snmp_v1_trap_destinations:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2600
    state: present
    name: 10.0.0.1
    data:
      communityString: "public"
      destination: "10.0.0.1"
      port: 162
  delegate_to: localhost

- debug:
    var: appliance_device_snmp_v1_trap_destinations

- name: Create or Update an Appliance Device SNMPv1 Trap Destination by URI
  oneview_appliance_device_snmp_v1_trap_destinations:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2600
    state: present
    name: 10.0.0.1
    data:
      communityString: "private"
      uri: "/rest/appliance/trap-destinations/1"
      port: 162
  delegate_to: localhost

- debug:
    var: appliance_device_snmp_v1_trap_destinations

- name: Delete an Appliance Device SNMPv1 Trap Destination by Destination Address
  oneview_appliance_device_snmp_v1_trap_destinations:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2600
    state: absent
    name: 10.0.0.1
  delegate_to: localhost

- debug:
    var: appliance_device_snmp_v1_trap_destinations
```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| appliance_device_snmp_v1_trap_destinations   | Has all the OneView facts about the OneView appliance SNMPv1 trap forwarding destinations. |  On state 'present'. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_appliance_device_snmp_v1_trap_destinations_facts
Retrieve the facts about the OneView appliance SNMPv1 trap forwarding destinations.

#### Synopsis
 The appliance has the ability to forward events received from monitored or managed server hardware to the specified destinations as SNMPv1 traps. This module retrives the facts about the appliance SNMPv1 trap forwarding destinations.

#### Requirements (on the host that executes the module)
  * python >= 3.4.2
  * hpeOneView >= 6.0.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Name of trap destination.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all appliance SNMPv1 trap forwarding destinations.
  oneview_appliance_device_snmp_v1_trap_destinations_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2600
  delegate_to: localhost

- debug:
    var: appliance_device_snmp_v1_trap_destinations

- name: Gather paginated, filtered and sorted facts about SNMPv1 trap forwarding destinations
  oneview_appliance_device_snmp_v1_trap_destinations_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2600
    params:
      start: 0
      count: 3
      sort: 'destination:descending'
      filter: "port='162'"
  delegate_to: localhost

- debug:
    var: appliance_device_snmp_v1_trap_destinations

- name: Gather facts about a Trap Destination by Name
  oneview_appliance_device_snmp_v1_trap_destinations_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2600
    name: '1.1.1.1'
  delegate_to: localhost

- debug:
    var: appliance_device_snmp_v1_trap_destinations

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| appliance_device_snmp_v1_trap_destinations   | Has all the OneView facts about the OneView appliance SNMPv1 trap forwarding destinations. |  Always. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_appliance_device_snmp_v3_trap_destinations
Manage the Appliance Device SNMPv3 Trap Destinations.

#### Synopsis
 Provides an interface to manage the Appliance Device SNMPv3 Trap Destinations.

#### Requirements (on the host that executes the module)
  * python >= 3.4.2
  * hpeOneView >= 6.0.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   Yes  |  | |  SNMPv3 Trap Destination Address  |
| data  |   No  |  | |  List with the SNMPv3 Trap Destinations properties  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  Indicates the desired state for the Appliance Device SNMPv3 Trap Destinations. `present` ensures data properties are compliant with OneView. `absent` removes the resource from OneView, if it exists.  |



#### Examples

```yaml

- name: Ensure that the SNMPv3 Trap Destination is present
  oneview_appliance_device_snmp_v3_trap_destinations:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2600
    state: present
    name: 10.0.0.1
    data:
        destinationAddress: "10.0.0.1"
        port: 162
        userName: "test1"
  delegate_to: localhost

- debug:
    var: appliance_device_snmp_v3_trap_destinations

- name: Update the userId of specified SNMPv3 Trap Destination
  oneview_appliance_device_snmp_v3_trap_destinations:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2600
    name: 10.0.0.1
    state: present
    data:
      destinationAddress: "10.0.0.1"
      userId: "3953867c-5283-4059-a9ae-33487f901e85"
  delegate_to: localhost

- debug:
    var: appliance_device_snmp_v3_trap_destinations

- name: Ensure that the SNMPv3 Trap Destination is absent
  oneview_appliance_device_snmp_v3_trap_destinations:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2600
    state: absent
    name: 10.0.0.1
  delegate_to: localhost

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| appliance_device_snmp_v3_trap_destinations   | Has all the OneView facts about the OneView appliance SNMPv3 Trap Destination. |  On state 'present'. Can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_appliance_device_snmp_v3_trap_destinations_facts
Retrieve the facts about the OneView appliance SNMPv3 trap forwarding destinations.

#### Synopsis
 The appliance has the ability to forward events received from monitored or managed server hardware to the specified destinations as SNMPv3 traps. This module retrives the facts about the appliance SNMPv3 trap forwarding destinations.

#### Requirements (on the host that executes the module)
  * python >= 3.4.2
  * hpeOneView >= 6.0.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Name of trap destination.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about the appliance SNMPv3 trap forwarding destinations.
  oneview_appliance_device_snmp_v3_trap_destinations_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2600
  delegate_to: localhost

- debug:
    var: appliance_device_snmp_v3_trap_destinations

- name: Gather paginated, filtered and sorted facts about SNMPv3 trap forwarding destinations
  oneview_appliance_device_snmp_v3_trap_destinations_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2600
    params:
      start: 0
      count: 3
      sort: 'destinationAddress:descending'
      filter: "port='162'"
  delegate_to: localhost

- debug:
    var: appliance_device_snmp_v3_trap_destinations

- name: Gather facts about a Trap Destination by Name
  oneview_appliance_device_snmp_v3_trap_destinations_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2600
    name: "test_user"
  delegate_to: localhost

- debug:
    var: appliance_device_snmp_v3_trap_destinations

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| appliance_device_snmp_v3_trap_destinations   | Has all the OneView facts about the OneView appliance SNMPv3 trap forwarding destinations. |  Always. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_appliance_device_snmp_v3_users
Manage the Appliance Device SNMPv3 Users.

#### Synopsis
 Provides an interface to manage the Appliance Device SNMPv3 Users.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with the SNMPv3 Users properties  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li>  <li>set_password</li> </ul> |  Indicates the desired state for the Appliance Device SNMPv3 User. `present` ensures data properties are compliant with OneView. `absent` removes the resource from OneView, if it exists. `set_password` will set a user password to the value specified. This operation is non-idempotent.  |



#### Examples

```yaml

- name: Ensure that the SNMPv3 user is present using the default configuration
  oneview_appliance_device_snmp_v3_users:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
        type: "Users"
        userName: "testUser"
        securityLevel: "Authentication"
        authenticationProtocol: "SHA512"
  delegate_to: localhost

- debug:
    var: appliance_device_snmp_v3_users

- name: Set the password of specified SNMPv3 user
  oneview_appliance_device_snmp_v3_users:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      userName: "testUser"
      authenticationPassphrase: "NewPass1234"
  delegate_to: localhost

- debug:
    var: appliance_device_snmp_v3_users

- name: Ensure that the SNMPv3 user is absent
  oneview_appliance_device_snmp_v3_users:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: absent
    data:
        userName: "testUser"
  delegate_to: localhost

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| appliance_device_snmp_v3_users   | Has all the OneView facts about the OneView appliance SNMPv3 users. |  On state 'present' and 'set_password'. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_appliance_device_snmp_v3_users_facts
Retrieve the facts about the OneView appliance SNMPv3 users.

#### Synopsis
 SNMPv3 user will be used for sending the SNMPv3 trap to the associated destinations. One user can be assigned to multiple destinations. This module retrives the facts about the appliance SNMPv3 users.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |



#### Examples

```yaml

- name: Gather facts about the appliance SNMPv3 users.
  oneview_appliance_device_snmp_v3_users_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200

- debug:
    var: appliance_device_snmp_v3_users

- name: Gather paginated, filtered and sorted facts about SNMPv3 users
  oneview_appliance_device_snmp_v3_users_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 0
      count: 3
      sort: 'name:descending'
      filter: "securityLevel='Authentication and privacy'"
  delegate_to: localhost

- debug:
    var: appliance_device_snmp_v3_users

- name: Gather facts about a SNMPv3 user by username
  oneview_appliance_device_snmp_v3_users_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "testUser"
  delegate_to: localhost

- debug:
    var: appliance_device_snmp_v3_users

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| appliance_device_snmp_v3_users   | Has all the OneView facts about the OneView appliance SNMPv3 users. |  Always. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---

## oneview_appliance_ssh_access
Manage the OneView Appliance SSH Access resources.

#### Synopsis
 Enables or disables OneView Appliance SSH Access.

#### Requirements (on the host that executes the module)
  * python >= 3.4.2
  * hpeOneView >= 6.0.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |  Yes  |  | |  List with ssh access properties and its associated states.



## Example Playbook

```yaml

- name: Ensures the Appliance SSH Access is false
  oneview_appliance_ssh_access:
    config: "{{ config }}"
    state: present
    data:
      allowSshAccess: false
  delegate_to: localhost
- debug: var=appliance_ssh_access

- name: Ensures the Appliance SSH Access is true
  oneview_appliance_ssh_access:
    config: "{{ config }}"
    state: present
    data:
      allowSshAccess: true
  delegate_to: localhost
- debug: var=appliance_ssh_access

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| appliance_ssh_access   | Has all the OneView facts about the appliance SSH access configuration. |  On 'present' state. Cannot be null. |  dict |
| data  |   Yes  |  | |  List with the Appliance SSH Access Configuration properties.  |
| state  |   |  | <ul> <li>present</li> </ul> |  Indicates the desired state for the Appliance SSH access Configuration. `present` will ensure data properties are compliant with OneView.  |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---

## oneview_appliance_ssh_access_facts
Retrieve facts about the OneView Appliance SSH Access.

#### Synopsis
 Retrieve facts about the OneView Appliance SSH Access.

#### Requirements (on the host that executes the module)
  * python >= 3.4.2
  * hpeOneView >= 6.0.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |



## Example Playbook

```yaml

- name: Gather facts about the Appliance SSH Access
  oneview_appliance_ssh_access_facts:
    config: "{{ config }}"
  delegate_to: localhost

- debug: var=appliance_ssh_access

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| appliance_ssh_access   | Has all the OneView facts about the appliance SSH access configuration. |  Always.  |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_appliance_time_and_locale_configuration
Manage OneView Appliance Locale and Time Configuration.

#### Synopsis
 Provides an interface to manage Appliance Locale and Time Configuration. It can only update it.

#### Requirements (on the host that executes the module)
  * python >= 3.4.2
  * hpeOneView >= 6.0.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with the Appliance Locale and Time Configuration properties.  |
| state  |   |  | <ul> <li>present</li> </ul> |  Indicates the desired state for the Appliance Locale and Time Configuration. `present` will ensure data properties are compliant with OneView.  |



#### Examples

```yaml

- name: Add the Appliance time and locale configuration locale is ja_JP.UTF-8
  oneview_appliance_time_and_locale_configuration:
    config: "{{ config }}"
    state: present
    data:
      locale: ja_JP.UTF-8
      ntpServers: [16.110.135.123]
      timezone: UTC
      type: TimeAndLocale
  delegate_to: localhost
- debug: var=appliance_time_and_locale_configuration

- name: Ensures the Appliance time and locale configuration locale is ja_JP.UTF-8 is already present
  oneview_appliance_time_and_locale_configuration:
    config: "{{ config }}"
    state: present
    data:
      locale: ja_JP.UTF-8
      ntpServers: [16.110.135.123]
      timezone: UTC
      type: TimeAndLocale
  delegate_to: localhost
- debug: var=appliance_time_and_locale_configuration

- name: Change the Appliance time and locale configuration locale to en_US.UTF-8
  oneview_appliance_time_and_locale_configuration:
    config: "{{ config }}"
    state: present
    data:
      locale: en_US.UTF-8
      ntpServers: [16.110.135.123]
      timezone: UTC
      type: TimeAndLocale
  delegate_to: localhost
- debug: var=appliance_time_and_locale_configuration

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| appliance_time_and_locale_configuration   | Has the facts about the OneView Appliance Locale and Time Configuration. |  On state 'present'. Can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_appliance_time_and_locale_configuration_facts
Retrieve the facts about the OneView appliance time and locale configuration.

#### Synopsis
 Retrieve the facts about the OneView appliance time and locale configuration.

#### Requirements (on the host that executes the module)
  * python >= 3.4.2
  * hpeOneView >= 6.0.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |



#### Examples

```yaml

- name: Gather facts about the Appliance time and locale configuration
  oneview_appliance_time_and_locale_configuration_facts:
    config: "{{ config }}"
  delegate_to: localhost

- debug: var=appliance_time_and_locale_configuration

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| appliance_time_and_locale_configuration   | Has all the OneView facts about the Appliance time and locale configuration. |  Always. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_certificates_server
Manage OneView Certificates Server resources.

#### Synopsis
 Provides an interface to manage Certificates Server resources. Can create, update, or delete.

#### Requirements (on the host that executes the module)
  * hpeOneView >= 5.4.0
  * python >= 3.4.2

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional and when used should be present in the host running the ansible commands. If the file path is not provided, the configuration will be loaded from environment variables. For links to example configuration files or how to use the environment variables verify the notes section.  |
| data  |   Yes  |  | |  List with the Certificates Server properties.  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  Indicates the desired state for the Certificates Server resource. `present` ensures data properties are compliant with OneView. `absent` removes the resource from OneView, if it exists.  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  |



#### Examples

```yaml

- name: Create a Server Certificate
  oneview_certificates_server:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: 'vcenter'
      certificateDetails:
        - aliasName: 'vcenter'
          base64Data: '--- Certificate ---'

- name: Update the Server Certificate name to 'vcenter Renamed'
  oneview_certificates_server:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: 'vcenter renamed'
      certificateDetails:
        - aliasName: 'vcenter'
          base64Data: '--- Certificate ---'

- name: Ensure that the Server Certificate is absent
  oneview_certificates_server:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: absent
    data:
      alias_name: 'vcenter'

```

---



#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples

- The OneView API version used will directly affect returned and expected fields in resources. Information on setting the desired API version and can be found at: https://github.com/HewlettPackard/oneview-ansible#setting-your-oneview-version


---


## oneview_certificates_server_facts
Retrieve the facts about one or more of the OneView Certificates Server.

#### Synopsis
 Retrieve the facts about one or more of the Certificates Server from OneView.

#### Requirements (on the host that executes the module)
  * hpeOneView >= 5.4.0
  * python >= 3.4.2

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional and when used should be present in the host running the ansible commands. If the file path is not provided, the configuration will be loaded from environment variables. For links to example configuration files or how to use the environment variables verify the notes section.  |
| aliasName  |   No  |  | |  Certificates Server aliasName.  |
| remote  |   No  |  | |  Remote Server Certificate.  |



#### Examples

```yaml

- name: Gather facts about a Server Certificate by aliasname
  oneview_certificates_server_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    aliasname: "vcenter"
  delegate_to: localhost

- debug: var=certificates_server

- name: Gather facts about a Server Certificate by remote server
  oneview_certificates_server_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    remote: "172.18.13.11"
  delegate_to: localhost

- debug: var=remote_certificate

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| certificates_servers   | Has all the OneView facts about the Certificates Server. |  Always, but can be null. |  dict |
| remote_certificate     | Has facts about remote server certificates               |  When required            |  dict |

#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples

- The OneView API version used will directly affect returned and expected fields in resources. Information on setting the desired API version and can be found at: https://github.com/HewlettPackard/oneview-ansible#setting-your-oneview-version


---



## oneview_connection_template
Manage the OneView Connection Template resources.

#### Synopsis
 Provides an interface to manage the Connection Template resources. Can update.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with Connection Template properties and its associated states.  |
| state  |   Yes  |  | <ul> <li>present</li> </ul> |  Indicates the desired state for the Connection Template resource. `present` will ensure data properties are compliant with OneView.  |



#### Examples

```yaml

- name: Update the Connection Template
  oneview_connection_template:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
        name: 'name1304244267-1467656930023'
        type : "connection-template"
        bandwidth :
            maximumBandwidth : 10000
            typicalBandwidth : 2200
        newName : "CT-23"
  delegate_to: localhost

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| connection_template   | Has the OneView facts about the Connection Template. |  On 'present' state, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_connection_template_facts
Retrieve facts about the OneView Connection Templates.

#### Synopsis
 Retrieve facts about the OneView Connection Templates.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Connection Template name.  |
| options  |   No  |  | |  List with options to gather additional facts about Connection Template related resources. Options allowed: `defaultConnectionTemplate`.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Connection Templates
  oneview_connection_template_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
  delegate_to: localhost
- debug: var=connection_templates

- name: Gather paginated, filtered and sorted facts about Connection Templates
  oneview_connection_template_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 0
      count: 3
      sort: 'name:descending'
      filter: 'name=defaultConnectionTemplate'

- debug: var=connection_templates

- name: Gather facts about a Connection Template by name
  oneview_connection_template_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: 'connection template name'
  delegate_to: localhost
- debug: var=connection_templates

- name: Gather facts about the Default Connection Template
  oneview_connection_template_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    options:
      - defaultConnectionTemplate
  delegate_to: localhost
- debug: var=default_connection_template

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| connection_templates   | Has all the OneView facts about the Connection Templates. |  Always, except when defaultConnectionTemplate is requested. Can be null. |  dict |
| default_connection_template   | Has the facts about the Default Connection Template. |  When requested, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_datacenter
Manage OneView Data Center resources.

#### Synopsis
 Provides an interface to manage Data Center resources. Can add, update, and remove.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with Data Center properties and its associated states.  |
| state  |   Yes  |  | <ul> <li>present</li>  <li>absent</li> </ul> |  Indicates the desired state for the Data Center resource. `present` will ensure data properties are compliant with OneView. `absent` will remove the resource from OneView, if it exists.  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  |



#### Examples

```yaml

- name: Add a Data Center
  oneview_datacenter:
    config: "{{ config }}"
    state: present
    data:
        name: "MyDatacenter"
        width: 5000
        depth: 6000
        contents:
            # You can choose either resourceName or resourceUri to inform the Rack
            - resourceName: '{{ datacenter_content_rack_name }}' # option 1
              resourceUri: ''                                    # option 2
              x: 1000
              y: 1000
  delegate_to: localhost

- name: Update the Data Center with specified properties (no racks)
  oneview_datacenter:
    config: "{{ config }}"
    state: present
    data:
        name: "MyDatacenter"
        coolingCapacity: '5'
        costPerKilowattHour: '0.10'
        currency: USD
        deratingType: NaJp
        deratingPercentage: '20.0'
        defaultPowerLineVoltage: '220'
        coolingMultiplier: '1.5'
        width: 4000
        depth: 5000
        contents: ~

  delegate_to: localhost

- name: Rename the Data Center
  oneview_datacenter:
    config: "{{ config }}"
    state: present
    data:
        name: "MyDatacenter"
        newName: "My Datacenter"
  delegate_to: localhost

- name: Remove the Data Center
  oneview_datacenter:
    config: "{{ config }}"
    state: absent
    data:
        name: 'My Datacenter'
  delegate_to: localhost

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| datacenter   | Has the OneView facts about the Data Center. |  On state 'present'. Can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_datacenter_facts
Retrieve facts about the OneView Data Centers.

#### Synopsis
 Retrieve facts about the OneView Data Centers.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Data Center name.  |
| options  |   No  |  | |  Retrieve additional facts. Options available: 'visualContent'.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Data Centers
  oneview_datacenter_facts:
    config: "{{ config }}"
  delegate_to: localhost
- debug: var=datacenters

- name: Gather paginated, filtered and sorted facts about Data Centers
  oneview_datacenter_facts:
    config: "{{ config }}"
    params:
      start: 0
      count: 3
      sort: 'name:descending'
      filter: 'state=Unmanaged'
- debug: var=datacenters

- name: Gather facts about a Data Center by name
  oneview_datacenter_facts:
    config: "{{ config }}"
    name: "My Data Center"
  delegate_to: localhost
- debug: var=datacenters

- name: Gather facts about the Data Center Visual Content
  oneview_datacenter_facts:
    config: "{{ config }}"
    name: "My Data Center"
    options:
      - visualContent
  delegate_to: localhost
- debug: var=datacenters
- debug: var=datacenter_visual_content

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| datacenter_visual_content   | Has facts about the Data Center Visual Content. |  When requested, but can be null. |  dict |
| datacenters   | Has all the OneView facts about the Data Centers. |  Always, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_drive_enclosure
Manage OneView Drive Enclosure resources.

#### Synopsis
 Provides an interface to manage Drive Enclosure resources.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with the Drive Enclosure properties.  |
| state  |   |  | <ul> <li>power_state_set</li>  <li>uid_state_set</li>  <li>hard_reset_state_set</li>  <li>refresh_state_set</li> </ul> |  Indicates the desired state for the Drive Enclosure resource. `power_state_set` will set the power state for the Drive Enclosure. `uid_state_set` will set the uid state for the Drive Enclosure. `hard_reset_state_set` will request a hard reset of the Drive Enclosure. `refresh_state_set` will refresh a Drive Enclosure.  |



#### Examples

```yaml

- name: Power off the Drive Enclosure
  oneview_drive_enclosure:
    config: "{{ config_file_path }}"
    state: power_state_set
    data:
        name: '0000A66108, bay 1'
        powerState: 'Off'

- name: Power on the UID for the Drive Enclosure
  oneview_drive_enclosure:
    config: "{{ config_file_path }}"
    state: uid_state_set
    data:
        name: '0000A66108, bay 1'
        uidState: 'On'

- name: Request a hard reset of the Drive Enclosure
  oneview_drive_enclosure:
    config: "{{ config_file_path }}"
    state: hard_reset_state_set
    data:
        name: '0000A66108, bay 1'

- name: Refresh the Drive Enclosure
  oneview_drive_enclosure:
    config: "{{ config_file_path }}"
    state: refresh_state_set
    data:
        name: '0000A66108, bay 1'
        refreshState: 'RefreshPending'

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| drive_enclosure   | Has the facts about the Drive Enclosure. |  Always, but can be null. |  dict |


#### Notes

- This resource is only available on HPE Synergy.

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_drive_enclosure_facts
Retrieve the facts about one or more of the OneView Drive Enclosures.

#### Synopsis
 Retrieve the facts about one or more of the Drive Enclosures from OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Drive Enclosure name.  |
| options  |   No  |  | |  List with options to gather additional facts about Drive Enclosure related resources. Options allowed: `portMap`. To gather additional facts it is required to inform the Drive Enclosure name. Otherwise, these options will be ignored.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Drive Enclosures
  oneview_drive_enclosure_facts:
    config: "{{ config_file_path }}"

- debug: var=drive_enclosures

- name: Gather paginated, filtered and sorted facts about Drive Enclosures
  oneview_drive_enclosure_facts:
    config: "{{ config_file_path }}"
    params:
      start: 0
      count: 3
      sort: 'name:descending'
      filter: 'status=Warning'

- debug: var=drive_enclosures

- name: Gather facts about a Drive Enclosure by name
  oneview_drive_enclosure_facts:
    config: "{{ config_file_path }}"
    name: Default Drive Enclosure

- debug: var=drive_enclosures

- name: Gather facts about a Drive Enclosure and the Port Map
  oneview_drive_enclosure_facts:
    config: "{{ config_file_path }}"
    name: Default Drive Enclosure
    options:
        - portMap

- debug: var=drive_enclosures
- debug: var=drive_enclosure_port_map

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| drive_enclosure_port_map   | Has all the OneView facts about the Drive Enclosure Port Map. |  When requested, but can be null. |  dict |
| drive_enclosures   | Has all the OneView facts about the Drive Enclosures. |  Always, but can be null. |  dict |


#### Notes

- This resource is only available on HPE Synergy.

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_enclosure
Manage OneView Enclosure resources.

#### Synopsis
 Provides an interface to manage Enclosure resources.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with the Enclosure properties.  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li>  <li>reconfigured</li>  <li>refreshed</li>  <li>appliance_bays_powered_on</li>  <li>uid_on</li>  <li>uid_off</li>  <li>manager_bays_uid_on</li>  <li>manager_bays_uid_off</li>  <li>manager_bays_power_state_e_fuse</li>  <li>manager_bays_power_state_reset</li>  <li>appliance_bays_power_state_e_fuse</li>  <li>device_bays_power_state_e_fuse</li>  <li>device_bays_power_state_reset</li>  <li>interconnect_bays_power_state_e_fuse</li>  <li>manager_bays_role_active</li>  <li>device_bays_ipv4_removed</li>  <li>interconnect_bays_ipv4_removed</li>  <li>support_data_collection_set</li>  <li>create_certificate_request</li>  <li>get_certificate_request</li>  <li>import_certificate_request</li> </ul> |  Indicates the desired state for the Enclosure resource. `present` will ensure data properties are compliant with OneView. You can rename the enclosure providing an attribute `newName`. You can also rename the rack providing an attribute `rackName`. `absent` will remove the resource from OneView, if it exists. `reconfigured` will reapply the appliance's configuration on the enclosure. This includes running the same configuration steps that were performed as part of the enclosure add. `refreshed` will refresh the enclosure along with all of its components, including interconnects and servers. Any new hardware is added, and any hardware that is no longer present within the enclosure is removed. `appliance_bays_powered_on` will set the appliance bay power state on. `uid_on` will set the UID state on. `uid_off` will set the UID state off. `manager_bays_uid_on` will set the UID state on for the Synergy Frame Link Module. `manager_bays_uid_off` will set the UID state off for the Synergy Frame Link Module. `manager_bays_power_state_e_fuse` will E-Fuse the Synergy Frame Link Module bay in the path. `manager_bays_power_state_reset` will Reset the Synergy Frame Link Module bay in the path. `appliance_bays_power_state_e_fuse` will E-Fuse the appliance bay in the path. `device_bays_power_state_e_fuse` will E-Fuse the device bay in the path. `device_bays_power_state_reset` will Reset the device bay in the path. `interconnect_bays_power_state_e_fuse` will E-Fuse the IC bay in the path. `manager_bays_role_active` will set the active Synergy Frame Link Module. `device_bays_ipv4_removed` will release the IPv4 address in the device bay. `interconnect_bays_ipv4_removed` will release the IPv4 address in the interconnect bay. `support_data_collection_set` will set the support data collection state for the enclosure. The supported values for this state are `PendingCollection`, `Completed`, `Error` and `NotSupported` `create_certificate_request` will create a Certificate Signing Request (CSR) for an enclosure `get_certificate_request` will return an enclosure's Certificate Signing Request (CSR) that was generated by previous POST to same URI. `import_certificate_request` will import a signed server certificate into the enclosure to be used for secure communication with the appliance.  |



#### Examples

```yaml

- name: Ensure that an Enclosure is present using the default configuration
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      enclosureGroupUri : '{{ enclosure_group_uri }}'
      hostname : '{{ enclosure_hostname }}'
      username : '{{ enclosure_username }}'
      password : '{{ enclosure_password }}'
      name: 'Test-Enclosure'
      licensingIntent : 'OneView'

- name: Updates the enclosure to have a name of "Test-Enclosure-Renamed".
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: 'Test-Enclosure'
      newName : 'Test-Enclosure-Renamed'

- name: Reconfigure the enclosure "Test-Enclosure"
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: reconfigured
    data:
      name: 'Test-Enclosure'

- name: Ensure that enclosure is absent
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: absent
    data:
      name: 'Test-Enclosure'

- name: Ensure that an enclosure is refreshed
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: refreshed
    data:
      name: 'Test-Enclosure'
      refreshState: Refreshing

- name: Create certificate signing request
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: create_certificate_request
    data:
      name: 'Test-Enclosure'
      type: CertificateDtoV2
      organization: HPE
      organizationalUnit: IT
      locality: 'Fort Collins'
      state: Colorado
      country: US
      commonName: 'e10-oa'
    bay_number: 1

- name: Get certificate signing request
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: get_certificate_request
    data:
      name: 'Test-Enclosure'
      bay_number: 1

- name: Import certificate signing request
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: import_certificate_request
    data:
      name: 'Test-Enclosure'
      type: CertificateDtoV2
      base64Data: certificate

- name: Set the calibrated max power of an unmanaged or unsupported enclosure
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: 'Test-Enclosure'
      calibratedMaxPower: 1700

- name: Set the appliance bay power state on
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: appliance_bays_powered_on
    data:
      name: 'Test-Enclosure'
      bayNumber: 1

- name: Set the appliance UID state on
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: uid_on
    data:
      name: 'Test-Enclosure'

- name: Set the appliance UID state off
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: uid_off
    data:
      name: 'Test-Enclosure'

- name: Set the UID for the Synergy Frame Link Module state on
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: manager_bays_uid_on
    data:
      name: 'Test-Enclosure'
      bayNumber: 1

- name: Set the UID for the Synergy Frame Link Module state off
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: manager_bays_uid_off
    data:
      name: 'Test-Enclosure'
      bayNumber: 1

- name: E-Fuse the Synergy Frame Link Module bay 1
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: manager_bays_power_state_e_fuse
    data:
      name: 'Test-Enclosure'
      bayNumber: 1

- name: Reset the Synergy Frame Link Module bay 1
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: manager_bays_power_state_reset
    data:
      name: 'Test-Enclosure'
      bayNumber: 1

- name: E-Fuse the appliance bay 1
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: appliance_bays_power_state_e_fuse
    data:
      name: 'Test-Enclosure'
      bayNumber: 1

- name: E-Fuse the device bay 10
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: device_bays_power_state_e_fuse
    data:
      name: 'Test-Enclosure'
      bayNumber: 10

- name: Reset the device bay 8
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: device_bays_power_state_reset
    data:
      name: 'Test-Enclosure'
      bayNumber: 8

- name: E-Fuse the IC bay 3
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: interconnect_bays_power_state_e_fuse
    data:
      name: 'Test-Enclosure'
      bayNumber: 3

- name: Set the active Synergy Frame Link Module on bay 2
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: manager_bays_role_active
    data:
      name: 'Test-Enclosure'
      bayNumber: 2

- name: Release IPv4 address in the bay 2
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: device_bays_ipv4_removed
    data:
      name: 'Test-Enclosure'
      bayNumber: 2

- name: Release IPv4 address in the bay 2
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: interconnect_bays_ipv4_removed
    data:
      name: 'Test-Enclosure'
      bayNumber: 2

- name: Set the supportDataCollectionState for the enclosure
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: support_data_collection_set
    data:
      name: 'Test-Enclosure'
      supportDataCollectionState: 'PendingCollection'

- name: Ensure that the Enclosure is present and is inserted in the desired scopes
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: 'Test-Enclosure'
      scopeUris:
        - '/rest/scopes/00SC123456'
        - '/rest/scopes/01SC123456'

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| enclosure   | Has all the facts about the enclosure. |  On states 'present', 'reconfigured', and 'refreshed'. Can be null. |  dict |


#### Notes

- These states are only available on HPE Synergy: `appliance_bays_powered_on`, `uid_on`, `uid_off`, `manager_bays_uid_on`, `manager_bays_uid_off`, `manager_bays_power_state_e_fuse`, `manager_bays_power_state_reset`, `appliance_bays_power_state_e_fuse`, `device_bays_power_state_e_fuse`, `device_bays_power_state_reset`, `interconnect_bays_power_state_e_fuse`, `manager_bays_role_active`, `device_bays_ipv4_removed` and `interconnect_bays_ipv4_removed`

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_enclosure_facts
Retrieve facts about one or more Enclosures

#### Synopsis
 Retrieve facts about one or more of the Enclosures from OneView.

#### Requirements (on the host that executes the module)
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   |  | |  Enclosure name.  |
| options  |   |  | |  List with options to gather additional facts about an Enclosure and related resources. Options allowed: `script`, `environmentalConfiguration`, and `utilization`. For the option `utilization`, you can provide specific parameters.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Enclosures
  oneview_enclosure_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
  no_log: true
  delegate_to: localhost
- debug: var=enclosures

- name: Gather paginated, filtered and sorted facts about Enclosures
  oneview_enclosure_facts:
    params:
      start: 0
      count: 3
      sort: name:descending
      filter: status=OK
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
  no_log: true
  delegate_to: localhost
- debug: var=enclosures

- name: Gather facts about an Enclosure by name
  oneview_enclosure_facts:
    name: Enclosure-Name
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
  no_log: true
  delegate_to: localhost
- debug: var=enclosures

- name: Gather facts about an Enclosure by name with options
  oneview_enclosure_facts:
    name: Test-Enclosure
    options:
      - script                       # optional
      - environmentalConfiguration   # optional
      - utilization                  # optional
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
  no_log: true
  delegate_to: localhost
- debug: var=enclosures
- debug: var=enclosure_script
- debug: var=enclosure_environmental_configuration
- debug: var=enclosure_utilization

- name: "Gather facts about an Enclosure with temperature data at a resolution of one sample per day, between two
         specified dates"
  oneview_enclosure_facts:
    name: Test-Enclosure
    options:
      - utilization:                   # optional
          fields: AmbientTemperature
          filter:
            - startDate=2016-07-01T14:29:42.000Z
            - endDate=2017-07-01T03:29:42.000Z
          view: day
          refresh: false
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
  no_log: true
  delegate_to: localhost
- debug: var=enclosures
- debug: var=enclosure_utilization

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| enclosure_environmental_configuration   | Has all the OneView facts about the environmental configuration of an Enclosure. |  When requested, but can be null. |  dict |
| enclosure_script   | Has all the OneView facts about the script of an Enclosure. |  When requested, but can be null. |  string |
| enclosure_utilization   | Has all the OneView facts about the utilization of an Enclosure. |  When requested, but can be null. |  dict |
| enclosures   | Has all the OneView facts about the Enclosures. |  Always, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_enclosure_group
Manage OneView Enclosure Group resources.

#### Synopsis
 Provides an interface to manage Enclosure Group resources. Can create, update, or delete.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with Enclosure Group properties.  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  Indicates the desired state for the Enclosure Group resource. `present` will ensure data properties are compliant with OneView. `absent` will remove the resource from OneView, if it exists.  |



#### Examples

```yaml

- name: Ensure that Enclosure Group is present using the default configuration
  oneview_enclosure_group:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
        name: "Enclosure Group 1"
        stackingMode: "Enclosure" # Not supported in V600
        interconnectBayMappings:
            - interconnectBay: 1
            - interconnectBay: 2
            - interconnectBay: 3
            - interconnectBay: 4
            - interconnectBay: 5
            - interconnectBay: 6
            - interconnectBay: 7
            - interconnectBay: 8
  delegate_to: localhost

- name: Update the Enclosure Group changing the name attribute
  oneview_enclosure_group:
        hostname: 172.16.101.48
        username: administrator
        password: my_password
        api_version: 2200
        state: present
        data:
            name: "Enclosure Group 1"
            newName: "Enclosure Group 1 (renamed)"
  delegate_to: localhost

- name: Ensure that Enclosure Group is absent
  oneview_enclosure_group:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: absent
    data:
      name: "Enclosure Group 1 (renamed)"
  delegate_to: localhost

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| enclosure_group   | Has the facts about the Enclosure Group. |  On state 'present'. Can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_enclosure_group_facts
Retrieve facts about one or more of the OneView Enclosure Groups.

#### Synopsis
 Retrieve facts about one or more of the Enclosure Groups from OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Enclosure Group name.  |
| options  |   No  |  | |  List with options to gather additional facts about Enclosure Group. Options allowed: `configuration_script` Gets the configuration script for an Enclosure Group.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Enclosure Groups
  oneview_enclosure_group_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
  delegate_to: localhost

- debug: var=enclosure_groups

- name: Gather paginated, filtered and sorted facts about Enclosure Groups
  oneview_enclosure_group_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 0
      count: 3
      sort: 'name:descending'
      filter: 'status=OK'
      scope_uris: '/rest/scopes/cd237b60-09e2-45c4-829e-082e318a6d2a'

- debug: var=enclosure_groups

- name: Gather facts about an Enclosure Group by name with configuration script
  oneview_enclosure_group_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "Test Enclosure Group Facts"
    options:
      - configuration_script
    delegate_to: localhost

- debug: var=enclosure_groups
- debug: var=enclosure_group_script

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| enclosure_group_script   | The configuration script for an Enclosure Group. |  When requested, but can be null. |  string |
| enclosure_groups   | Has all the OneView facts about the Enclosure Groups. |  Always, but can be null. |  dict |

#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_ethernet_network
Manage OneView Ethernet Network resources.

#### Synopsis
 Provides an interface to manage Ethernet Network resources. Can create, update, or delete.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with Ethernet Network properties.  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li>  <li>default_bandwidth_reset</li> </ul> |  Indicates the desired state for the Ethernet Network resource. `present` will ensure data properties are compliant with OneView. `absent` will remove the resource from OneView, if it exists. `default_bandwidth_reset` will reset the network connection template to the default.  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  |



#### Examples

```yaml

- name: Ensure that the Ethernet Network is present using the default configuration
  oneview_ethernet_network:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: 'Test Ethernet Network'
      vlanId: '201'

- name: Update the Ethernet Network changing bandwidth and purpose
  oneview_ethernet_network:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: 'Test Ethernet Network'
      purpose: Management
      bandwidth:
          maximumBandwidth: 3000
          typicalBandwidth: 2200
  delegate_to: localhost

- name: Ensure that the Ethernet Network is present with name 'Renamed Ethernet Network'
  oneview_ethernet_network:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: 'Test Ethernet Network'
      newName: 'Renamed Ethernet Network'

- name: Ensure that the Ethernet Network is absent
  oneview_ethernet_network:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: absent
    data:
      name: 'New Ethernet Network'

- name: Create Ethernet networks in bulk
  oneview_ethernet_network:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      vlanIdRange: '1-10,15,17'
      purpose: General
      namePrefix: TestNetwork
      smartLink: false
      privateNetwork: false
      bandwidth:
        maximumBandwidth: 10000
        typicalBandwidth: 2200

- name: Reset to the default network connection template
  oneview_ethernet_network:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: default_bandwidth_reset
    data:
      name: 'Test Ethernet Network'
  delegate_to: localhost

- name: Update the ethernet network scopes
  oneview_ethernet_network:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: 'Test Ethernet Network'
      scopeUris:
        - '/rest/scopes/00SC123456'
        - '/rest/scopes/01SC123456'
  delegate_to: localhost

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| ethernet_network   | Has the facts about the Ethernet Networks. |  On state 'present'. Can be null. |  dict |
| ethernet_network_bulk   | Has the facts about the Ethernet Networks affected by the bulk insert. |  When 'vlanIdRange' attribute is in data argument. Can be null. |  dict |
| ethernet_network_connection_template   | Has the facts about the Ethernet Network Connection Template. |  On state 'default_bandwidth_reset'. Can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_ethernet_network_facts
Retrieve the facts about one or more of the OneView Ethernet Networks.

#### Synopsis
 Retrieve the facts about one or more of the Ethernet Networks from OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Ethernet Network name.  |
| options  |   No  |  | |  List with options to gather additional facts about an Ethernet Network and related resources. Options allowed: `associatedProfiles` and `associatedUplinkGroups`.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Ethernet Networks
  oneview_ethernet_network_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200

- debug: var=ethernet_networks

- name: Gather paginated and filtered facts about Ethernet Networks
  oneview_ethernet_network_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 1
      count: 3
      sort: 'name:descending'
      filter: 'purpose=General'

- debug: var=ethernet_networks

- name: Gather facts about an Ethernet Network by name
  oneview_ethernet_network_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: Ethernet network name

- debug: var=ethernet_networks

- name: Gather facts about an Ethernet Network by name with options
  oneview_ethernet_network_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "{{ name }}"
    options:
      - associatedProfiles
      - associatedUplinkGroups
  delegate_to: localhost

- debug: var=enet_associated_profiles
- debug: var=enet_associated_uplink_groups

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| enet_associated_profiles   | Has all the OneView facts about the profiles which are using the Ethernet network. |  When requested, but can be null. |  dict |
| enet_associated_uplink_groups   | Has all the OneView facts about the uplink sets which are using the Ethernet network. |  When requested, but can be null. |  dict |
| ethernet_networks   | Has all the OneView facts about the Ethernet Networks. |  Always, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_event
Manage OneView Events.

#### Synopsis
 Provides an interface to manage Events. Can only create.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with the Event properties.  |
| state  |   |  | <ul> <li>present</li> </ul> |  Indicates the desired state for the Event. `present` will ensure data properties are compliant with OneView. This operation is non-idempotent.  |



#### Examples

```yaml

- name: Ensure that the Event is present using a test type id
  oneview_event:
    config: "{{ config_file_path }}"
    state: present
    data:
      description: "This is a very simple test event"
      eventTypeID: "hp.justATest"
      eventDetails:
        - eventItemName: ipv4Address
          eventItemValue: 198.51.100.5
          isThisVarbindData: false
          varBindOrderIndex: -1

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| event   | Has the facts about the OneView Events. |  On state 'present'. Can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_event_facts
Retrieve the facts about one or more of the OneView Events.

#### Synopsis
 Retrieve the facts about one or more of the Events from OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Event name.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Events
  oneview_event_facts:
    config: "{{ config_file_path }}"

- debug: var=events

- name: Gather paginated, filtered and sorted facts about Events
  oneview_event_facts:
    config: "{{ config }}"
    params:
      start: 1
      count: 3
      sort: 'description:descending'
      filter: 'eventTypeID=hp.justATest'
- debug: var=events


```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| events   | Has all the OneView facts about the Events. |  Always, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_fabric
Manage OneView Fabric resources.

#### Synopsis
 Provides an interface for managing fabrics in OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with Fabrics properties.  |
| name  |   No  |  | |  Fabric name.  |



#### Examples

```yaml

- name: Update the range of the fabric
  oneview_fabric:
    config: '{{ config }}'
    state: reserved_vlan_range_updated
    data:
      name: '{{ name }}'
      reservedVlanRangeParameters:
        start: '300'
        length: '62'

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| fabric   | Has all the OneView facts about the Fabrics. |  Always, but can be null. |  dict |


#### Notes

- This module is only available on HPE Synergy.

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_fabric_facts
Retrieve the facts about one or more of the OneView Fabrics.

#### Synopsis
 Retrieve the facts about one or more of the Fabrics from OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Fabric name.  |
| options  |   No  |  | |  List with options to gather additional facts about an Fabrics and related resources. Options allowed: `reservedVlanRange`.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Fabrics
  oneview_fabric_facts:
    config: "{{ config_file_path }}"

- debug: var=fabrics

- name: Gather paginated, filtered and sorted facts about Fabrics
  oneview_fabric_facts:
    config: "{{ config }}"
    params:
      start: 0
      count: 3
      sort: 'name:descending'
      filter: 'name=DefaultFabric'

- debug: var=fabrics

- name: Gather facts about a Fabric by name
  oneview_fabric_facts:
    config: "{{ config_file_path }}"
    name: DefaultFabric

- debug: var=fabrics

- name: Gather facts about a Fabric by name with options
  oneview_fabric_facts:
    config: "{{ config }}"
    name: DefaultFabric
    options:
      - reservedVlanRange          # optional

- debug: var=fabrics

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| fabric_reserved_vlan_range   | Has all the OneView facts about the reserved VLAN range |  When requested, but can be null. |  dict |
| fabrics   | Has all the OneView facts about the Fabrics. |  Always, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_fc_network
Manage OneView Fibre Channel Network resources.

#### Synopsis
 Provides an interface to manage Fibre Channel Network resources. Can create, update, and delete.

#### Requirements (on the host that executes the module)
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with the Fibre Channel Network properties.  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  Indicates the desired state for the Fibre Channel Network resource. `present` will ensure data properties are compliant with OneView. `absent` will remove the resource from OneView, if it exists.  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  |



#### Examples

```yaml

- name: Ensure that the Fibre Channel Network is present using the default configuration
  oneview_fc_network:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: 'New FC Network'

- name: Ensure that the Fibre Channel Network is present with fabricType 'DirectAttach'
  oneview_fc_network:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: 'New FC Network'
      fabricType: 'DirectAttach'

# This feature is available only till OneView 3.10
- name: Ensure that the Fibre Channel Network is present and is inserted in the desired scopes
  oneview_fc_network:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 500
    state: present
    data:
      name: 'New FC Network'
      scopeUris:
        - '/rest/scopes/00SC123456'
        - '/rest/scopes/01SC123456'

- name: Ensure that the Fibre Channel Network is absent
  oneview_fc_network:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: absent
    data:
      name: 'New FC Network'

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| fc_network   | Has the facts about the managed OneView FC Network. |  On state 'present'. Can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_fc_network_facts
Retrieve the facts about one or more of the OneView Fibre Channel Networks

#### Synopsis
 Retrieve the facts about one or more of the Fibre Channel Networks from OneView.

#### Requirements (on the host that executes the module)
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   |  | |  Fibre Channel Network name.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Fibre Channel Networks
  oneview_fc_network_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
  delegate_to: localhost

- debug: var=fc_networks

- name: Gather paginated, filtered and sorted facts about Fibre Channel Networks
  oneview_fc_network_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 1
      count: 3
      sort: 'name:descending'
      filter: 'fabricType=FabricAttach'
  delegate_to: localhost
- debug: var=fc_networks

- name: Gather facts about a Fibre Channel Network by name
  oneview_fc_network_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: network name
  delegate_to: localhost

- debug: var=fc_networks

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| fc_networks   | Has all the OneView facts about the Fibre Channel Networks. |  Always, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_fcoe_network
Manage OneView FCoE Network resources

#### Synopsis
 Provides an interface to manage FCoE Network resources. Can create, update, or delete.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with FCoE Network properties.  |
| state  |   |  present  | <ul> <li>present</li>  <li>absent</li> </ul> |  Indicates the desired state for the FCoE Network resource. `present` will ensure data properties are compliant with OneView. `absent` will remove the resource from OneView, if it exists.  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  |



#### Examples

```yaml

- name: Ensure that FCoE Network is present using the default configuration
  oneview_fcoe_network:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: Test FCoE Network
      vlanId: 201
  delegate_to: localhost
# Below task is supported only with OneView 3.10
- name: Update the FCOE network scopes
  oneview_fcoe_network:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: New FCoE Network
      scopeUris:
        - '/rest/scopes/00SC123456'
        - '/rest/scopes/01SC123456'
  delegate_to: localhost

- name: Ensure that FCoE Network is absent
  oneview_fcoe_network:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: absent
    data:
      name: New FCoE Network
  delegate_to: localhost

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| fcoe_network   | Has the facts about the OneView FCoE Networks. |  On state 'present'. Can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_fcoe_network_facts
Retrieve the facts about one or more of the OneView FCoE Networks

#### Synopsis
 Retrieve the facts about one or more of the FCoE Networks from OneView.

#### Requirements (on the host that executes the module)
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   |  | |  FCoE Network name.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all FCoE Networks
  oneview_fcoe_network_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
  delegate_to: localhost

- debug: var=fcoe_networks

- name: Gather paginated, filtered and sorted facts about FCoE Networks
  oneview_fcoe_network_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 0
      count: 3
      sort: 'name:descending'
      filter: 'vlanId=2'
  delegate_to: localhost

- debug: var=fcoe_networks

- name: Gather facts about a FCoE Network by name
  oneview_fcoe_network_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: Test FCoE Network Facts
  delegate_to: localhost

- debug: var=fcoe_networks

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| fcoe_networks   | Has all the OneView facts about the FCoE Networks. |  Always, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_firmware_bundle
Upload OneView Firmware Bundle resources.

#### Synopsis
 Upload an SPP ISO image file or a hotfix file to the appliance.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| file_path  |   Yes  |  | |  The full path of a local file to be loaded.  |
| state  |   |  | <ul> <li>present</li> </ul> |  Indicates the desired state for the Firmware Driver resource. `present` will ensure that the firmware bundle is at OneView.  |



#### Examples

```yaml

- name: Ensure that the Firmware Driver is present
  oneview_firmware_bundle:
    config: "{{ config_file_path }}"
    state: present
    file_path: "/home/user/Downloads/hp-firmware-hdd-a1b08f8a6b-HPGH-1.1.x86_64.rpm"


```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| firmware_bundle   | Has the facts about the OneView Firmware Bundle. |  Always. Can be null. |  dict |


#### Notes

- This module is non-idempotent

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_firmware_driver
Provides an interface to remove Firmware Driver resources.

#### Synopsis
 Provides an interface to remove Firmware Driver resources.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   No  |  | |  List with the Firmware Driver properties.  |
| name  |   No  |  | |  Firmware driver name.  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  Indicates the desired state for the Firmware Driver. `present` will ensure data properties are compliant with OneView. `absent` will remove the resource from OneView, if it exists.  |



#### Examples

```yaml

- name: Create the Firmware Driver using names to find the baseline and hotfix firmwares.
  oneview_firmware_driver:
    config: "{{ config_file_path }}"
    state: present
    data:
      customBaselineName: "Service Pack for ProLiant - Custom"
      baselineName: "Service Pack for ProLiant"
      hotfixNames: ['hotfix 1', 'hotfix 2']

- name: Create the Firmware Driver using URIs to find the baseline and hotfix firmwares.
  oneview_firmware_driver:
    config: "{{ config_file_path }}"
    state: present
    data:
      customBaselineName: "Service Pack for ProLiant - Custom"
      baselineUri: "/rest/firmware-driver/SPP1"
      hotfixUris: ['/rest/firmware-driver/hotfix1', '/rest/firmware-driver/hotfix2']

- name: Ensure that Firmware Driver is absent
  oneview_firmware_driver:
    config: "{{ config_file_path }}"
    state: absent
    name: "Service Pack for ProLiant.iso"

```



#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_firmware_driver_facts
Retrieve the facts about one or more of the OneView Firmware Drivers.

#### Synopsis
 Retrieve the facts about one or more of the Firmware Drivers from OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Firmware driver name.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Firmware Drivers
  oneview_firmware_driver_facts:
    config: "{{ config_file_path }}"

- debug: var=firmware_drivers

- name: Gather paginated, filtered and sorted facts about Firmware Drivers
  oneview_firmware_driver_facts:
    config: "{{ config }}"
    params:
      start: 0
      count: 3
      sort: 'name:descending'

- debug: var=firmware_drivers

- name: Gather facts about a Firmware Driver by name
  oneview_firmware_driver_facts:
    config: "{{ config_file_path }}"
    name: "Service Pack for ProLiant.iso"

- debug: var=firmware_drivers

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| firmware_drivers   | Has all the OneView facts about the Firmware Drivers. |  Always, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_hypervisor_cluster_profile
Manage OneView Hypervisor Cluster Profile resources.

#### Synopsis
 Provides an interface to manage Hypervisor Cluster Profile resources. Can create, update, or delete.

#### Requirements (on the host that executes the module)
  * hpeOneView >= 5.4.0
  * python >= 3.4.2

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional and when used should be present in the host running the ansible commands. If the file path is not provided, the configuration will be loaded from environment variables. For links to example configuration files or how to use the environment variables verify the notes section.  |
| data  |   Yes  |  | |  List with the Hypervisor Cluster Profile properties.  |
| params  |     |  | |  force flag  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  Indicates the desired state for the Hypervisor Cluster Profile resource. `present` ensures data properties are compliant with OneView. `absent` removes the resource from OneView, if it exists.  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  |



#### Examples

```yaml

- name: Create a Hypervisor Cluster Profile
  oneview_hypervisor_cluster_profile:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: 'hcp'
      path: 'DC1'
      hypervisorType: 'Vmware'
      hypervisorManagerUri: '/rest/hypervisor-manager/rdy-dfdf12'
      hypervisorHostProfileTemplate:
        serverProfileTemplateUri: '/rest/server-profile-template/2323-32323'
        hostprefix: 'test-host'

- name: Update the Hypervisor Cluster Profile name to 'hcp Renamed'
  oneview_hypervisor_cluster_profile:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: 'hcp Renamed'
      path: 'DC1'
      hypervisorType: 'Vmware'
      hypervisorManagerUri: '/rest/hypervisor-manager/rdy-dfdf12'
    params:
      force: True

- name: Ensure that the Hypervisor Cluster Profile is absent
  oneview_hypervisor_cluster_profile:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: absent
    data:
      name: 'hcp'

---



#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples

- The OneView API version used will directly affect returned and expected fields in resources. Information on setting the desired API version and can be found at: https://github.com/HewlettPackard/oneview-ansible#setting-your-oneview-version


---


## oneview_hypervisor_cluster_profile_facts
Retrieve the facts about one or more of the OneView Hypervisor Cluster Profiles.

#### Synopsis
 Retrieve the facts about one or more of the Hypervisor Cluster Profiles from OneView.

#### Requirements (on the host that executes the module)
  * hpeOneView >= 5.4.0
  * python >= 3.4.2

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional and when used should be present in the host running the ansible commands. If the file path is not provided, the configuration will be loaded from environment variables. For links to example configuration files or how to use the environment variables verify the notes section.  |
| name  |   No  |  | |  Hypervisor Cluster Profile name.  |
| options  |   No  |  | |  Hypervisor Cluster Profile compliance.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Hypervisor Cluster Profiles
  oneview_hypervisor_cluster_profile_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
  delegate_to: localhost

- debug: var=hypervisor_cluster_profiles

- name: Gather paginated, filtered and sorted facts about Hypervisor Managers
  oneview_hypervisor_cluster_profile_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 1
      count: 3
      sort: 'name:descending'
      filter: 'hypervisorType=Vmware'
  delegate_to: localhost

- debug: var=hypervisor_cluster_profiles

- name: Gather facts about a Hypervisor Manager by name
  oneview_hypervisor_cluster_profile_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: hypervisor cluster profile name
  delegate_to: localhost

- debug: var=hypervisor_cluster_profiles

- name: Gather facts about a Hypervisor Manager by name with options
  oneview_hypervisor_cluster_profile_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: hypervisor cluster profile name
    options:
      - compliancePreview
  delegate_to: localhost

- debug: var=hypervisor_cluster_profiles
- debug: var=hypervisor_cluster_profile_compliance_preview

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| hypervisor_cluster_profiles   | Has all the OneView facts about the Hypervisor Cluster Profiles. |  Always, but can be null. |  dict |
| hypervisor_cluster_profile_compliance_preview   | Has the OneView facts about the Hypervisor Cluster Profile Compliance Preview. |  When required. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples

- The OneView API version used will directly affect returned and expected fields in resources. Information on setting the desired API version and can be found at: https://github.com/HewlettPackard/oneview-ansible#setting-your-oneview-version


---



## oneview_hypervisor_manager
Manage OneView Hypervisor Manager resources.

#### Synopsis
 Provides an interface to manage Hypervisor Manager resources. Can create, update, or delete.

#### Requirements (on the host that executes the module)
  * hpeOneView >= 5.4.0
  * python >= 3.4.2

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional and when used should be present in the host running the ansible commands. If the file path is not provided, the configuration will be loaded from environment variables. For links to example configuration files or how to use the environment variables verify the notes section.  |
| data  |   Yes  |  | |  List with the Hypervisor Manager properties.  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  Indicates the desired state for the Hypervisor Manager resource. `present` ensures data properties are compliant with OneView. `absent` removes the resource from OneView, if it exists.  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  |



#### Examples

```yaml

- name: Create a Hypervisor Manager
  oneview_hypervisor_manager:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: '172.18.13.11'
      displayName: 'vcenter'
      hypervisorType: 'Vmware'
      username: 'dcs'
      password: 'dcs'

- name: Update the Hypervisor Manager display name to 'vcenter Renamed'
  oneview_hypervisor_manager:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: '172.18.13.11'
      displayName: 'vcenter Renamed'
      hypervisorType: 'Vmware'
      username: 'dcs'
      password: 'dcs'

- name: Ensure that the Hypervisor Manager is absent
  oneview_hypervisor_manager:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: absent
    data:
      name: '172.18.13.11'

---



#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples

- The OneView API version used will directly affect returned and expected fields in resources. Information on setting the desired API version and can be found at: https://github.com/HewlettPackard/oneview-ansible#setting-your-oneview-version


---


## oneview_hypervisor_manager_facts
Retrieve the facts about one or more of the OneView Hypervisor Managers.

#### Synopsis
 Retrieve the facts about one or more of the Hypervisor Managers from OneView.

#### Requirements (on the host that executes the module)
  * hpeOneView >= 5.4.0
  * python >= 3.4.2

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional and when used should be present in the host running the ansible commands. If the file path is not provided, the configuration will be loaded from environment variables. For links to example configuration files or how to use the environment variables verify the notes section.  |
| name  |   No  |  | |  Hypervisor Manager name.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Hypervisor Managers
  oneview_hypervisor_manager_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
  delegate_to: localhost

- debug: var=hypervisor_managers

- name: Gather paginated, filtered and sorted facts about Hypervisor Managers
  oneview_hypervisor_manager_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 1
      count: 3
      sort: 'name:descending'
      filter: 'hypervisorType=Vmware'
  delegate_to: localhost

- debug: var=hypervisor_managers

- name: Gather facts about a Hypervisor Manager by name
  oneview_hypervisor_manager_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: hypervisor manager name
  delegate_to: localhost

- debug: var=hypervisor_managers

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| hypervisor_managers   | Has all the OneView facts about the Hypervisor Managers. |  Always, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples

- The OneView API version used will directly affect returned and expected fields in resources. Information on setting the desired API version and can be found at: https://github.com/HewlettPackard/oneview-ansible#setting-your-oneview-version


---


## oneview_id_pools
Manage OneView ID Pools resources.

#### Synopsis
 Provides an interface to manage ID Pools resources. Can create, update, and delete.

#### Requirements (on the host that executes the module)
  * python >= 3.4.2
  * hpeOneView >= 6.0.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with the ID Pool properties.  |
| state  |   |  | <ul> <li>allocate</li>  <li>collect</li> </ul> |  Indicates the desired state for the resource. `allocate` will reserve set of Ids. `collect` will gather the allocated Ids.  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  |

## Example Playbook

```yaml

- name: Enables or disables the pool type
  oneview_id_pools:
    config: "{{ config }}"
    state: update_pool_type
    data:
      poolType: '{{ poolType }}'
      enabled: True
  delegate_to: localhost

- name: Allocates one or more IDs from a pool
  oneview_id_pools:
    config: "{{ config }}"
    state: allocate
    data:
      poolType: '{{ poolType }}'
      count: 2
  delegate_to: localhost
- debug: var=id_pool

- name: Collects one or more IDs to be returned to a pool
  oneview_id_pools:
    config: "{{ config }}"
    state: collect
    data:
      poolType: '{{ poolType }}'
      idList: '{{ id_pool["idList"] }}'
  delegate_to: localhost

- name: Generates a random range
  oneview_id_pools_facts:
    config: "{{ config }}"
    state: generate
    data:
      poolType: '{{ poolType }}'
  delegate_to: localhost
- debug: var=id_pool

- name: Validates a set of IDs to reserve in the pool
  oneview_id_pools:
    config: "{{ config }}"
    state: validate
    data:
      poolType: '{{ poolType }}'
      idList: ['{{ id_pool["startAddress"] }}', 
               '{{ id_pool["endAddress"] }}']
  delegate_to: localhost

```

#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| id_pools | Has the facts about the managed OneView ID Pools |  On state 'collect'. Can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_id_pools_facts
Manage OneView ID Pools resources.

#### Synopsis
 Provides an interface to manage ID Pools resources. Can get schema, validate, and generate range.

#### Requirements (on the host that executes the module)
  * ppython >= 3.4.2
  * hpeOneView >= 6.0.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with the ID Pool properties.  |
| state  |   |  | <ul> <li>schema</li>  <li>validate</li> </ul> |  Indicates the desired state for the resource. `schema` will fetch Id Pool schema. `validate` will ensure Ids are validated or not.  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  |

## Example Playbook

```yaml

- name: Get schema of the id pools
  oneview_id_pools_facts:
    config: "{{ config }}"
    state: schema
    data:
      description: 'ID pool schema'
  delegate_to: localhost

- name: Generates a random range
  oneview_id_pools_facts:
    config: "{{ config }}"
    state: generate
    data:
      poolType: '{{ poolType }}'
  delegate_to: localhost

- name: Get the ID Pools type
  oneview_id_pools_facts:
    config: "{{ config }}"
    state: get_pool_type
    data:
      poolType: '{{ poolType }}'
  delegate_to: localhost
- debug: var=id_pool

- name: Checks the range availability in the ID pool
  oneview_id_pools_facts:
    config: "{{ config }}"
    state: check_range_availability
    data:
      poolType: '{{ poolType }}'
      idList: ["42:CE:78:00:00:00", "42:CE:78:8F:FF:FF"]
  delegate_to: localhost

- name: Validates the list of ID's from IPv4 Subnet
  oneview_id_pools_facts:
    config: "{{ config }}"
    state: validate_id_pool
    data:
      poolType: 'ipv4'
      idList: ['172.18.9.11']
  delegate_to: localhost

```

#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| id_pools_facts | Has the facts about the managed OneView ID Pools |  On state 'generate'. Can be null. |  dict |

#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_id_pools_ipv4_range
Manage OneView ID pools IPV4 Range resources.

#### Synopsis
 Provides an interface to manage ID pools IPV4 Range resources. Can create, update, or delete.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with ID pools IPV4 Range properties.  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  Indicates the desired state for the ID pools IPV4 Range resource. `present` will ensure data properties are compliant with OneView. `absent` will remove the resource from OneView, if it exists.  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  |



#### Examples

```yaml

- name: Ensure that ID pools IPV4 Range is present using the default configuration
  oneview_id_pools_ipv4_range:
    config: "{{ config_file_path }}"
    state: present
    data:
      name: 'Test ID pools IPV4 Range'

- name: Ensure that ID pools IPV4 Range is absent
  oneview_id_pools_ipv4_range:
    config: "{{ config_file_path }}"
    state: absent
    data:
      name: 'ID pools IPV4 Range'

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| id_pools_ipv4_range   | Has the facts about the OneView ID pools IPV4 Ranges. |  On state 'present'. Can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_id_pools_ipv4_range_facts
Retrieve the facts about one or more of the OneView ID Pools IPV4 Ranges.

#### Synopsis
 Retrieve the facts about one or more of the ID Pools IPV4 Ranges from OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  ID Pools IPV4 Range name.  |
| options  |   No  |  | |  List with options to gather additional facts about an IPv4 Range and related resources. Options allowed: `allocatedFragments` gets all fragments that have been allocated in range. `freeFragments` gets all free fragments in an IPv4 range.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |
| uri  |   No  |  | |  ID Pools IPV4 Range ID or URI.  |



#### Examples

```yaml

- name: Gather facts about all ID Pools IPV4 Ranges
  oneview_id_pools_ipv4_range_facts:
    config: "{{ config_file_path }}"

- debug: var=id_pools_ipv4_ranges

- name: Gather paginated, filtered and sorted facts about ID Pools IPV4 Ranges
  oneview_id_pools_ipv4_range_facts:
    config: "{{ config }}"
    params:
      start: 1
      count: 3
      sort: 'name:descending'
- debug: var=id_pools_ipv4_ranges

- name: Gather facts about a ID Pools IPV4 Range by name
  oneview_id_pools_ipv4_range_facts:
    config: "{{ config_file_path }}"
    name: IPV4Range_01

- debug: var=id_pools_ipv4_ranges

- name: Gather facts about the 3 first ID Pools IPV4 Range free fragments
  oneview_id_pools_ipv4_range_facts:
    config: "{{ config_file_path }}"
    options:
      - freeFragments
    name: IPV4Range_01
    params:
      count: 3
      start: 0

- name: Gather facts about all the ID Pools IPV4 Range allocated fragments
  oneview_id_pools_ipv4_range_facts:
    config: "{{ config_file_path }}"
    options:
      - allocatedFragments
    name: IPV4Range_01
    params:
      count: -1
      start: 0

- debug: var=id_pools_ipv4_range_allocated_fragments

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| id_pools_ipv4_ranges   | Has all the OneView facts about the ID Pools IPV4 Ranges. |  Always, but can be null. |  dict |
| id_pools_ipv4_ranges_allocated_fragments   | Has all the OneView facts about the ID Pools IPV4 Range allocated fragments. |  Always, but can be null. |  dict |
| id_pools_ipv4_ranges_free_fragments   | Has all the OneView facts about the ID Pools IPV4 Range Free fragments. |  Always, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_id_pools_ipv4_subnet
Manage OneView ID pools IPV4 Subnet resources.

#### Synopsis
 Provides an interface to manage ID pools IPV4 Subnet resources. Can create, update, or delete.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with ID pools IPV4 Subnet properties.  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  Indicates the desired state for the ID pools IPV4 Subnet resource. `present` will ensure data properties are compliant with OneView. `absent` will remove the resource from OneView, if it exists.  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  |



#### Examples

```yaml

- name: Ensure that ID pools IPV4 Subnet is present using the default configuration
  oneview_id_pools_ipv4_subnet:
    config: "{{ config_file_path }}"
    state: present
    data:
      name: 'Test ID pools IPV4 Subnet'
      vlanId: '201'

- name: Ensure that ID pools IPV4 Subnet is absent
  oneview_id_pools_ipv4_subnet:
    config: "{{ config_file_path }}"
    state: absent
    data:
      name: 'ID pools IPV4 Subnet'

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| id_pools_ipv4_subnet   | Has the facts about the OneView ID pools IPV4 Subnets. |  On state 'present'. Can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_id_pools_ipv4_subnet_facts
Retrieve the facts about one or more of the OneView ID Pools IPV4 Subnets.

#### Synopsis
 Retrieve the facts about one or more of the ID Pools IPV4 Subnets from OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  ID Pools IPV4 Subnet name.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |
| uri  |   No  |  | |  ID Pools IPV4 Subnet ID or URI.  |



#### Examples

```yaml

- name: Gather facts about all ID Pools IPV4 Subnets
  oneview_id_pools_ipv4_subnet_facts:
    config: "{{ config_file_path }}"

- debug: var=id_pools_ipv4_subnets

- name: Gather paginated, filtered and sorted facts about ID Pools IPV4 Subnets
  oneview_id_pools_ipv4_subnet_facts:
    config: "{{ config }}"
    params:
      start: 1
      count: 3
      sort: 'name:descending'
- debug: var=id_pools_ipv4_subnets

- name: Gather facts about a ID Pools IPV4 Subnet by name
  oneview_id_pools_ipv4_subnet_facts:
    config: "{{ config_file_path }}"
    name: IPV4Subnet_01

- debug: var=id_pools_ipv4_subnets

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| id_pools_ipv4_subnets   | Has all the OneView facts about the ID Pools IPV4 Subnets. |  Always, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_interconnect
Manage the OneView Interconnect resources.

#### Synopsis
 Provides an interface to manage Interconnect resources. Can change the power state, UID light state, perform device reset, reset port protection, and update the interconnect ports.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| ip  |   No  |  | |  Interconnect IP address.  |
| name  |   No  |  | |  Interconnect name.  |
| ports  |   No  |  | |  List with ports to update. This option should be used together with `update_ports` state.  |
| state  |   |  | <ul> <li>powered_on</li>  <li>powered_off</li>  <li>uid_on</li>  <li>uid_off</li>  <li>device_reset</li>  <li>update_ports</li>  <li>reset_port_protection</li>  <li>reconfigured</li> </ul> |  Indicates the desired state for the Interconnect resource. `powered_on` turns the power on. `powered_off` turns the power off. `uid_on` turns the UID light on. `uid_off` turns the UID light off. `device_reset` perform a device reset. `update_ports` updates the interconnect ports. `reset_port_protection` triggers a reset of port protection. `reconfigured` will reapply the appliance's configuration on the interconnect. This includes running the same configuration steps that were performed as part of the interconnect add by the enclosure.  |



#### Examples

```yaml

- name: Turn the power off for Interconnect named '0000A66102, interconnect 2'
  oneview_interconnect:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: 'powered_off'
    name: '0000A66102, interconnect 2'

- name: Turn the UID light to 'On' for interconnect named '0000A66102, interconnect 2'
  oneview_interconnect:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: 'uid_on'
    name: '0000A66102, interconnect 2'

- name: Turn the UID light to 'Off' for interconnect that matches the ip 172.18.1.114
  oneview_interconnect:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: 'uid_on'
    ip: '172.18.1.114'

- name: Reconfigures the interconnect that matches the ip 172.18.1.114
  oneview_interconnect:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: 'reconfigured'
    ip: '172.18.1.114'

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| interconnect   | Has the facts about the OneView Interconnect. |  Always. Can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_interconnect_facts
Retrieve facts about one or more of the OneView Interconnects.

#### Synopsis
 Retrieve facts about one or more of the Interconnects from OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Interconnect name.  |
| options  |   No  |  | |  List with options to gather additional facts about Interconnect. Options allowed: `nameServers` gets the named servers for an interconnect. `statistics` gets the statistics from an interconnect. `portStatistics` gets the statistics for the specified port name on an interconnect. `subPortStatistics` gets the subport statistics on an interconnect. `ports` gets all interconnect ports. `port` gets a specific interconnect port. `pluggableModuleInformation` gets all the SFP information.  To gather additional facts it is required inform the Interconnect name. Otherwise, these options will be ignored.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all interconnects
  oneview_interconnect_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200

- debug: var=interconnects

- name: Gather paginated, filtered and sorted facts about Interconnects
  oneview_interconnect_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 0
      count: 5
      sort: 'name:descending'
      filter: "enclosureName='0000A66101'"

- debug: var=interconnects

- name: Gather facts about the interconnect that matches the specified name
  oneview_interconnect_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: '0000A66102, interconnect 2'

- debug: var=interconnects


- name: Gather facts about the interconnect that matches the specified name and its name servers
  oneview_interconnect_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: '0000A66102, interconnect 2'
    options:
        - nameServers

- debug: var=interconnects
- debug: var=interconnect_name_servers

- name: Gather facts about statistics for the Interconnect named '0000A66102, interconnect 2'
  oneview_interconnect_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: '0000A66102, interconnect 2'
    options:
        - statistics

- debug: var=interconnects
- debug: var=interconnect_statistics

- name: Gather facts about statistics for the Port named 'd3' of the Interconnect named '0000A66102, interconnect 2'
  oneview_interconnect_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: '0000A66102, interconnect 2'
    options:
        - portStatistics: 'd3'

- debug: var=interconnects
- debug: var=interconnect_port_statistics

- name: Gather facts about statistics for the sub Port number '1' of the Interconnect named 'Enc2, interconnect 2'
  oneview_interconnect_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: 'Enc2, interconnect 2'
    options:
        - subPortStatistics:
            portName: 'd4'
            subportNumber: 1

- debug: var=interconnects
- debug: var=interconnect_subport_statistics

- name: Gather facts about all the Interconnect ports
  oneview_interconnect_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: '0000A66102, interconnect 2'
    options:
        - ports

- debug: var=interconnects
- debug: var=interconnect_ports

- name: Gather facts about an Interconnect port
  oneview_interconnect_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: '0000A66102, interconnect 2'
    options:
        - port: d1

- debug: var=interconnects
- debug: var=interconnect_port

- name: Gather facts about all the SFPs plugged
  oneview_interconnect_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: '0000A66102, interconnect 2'
    options:
        - pluggableModuleInformation

- debug: var=interconnects
- debug: var=interconnect_pluggable_module_information


```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| interconnect_name_servers   | The named servers for an interconnect. |  When requested, but can be null. |  list |
| interconnect_pluggable_module_information   | The plugged SFPs information. |  When requested, but can be null. |  list |
| interconnect_port   | The interconnect port. |  When requested, but can be null. |  dict |
| interconnect_port_statistics   | Statistics for the specified port name on an interconnect. |  When requested, but can be null. |  dict |
| interconnect_ports   | All interconnect ports. |  When requested, but can be null. |  list |
| interconnect_statistics   | Has all the OneView facts about the Interconnect Statistics. |  When requested, but can be null. |  dict |
| interconnect_subport_statistics   | The subport statistics on an interconnect. |  When requested, but can be null. |  dict |
| interconnects   | The list of interconnects. |  Always, but can be null. |  list |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_interconnect_link_topology_facts
Retrieve facts about the OneView Interconnect Link Topologies.

#### Synopsis
 Retrieve facts about the Interconnect Link Topologies from OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Name of the Interconnect Link Topology.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Interconnect Link Topologies
  oneview_interconnect_link_topology_facts:
    config: "{{ config_path }}"

- debug: var=interconnect_link_topologies

- name: Gather paginated, filtered and sorted facts about Interconnect Link Topologies
  oneview_interconnect_link_topology_facts:
    config: "{{ config }}"
    params:
      start: 0
      count: 3
      sort: 'name:descending'
      filter: "name='name1900571853-1483553596802'"

- debug: var=interconnect_link_topologies

- name: Gather facts about an Interconnect Link Topology by name
  oneview_interconnect_link_topology_facts:
    config: "{{ config_path }}"
    name: "Name of the Interconnect Link Topologies"

- debug: var=interconnect_link_topologies

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| interconnect_link_topologies   | Has all the OneView facts about the Interconnect Link Topologies. |  Always, but can be null. |  dict |


#### Notes

- This resource is only available on HPE Synergy.

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_interconnect_type_facts
Retrieve facts about one or more of the OneView Interconnect Types.

#### Synopsis
 Retrieve facts about one or more of the Interconnect Types from OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Interconnect Type name.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Interconnect Types
  oneview_interconnect_type_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200

- debug: var=interconnect_types

- name: Gather paginated, filtered and sorted facts about Interconnect Types
  oneview_interconnect_type_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 0
      count: 3
      sort: 'name:descending'
      filter: "maximumFirmwareVersion='4000.99'"

- debug: var=interconnect_types

- name: Gather facts about an Interconnect Type by name
  oneview_interconnect_type_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: HP VC Flex-10 Enet Module

- debug: var=interconnect_types

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| interconnect_types   | Has all the OneView facts about the Interconnect Types. |  Always, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_internal_link_set_facts
Retrieve facts about the OneView Internal Link Sets.

#### Synopsis
 Retrieve facts about the Internal Link Sets from OneView. It is possible get all Internal Link Sets or filter by name.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Name of the Internal Link Set.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set. `query`: A general query string to narrow the list of resources returned. `fields`: Specifies which fields should be returned in the result set. `view`: Return a specific subset of the attributes of the resource or collection, by specifying the name of a predefined view.  |



#### Examples

```yaml

- name: Gather facts about all Internal Link Sets
  oneview_internal_link_set_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200

- debug: var=internal_link_sets

- name: Gather paginated and sorted facts about Internal Link Sets
  oneview_internal_link_set_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 0
      count: 3
      sort: 'name:ascending'

- debug: var=internal_link_sets

- name: Gather facts about an Internal Link Set by name
  oneview_internal_link_set_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "Internal Link Set Name"

- debug: var=internal_link_sets

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| internal_link_sets   | Has all the OneView facts about the Internal Link Sets. |  Always, but can be null. |  dict |


#### Notes

- This resource is available for API version 300 or later

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_label
Manage the Oneview Label Resources.

#### Synopsis
Label Resource manages the labels assigned to a given resource.

#### Requirements (on the host that executes the module)
  * python >= 3.4.2
  * hpeOneView >= 6.1.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Label name.  |
| uri | No |  | | URI of Label.  |
| resourceUri | No | | URI of Resource.   |


#### Examples

``` yaml

- name: Create Labels for enclosure resource
  oneview_label:
    config: "{{ config }}"
    state: present
    data:
      resourceUri: "/rest/enclosures/0000000000A66102"
      labels:
        - name: "Test label 1"
        - name: "Test Label 2"
  delegate_to: localhost
  register: label

- name: Update label of given resource for enclosure resource
  oneview_label:
    config: "{{ config }}"
    state: present
    data:
      resourceUri: "/rest/enclosures/0000000000A66102"
      labels:
        - name: "Test label 1 Renamed"
          uri: "/rest/labels/130"
        - name: "Test label 2 Renamed"
          uri: null 
        - name: "Test label 3"
          uri: null 
  delegate_to: localhost

- name: Delete Labels for enclosure resource
  oneview_label:
    config: "{{ config }}"
    state: absent
    data:
      resourceUri: "/rest/enclosures/0000000000A66102"
  delegate_to: localhost

```

#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| label   | Has the labels for a resource. |  Always. |  dict |

#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---

## oneview_label_facts
Retrive facts about Oneview Label Resources.

#### Synopsis
Gets a list of the labels.

#### Requirements (on the host that executes the module)
  * python >= 3.4.2
  * hpeOneView >= 6.1.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |
| name  |   No  |  | |  Label name.  |
| resourceUri | No | | URI of Resource.   |


#### Examples

```yaml

- name: Gather facts about all Labels 
  oneview_label_facts:
    config: "{{ config }}"
  delegate_to: localhost

- debug: var=labels

- name: Gather paginated, filtered and sorted facts about Labels
  oneview_label_facts:
    config: "{{ config }}"
    params:
      start: 0
      count: 3
      sort: 'name:descending'
      filter: ''
- debug: var=labels

- name: Gather facts about a Label by name
  oneview_label_facts:
    config: "{{ config }}"
    name: "{{ labels[0]['name'] }}"
  delegate_to: localhost

- debug: var=labels
 
- name: Gather facts about a Label by Resource
  oneview_label_facts:
    config: "{{ config }}"
    resourceUri: "/rest/enclosures/0000000000A66102"
  delegate_to: localhost 

- debug: var=labels

```

#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| labels   | list of Labels. |  Always. but, can be null |  dict |


## oneview_logical_downlinks_facts
Retrieve facts about one or more of the OneView Logical Downlinks.

#### Synopsis
 Retrieve facts about one or more of the Logical Downlinks from OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| excludeEthernet  |   No  |  | |  Excludes any facts about Ethernet networks from the Logical Downlinks.  |
| name  |   No  |  | |  Logical Downlink name.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Logical Downlinks
  oneview_logical_downlinks_facts:
    config: "{{ config }}"
    delegate_to: localhost

- debug: var=logical_downlinks

- name: Gather paginated, filtered and sorted facts about Logical Downlinks
  oneview_logical_downlinks_facts:
    config: "{{ config }}"
    params:
      start: 0
      count: 3
      sort: 'name:descending'
      filter: "name='LDa4c64fd9-0b76-46c3-8335-0bbb76459aff (Cisco Fabric Extender for HP BladeSystem)'"

- debug: var=logical_downlinks

- name: Gather facts about all Logical Downlinks excluding any existing Ethernet networks
  oneview_logical_downlinks_facts:
    config: "{{ config }}"
    excludeEthernet: true
    delegate_to: localhost

- debug: var=logical_downlinks

- name: Gather facts about a Logical Downlink by name and excluding any existing Ethernet networks
  oneview_logical_downlinks_facts:
    config: "{{ config }}"
    name: "LD415a472f-ed77-42cc-9a5e-b9bd5d096923 (HP VC FlexFabric-20/40 F8 Module)"
    excludeEthernet: true
    delegate_to: localhost

- debug: var=logical_downlinks

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| logical_downlinks   | The list of logical downlinks. |  Always, but can be null. |  list |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_logical_enclosure
Manage OneView Logical Enclosure resources.

#### Synopsis
 Provides an interface to manage Logical Enclosure resources. Can create, update, update firmware, perform dump, update configuration script, reapply configuration, update from group, or delete.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with Logical Enclosure properties and its associated states.  |
| state  |   Yes  |  | <ul> <li>present</li>  <li>firmware_updated</li>  <li>script_updated</li>  <li>dumped</li>  <li>reconfigured</li>  <li>updated_from_group</li>  <li>absent</li> </ul> |  Indicates the desired state for the Logical Enclosure resource. `present` ensures data properties are compliant with OneView. You can rename the enclosure providing an attribute `newName`. `firmware_updated` updates the firmware for the Logical Enclosure. `script_updated` updates the Logical Enclosure configuration script. `dumped` generates a support dump for the Logical Enclosure. `reconfigured` reconfigures all enclosures associated with a logical enclosure. `updated_from_group` makes the logical enclosure consistent with the enclosure group. `absent` will remove the resource from OneView, if it exists.  |



#### Examples

```yaml

- name: Create a Logical Enclosure (available only on HPE Synergy)
  oneview_logical_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
        enclosureUris:
          - "/rest/enclosures/0000000000A66101"
        enclosureGroupUri: "/rest/enclosure-groups/9fafc382-bbef-4a94-a9d1-05f77042f3ac"
        name: "Encl1"
  ignore_errors: true
  delegate_to: localhost

- name: Update the firmware for the Logical Enclosure
  oneview_logical_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: firmware_updated
    data:
        name: "Encl1"
        firmware:
            firmwareBaselineUri: "/rest/firmware-drivers/SPPGen9Snap3_2015_0221_71"
            firmwareUpdateOn: "EnclosureOnly"
            forceInstallFirmware: "false"
        custom_headers:
            if-Match: '*'
  delegate_to: localhost

# This play is compatible with Synergy Enclosures
- name: Update the firmware for the Logical Enclosure with the logical-interconnect validation set as true
  oneview_logical_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: firmware_updated
    data:
        name: "Encl1"
        firmware:
            firmwareBaselineUri: "/rest/firmware-drivers/SPPGen9Snap3_2015_0221_71"
            firmwareUpdateOn: "EnclosureOnly"
            forceInstallFirmware: "false"
            validateIfLIFirmwareUpdateIsNonDisruptive: "true"
            logicalInterconnectUpdateMode: "Orchestrated"
            updateFirmwareOnUnmanagedInterconnect: "true"
        custom_headers:
            if-Match: '*'
  delegate_to: localhost

- name: Update the Logical Enclosure configuration script
  oneview_logical_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: script_updated
    data:
        name: "Encl1"
        configurationScript: "# script (updated)"
  delegate_to: localhost

- name: Generates a support dump for the Logical Enclosure
  oneview_logical_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: dumped
    data:
        name: "Encl1"
        dump:
          errorCode: "MyDump16"
          encrypt: "true"
          excludeApplianceDump: "false"
  delegate_to: localhost
- debug: var=generated_dump_uri

- name: Reconfigure all enclosures associated with logical enclosure
  oneview_logical_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: reconfigured
    data:
        name: "Encl1"
  delegate_to: localhost

- name: Makes the logical enclosure consistent with the enclosure group
  oneview_logical_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: updated_from_group
    data:
        name: "Encl1"
  delegate_to: localhost

- name: Update the Logical Enclosure changing the name attribute
  oneview_logical_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
        name: "Encl1"
        newName: "Encl1 (renamed)"
  delegate_to: localhost

- name: Delete a Logical Enclosure (available only on HPE Synergy)
  oneview_logical_enclosure:
      hostname: 172.16.101.48
      username: administrator
      password: my_password
      api_version: 2200
      state: absent
      data:
          name: 'Encl1'
  delegate_to: localhost

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| configuration_script   | Has the facts about the Logical Enclosure configuration script. |  On state 'script_updated'. Can be null. |  dict |
| generated_dump_uri   | Has the facts about the Logical Enclosure generated support dump URI. |  On state 'dumped'. Can be null. |  dict |
| logical_enclosure   | Has the facts about the OneView Logical Enclosure. |  On states 'present', 'firmware_updated', 'reconfigured', 'updated_from_group', and 'absent'. Can be null. |  dict |


#### Notes

- The `absent` state and the creation of a Logical Enclosure done through the `present` state are available only on HPE Synergy.

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_logical_enclosure_facts
Retrieve facts about one or more of the OneView Logical Enclosures.

#### Synopsis
 Retrieve facts about one or more of the Logical Enclosures from OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Logical Enclosure name.  |
| options  |   No  |  | |  List with options to gather additional facts about a Logical Enclosure and related resources. Options allowed: script.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Logical Enclosures
  oneview_logical_enclosure_facts:
      hostname: 172.16.101.48
      username: administrator
      password: my_password
      api_version: 2200
  delegate_to: localhost

- debug: var=logical_enclosures

- name: Gather paginated, filtered and sorted facts about Logical Enclosures
  oneview_logical_enclosure_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 0
      count: 3
      sort: 'name:descending'
      filter: 'status=OK'
      scope_uris: '/rest/scope/637fa556-a78d-4796-8fce-2179e249ea7d'

- debug: var=logical_enclosures

- name: Gather facts about a Logical Enclosure by name
  oneview_logical_enclosure_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "Encl1"
  delegate_to: localhost

- debug: var=logical_enclosures

- name: Gather facts about a Logical Enclosure by name with options
  oneview_logical_enclosure_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "Encl1"
    options:
      - script
  delegate_to: localhost

- debug: var=logical_enclosures
- debug: var=logical_enclosure_script

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| logical_enclosure_script   | Has the facts about the script of a Logical Enclosure. |  When required, but can be null. |  dict |
| logical_enclosures   | Has all the OneView facts about the Logical Enclosures. |  Always, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_logical_interconnect
Manage OneView Logical Interconnect resources.

#### Synopsis
 Provides an interface to manage Logical Interconnect resources.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.6.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with the options.  |
| state  |   |  | <ul> <li>compliant</li>  <li>ethernet_settings_updated</li>  <li>internal_networks_updated</li>  <li>settings_updated</li>  <li>forwarding_information_base_generated</li>  <li>qos_aggregated_configuration_updated</li>  <li>snmp_configuration_updated</li>  <li>port_monitor_updated</li>  <li>configuration_updated</li>  <li>firmware_installed</li>  <li>telemetry_configuration_updated</li>   </ul> |  Indicates the desired state for the Logical Interconnect resource. `compliant` brings the logical interconnect back to a consistent state. `ethernet_settings_updated` updates the Ethernet interconnect settings for the logical interconnect. `internal_networks_updated` updates the internal networks on the logical interconnect. This operation is non-idempotent. `settings_updated` updates the Logical Interconnect settings. `forwarding_information_base_generated` generates the forwarding information base dump file for the logical interconnect. This operation is non-idempotent and asynchronous. `qos_aggregated_configuration_updated` updates the QoS aggregated configuration for the logical interconnect. `snmp_configuration_updated` updates the SNMP configuration for the logical interconnect. `port_monitor_updated` updates the port monitor configuration of a logical interconnect. `configuration_updated` asynchronously applies or re-applies the logical interconnect configuration to all managed interconnects. This operation is non-idempotent. `firmware_installed` installs firmware to a logical interconnect. The three operations that are supported for the firmware update are Stage (uploads firmware to the interconnect), Activate (installs firmware on the interconnect) and Update (which does a Stage and Activate in a sequential manner). All of them are non-idempotent. `telemetry_configuration_updated` updates the telemetry configuration of a logical interconnect. `scopes_updated` updates the scopes associated with the logical interconnect.
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  |



#### Examples

```yaml

- name: Return the Logical Interconnect to a consistent state
  oneview_logical_interconnect:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: compliant
    data:
      name: "Name of the Logical Interconnect"

- name: Update the Ethernet interconnect settings for the logical interconnect
  oneview_logical_interconnect:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: ethernet_settings_updated
    data:
      name: "Name of the Logical Interconnect"
      ethernetSettings:
        macRefreshInterval: 10

- name: Update the internal networks on the logical interconnect
  oneview_logical_interconnect:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: internal_networks_updated
    data:
      name: "Name of the Logical Interconnect"
      internalNetworks:
        - name: "Name of the Ethernet Network 1"
        - name: "Name of the Ethernet Network 2"
        - uri: "/rest/ethernet-networks/8a58cf7c-d49d-43b1-94ce-da5621be490c"

- name: Update the interconnect settings
  oneview_logical_interconnect:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: settings_updated
    data:
      name: "Name of the Logical Interconnect"
      ethernetSettings:
        macRefreshInterval: 10

- name: Generate the forwarding information base dump file for the logical interconnect
  oneview_logical_interconnect:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: forwarding_information_base_generated
    data:
      name: "Name of the Logical Interconnect"  # could also be 'uri'

- name: Update the QoS aggregated configuration for the logical interconnect
  oneview_logical_interconnect:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: qos_aggregated_configuration_updated
    data:
      name: "Name of the Logical Interconnect"
      qosConfiguration:
      activeQosConfig:
        category: 'qos-aggregated-configuration'
        configType: 'Passthrough'
        downlinkClassificationType: ~
        uplinkClassificationType: ~
        qosTrafficClassifiers: []
        type: 'QosConfiguration'

- name: Update the SNMP configuration for the logical interconnect
  oneview_logical_interconnect:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: snmp_configuration_updated
    data:
      name: "Name of the Logical Interconnect"
      snmpConfiguration:
        enabled: True

- name: Update the IGMP settings for the logical interconnect
  oneview_logical_interconnect:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2400
    state: igmp_settings_updated
    data:
      name: "Name of the Logical Interconnect"
      igmpSettings:
        igmpIdleTimeoutInterval: 200

- name: Update the port monitor configuration of the logical interconnect
  oneview_logical_interconnect:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: port_monitor_updated
    data:
      name: "Name of the Logical Interconnect"
      portMonitor:
        enablePortMonitor: False

- name: Update the port flap settings of the logical interconnect
  oneview_logical_interconnect:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2400
    state: port_flap_settings_updated
    data:
      name: "Name of the Logical Interconnect"
      portFlapProtection:
        portFlapThresholdPerInterval: 5

- name: Update the configuration on the logical interconnect
  oneview_logical_interconnect:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: configuration_updated
    data:
      name: "Name of the Logical Interconnect"

- name: Install a firmware to the logical interconnect, running the stage operation to upload the firmware
  oneview_logical_interconnect:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: firmware_installed
    data:
      name: "Name of the Logical Interconnect"
      firmware:
        command: Stage
        spp: "filename"  # could also be sppUri: '/rest/firmware-drivers/<filename>'

- name: Validates the bulk update from group operation of the given LI URLs
  oneview_logical_interconnect:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2400
    state: bulk_inconsistency_validated
    data:
      name: "Name of the Logical Interconnect"
      bulk_update:
        logicalInterconnectUris:
          - /rest/logical-interconnects/d0432852-28a7-4060-ba49-57ca973ef6c2

- name: Updates the telemetry configuration of a logical interconnect.
  oneview_logical_interconnect:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: telemetry_configuration_updated
    data:
      name: "Name of the Logical Interconnect"
      telemetryConfiguration:
        sampleCount: 12
        enableTelemetry: True
        sampleInterval: 300

- debug: var=telemetry_configuration

- name: Updates the scopes of a logical interconnect.
  oneview_logical_interconnect:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    state: scopes_updated
    data:
      name: "Name of the Logical Interconnect"
      scopeUris:
        - '/rest/scopes/00SC123456'
        - '/rest/scopes/01SC123456'

- debug: var=scope_uris

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| interconnect_fib   | Has the OneView facts about the Forwarding information Base. |  On 'forwarding_information_base_generated' state, but can be null. |  dict |
| li_firmware   | Has the OneView facts about the installed Firmware. |  On 'firmware_installed' state, but can be null. |  dict |
| port_monitor   | Has the OneView facts about the Port Monitor Configuration. |  On 'port_monitor_updated' state, but can be null. |  dict |
| qos_configuration   | Has the OneView facts about the QoS Configuration. |  On 'qos_aggregated_configuration_updated' state, but can be null. |  dict |
| scope_uris   | Has the scope URIs the specified logical interconnect is inserted into. |  On 'scopes_updated' state, but can be null. |  dict |
| snmp_configuration   | Has the OneView facts about the SNMP Configuration. |  On 'snmp_configuration_updated' state, but can be null. |  dict |
| igmp_settings   | Has the OneView facts about the IGMP settings. |  On 'igmp_settings_updated' state, but can be null. |  dict |
| port_flap_settings   | Has the OneView facts about the port flap settings. |  On 'port_flap_settings_updated' state, but can be null. |  dict |
| li_inconsistency_report   | Has the OneView facts about the bulk inconsistency report. |  On 'bulk_inconsistency_validated' state, but can be null. |  dict |
| storage_volume_template   | Has the OneView facts about the Logical Interconnect. |  On 'compliant', 'ethernet_settings_updated', 'internal_networks_updated', 'settings_updated',               and 'configuration_updated' states, but can be null. |  dict |
| telemetry_configuration   | Has the OneView facts about the Telemetry Configuration. |  On 'telemetry_configuration_updated' state, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_logical_interconnect_facts
Retrieve facts about one or more of the OneView Logical Interconnects.

#### Synopsis
 Retrieve facts about one or more of the OneView Logical Interconnects.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.6.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Logical Interconnect name.  |
| options  |   No  |  | |  List with options to gather additional facts about Logical Interconnect. Options allowed: `qos_aggregated_configuration` gets the QoS aggregated configuration for the logical interconnect. `snmp_configuration` gets the SNMP configuration for a logical interconnect. `port_monitor` gets the port monitor configuration of a logical interconnect. `internal_vlans` gets the internal VLAN IDs for the provisioned networks on a logical interconnect. `forwarding_information_base` gets the forwarding information base data for a logical interconnect. `firmware` get the installed firmware for a logical interconnect. `unassigned_ports` gets a collection of ports from the member interconnects which are eligible for assignment to an analyzer port. `unassigned_uplink_ports` gets a collection of uplink ports from the member interconnects which are eligible for assignment to an analyzer port. `telemetry_configuration` gets the telemetry configuration of the logical interconnect. `ethernet_settings` gets the Ethernet interconnect settings for the Logical Interconnect. - These options are valid just when a `name` is provided. Otherwise it will be ignored.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Logical Interconnects
  oneview_logical_interconnect_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200

- debug: var=logical_interconnects

- name: Gather paginated and sorted facts about Logical Interconnects
  oneview_logical_interconnect_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 0
      count: 3
      sort: 'name:descending'

- debug: var=logical_interconnects

- name: Gather facts about a Logical Interconnect by name with QOS Configuration
  oneview_logical_interconnect_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "Name of the Logical Interconnect"
    options:
      - qos_aggregated_configuration

- debug: var=logical_interconnects
- debug: var=qos_aggregated_configuration

- name: Gather facts about a Logical Interconnect by name with all options
  oneview_logical_interconnect_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "Name of the Logical Interconnect"
    options:
      - qos_aggregated_configuration
      - snmp_configuration
      - igmp_settings
      - port_monitor
      - internal_vlans
      - forwarding_information_base
      - firmware
      - unassigned_uplink_ports
      - unassigned_ports
      - telemetry_configuration
      - ethernet_settings

- debug: var=logical_interconnects
- debug: var=qos_aggregated_configuration
- debug: var=snmp_configuration
- debug: var=igmp_settings
- debug: var=port_monitor
- debug: var=internal_vlans
- debug: var=forwarding_information_base
- debug: var=firmware
- debug: var=unassigned_uplink_ports
- debug: var=unassigned_ports
- debug: var=telemetry_configuration
- debug: var=ethernet_settings

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| ethernet_settings   | The Ethernet Interconnect Settings. |  When requested, but can be null. |  dict |
| firmware   | The installed firmware for a logical interconnect. |  When requested, but can be null. |  dict |
| forwarding_information_base   | The forwarding information base data for a logical interconnect. |  When requested, but can be null. |  dict |
| internal_vlans   | The internal VLAN IDs for the provisioned networks on a logical interconnect. |  When requested, but can be null. |  dict |
| logical_interconnects   | The list of logical interconnects. |  Always, but can be null. |  list |
| port_monitor   | The port monitor configuration of a logical interconnect. |  When requested, but can be null. |  dict |
| qos_aggregated_configuration   | The QoS aggregated configuration for the logical interconnect. |  When requested, but can be null. |  dict |
| snmp_configuration   | The SNMP configuration for a logical interconnect. |  When requested, but can be null. |  dict |
| igmp_settings   | The IGMP settings for a logical interconnect. |  When requested, but can be null. |  dict |
| telemetry_configuration   | The telemetry configuration of the logical interconnect. |  When requested, but can be null. |  dict |
| unassigned_ports   | A collection of ports from the member interconnects which are eligible for assignment to an analyzer port on a logical interconnect. |  When requested, but can be null. |  dict |
| unassigned_uplink_ports   | A collection of uplink ports from the member interconnects which are eligible for assignment to an analyzer port on a logical interconnect. |  When requested, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_logical_interconnect_group
Manage OneView Logical Interconnect Group resources.

#### Synopsis
 Provides an interface to manage Logical Interconnect Group resources. Can create, update, or delete.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with the Logical Interconnect Group properties.  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  Indicates the desired state for the Logical Interconnect Group resource. `present` will ensure data properties are compliant with OneView. `absent` will remove the resource from OneView, if it exists.  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  |



#### Examples

```yaml

- name: Ensure that the Logical Interconnect Group is present
  oneview_logical_interconnect_group:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: 'Test Logical Interconnect Group'
      uplinkSets: []
      enclosureType: 'C7000'
      interconnectMapTemplate:
        interconnectMapEntryTemplates:
          - logicalDownlinkUri: ~
            logicalLocation:
                locationEntries:
                    - relativeValue: "1"
                      type: "Bay"
                    - relativeValue: 1
                      type: "Enclosure"
            permittedInterconnectTypeName: 'HP VC Flex-10/10D Module'
            # Alternatively you can inform permittedInterconnectTypeUri
# Below Task is available only till OneView 3.10
- name: Ensure that the Logical Interconnect Group has the specified scopes
  oneview_logical_interconnect_group:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: 'Test Logical Interconnect Group'
      scopeUris:
        - '/rest/scopes/00SC123456'
        - '/rest/scopes/01SC123456'

- name: Ensure that the Logical Interconnect Group is present with uplinkSets
  oneview_logical_interconnect_group:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: 'Test Logical Interconnect Group'
      uplinkSets:
        - name: 'e23 uplink set'
          mode: 'Auto'
          networkType: 'Ethernet'
          networkUris:
            - '/rest/ethernet-networks/b2be27ec-ae31-41cb-9f92-ff6da5905abc'
          logicalPortConfigInfos:
            - desiredSpeed: 'Auto'
              logicalLocation:
                  locationEntries:
                    - relativeValue: 1
                      type: "Bay"
                    - relativeValue: 23
                      type: "Port"
                    - relativeValue: 1
                      type: "Enclosure"

- name: Ensure that the Logical Interconnect Group is present with name 'Test'
  oneview_logical_interconnect_group:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: 'New Logical Interconnect Group'
      newName: 'Test'

- name: Ensure that the Logical Interconnect Group is absent
  oneview_logical_interconnect_group:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: absent
    data:
      name: 'New Logical Interconnect Group'

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| logical_interconnect_group   | Has the facts about the OneView Logical Interconnect Group. |  On state 'present'. Can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_logical_interconnect_group_facts
Retrieve facts about one or more of the OneView Logical Interconnect Groups

#### Synopsis
 Retrieve facts about one or more of the Logical Interconnect Groups from OneView

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   |  | |  Logical Interconnect Group name.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Logical Interconnect Groups
  oneview_logical_interconnect_group_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
  no_log: true
  delegate_to: localhost

- debug: var=logical_interconnect_groups

- name: Gather paginated, filtered and sorted facts about Logical Interconnect Groups
  oneview_logical_interconnect_group_facts:
    params:
      start: 0
      count: 3
      sort: name:descending
      filter: name=LIGName
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
  no_log: true
  delegate_to: localhost

- debug: var=logical_interconnect_groups

- name: Gather facts about a Logical Interconnect Group by scopeUris
  oneview_logical_interconnect_group_facts:
    params:
      scope_uris: "/rest/scopes/63d1ca81-95b3-41f1-a1ee-f9e1bc2d635f"
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
  no_log: true
  delegate_to: localhost

- debug: var=logical_interconnect_groups

- name: Gather facts about a Logical Interconnect Group by name
  oneview_logical_interconnect_group_facts:
    name: logical lnterconnect group name
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
  no_log: true
  delegate_to: localhost

- debug: var=logical_interconnect_groups

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| logical_interconnect_groups   | Has all the OneView facts about the Logical Interconnect Groups. |  Always, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_logical_switch
Manage OneView Logical Switch resources.

#### Synopsis
 Provides an interface to manage Logical Switch resources. Can create, update, delete, or refresh.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with the Logical Switches properties. You can choose set the Logical Switch Group by `logicalSwitchGroupName` or `logicalSwitchGroupUri`.  |
| state  |   Yes  |  | <ul> <li>present</li>  <li>updated</li>  <li>absent</li>  <li>refreshed</li> </ul> |  Indicates the desired state for the Logical Switch resource. `present` creates a Logical Switch, if it doesn't exist. To update the Logical Switch, use the `updated` state instead. `updated` ensures the Logical Switch is updated. Currently OneView only supports updating the credentials , scopes and name of the Logical Switch. To change the name of the Logical Switch, a `newName` in the data must be provided. The update operation is non-idempotent. `absent` removes the resource from OneView, if it exists. `refreshed` reclaims the top-of-rack switches in the logical switch. This operation is non-idempotent.  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  |



#### Examples

```yaml

- name: Create a Logical Switch
  oneview_logical_switch:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      logicalSwitch:
        name: 'Test Logical Switch'
        # You can choose set the Logical Switch Group by logicalSwitchGroupName or logicalSwitchGroupUri
        logicalSwitchGroupName: 'Group Nexus 55xx'                                                   # option 1
        # logicalSwitchGroupUri: '/rest/logical-switch-groups/dce11b79-6fce-48af-84fb-a315b9644571'  # option 2
        switchCredentialConfiguration:
          - snmpV1Configuration:  # Switch 1
              communityString: 'public'
            logicalSwitchManagementHost: '172.18.16.1'
            snmpVersion: 'SNMPv1'
            snmpPort: 161
          - snmpV1Configuration:  # Switch 2
              communityString: 'public'
            logicalSwitchManagementHost: '172.18.16.2'
            snmpVersion: 'SNMPv1'
            snmpPort: 161
      logicalSwitchCredentials:
        - connectionProperties:  # Switch 1
            - propertyName: 'SshBasicAuthCredentialUser'
              value: 'ssh_username_switch_1'
              valueFormat: 'Unknown'
              valueType: 'String'
            - propertyName: 'SshBasicAuthCredentialPassword'
              value: 'ssh_password_switch_1'
              valueFormat: 'SecuritySensitive'
              valueType: 'String'
        - connectionProperties:  # Switch 2
            - propertyName: 'SshBasicAuthCredentialUser'
              value: 'ssh_username_switch_2'
              valueFormat: 'Unknown'
              valueType: 'String'
            - propertyName: 'SshBasicAuthCredentialPassword'
              value: 'ssh_password_switch_2'
              valueFormat: 'SecuritySensitive'
              valueType: 'String'

- name: Update the Logical Switch name and credentials
  oneview_logical_switch:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: updated
    data:
      logicalSwitch:
        name: 'Test Logical Switch'
        newName: 'Test Logical Switch - Renamed'
      logicalSwitchCredentials:
        - connectionProperties:  # Switch 1
            - propertyName: 'SshBasicAuthCredentialUser'
              value: 'ssh_username_switch_1'
              valueFormat: 'Unknown'
              valueType: 'String'
            - propertyName: 'SshBasicAuthCredentialPassword'
              value: 'ssh_password_switch_1'
              valueFormat: 'SecuritySensitive'
              valueType: 'String'
        - connectionProperties:  # Switch 2
            - propertyName: 'SshBasicAuthCredentialUser'
              value: 'ssh_username_switch_2'
              valueFormat: 'Unknown'
              valueType: 'String'
            - propertyName: 'SshBasicAuthCredentialPassword'
              value: 'ssh_password_switch_2'
              valueFormat: 'SecuritySensitive'
              valueType: 'String'
      scopeUris: # This field is available only till OneView 3.10
        - '/rest/scopes/d1f79dea-6393-4bb0-9723-8adc9b96de94'


- name: Reclaim the top-of-rack switches in the logical switch
  oneview_logical_switch:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: refreshed
    data:
      logicalSwitch:
        name: 'Test Logical Switch'

- name: Delete a Logical Switch
  oneview_logical_switch:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: absent
    data:
      logicalSwitch:
        name: 'Test Logical Switch'

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| logical_switch   | Has the facts about the OneView Logical Switch. |  On the states 'present', 'updated', and 'refreshed'. Can be null. |  dict |


#### Notes

- This resource is only available on C7000 enclosures

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_logical_switch_facts
Retrieve the facts about one or more of the OneView Logical Switches.

#### Synopsis
 Retrieve the facts about one or more of the Logical Switches from OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Logical Switch name.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Logical Switches
  oneview_logical_switch_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
- debug: var=logical_switches

- name: Gather paginated, filtered and sorted facts about Logical Switches
  oneview_logical_switch_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 0
      count: 3
      sort: 'name:descending'
      filter: 'status=OK'

- debug: var=logical_switches

- name: Gather facts about a Logical Switch by name
  oneview_logical_switch_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: 'Name of the Logical Switch'

- debug: var=logical_switches

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| logical_switches   | Has all the OneView facts about the Logical Switches. |  Always, but can be null. |  dict |


#### Notes

- This resource is only available on C7000 enclosures

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_logical_switch_group
Manage OneView Logical Switch Group resources.

#### Synopsis
 Provides an interface to manage Logical Switch Group resources. Can add, update, remove.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with Logical Switch Group properties and its associated states.  |
| state  |   Yes  |  | <ul> <li>present</li>  <li>absent</li> </ul> |  Indicates the desired state for the Logical Switch Group resource. `present` will ensure data properties are compliant with OneView. `absent` will remove the resource from OneView, if it exists.  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  |



#### Examples

```yaml

- name: Create a Logical Switch Group
  oneview_logical_switch_group:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
        name: "OneView Test Logical Switch Group"
        switchMapTemplate:
            switchMapEntryTemplates:
                - logicalLocation:
                    locationEntries:
                       - relativeValue: 1
                         type: "StackingMemberId"
                  # You can choose either permittedSwitchTypeName or permittedSwitchTypeUri to inform the Switch Type
                  permittedSwitchTypeName: 'Cisco Nexus 50xx'
                  permittedSwitchTypeUri: '/rest/switch-types/2f36bc8f-65d8-4ea2-9300-750180402a5e'
  delegate_to: localhost

- name: Update the Logical Switch Group and make sure it is present in the desired scopes
  oneview_logical_switch_group:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
        name: "OneView Test Logical Switch Group"
        newName: "Test Logical Switch Group"
        scopeUris:
          - '/rest/scopes/00SC123456'
          - '/rest/scopes/01SC123456'
        switchMapTemplate:
            switchMapEntryTemplates:
                - logicalLocation:
                    locationEntries:
                       - relativeValue: 1
                         type: "StackingMemberId"
                  permittedSwitchTypeUri: '/rest/switch-types/2f36bc8f-65d8-4ea2-9300-750180402a5e'
  delegate_to: localhost

- name: Delete the Logical Switch Group
  oneview_logical_switch_group:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: absent
    data:
        name: 'Test Logical Switch Group'
  delegate_to: localhost

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| logical_switch_group   | Has the OneView facts about the Logical Switch Group. |  On state 'present'. Can be null. |  dict |


#### Notes

- This resource is only available on C7000 enclosures

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_logical_switch_group_facts
Retrieve facts about OneView Logical Switch Groups.

#### Synopsis
 Retrieve facts about the Logical Switch Groups of the OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Logical Switch Group name.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Logical Switch Groups
  oneview_logical_switch_group_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
  delegate_to: localhost

- debug: var=logical_switch_groups

- name: Gather paginated, filtered and sorted facts about Logical Switch Groups
  oneview_logical_switch_group_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 0
      count: 3
      sort: 'name:descending'
      filter: "name='Logical_Switch_Group+56'"

- debug: var=logical_switch_groups

- name: Gather facts about a Logical Switch Group by name
  oneview_logical_switch_group_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "LogicalSwitchGroupDemo"
  delegate_to: localhost

- debug: var=logical_switch_groups

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| logical_switch_groups   | Has all the OneView facts about the Logical Switch Groups. |  Always, but can be null. |  dict |


#### Notes

- This resource is only available on C7000 enclosures

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_login_detail_facts
Retrieve the facts about login details

#### Synopsis
 Retrieve the facts about login details from oneview.

#### Requirements (on the host that executes the module)
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |



#### Examples

```yaml

- name: Gather facts about login details
  oneview_login_detail_facts:
    config: "{{ config }}"
    delegate_to: localhost

- debug: var=login_details

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| login_details   | Lists all the login details |  Always, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_managed_san
Manage OneView Managed SAN resources.

#### Synopsis
 Provides an interface to manage Managed SAN resources. Can update the Managed SAN, set the refresh state, create a SAN endpoints CSV file, and create an unexpected zoning issue report.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with Managed SAN properties and its associated states. Warning: For the 'present' state, the contents of the publicAttributes will replace the existing list, so leaving out a public attribute from the given list will effectively delete it.  |
| state  |   Yes  |  | <ul> <li>present</li>  <li>refresh_state_set</li>  <li>endpoints_csv_file_created</li>  <li>issues_report_created</li> </ul> |  Indicates the desired state for the Managed SAN resource. `present` ensures data properties are compliant with OneView. `refresh_state_set` updates the refresh state of the Managed SAN. `endpoints_csv_file_created` creates a SAN endpoints CSV file. `issues_report_created` creates an unexpected zoning report for a SAN.  |



#### Examples

```yaml

  - name: Refresh the Managed SAN
    oneview_managed_san:
      hostname: 172.16.101.48
      username: administrator
      password: my_password
      api_version: 2200
      state: refresh_state_set
      data:
          name: 'SAN1_0'
          refreshStateData:
              refreshState: 'RefreshPending'
    delegate_to: localhost

  - name: Update the Managed SAN
    oneview_managed_san:
      hostname: 172.16.101.48
      username: administrator
      password: my_password
      api_version: 2200
      state: present
      data:
          name: 'SAN1_0'
          publicAttributes:
            - name: 'MetaSan'
              value: 'Neon SAN'
              valueType: 'String'
              valueFormat: 'None'
          sanPolicy:
            zoningPolicy: 'SingleInitiatorAllTargets'
            zoneNameFormat: '{hostName}_{initiatorWwn}'
            enableAliasing: True
            initiatorNameFormat: '{hostName}_{initiatorWwn}'
            targetNameFormat: '{storageSystemName}_{targetName}'
            targetGroupNameFormat: '{storageSystemName}_{targetGroupName}'
    delegate_to: localhost

  - name: Create an endpoints CSV file for the SAN
    oneview_managed_san:
      hostname: 172.16.101.48
      username: administrator
      password: my_password
      api_version: 2200
      state: endpoints_csv_file_created
      data:
          name: '{{ name }}'
    delegate_to: localhost

  - name: Create an unexpected zoning report for the SAN
    oneview_managed_san:
      hostname: 172.16.101.48
      username: administrator
      password: my_password
      api_version: 2200
      state: issues_report_created
      data:
          name: '{{ name }}'
    delegate_to: localhost

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| managed_san   | Has the OneView facts about the Managed SAN. |  On states 'present' and 'refresh_state_set'. Can be null. |  dict |
| managed_san_endpoints   | Has the OneView facts about the Endpoints CSV File created. |  On state 'endpoints_csv_file_created'. Can be null. |  dict |
| managed_san_issues   | Has the OneView facts about the unexpected zoning report created. |  On state 'issues_report_created'. Can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_managed_san_facts
Retrieve facts about the OneView Managed SANs.

#### Synopsis
 Retrieve facts about the OneView Managed SANs.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Name of the Managed SAN.  |
| options  |   No  |  | |  List with options to gather additional facts about Managed SAN. Options allowed: `endpoints` gets the list of endpoints in the SAN identified by name. `wwn` gets the list of Managed SANs associated with an informed WWN `locate`.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `query`: A general query string to narrow the list of resources returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Managed SANs
  oneview_managed_san_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
  delegate_to: localhost

- debug: var=managed_sans

- name: Gather paginated, filtered and sorted facts about Managed SANs
  oneview_managed_san_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 0
      count: 3
      sort: name:ascending
      query: imported eq true
  delegate_to: localhost

- debug: var=managed_sans

- name: Gather facts about a Managed SAN by name
  oneview_managed_san_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "SAN1_0"
  delegate_to: localhost

- debug: var=managed_sans

- name: Gather facts about the endpoints in the SAN identified by name
  oneview_managed_san_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "SAN1_0"
    options:
      - endpoints
  delegate_to: localhost

- debug: var=managed_sans
- debug: var=managed_san_endpoints

- name: Gather facts about Managed SANs for an associated WWN
  oneview_managed_san_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    options:
      - wwn:
         locate: "20:00:4A:2B:21:E0:00:01"
  delegate_to: localhost

- debug: var=wwn_associated_sans

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| managed_san_endpoints   | The list of endpoints in the SAN identified by name. |  When requested, but can be null. |  dict |
| managed_sans   | The list of Managed SANs. |  Always, but can be null. |  list |
| wwn_associated_sans   | The list of associations between provided WWNs and the SANs. |  When requested, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_network_set
Manage OneView Network Set resources.

#### Synopsis
 Provides an interface to manage Network Set resources. Can create, update, or delete.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with the Network Set properties.  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  Indicates the desired state for the Network Set resource. `present` ensures data properties are compliant with OneView. `absent` removes the resource from OneView, if it exists.  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  |



#### Examples

```yaml

- name: Create a Network Set
  oneview_network_set:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: 'OneViewSDK Test Network Set'
      networkUris:
        - 'Test Ethernet Network_1'                                       # can be a name
        - '/rest/ethernet-networks/e4360c9d-051d-4931-b2aa-7de846450dd8'  # or a URI

- name: Update the Network Set name to 'OneViewSDK Test Network Set - Renamed' and change the associated networks
  oneview_network_set:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: 'OneViewSDK Test Network Set'
      newName: 'OneViewSDK Test Network Set - Renamed'
      networkUris:
        - 'Test Ethernet Network_1'

- name: Delete the Network Set
  oneview_network_set:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: absent
    data:
        name: 'OneViewSDK Test Network Set - Renamed'

# This feature is only available for V300 and V500
- name: Update the Network set with two scopes
  oneview_network_set:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: OneViewSDK Test Network Set
      scopeUris:
        - /rest/scopes/01SC123456
        - /rest/scopes/02SC123456
  delegate_to: localhost

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| network_set   | Has the facts about the Network Set. |  On state 'present', but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_network_set_facts
Retrieve facts about the OneView Network Sets

#### Synopsis
 Retrieve facts about the Network Sets from OneView.

#### Requirements (on the host that executes the module)
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   |  | |  Network Set name.  |
| options  |   |  | |  List with options to gather facts about Network Set. Option allowed: `withoutEthernet`. The option `withoutEthernet` retrieves the list of network_sets excluding Ethernet networks.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Network Sets
  oneview_network_set_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
  no_log: true
  delegate_to: localhost

- debug: var=network_sets

- name: Gather paginated, filtered, and sorted facts about Network Sets
  oneview_network_set_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 0
      count: 3
      sort: 'name:descending'
      filter: name='netset001'
  no_log: true
  delegate_to: localhost

- debug: var=network_sets

- name: Gather facts about all Network Sets, excluding Ethernet networks
  oneview_network_set_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    options:
        - withoutEthernet
  no_log: true
  delegate_to: localhost

- debug: var=network_sets


- name: Gather facts about a Network Set by name
  oneview_network_set_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: Name of the Network Set
  no_log: true
  delegate_to: localhost

- debug: var=network_sets


- name: Gather facts about a Network Set by name, excluding Ethernet networks
  oneview_network_set_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: Name of the Network Set
    options:
        - withoutEthernet
  no_log: true
  delegate_to: localhost

- debug: var=network_sets

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| network_sets   | Has all the OneView facts about the Network Sets. |  Always, but can be empty. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_os_deployment_plan_facts
Retrieve facts about one or more OS Deployment Plans.

#### Synopsis
 Retrieve facts about one or more of the OS Deployment Plans from OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Os Deployment Plan name.  |
| options  |   No  |  | |  List with options to gather facts about OS Deployment Plan. Option allowed: `osCustomAttributesForServerProfile` The option `osCustomAttributesForServerProfile` retrieves the list of editable OS Custom Atributes, prepared for Server Profile use.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all OS Deployment Plans
  oneview_os_deployment_plan_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
  delegate_to: localhost
- debug: var=os_deployment_plans

- name: Gather paginated, filtered and sorted facts about OS Deployment Plans
  oneview_os_deployment_plan_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 0
      count: 3
      sort: name:ascending
      filter: deploymentApplianceIpv4='15.212.171.216'
  delegate_to: localhost
- debug: var=os_deployment_plans

- name: Gather facts about an OS Deployment Plan by name
  oneview_os_deployment_plan_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "Deployment Plan"
  delegate_to: localhost
- debug: var=os_deployment_plans

- name: Gather facts about an OS Deployment Plan by name with OS Custom Attributes option
  oneview_os_deployment_plan_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "Deployment Plan"
    options:
      # This option will generate an os_deployment_plan_custom_attributes facts in the Server Profile format.
      - osCustomAttributesForServerProfile
  delegate_to: localhost
- debug: var=os_deployment_plans
- debug: var=os_deployment_plan_custom_attributes

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| os_deployment_plan_custom_attributes   | Has the editable Custom Attribute facts of the Os Deployment Plans in the Server Profiles format. |  When requested, but can be empty. |  dict |
| os_deployment_plans   | Has all the OneView facts about the Os Deployment Plans. |  Always, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_os_deployment_server
Manage OneView Deployment Server resources.

#### Synopsis
 Provides an interface to manage Deployment Server resources. Can create, update, or delete.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with Deployment Server properties.  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  Indicates the desired state for the Deployment Server resource. `present` will ensure data properties are compliant with OneView. `absent` will remove the resource from OneView, if it exists.  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  |



#### Examples

```yaml

- name: Ensure that the Deployment Server is present
  oneview_os_deployment_server:
    config: "{{ config_file_path }}"
    state: present
    data:
      name: 'Test Deployment Server'
      description: "OS Deployment Server"
      mgmtNetworkUri: "/rest/ethernet-networks/1b96d2b3-bc12-4757-ac72-e4cd0ef20535"
      applianceUri: "/rest/deployment-servers/image-streamer-appliances/aca554e2-09c2-4b14-891d-e51c0058efab"
- debug: var=os_deployment_server

- name: Ensure that the Deployment Server is present with name 'Renamed Deployment Server'
  oneview_os_deployment_server:
    config: "{{ config_file_path }}"
    state: present
    data:
      name: 'Test Deployment Server'
      newName: 'Renamed Deployment Server'
- debug: var=os_deployment_server

- name: Ensure that the Deployment Server is absent
  oneview_os_deployment_server:
    config: "{{ config_file_path }}"
    state: absent
    data:
      name: 'Renamed Deployment Server'

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| os_deployment_server   | Has the facts about the Deployment Servers. |  On state 'present'. Can be null. |  dict |


#### Notes

- For the following data, you can provide either a name or a URI: `mgmtNetworkName` or `mgmtNetworkUri`, and `applianceName` or `applianceUri`

- This resource is only available on HPE Synergy

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_os_deployment_server_facts
Retrieve facts about one or more OS Deployment Servers.

#### Synopsis
 Retrieve facts about one or more of the OS Deployment Servers from OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  OS Deployment Server name.  |
| options  |   No  |  | |  List with options to gather additional facts about an OS Deployment Server and related resources. Options allowed: `networks`, `appliances`, and `appliance`.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set. `query`: A general query string to narrow the list of resources returned. `fields`: Specifies which fields should be returned in the result set. `view`: Return a specific subset of the attributes of the resource or collection, by specifying the name of a predefined view.  |



#### Examples

```yaml

- name: Gather facts about all OS Deployment Servers
  oneview_os_deployment_server_facts:
    config: "{{ config_file_path }}"

- debug: var=os_deployment_servers

- name: Gather facts about an OS Deployment Server by name
  oneview_os_deployment_server_facts:
    config: "{{ config_file_path }}"
    name: "OS Deployment Server-Name"
  delegate_to: localhost

- debug: var=os_deployment_servers

- name: Gather facts about an OS Deployment Server by name with options
  oneview_os_deployment_server_facts:
    config: "{{ config_file_path }}"
    name: 'Test-OS Deployment Server'
    options:
      - networks                    # optional
      - appliances                  # optional
      - appliance: 'Appliance name' # optional
  delegate_to: localhost

- debug: var=os_deployment_servers
- debug: var=os_deployment_server_networks
- debug: var=os_deployment_server_appliances
- debug: var=os_deployment_server_appliance

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| os_deployment_server_appliance   | Has the facts about the particular Image Streamer resource. |  When requested, but can be null. |  dict |
| os_deployment_server_appliances   | Has all the OneView facts about all the Image Streamer resources. |  When requested, but can be null. |  dict |
| os_deployment_server_networks   | Has all the OneView facts about the OneView networks. |  When requested, but can be null. |  dict |
| os_deployment_servers   | Has all the OneView facts about the OS Deployment Servers. |  Always, but can be null. |  dict |


#### Notes

- This resource is only available on HPE Synergy

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_power_device
Manage OneView Power Device resources.

#### Synopsis
 Provides an interface to manage Power delivery devices resources. Can add, update, remove, change power state, change UID state and refresh state.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with Power Device properties and its associated states.  |
| state  |   Yes  |  | <ul> <li>present</li>  <li>discovered</li>  <li>absent</li>  <li>power_state_set</li>  <li>refresh_state_set</li>  <li>uid_state_set</li> </ul> |  Indicates the desired state for the Power Device resource. `present` will ensure data properties are compliant with OneView. `discovered` will add an iPDU to the OneView. `absent` will remove the resource from OneView, if it exists. `power_state_set` will set the power state of the Power Device. `refresh_state_set` will set the refresh state of the Power Device. `uid_state_set` will set the UID state of the Power Device.  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  |



#### Examples

```yaml

- name: Add a Power Device
  oneview_power_device:
    config: "{{ config }}"
    state: present
    data:
        name: 'Power Device Name'
        ratedCapacity: 40
  delegate_to: localhost

- name: Add an iPDU
  oneview_power_device:
    config: "{{ config }}"
    state: discovered
    data:
         hostname : '{{ power_device_hostname }}'
         username : '{{ power_device_username }}'
         password : '{{ power_device_password }}'
         force : false
  delegate_to: localhost

- name: Power off the Power Device
  oneview_power_device:
    config: "{{ config }}"
    state: power_state_set
    data:
        name: 'Power Device Name'
        powerStateData:
            powerState: "Off"
  delegate_to: localhost

- name: Refresh the Power Device
  oneview_power_device:
    config: "{{ config }}"
    state: refresh_state_set
    data:
        name: 'Power Device Name'
        refreshStateData:
            refreshState : "RefreshPending"
  delegate_to: localhost

- name: Set UID light state of the Power Device on
  oneview_power_device:
    config: "{{ config }}"
    state: uid_state_set
    data:
        name: 'Power Device Name'
        uidStateData:
            uidState: "On"
  delegate_to: localhost

- name: Remove the Power Device by its name
  oneview_power_device:
    config: "{{ config }}"
    state: absent
    data:
        name: 'Power Device Name'
  delegate_to: localhost

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| power_device   | Has the OneView facts about the Power Device. |  On states 'present', 'discovered', 'power_state_set', 'refresh_state_set', 'uid_state_set'. Can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_power_device_facts
Retrieve facts about the OneView Power Devices.

#### Synopsis
 Retrieve facts about the Power Delivery Devices from OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Power Device name.  |
| options  |   No  |  | |  List with options to gather additional facts about Power Device. Options allowed: `powerState`, `uidState`, `utilization`  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `query`: A general query string to narrow the list of resources returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Power Devices
  oneview_power_device_facts:
    config: "{{ config }}"
  delegate_to: localhost
- debug: msg="{{power_devices | map(attribute='name') | list }}"

- name:  Gather paginated, filtered and sorted facts about Power Devices
  oneview_power_device_facts:
    config: "{{ config }}"
    params:
      start: 0
      count: 3
      sort: name:ascending
      filter: state='Unmanaged'
      query: feedIdentifier eq 'A'
  delegate_to: localhost
- debug: var=power_devices

- name: Gather facts about a Power Device by name
  oneview_power_device_facts:
    config: "{{ config }}"
    name: "Power Device Name"
  delegate_to: localhost
- debug: var=power_devices

- name: Gather facts about the power state of a Power Device
  oneview_power_device_facts:
    config: "{{ config }}"
    name: "Power Device Name"
    options:
      - powerState            # optional
  delegate_to: localhost
- debug: msg="{{power_devices | map(attribute='name') | list }}"
- debug: var=power_device_power_state

- name: Gather all facts about a Power Device with all options
  oneview_power_device_facts:
   config: "{{ config }}"
   name : "Power Device Name"
   options:
       - powerState             # optional
       - uidState               # optional
       - utilization:           # optional
                fields : 'AveragePower'
                filter : ['startDate=2016-05-30T03:29:42.000Z']
                view : 'day'
  delegate_to: localhost

- debug: msg="{{power_devices | map(attribute='name') | list }}"
- debug: var=power_device_power_state
- debug: var=power_device_uid_state
- debug: var=power_device_utilization

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| power_device_power_state   | Has all the facts about the Power state of the Power Device. |  When requested, but can be null. |  dict |
| power_device_uid_state   | Has all the facts about the Power Device UID state. |  When requested, but can be null. |  dict |
| power_device_utilization   | Has all the facts about the Power Device utilization. |  When requested, but can be null. |  dict |
| power_devices   | Has all the OneView facts about the Power Device. |  Always, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_rack
Manage OneView Racks resources.

#### Synopsis
 Provides an interface to manage Rack resources. Can create, update, and delete.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with the Rack properties.  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  Indicates the desired state for the Rack resource. `present` will ensure data properties are compliant with OneView. To change the name of the Rack, a _newName_ in the data must be provided. `absent` will remove the resource from OneView, if it exists.  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  |



#### Examples

```yaml

- name: Ensure that a Rack is present using the default configuration
  oneview_rack:
    config: "{{ config_file_path }}"
    state: present
    data:
      name: 'Rack Name'

- name: Add rack with custom size and a single mounted enclosure at slot 20
  oneview_rack:
    config: "{{ config_file_path }}"
    state: present
    data:
      name: 'Rack101'
      depth: 1500
      height: 2500
      width: 2200
      rackMounts:
        - mountUri: "/rest/enclosures/39SGH102X6J2"
          topUSlot: 20
          uHeight: 10

- name: Rename the Rack to 'Rack101'
  oneview_rack:
    config: "{{ config_file_path }}"
    state: present
    data:
      name: 'Rack Name'
      newName: 'Rack101'

- name: Ensure that Rack is absent
  oneview_rack:
    config: "{{ config_file_path }}"
    state: absent
    data:
      name: 'Rack Name'

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| rack   | Has the facts about the OneView Racks. |  On state 'present'. Can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_rack_facts
Retrieve facts about Rack resources.

#### Synopsis
 Gets a list of rack resources. Filter by name can be used to get a specific Rack. If a name is specified, it is  allowed to retrieve information about the device topology.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Rack name.  |
| options  |   No  |  | |  Retrieve additional facts. Options available: 'deviceTopology'.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Racks
  oneview_rack_facts:
    config: "{{ config }}"
  delegate_to: localhost
- debug: var=racks

- name: Gather paginated, filtered and sorted facts about Racks
  oneview_rack_facts:
    config: "{{ config }}"
    params:
      start: 0
      count: 5
      sort: 'name:descending'
      filter: "depth=1000"

- name: Gather facts about a Rack by name
  oneview_rack_facts:
    config: "{{ config }}"
    name: "Rack Name"
  delegate_to: localhost
- debug: var=racks

- name: Gather facts about the topology information for the rack
  oneview_rack_facts:
    config: "{{ config }}"
    name: "Rack Name"
    options:
      - deviceTopology
  delegate_to: localhost
- debug: var=racks
- debug: var=rack_device_topology

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| rack_device_topology   | Retrieves the topology information for the rack resource. |  When requested, but can be null. |  dict |
| racks   | Has all the OneView facts about the Racks. |  Always, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_san_manager
Manage OneView SAN Manager resources.

#### Synopsis
 Provides an interface to manage SAN Manager resources. Can create, update, or delete.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with SAN Manager properties.  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li>  <li>connection_information_set</li> </ul> |  Indicates the desired state for the Uplink Set resource. `present` ensures data properties are compliant with OneView. `absent` removes the resource from OneView, if it exists. `connection_information_set` updates the connection information for the SAN Manager. This operation is non-idempotent.  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  |



#### Examples

```yaml

- name: Creates a Device Manager for the Brocade SAN provider with the given hostname and credentials
  oneview_san_manager:
    config: "{{ config }}"
    state: present
    data:
      providerDisplayName: 'Brocade Network Advisor'
      connectionInfo:
        - name: Host
          value: '172.18.15.1'
        - name: Port
          value: '5989'
        - name: Username
          value: 'username'
        - name: Password
          value: 'password'
        - name: UseSsl
          value: true

- name: Sets the SAN Manager connection information
  oneview_san_manager:
    config: "{{ config_path }}"
    state: connection_information_set
    data:
      connectionInfo:
        - name: Host
          value: '172.18.15.1'
        - name: Port
          value: '5989'
        - name: Username
          value: 'username'
        - name: Password
          value: 'password'
        - name: UseSsl
          value: true

- name: Refreshes the SAN Manager
  oneview_san_manager:
    config: "{{ config_path }}"
    state: present
    data:
      name: '172.18.15.1'
      refreshState: 'RefreshPending'

- name: Delete the SAN Manager recently created
  oneview_san_manager:
    config: "{{ config_path }}"
    state: absent
    data:
      name: '172.18.15.1'

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| san_manager   | Has the OneView facts about the SAN Manager. |  On state 'present'. Can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_san_manager_facts
Retrieve facts about one or more of the OneView SAN Managers

#### Synopsis
 Retrieve facts about one or more of the SAN Managers from OneView

#### Requirements (on the host that executes the module)
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| params  |   |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: - `start`: The first item to return, using 0-based indexing. - `count`: The number of resources to return. - `query`: A general query string to narrow the list of resources returned. - `sort`: The sort order of the returned data set.  |
| provider_display_name  |   |  | |  Provider Display Name.  |



#### Examples

```yaml

- name: Gather facts about all SAN Managers
  oneview_san_manager_facts:
    config: /etc/oneview/oneview_config.json
  delegate_to: localhost

- debug: var=san_managers

- name: Gather paginated, filtered and sorted facts about SAN Managers
  oneview_san_manager_facts:
    config: /etc/oneview/oneview_config.json
    params:
      start: 0
      count: 3
      sort: name:ascending
      query: isInternal eq false
  delegate_to: localhost

- debug: var=san_managers

- name: Gather facts about a SAN Manager by provider display name
  oneview_san_manager_facts:
    config: /etc/oneview/oneview_config.json
    provider_display_name: Brocade Network Advisor
  delegate_to: localhost

- debug: var=san_managers

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| san_managers   | Has all the OneView facts about the SAN Managers. |  Always, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_sas_interconnect
Manage the OneView SAS Interconnect resources.

#### Synopsis
 Provides an interface to manage the SAS Interconnect. Can change the power state, UID light state, perform soft and hard reset, and refresh the SAS Interconnect state.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   Yes  |  | |  The SAS Interconnect name.  |
| state  |   |  | <ul> <li>powered_on</li>  <li>powered_off</li>  <li>uid_on</li>  <li>uid_off</li>  <li>soft_reset</li>  <li>hard_reset</li>  <li>refreshed</li> </ul> |  Indicates the desired state for the Switch. `powered_on` turns the power on. `powered_off` turns the power off. `uid_on` turns the UID light on. `uid_off` turns the UID light off. `soft_reset` performs a soft reset. `hard_reset` performs a hard reset. `refreshed` performs a refresh.  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  |



#### Examples

```yaml

- name: Ensure that a SAS Interconnect is powered on
  oneview_sas_interconnect:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: powered_on
    name: "0000A66101, interconnect 1"

- name: Refresh a SAS Interconnect
  oneview_sas_interconnect:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: refreshed
    name: "0000A66101, interconnect 1"

- name: Perform a hard reset
  oneview_sas_interconnect:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: hard_reset
    name: "0000A66101, interconnect 1"

```



#### Notes

- This resource is only available on HPE Synergy

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_sas_interconnect_facts
Retrieve facts about the OneView SAS Interconnects.

#### Synopsis
 Retrieve facts about the OneView SAS Interconnects.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  SAS Interconnect name.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all SAS Interconnects
  oneview_sas_interconnect_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200

- name: Gather paginated, filtered and sorted facts about SAS Interconnects
  oneview_sas_interconnect_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 0
      count: 3
      sort: 'name:descending'
      filter: "softResetState='Normal'"

- name: Gather facts about a SAS Interconnect by name
  oneview_sas_interconnect_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "0000A66103, interconnect 1"

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| sas_interconnects   | The list of SAS Interconnects. |  Always, but can be null. |  list |


#### Notes

- This resource is only available on HPE Synergy

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_sas_interconnect_type_facts
Retrieve facts about the OneView SAS Interconnect Types.

#### Synopsis
 Retrieve facts about the SAS Interconnect Types from OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Name of the SAS Interconnect Type.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all SAS Interconnect Types
  oneview_sas_interconnect_type_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200

- debug: var=sas_interconnect_types

- name: Gather paginated, filtered and sorted facts about SAS Interconnect Types
  oneview_sas_interconnect_type_facts:
    config: "{{ config }}"
    params:
      start: 0
      count: 3
      sort: 'name:descending'
      filter: "enclosureType='SY22000'"

- debug: var=sas_interconnect_types

- name: Gather facts about a SAS Interconnect Type by name
  oneview_sas_interconnect_type_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "SAS Interconnect Type Name"

- debug: var=sas_interconnect_types

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| sas_interconnect_types   | Has all the OneView facts about the SAS Interconnect Types. |  Always, but can be null. |  dict |


#### Notes

- This resource is only available on HPE Synergy

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_sas_logical_interconnect
Manage OneView SAS Logical Interconnect resources.

#### Synopsis
 Provides an interface to manage SAS Logical Interconnect resources.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with SAS Logical Interconnect properties and its associated states.  |
| state  |   Yes  |  | <ul> <li>compliant</li>  <li>drive_enclosure_replaced</li>  <li>configuration_updated</li>  <li>firmware_updated</li> </ul> |  Indicates the desired state for the SAS Logical Interconnect resources. `compliant` brings the list of SAS Logical Interconnect back to a consistent state. `configuration_updated` asynchronously applies or re-applies the SAS Logical Interconnect configuration to all managed interconnects. `firmware_updated` installs firmware to a SAS Logical Interconnect. `drive_enclosure_replaced` replacement operation of a drive enclosure. * All of them are non-idempotent.  |



#### Examples

```yaml

- name: Update the configuration on the SAS Logical Interconnect
  oneview_sas_logical_interconnect:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: configuration_updated
    data:
      name: "SAS Logical Interconnect name"
  delegate_to: localhost

- name: Install a firmware to the SAS Logical Interconnect, running the stage operation to upload the firmware
  oneview_sas_logical_interconnect:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: firmware_updated
    data:
      name: "SAS Logical Interconnect name"
      firmware:
        command: Stage
        sppName: "firmware_driver_name"
        # Can be either the firmware name with "sppName" or the uri with "sppUri", e.g.:
        # sppUri: '/rest/firmware-drivers/<filename>'
  delegate_to: localhost

- name: Replace drive enclosure
  oneview_sas_logical_interconnect:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: drive_enclosure_replaced
    data:
      name: "SAS Logical Interconnect name"
      replace_drive_enclosure:
        oldSerialNumber: "S46016710000J4524YPT"
        newSerialNumber: "S46016710001J4524YPT"
  delegate_to: localhost

- name: Return a SAS Logical Interconnect list to a consistent state by its names
  oneview_sas_logical_interconnect:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: compliant
    data:
      logicalInterconnectNames: ["SAS Logical Interconnect name 1", "SAS Logical Interconnect name 2"]
  delegate_to: localhost

- name: Return a SAS Logical Interconnect list to a consistent state by its URIs
  oneview_sas_logical_interconnect:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: compliant
    data:
      logicalInterconnectUris: [
        '/rest/sas-logical-interconnects/16b2990f-944a-449a-a78f-004d8b4e6824',
        '/rest/sas-logical-interconnects/c800b2e4-92bb-44fa-8a46-f71d40737fa5']
  delegate_to: localhost

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| li_firmware   | Has the OneView facts about the updated Firmware. |  On 'firmware_updated' state, but can be null. |  dict |
| sas_logical_interconnect   | Has the OneView facts about the SAS Logical Interconnect. |  On states 'drive_enclosure_replaced', 'configuration_updated', but can be null. |  dict |


#### Notes

- This resource is only available on HPE Synergy

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_sas_logical_interconnect_facts
Retrieve facts about one or more of the OneView SAS Logical Interconnects.

#### Synopsis
 Retrieve facts about one or more of the OneView SAS Logical Interconnects.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  SAS Logical Interconnect name.  |
| options  |   No  |  | |  List with options to gather additional facts about SAS Logical Interconnect. `firmware` gets the installed firmware for a SAS Logical Interconnect.  These options are valid just when a `name` is provided. Otherwise it will be ignored.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all SAS Logical Interconnects
  oneview_sas_logical_interconnect_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
  delegate_to: localhost
- debug: var=sas_logical_interconnects

- name: Gather paginated, filtered and sorted facts about SAS Logical Interconnects
  oneview_sas_logical_interconnect_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 0
      count: 2
      sort: 'name:descending'
      filter: "status='OK'"
- debug: var=sas_logical_interconnects

- name: Gather facts about a SAS Logical Interconnect by name
  oneview_sas_logical_interconnect_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "LOG_EN-LIG_SAS-1"
  delegate_to: localhost
- debug: var=sas_logical_interconnects

- name: Gather facts about an installed firmware for a SAS Logical Interconnect that matches the specified name
  oneview_sas_logical_interconnect_facts:
    chostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "LOG_EN-LIG_SAS-1"
    options:
      - firmware
  delegate_to: localhost
- debug: var=sas_logical_interconnect_firmware

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| sas_logical_interconnect_firmware   | The installed firmware for a SAS Logical Interconnect. |  When requested, but can be null. |  dict |
| sas_logical_interconnects   | The list of SAS Logical Interconnects. |  Always, but can be null. |  list |


#### Notes

- This resource is only available on HPE Synergy

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_sas_logical_interconnect_group
Manage OneView SAS Logical Interconnect Group resources.

#### Synopsis
 Provides an interface to manage SAS Logical Interconnect Group resources. Can create, update, or delete.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with the SAS Logical Interconnect Group properties.  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  Indicates the desired state for the SAS Logical Interconnect Group resource. `present` will ensure data properties are compliant with OneView. `absent` will remove the resource from OneView, if it exists.  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  |



#### Examples

```yaml

- name: Ensure that the SAS Logical Interconnect Group is present
  oneview_sas_logical_interconnect_group:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: "Test SAS Logical Interconnect Group"
      state: "Active"
      interconnectMapTemplate:
        interconnectMapEntryTemplates:
          - logicalLocation:
              locationEntries:
                - type: "Bay"
                  relativeValue: "1"
                - type: "Enclosure"
                  relativeValue: "1"
            enclosureIndex: "1"
            permittedInterconnectTypeUri: "/rest/sas-interconnect-types/Synergy12GbSASConnectionModule"
          - logicalLocation:
              locationEntries:
                - type: "Bay"
                  relativeValue: "4"
                - type: "Enclosure"
                  relativeValue: "1"
            enclosureIndex: "1"
            permittedInterconnectTypeUri: "/rest/sas-interconnect-types/Synergy12GbSASConnectionModule"
      enclosureType: "SY22000"
      enclosureIndexes: [1]
      interconnectBaySet: "1"

- name: Ensure that the SAS Logical Interconnect Group is present with name 'Test'
  oneview_sas_logical_interconnect_group:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: 'New SAS Logical Interconnect Group'
      newName: 'Test'

- name: Ensure that the SAS Logical Interconnect Group is absent
  oneview_sas_logical_interconnect_group:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: absent
    data:
      name: 'New SAS Logical Interconnect Group'

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| sas_logical_interconnect_group   | Has the facts about the OneView SAS Logical Interconnect Group. |  On state 'present'. Can be null. |  dict |


#### Notes

- This resource is only available on HPE Synergy

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_sas_logical_interconnect_group_facts
Retrieve facts about one or more of the OneView SAS Logical Interconnect Groups.

#### Synopsis
 Retrieve facts about one or more of the SAS Logical Interconnect Groups from OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Name of the SAS Logical Interconnect Group.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all SAS Logical Interconnect Groups
  oneview_sas_logical_interconnect_group_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
- debug: var=sas_logical_interconnect_groups

- name: Gather paginated, filtered and sorted facts about SAS Logical Interconnect Groups
  oneview_sas_logical_interconnect_group_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 0
      count: 5
      sort: 'name:descending'
      filter: "state='Active'"
- debug: var=sas_logical_interconnect_groups

- name: Gather facts about a SAS Logical Interconnect Group by scopeUris
  oneview_sas_logical_interconnect_group_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      scope_uris: "/rest/scopes/be263683-b147-4818-8bbe-c5a5629b9bfe"
- debug: var=sas_logical_interconnect_groups

- name: Gather facts about a SAS Logical Interconnect Group by name
  oneview_sas_logical_interconnect_group_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "LIG-SLJA-1"
- debug: var=sas_logical_interconnect_groups

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| sas_logical_interconnect_groups   | Has all the OneView facts about the SAS Logical Interconnect Groups. |  Always, but can be null. |  dict |


#### Notes

- This resource is only available on HPE Synergy

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_sas_logical_jbod_attachment_facts
Retrieve facts about one or more of the OneView SAS Logical JBOD Attachments.

#### Synopsis
 Retrieve facts about one or more of the SAS Logical JBOD Attachments from OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Name of SAS Logical JBOD Attachment.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all SAS Logical JBOD Attachment
  oneview_sas_logical_jbod_attachment_facts:
  config: "{{ config_path }}"

- debug: var=sas_logical_jbod_attachments

- name: Gather paginated, filtered and sorted facts about SAS Logical JBOD Attachment
  oneview_sas_logical_jbod_attachment_facts:
    config: "{{ config }}"
    params:
      start: 0
      count: 2
      sort: 'name:descending'
      filter: "state=Deployed"

- debug: var=sas_logical_jbod_attachments


- name: Gather facts about a SAS Logical JBOD Attachment by name
  oneview_sas_logical_jbod_attachment_facts:
    config: "{{ config_path }}"
    name: "logical-enclosure-SAS-Logical-Interconnect-Group-BDD-1-SLJA-1"

- debug: var=sas_logical_jbod_attachments

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| sas_logical_jbod_attachments   | Has all the OneView facts about the SAS Logical JBOD Attachment. |  Always, but can be null. |  dict |


#### Notes

- This resource is only available on HPE Synergy

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_sas_logical_jbod_facts
Retrieve facts about one or more of the OneView SAS Logical JBODs.

#### Synopsis
 Retrieve facts about one or more of the SAS Logical JBODs from OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Name of SAS Logical JBODs.  |
| options  |   No  |  | |  List with options to gather additional facts about SAS Logical JBODs and related resources. Options allowed: `drives`.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all SAS Logical JBODs
  oneview_sas_logical_jbod_facts:
    config: "{{ config }}"

- debug: var=sas_logical_jbods

- name: Gather paginated, filtered and sorted facts about SAS Logical JBODs
  oneview_sas_logical_jbod_facts:
    config: "{{ config }}"
    params:
      start: 0
      count: 2
      sort: 'name:descending'
      filter: "state='Configured'"

- debug: var=sas_logical_jbods

- name: Gather facts about a SAS Logical JBOD by name
  oneview_sas_logical_jbod_facts:
    config: "{{ config_path }}"
    name: "Name of the SAS Logical JBOD"

- debug: var=sas_logical_jbods

- name: Gather facts about a SAS Logical JBOD by name, with the list of drives allocated
  oneview_sas_logical_jbod_facts:
    config: "{{ config }}"
    name: "{{ sas_logical_jbod_name }}"
    options:
      - drives

- debug: var=sas_logical_jbods
- debug: var=sas_logical_jbod_drives

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| sas_logical_jbod_drives   | Has all the OneView facts about the list of drives allocated to a SAS logical JBOD. |  Always, but can be null. |  dict |
| sas_logical_jbods   | Has all the OneView facts about the SAS Logical JBODs. |  Always, but can be null. |  dict |


#### Notes

- This resource is only available on HPE Synergy

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_scope
Manage OneView Scope resources.

#### Synopsis
 Provides an interface to manage scopes. Can create, update, or delete scopes, and modify the scope membership by adding or removing resource assignments.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with the Scopes properties.  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li>  <li>resource_assignments_updated</li> </ul> |  Indicates the desired state for the Scope resource. `present` ensures data properties are compliant with OneView. `absent` removes the resource from OneView, if it exists. `resource_assignments_updated` modifies scope membership by adding or removing resource assignments. This operation is non-idempotent.  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  |



#### Examples

```yaml

- name: Create a scope
  oneview_scope:
    config: '{{ config }}'
    state: present
    data:
      name: 'SampleScope'
  delegate_to: localhost

- name: Update the scope
  oneview_scope:
    config: '{{ config }}'
    state: present
    data:
      name: 'SampleScope'
      newName: 'SampleScopeRenamed'
  delegate_to: localhost

- name: Delete the Scope
  oneview_scope:
    config: '{{ config }}'
    state: absent
    data:
      name: 'SampleScopeRenamed'
  delegate_to: localhost

- name: Update the scope resource assignments, adding two resources
  oneview_scope:
    config: '{{ config }}'
    state: resource_assignments_updated
    data:
      name: 'SampleScopeRenamed'
      resourceAssignments:
        addedResourceUris:
          - '{{ fc_network_1.uri }}'
          - '{{ fc_network_2.uri }}'
  delegate_to: localhost

- name: Update the scope resource assignments, adding one resource and removing another previously added
  oneview_scope:
    config: '{{ config }}'
    state: resource_assignments_updated
    data:
      name: 'SampleScopeRenamed'
      resourceAssignments:
        addedResourceUris:
          - '{{ fc_network_3.uri }}'
        removedResourceUris:
          - '{{ fc_network_1.uri }}'
  delegate_to: localhost

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| scope   | Has the facts about the Scope. |  On state 'present' and 'resource_assignments_updated', but can be null. |  dict |


#### Notes

- This resource is available for API version 300 or later.

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_scope_facts
Retrieve facts about one or more of the OneView Scopes.

#### Synopsis
 Retrieve facts about one or more of the Scopes from OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Name of the scope.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: c(start): The first item to return, using 0-based indexing. c(count): The number of resources to return. c(query): A general query string to narrow the list of resources returned. c(sort): The sort order of the returned data set. c(view): Returns a specific subset of the attributes of the resource or collection, by specifying the name of a predefined view.  |



#### Examples

```yaml

- name: Gather facts about all Scopes
  oneview_scope_facts:
    config: "{{ config_path }}"

- debug: var=scopes

- name: Gather paginated, filtered and sorted facts about Scopes
  oneview_scope_facts:
    config: "{{ config }}"
    params:
      start: 0
      count: 3
      sort: name:ascending
      query: name eq 'SampleScope'
  delegate_to: localhost

- debug: var=scopes

- name: Gather facts about a Scope by name
  oneview_scope_facts:
    config: "{{ config_path }}"
    name: "Name of the Scope"

- debug: var=scopes

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| scopes   | Has all the OneView facts about the Scopes. |  Always, but can be null. |  dict |


#### Notes

- This resource is available for API version 300 or later.

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_server_hardware
Manage OneView Server Hardware resources.

#### Synopsis
 Provides an interface to manage Server Hardware resources.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with Server Hardware properties and its associated states.  |
| state  |   Yes  |  | <ul> <li>present</li>  <li>absent</li>  <li>power_state_set</li>  <li>refresh_state_set</li>  <li>ilo_firmware_version_updated</li>  <li>ilo_state_reset</li>  <li>uid_state_on</li>  <li>uid_state_off</li>  <li>environmental_configuration_set</li>  <li>multiple_servers_added</li> </ul> |  Indicates the desired state for the Server Hardware resource. `present` will ensure data properties are compliant with OneView. `absent` will remove the resource from OneView, if it exists. `power_state_set` will set the power state of the Server Hardware. `refresh_state_set` will set the refresh state of the Server Hardware. `ilo_firmware_version_updated` will update the iLO firmware version of the Server Hardware. `ilo_state_reset` will reset the iLO state. `uid_state_on` will set on the UID state, if necessary. `uid_state_off` will set off the UID state, if necessary. `environmental_configuration_set` will set the environmental configuration of the Server Hardware. `multiple_servers_added` will add multiple rack-mount servers.  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  |



#### Examples

```yaml

- name: Add a Server Hardware
  oneview_server_hardware:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
         hostname : "172.18.6.15"
         username : "username"
         password : "password"
         force : false
         licensingIntent: "OneView"
         configurationState: "Managed"
  delegate_to: localhost

- name: Ensure that the Server Hardware is present and is inserted in the desired scopes
  oneview_server_hardware:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
         name : "172.18.6.15"
         scopeUris:
           - '/rest/scopes/00SC123456'
           - '/rest/scopes/01SC123456'
  delegate_to: localhost

- name: Add multiple rack-mount servers
  oneview_server_hardware:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: multiple_servers_added
    data:
        mpHostsAndRanges :
          - '172.18.6.15'
        username : 'username'
        password : 'password'
        initialScopeUris:
          - "/rest/scopes/01SC123456"
        licensingIntent: "OneView"
        configurationState: "Managed"
  delegate_to: localhost

- name: Power Off the server hardware
  oneview_server_hardware:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: power_state_set
    data:
        name : "172.18.6.15"
        powerStateData:
            powerState: "Off"
            powerControl: "MomentaryPress"
  delegate_to: localhost

- name: Refresh the server hardware
  oneview_server_hardware:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: refresh_state_set
    data:
        name : "172.18.6.15"
        refreshStateData:
            refreshState : "RefreshPending"
  delegate_to: localhost

- name: Update the Server Hardware iLO firmware version
  oneview_server_hardware:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: ilo_firmware_version_updated
    data:
        name : "172.18.6.15"
  delegate_to: localhost

- name: Set the calibrated max power of a server hardware
  oneview_server_hardware:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: environmental_configuration_set
    data:
        name : "172.18.6.15"
        environmentalConfigurationData:
            calibratedMaxPower: 2500
  delegate_to: localhost

- name: Remove the server hardware by its IP
  oneview_server_hardware:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: absent
    data:
        name : "172.18.6.15"
  delegate_to: localhost

- name: Set the server UID state off
  oneview_server_hardware:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: uid_state_off
    data:
        name : '0000A66102, bay 12'
  delegate_to: localhost

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| server_hardware   | Has the OneView facts about the Server Hardware. |  On states 'present', 'power_state_set', 'refresh_state_set', and 'ilo_firmware_version_updated'. Can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_server_hardware_facts
Retrieve facts about the OneView Server Hardware.

#### Synopsis
 Retrieve facts about the Server Hardware from OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Server Hardware name.  |
| uri  |   No  |  | |  Server Hardware uri.  |
| options  |   No  |  | |  List with options to gather additional facts about Server Hardware related resources. Options allowed: `bios`, `javaRemoteConsoleUrl`, `environmentalConfig`, `iloSsoUrl`, `remoteConsoleUrl`, `utilization`, `firmware`, `firmwares` and `physicalServerHardware`.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Server Hardwares
  oneview_server_hardware_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
  delegate_to: localhost

- debug: var=server_hardwares


- name: Gather paginated, filtered and sorted facts about Server Hardware
  oneview_server_hardware_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 0
      count: 3
      sort: name:ascending
      filter: uidState='Off'
  delegate_to: localhost

- debug: msg="{{server_hardwares | map(attribute='name') | list }}"


- name: Gather facts about a Server Hardware by name
  oneview_server_hardware_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "172.18.6.15"
  delegate_to: localhost

- debug: var=server_hardwares

- name: Gather facts about a Server Hardware by uri
  oneview_server_hardware_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    uri: "/rest/server-hardware/30303437-3034-4D32-3230-313030364752"
  delegate_to: localhost

- debug: var=server_hardwares


- name: Gather BIOS facts about a Server Hardware
  oneview_server_hardware_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "Encl1, bay 1"
    options:
      - bios
  delegate_to: localhost

- debug: var=server_hardwares
- debug: var=server_hardware_bios


- name: Gather all facts about a Server Hardware
  oneview_server_hardware_facts:
   hostname: 172.16.101.48
   username: administrator
   password: my_password
   api_version: 2200
   name : "Encl1, bay 1"
   options:
       - bios                   # optional
       - javaRemoteConsoleUrl   # optional
       - physicalServerHardware   # optional
       - environmentalConfig    # optional
       - iloSsoUrl              # optional
       - remoteConsoleUrl       # optional
       - utilization:           # optional
                fields : 'AveragePower'
                filter : ['startDate=2016-05-30T03:29:42.000Z']
                view : 'day'
       - firmware               # optional
  delegate_to: localhost

- debug: var=server_hardwares
- debug: var=server_hardware_bios
- debug: var=server_hardware_env_config
- debug: var=server_hardware_java_remote_console_url
- debug: var=server_hardware_ilo_sso_url
- debug: var=server_hardware_physical_server_hardware
- debug: var=server_hardware_remote_console_url
- debug: var=server_hardware_utilization
- debug: var=server_hardware_firmware

- name: Gather facts about the Server Hardware firmware
  oneview_server_hardware_facts:
   hostname: 172.16.101.48
   username: administrator
   password: my_password
   api_version: 2200
   name : "0000A66102, bay 12"
   options:
       - firmware
  delegate_to: localhost

- debug: var=server_hardware_firmware

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| server_hardware_bios   | Has all the facts about the Server Hardware BIOS. |  When requested, but can be null. |  dict |
| server_hardware_env_config   | Has all the facts about the Server Hardware environmental configuration. |  When requested, but can be null. |  dict |
| server_hardware_firmware   | Has all the facts about the Server Hardware firmware. |  When requested, but can be null. |  dict |
| server_hardware_firmwares   | Has all the facts about the firmwares inventory across all servers. |  When requested, but can be null. |  dict |
| server_hardware_ilo_sso_url   | Has the facts about the Server Hardware iLO SSO url. |  When requested, but can be null. |  dict |
| server_hardware_java_remote_console_url   | Has the facts about the Server Hardware java remote console url. |  When requested, but can be null. |  dict |
| server_hardware_physical_server_hardware   | Has all the facts describing an 'SDX' partition. Used with SDX enclosures only. |  When requested, but can be null. |  dict |
| server_hardware_remote_console_url   | Has the facts about the Server Hardware remote console url. |  When requested, but can be null. |  dict |
| server_hardware_utilization   | Has all the facts about the Server Hardware utilization. |  When requested, but can be null. |  dict |
| server_hardwares   | Has all the OneView facts about the Server Hardware. |  Always, but can be null. |  dict |


#### Notes

- The options `firmware` and `firmwares` are only available for API version 300 or later.

- The option `physicalServerHardware` is only available for API version 500 or later on SDX enclosures.

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_server_hardware_type
Manage OneView Server Hardware Type resources.

#### Synopsis
 Provides an interface to manage Server Hardware Type resources. Can update, and remove.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with Server Hardware Type properties and its associated states.  |
| state  |   Yes  |  | <ul> <li>present</li>  <li>absent</li> </ul> |  Indicates the desired state for the Server Hardware Type resource. `present` will ensure data properties are compliant with OneView. `absent` will remove the resource from OneView, if it exists.  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  |



#### Examples

```yaml

- name: Update the Server Hardware Type description
  oneview_server_hardware_type:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: 'DL380p Gen8 1'
      description: "New Description"
  delegate_to: localhost

- name: Rename the Server Hardware Type
  oneview_server_hardware_type:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: 'DL380p Gen8 1'
      newName: 'DL380p Gen8 1 (new name)'
  delegate_to: localhost

- name: Delete the Server Hardware Type
  oneview_server_hardware_type:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: absent
    data:
      name: 'DL380p Gen8 1 (new name)'
  delegate_to: localhost

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| server_hardware_type   | Has the OneView facts about the Server Hardware Type. |  On state 'present'. Can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_server_hardware_type_facts
Retrieve facts about Server Hardware Types of the OneView.

#### Synopsis
 Retrieve facts about Server Hardware Types of the OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Server Hardware Type name.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Server Hardware Types
  oneview_server_hardware_type_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
  delegate_to: localhost
- debug: var=server_hardware_types

- name: Gather paginated, filtered and sorted facts about Server Hardware Types
  oneview_server_hardware_type_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 0
      count: 5
      sort: name:ascending
      filter: formFactor='HalfHeight'
  delegate_to: localhost
- debug: msg="{{server_hardware_types | map(attribute='name') | list }}"

- name: Gather facts about a Server Hardware Type by name
  oneview_server_hardware_type_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "BL460c Gen8 1"
  delegate_to: localhost
- debug: var=server_hardware_types

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| server_hardware_types   | Has all the OneView facts about the Server Hardware Types. |  Always, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_server_profile
Manage OneView Server Profile resources

#### Synopsis
 Manage the servers lifecycle with OneView Server Profiles. On `present` state, it selects a server hardware automatically based on the server profile configuration if no server hardware was provided.

#### Requirements (on the host that executes the module)
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| auto_assign_server_hardware  |   |  True  | <ul> <li>True</li>  <li>False</li> </ul> |  Bool indicating whether or not a Server Hardware should be automatically retrieved and assigned to the Server Profile. When set to true, creates and updates try to ensure that an available Server Hardware is assigned to the Server Profile. When set to false, if no Server Hardware is specified during creation, the profile is created as 'unassigned'. If the profile already has a Server Hardware assigned to it and a serverHardwareName or serverHardwareUri is specified as None, the Server Profile will have its Server Hardware unassigned.  |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with Server Profile properties.  |
| params  |   No  |  | |  Dict with query parameters.  |
| state  |   |  present  | <ul> <li>present</li>  <li>absent</li>  <li>compliant</li> </ul> |  Indicates the desired state for the Server Profile resource by the end of the playbook execution. `present` will ensure data properties are compliant with OneView. This operation will power off the Server Hardware before configuring the Server Profile. After it completes, the Server Hardware is powered on. `absent` will remove the resource from OneView, if it exists. `compliant` will make the server profile compliant with its server profile template, when this option was specified. If there are Offline updates, the Server Hardware is turned off before remediate compliance issues and turned on after that.  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  |



#### Examples

```yaml

- name: Create a Server Profile from a Server Profile Template with automatically selected hardware
  oneview_server_profile:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
        name: Web-Server-L2
        description: Server Profile created from a selected Server Profile Template
        # You can choose either server_template or serverProfileTemplateUri to inform the Server Profile Template
        # serverProfileTemplateUri: "/rest/server-profile-templates/31ade62c-2112-40a0-935c-2f9450a75198"
        server_template: Compute-node-template
        # You can inform a server_hardware or a serverHardwareUri. If any hardware was informed, it will try
        # get one available automatically
        # server_hardware: Encl1, bay 12
        # serverHardwareUri: /rest/server-hardware/30303437-3933-4753-4831-30335835524E

        # You can choose either serverHardwareTypeUri or serverHardwareTypeName to inform the Server Hardware Type
        # serverHardwareTypeUri: /rest/server-hardware-types/BCAB376E-DA2E-450D-B053-0A9AE7E5114C
        # serverHardwareTypeName: SY 480 Gen9 1
        # You can choose either enclosureGroupName or enclosureGroupUri to inform the EnclosureGroup
        # enclosureGroupUri: /rest/enclosuregroups/EG
        enclosureGroupName: EG
        # You can choose either enclosureName or enclosureUri to inform the Enclosure
        # enclosureUri: /rest/enclosures/09SGH100Z6J1
        enclosureName: 0000A66102
        sanStorage:
          hostOSType: Windows 2012 / WS2012 R2
          manageSanStorage: true
          volumeAttachments:
            - id: 1
              # You can choose either volumeName or volumeUri to inform the Volumes
              # volumeName: DemoVolume001
              volumeUri: /rest/storage-volumes/BCAB376E-DA2E-450D-B053-0A9AE7E5114C
              # You can choose either volumeStoragePoolUri or volumeStoragePoolName to inform the Volume Storage Pool
              # volumeStoragePoolName: FST_CPG2
              volumeStoragePoolUri: /rest/storage-pools/30303437-3933-4753-4831-30335835524E
              # You can choose either volumeStorageSystemUri or volumeStorageSystemName to inform the Volume Storage
              # System
              # volumeStorageSystemName: ThreePAR7200-2127
              volumeStorageSystemUri: /rest/storage-systems/TXQ1000307
              lunType: 'Auto'
              storagePaths:
                - isEnabled: true
                  connectionId: 1
                  storageTargetType: Auto
                - isEnabled: true
                  connectionId: 2
                  storageTargetType: Auto
  delegate_to: localhost
- debug: var=server_profile
- debug: var=serial_number
- debug: var=server_hardware
- debug: var=compliance_preview
- debug: var=created

- name: Create a Server Profile with connections
  oneview_server_profile:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    data:
      name: server-profile-with-connections
      serverHardwareTypeName: "BL460c Gen8 1"
      description: Server Profile with connections created from a selected Server Profile Template
      connectionSettings:
        connections:
          - id: 1
            name: connection1
            functionType: Ethernet
            portId: Auto
            requestedMbps: 2500
            networkName: eth-demo
  delegate_to: localhost

- name: Unassign Server Hardware from Server Profile
  oneview_server_profile:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    # This is required for unassigning a SH, or creating a SP and not auto-assigning a SH
    auto_assign_server_hardware: False
    data:
      name: server-profile-with-sh
      # Specify a blank serverHardwareName or serverHardwareUri when auto_assign_server_hardware is False to unassign a SH
      serverHardwareName:
  delegate_to: localhost

- name : Remediate compliance issues
  oneview_server_profile:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: compliant
    data:
        name: Web-Server-L2
  delegate_to: localhost

- name : Remove the server profile
  oneview_server_profile:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: absent
    data:
        name: Web-Server-L2
  delegate_to: localhost

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| compliance_preview   | Has the OneView facts about the manual and automatic updates required to make the server profile consistent with its template. |  On states 'present' and 'compliant'. |  dict |
| created   | Indicates if the Server Profile was created. |  On states 'present' and 'compliant'. |  bool |
| serial_number   | Has the Server Profile serial number. |  On states 'present' and 'compliant'. |  dict |
| server_hardware   | Has the OneView facts about the Server Hardware. |  On states 'present' and 'compliant'. |  dict |
| server_profile   | Has the OneView facts about the Server Profile. |  On states 'present' and 'compliant'. |  dict |


#### Notes

- For the following data, you can provide either a name or a URI: enclosureGroupName or enclosureGroupUri, osDeploymentPlanName or osDeploymentPlanUri (on the osDeploymentSettings), networkName or networkUri (on the connections list), volumeName or volumeUri (on the volumeAttachments list), volumeStoragePoolName or volumeStoragePoolUri (on the volumeAttachments list), volumeStorageSystemName or volumeStorageSystemUri (on the volumeAttachments list), serverHardwareTypeName or  serverHardwareTypeUri, enclosureName or enclosureUri, firmwareBaselineName or firmwareBaselineUri (on the firmware), sasLogicalJBODName or sasLogicalJBODUri (on the sasLogicalJBODs list) and initialScopeNames or initialScopeUris

- If you define the volumeUri as null in the volumeAttachments list, it will be understood that the volume does not exist, so it will be created along with the server profile. Be warned that every time this option is executed it will always be understood that a new volume needs to be created, so this will not be idempotent. It is strongly recommended to ensure volumes with Ansible and then assign them to the desired server profile. does not exists, so it will be created along with the server profile

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_server_profile_facts
Retrieve facts about the OneView Server Profiles.

#### Synopsis
 Retrieve facts about the Server Profile from OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   |  | |  Server Profile name.  |
| options  |   |  | |  List with options to gather additional facts about Server Profile related resources. Options allowed: `schema`, `compliancePreview`, `profilePorts`, `messages`, `transformation`, `available_networks`, `available_servers`, `available_storage_system`, `available_storage_systems`, `available_targets`, `newProfileTemplate`,  To gather facts about `compliancePreview`, `messages`, `newProfileTemplate` and `transformation` a Server Profile name is required. Otherwise, these options will be ignored.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |
| uri  |   |  | |  Server Profile uri.  |



#### Examples

```yaml

- name: Gather facts about all Server Profiles
  oneview_server_profile_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
  delegate_to: localhost

- debug: var=server_profiles

- name: Gather paginated, filtered and sorted facts about Server Profiles
  oneview_server_profile_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 0
      count: 3
      sort: name:ascending
      filter: macType='Virtual'
  delegate_to: localhost

- debug: var=server_profiles


- name: Gather facts about a Server Profile by name
  oneview_server_profile_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: WebServer-1
  delegate_to: localhost

- debug: var=server_profiles


- name: Gather facts about a Server Profile by uri
  oneview_server_profile_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    uri: /rest/server-profiles/e23d9fa4-f926-4447-b971-90116ca3e61e
  delegate_to: localhost

- debug: var=server_profiles

- name: Gather facts about available servers and bays for a given enclosure group and server hardware type
  oneview_server_profile_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    options:
      - availableTargets:
          enclosureGroupUri: '/rest/enclosure-groups/3af25c76-dec7-4753-83f6-e1ad06c29a43'
          serverHardwareTypeUri: '/rest/server-hardware-types/C8DEF9A6-9586-465E-A951-3070988BC226'
  delegate_to: localhost

- debug: var=server_profile_available_targets


- name: Gather all facts about a Server Profile
  oneview_server_profile_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name : "Encl1, bay 1"
    options:
        - schema
        - compliancePreview
        - newProfileTemplate
        - profilePorts:
           enclosureGroupUri: '/rest/enclosure-groups/3af25c76-dec7-4753-83f6-e1ad06c29a43'
           serverHardwareTypeUri: '/rest/server-hardware-types/C8DEF9A6-9586-465E-A951-3070988BC226'
        - messages
        - transformation:
            enclosureGroupUri: '/rest/enclosure-groups/3af25c76-dec7-4753-83f6-e1ad06c29a43'
            serverHardwareTypeUri: '/rest/server-hardware-types/C8DEF9A6-9586-465E-A951-3070988BC226'
        - availableNetworks:
            enclosureGroupUri: '/rest/enclosure-groups/3af25c76-dec7-4753-83f6-e1ad06c29a43'
            serverHardwareTypeUri: '/rest/server-hardware-types/C8DEF9A6-9586-465E-A951-3070988BC226'
        - availableServers
        - availableStorageSystem:
            storageSystemId: "{{storage_system_id}}"
            enclosureGroupUri: '/rest/enclosure-groups/3af25c76-dec7-4753-83f6-e1ad06c29a43'
            serverHardwareTypeUri: '/rest/server-hardware-types/C8DEF9A6-9586-465E-A951-3070988BC226'
        - availableStorageSystems:
            enclosureGroupUri: '/rest/enclosure-groups/3af25c76-dec7-4753-83f6-e1ad06c29a43'
            serverHardwareTypeUri: '/rest/server-hardware-types/C8DEF9A6-9586-465E-A951-3070988BC226'
        - availableTargets

  delegate_to: localhost

- debug: var=server_profiles
- debug: var=server_profile_schema
- debug: var=server_profile_compliance_preview
- debug: var=server_profile_new_profile_template
- debug: var=server_profile_profile_ports
- debug: var=server_profile_messages
- debug: var=server_profile_transformation
- debug: var=server_profile_available_networks
- debug: var=server_profile_available_servers
- debug: var=server_profile_available_storage_system
- debug: var=server_profile_available_storage_systems
- debug: var=server_profile_available_targets

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| server_profile_available_networks   | Has all the facts about the list of Ethernet networks, Fibre Channel networks and network sets that are available to the server profile along with their respective ports. |  When requested, but can be null. |  dict |
| server_profile_available_servers   | Has the facts about the list of available servers. |  When requested, but can be null. |  dict |
| server_profile_available_storage_system   | Has the facts about a specific storage system and its associated volumes that are available to the server profile. |  When requested, but can be null. |  dict |
| server_profile_available_storage_systems   | Has the facts about the list of the storage systems and their associated volumes that are available to the server profile. |  When requested, but can be null. |  dict |
| server_profile_available_targets   | Has the facts about the target servers and empty device bays that are available for assignment to the server profile. |  When requested, but can be null. |  dict |
| server_profile_compliance_preview   | Has all the facts about the manual and automatic updates required to make the server profile compliant with its template. |  When requested, but can be null. |  dict |
| server_profile_messages   | Has the facts about the profile status messages associated with the profile. |  When requested, but can be null. |  dict |
| server_profile_new_profile_template   | Has the facts derived from a server profile, which can be used to generate a server profile template. |  When requested, but can be null. |  dict |
| server_profile_profile_ports   | Has the facts about the port model associated with the profile. |  When requested, but can be null. |  dict |
| server_profile_schema   | Has the facts about the Server Profile schema. |  When requested, but can be null. |  dict |
| server_profile_transformation   | Has the facts about the transformation of an existing profile by supplying a new server hardware type and/or enclosure group. |  When requested, but can be null. |  dict |
| server_profiles   | Has all the OneView facts about the Server Profiles. |  Always, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_server_profile_template
Manage OneView Server Profile Template resources.

#### Synopsis
 Provides an interface to create, modify, and delete server profile templates.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  Dict with Server Profile Template properties.  |
| params  |   No  |  | |  Dict with query parameters.  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  Indicates the desired state for the Server Profile Template. `present` will ensure data properties are compliant with OneView. `absent` will remove the resource from OneView, if it exists.  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  |



#### Examples

```yaml

- name: Create a basic connection-less server profile template (using URIs)
  oneview_server_profile_template:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: "ProfileTemplate101"
      serverHardwareTypeUri: "/rest/server-hardware-types/94B55683-173F-4B36-8FA6-EC250BA2328B"
      enclosureGroupUri: "/rest/enclosure-groups/ad5e9e88-b858-4935-ba58-017d60a17c89"
    params:
      force: True
    delegate_to: localhost

- name: Create a basic connection-less server profile template (using names)
  oneview_server_profile_template:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: "ProfileTemplate102"
      serverHardwareTypeName: "BL460c Gen8 1"
      enclosureGroupName: "EGSAS_3"
    params:
      force: True
  delegate_to: localhost

- name: Delete the Server Profile Template
  oneview_server_profile_template:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: absent
    data:
      name: "ProfileTemplate101"
    params:
      force: True
    delegate_to: localhost

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| server_profile_template   | Has the OneView facts about the Server Profile Template. |  On state 'present'. Can be null. |  dict |


#### Notes

- For the following data, you can provide either a name  or a URI: enclosureGroupName or enclosureGroupUri, osDeploymentPlanName or osDeploymentPlanUri (on the osDeploymentSettings), networkName or networkUri (on the connections list), volumeName or volumeUri (on the volumeAttachments list), volumeStoragePoolName or volumeStoragePoolUri (on the volumeAttachments list), volumeStorageSystemName or volumeStorageSystemUri (on the volumeAttachments list), serverHardwareTypeName or  serverHardwareTypeUri, enclosureName or enclosureUri, firmwareBaselineName or firmwareBaselineUri (on the firmware), sasLogicalJBODName or sasLogicalJBODUri (on the sasLogicalJBODs list) and initialScopeNames or initialScopeUris

- If you define the volumeUri as null in the volumeAttachments list, it will be understood that the volume does not exist, so it will be created along with the server profile. Be warned that every time this option is executed it will always be understood that a new volume needs to be created, so this will not be idempotent. It is strongly recommended to ensure volumes with Ansible and then assign them to the desired server profile template.

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_server_profile_template_facts
Retrieve facts about the Server Profile Templates from OneView.

#### Synopsis
 Retrieve facts about the Server Profile Templates from OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   |  | |  Server Profile Template name.  |
| options  |   |  | |  List with options to gather additional facts about Server Profile Template resources. Options allowed: `new_profile`, `transformation` and `available_networks`.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |
| uri  |   |  | |  Server Profile Template uri.  |



#### Examples

```yaml

- name: Gather facts about all Server Profile Templates
  oneview_server_profile_template_facts:
    config: "{{ config }}"

- debug: var=server_profile_templates

- name: Gather paginated, filtered and sorted facts about Server Profile Templates
  oneview_server_profile_template_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 0
      count: 3
      sort: name:ascending
      filter: macType='Virtual'
      scope_uris: /rest/scopes/af62ae65-06b2-4aaf-94d3-6a92562888cf
  delegate_to: localhost

- debug: var=server_profile_templates

- name: Gather facts about a Server Profile Template by name
  oneview_server_profile_template_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "ProfileTemplate101"

- name: Gather facts about a Server Profile by uri
  oneview_server_profile_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    uri: /rest/server-profile-templates/c0868397-eff6-49ed-8151-4338702792d3
  delegate_to: localhost

- name: Gather facts about a template and a profile with the configuration based on this template
  oneview_server_profile_template_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "ProfileTemplate101"
    options:
      - new_profile

- name: Gather facts about available networks.
  oneview_server_profile_template_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    options:
      - available_networks:
          serverHardwareTypeUri: "/rest/server-hardware-types/253F1D49-0FEE-4DCD-B14C-B26234E9D414"
          enclosureGroupUri: "/rest/enclosure-groups/293e8efe-c6b1-4783-bf88-2d35a8e49071"
  delegate_to: localhost


```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| new_profile   | A profile object with the configuration based on this template. |  When requested, but can be null. |  dict |
| server_profile_template_available_networks   | Has all the facts about the list of Ethernet networks, Fibre Channel networks and network sets that are available to the server profile along with their respective ports. |  When requested, but can be null. |  dict |
| server_profile_templates   | Has all the OneView facts about the Server Profile Templates. |  Always, but can be null. |  dict |


#### Notes

- The option `transformation` is only available for API version 300 or later.

- The option `available_networks` is only available for API version 600 or later.

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_storage_pool
Manage OneView Storage Pool resources.

#### Synopsis
 Provides an interface to manage Storage Pool resources. Can add and remove.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with Storage Pool properties and its associated states.  |
| state  |   Yes  |  | <ul> <li>present</li>  <li>absent</li> </ul> |  Indicates the desired state for the Storage Pool resource. `present` will ensure data properties are compliant with OneView. From API500 onwards it is only possible to update its state. `absent` will remove the resource from OneView, if it exists. From API500 onwards absent state is immutable.  |



#### Examples

```yaml

- name: Create a Storage Pool (prior to API500)
  oneview_storage_pool:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 300
    state: present
    data:
       storageSystemUri: "/rest/storage-systems/TXQ1010307"
       poolName: "FST_CPG2"
  delegate_to: localhost
- name: Delete the Storage Pool (prior to API500)
  oneview_storage_pool:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 300
    state: absent
    data:
       poolName: "FST_CPG2"
  delegate_to: localhost
- name: Ensure the storage pool 'FST_CPG2' is managed by the appliance (API500 onwards)
  oneview_storage_pool:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
       storageSystemUri: "/rest/storage-systems/TXQ1010307"
       poolName: FST_CPG2
       isManaged: True
  delegate_to: localhost
- name: Ensure the storage pool 'FST_CPG2' is unmanaged (API500 onwards)
  oneview_storage_pool:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
       storageSystemUri: "/rest/storage-systems/TXQ1010307"
       poolName: FST_CPG2
       isManaged: False
  delegate_to: localhost

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| storage_pool   | Has the OneView facts about the Storage Pool. |  On 'present' state, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_storage_pool_facts
Retrieve facts about one or more Storage Pools.

#### Synopsis
 Retrieve facts about one or more of the Storage Pools from OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Storage Pool name.  |
| options  |   No  |  | |  List with options to gather additional facts about Storage Pools. Options allowed: `reachableStoragePools` gets the list of reachable Storage pools based on the network param. If the network param is not specified it gets all of them.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Storage Pools
  oneview_storage_pool_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
  delegate_to: localhost
- debug: var=storage_pools
- name: Gather paginated, filtered and sorted facts about Storage Pools
  oneview_storage_pool_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 0
      count: 3
      sort: 'name:descending'
      filter: status='OK'
- debug: var=storage_pools
- name: Gather facts about a Storage Pool by name
  oneview_storage_pool_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "CPG_FC-AO"
  delegate_to: localhost
- debug: var=storage_pools
- name: Gather facts about the reachable Storage Pools
  oneview_storage_pool_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    options:
        - reachableStoragePools
    params:
        sort: 'name:ascending'
        filter: status='OK'
        networks:
            - /rest/network/123456A
            - /rest/network/123456B
        scope_exclusions:
            - /rest/storage-pools/5F9CA89B-C632-4F09-BC55-A8AA00DA5C4A
        scope_uris: '/rest/scopes/754e0dce-3cbd-4188-8923-edf86f068bf7'
  delegate_to: localhost
- debug: var=storage_pools_reachable_storage_pools

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| storage_pools   | Has all the OneView facts about the Storage Pools. |  Always, but can be null. |  dict |
| storage_pools_reachable_storage_pools   | Has all the OneView facts about the Reachable Storage Pools. |  Always, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_storage_system
Manage OneView Storage System resources.

#### Synopsis
 Provides an interface to manage Storage System resources. Can add, update and remove.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with Storage System properties and its associated states.  |
| state  |   Yes  |  | <ul> <li>present</li>  <li>absent</li> </ul> |  Indicates the desired state for the Storage System resource. `present` will ensure data properties are compliant with OneView. `absent` will remove the resource from OneView, if it exists.  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  |



#### Examples

```yaml

- name: Add a Storage System with one managed pool (before API500)
  oneview_storage_system:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
        credentials:
            ip_hostname: '{{ storage_system_ip_hostname }}'
            username: '{{ storage_system_username }}'
            password: '{{ storage_system_password }}'
        managedDomain: TestDomain
        managedPools:
          - domain: TestDomain
            type: StoragePoolV2
            name: CPG_FC-AO
            deviceType: FC

  delegate_to: localhost

- name: Add a StoreServ Storage System with one managed pool (API500 onwards)
  oneview_storage_system:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      credentials:
          username: '{{ storage_system_username }}'
          password: '{{ storage_system_password }}'
      hostname: '{{ storage_system_ip }}'
      family: StoreServ
      deviceSpecificAttributes:
          managedDomain: TestDomain
          managedPools:
              - domain: TestDomain
                type: StoragePoolV2
                name: CPG_FC-AO
                deviceType: FC

  delegate_to: localhost

- name: Remove the storage system by its IP (before API500)
  oneview_storage_system:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: absent
    data:
        credentials:
            ip_hostname: 172.18.11.12
  delegate_to: localhost

- name: Remove the storage system by its IP (API500 onwards)
  oneview_storage_system:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: absent
    data:
        credentials:
            hostname: 172.18.11.12
  delegate_to: localhost

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| storage_system   | Has the OneView facts about the Storage System. |  On state 'present'. Can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_storage_system_facts
Retrieve facts about the OneView Storage Systems

#### Synopsis
 Retrieve facts about the Storage Systems from OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   |  | |  Storage System name.  |
| options  |   |  | |  List with options to gather additional facts about a Storage System and related resources. Options allowed: `hostTypes` gets the list of supported host types. `storagePools` gets a list of storage pools belonging to the specified storage system. `reachablePorts` gets a list of storage system reachable ports. Accepts `params`. An additional `networks` list param can be used to restrict the search for only these ones. `templates` gets a list of storage templates belonging to the storage system.  To gather facts about `storagePools`, `reachablePorts`, and `templates` it is required to inform either the argument `name`, `ip_hostname`, or `hostname`. Otherwise, this option will be ignored.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |
| storage_hostname  |   |  | |  Storage System IP or hostname.  |



#### Examples

```yaml

- name: Gather facts about all Storage Systems
  oneview_storage_system_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
  delegate_to: localhost

- debug: var=storage_systems

- name: Gather paginated, filtered and sorted facts about Storage Systems
  oneview_storage_system_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 0
      count: 3
      sort: 'name:descending'
      filter: managedDomain=TestDomain

- debug: var=storage_systems

- name: Gather facts about a Storage System by IP (ip_hostname)
  oneview_storage_system_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    ip_hostname: "172.18.11.12"
  delegate_to: localhost

- debug: var=storage_systems

- name: Gather facts about a Storage System by IP (hostname)
  oneview_storage_system_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    hostname: "172.18.11.12"
  delegate_to: localhost

- debug: var=storage_systems


- name: Gather facts about a Storage System by name
  oneview_storage_system_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "ThreePAR7200-4555"
  delegate_to: localhost

- debug: var=storage_systems

- name: Gather facts about a Storage System and all options
  oneview_storage_system_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "ThreePAR7200-4555"
    options:
        - hostTypes
        - storagePools
  delegate_to: localhost

- debug: var=storage_systems
- debug: var=storage_system_host_types
- debug: var=storage_system_pools

- name: Gather queried facts about Storage System reachable ports (API500 onwards)
  oneview_storage_system_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    hostname: "172.18.11.12"
    options:
        - reachablePorts
    params:
      networks:
        - /rest/fc-networks/01FC123456
        - /rest/fc-networks/02FC123456
      sort: 'name:descending'

- debug: var=storage_system_reachable_ports

- name: Gather facts about Storage System storage templates (API500 onwards)
  oneview_storage_system_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    hostname: "172.18.11.12"
    options:
      - templates
    params:
      sort: 'name:descending'

- debug: var=storage_system_templates

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| storage_system_host_types   | Has all the OneView facts about the supported host types. |  When requested, but can be null. |  dict |
| storage_system_pools   | Has all the OneView facts about the Storage Systems - Storage Pools. |  When requested, but can be null. |  dict |
| storage_system_reachable_ports   | Has all the OneView facts about the Storage Systems reachable ports. |  When requested, but can be null. |  dict |
| storage_system_templates   | Has all the OneView facts about the Storage Systems - Storage Templates. |  When requested, but can be null. |  dict |
| storage_systems   | Has all the OneView facts about the Storage Systems. |  Always, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_storage_volume_attachment
Provides an interface to remove extra presentations from a specified server profile.

#### Synopsis
 Provides an interface to remove extra presentations from a specified server profile.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| server_profile  |   Yes  |  | |  Server Profile name or Server Profile URI  |
| state  |   Yes  |  | <ul> <li>extra_presentations_removed</li> </ul> |  Indicates the desired state for the Storage Volume Attachment `extra_presentations_removed` will remove extra presentations from a specified server profile.  |



#### Examples

```yaml

- name: Removes extra presentations from a specified server profile URI
  oneview_storage_volume_attachment:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: extra_presentations_removed
    server_profile: "/rest/server-profiles/e6516410-c873-4644-ab93-d26dba6ccf0d"
  delegate_to: localhost

- debug: var=server_profile


- name: Removes extra presentations from a specified server profile name
  oneview_storage_volume_attachment:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: extra_presentations_removed
    server_profile: "SV-1001"
  delegate_to: localhost

- debug: var=server_profile

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| server_profile   | Has all the OneView facts about the repaired Server Profile. |  Always. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_storage_volume_attachment_facts
Retrieve facts about the OneView Storage Volume Attachments.

#### Synopsis
 Retrieve facts about the OneView Storage Volume Attachments. To gather facts about a specific Storage Volume Attachment it is required to inform the option _storageVolumeAttachmentUri_. It is also possible to retrieve a specific Storage Volume Attachment by the Server Profile and the Volume. For this option, it is required to inform the option _serverProfileName_ and the param _storageVolumeName_ or _storageVolumeUri_.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| options  |   No  |  | |  Retrieve additional facts. Options available: `extraUnmanagedStorageVolumes` retrieve the list of extra unmanaged storage volumes. `paths` retrieve all paths or a specific attachment path for the specified volume attachment. To retrieve a specific path a `pathUri` or a `pathId` must be informed  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |
| serverProfileName  |   No  |  | |  Server Profile name.  |
| storageVolumeAttachmentUri  |   No  |  | |  Storage Volume Attachment uri.  |
| storageVolumeName  |   No  |  | |  Storage Volume name.  |
| storageVolumeUri  |   No  |  | |  Storage Volume uri.  |



#### Examples

```yaml

- name: Gather facts about all Storage Volume Attachments
  oneview_storage_volume_attachment_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
  delegate_to: localhost

- debug: var=storage_volume_attachments

- name: Gather paginated, filtered and sorted facts about Storage Volume Attachments
  oneview_storage_volume_attachment_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 0
      count: 2
      sort: 'name:descending'
      filter: "storageVolumeUri='/rest/storage-volumes/E5B84BC8-75CF-4305-8DB5-7585A2979351'"

- debug: var=storage_volume_attachments

- name: Gather facts about a Storage Volume Attachment by Server Profile and Volume
  oneview_storage_volume_attachment_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    serverProfileName: "sp-web"
    storageVolumeName: "volume-test" # You could inform either the volume name or the volume uri
    # storageVolumeUri: "volume-test"
  delegate_to: localhost

- debug: var=storage_volume_attachments


- name: Gather facts about extra unmanaged storage volumes
  oneview_storage_volume_attachment_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    options:
      - extraUnmanagedStorageVolumes:
            start: 0     # optional
            count: '-1'  # optional
            filter: ''   # optional
            sort: ''     # optional
  delegate_to: localhost

- debug: var=storage_volume_attachments
- debug: var=extra_unmanaged_storage_volumes

- name: Gather facts about all paths for the specified volume attachment
  oneview_storage_volume_attachment_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    serverProfileName: "sp-web"
    storageVolumeUri: "/rest/storage-volumes/12345-AAA-BBBB-CCCC-121212AA"
    options:
      - paths
  delegate_to: localhost

- debug: var=storage_volume_attachments
- debug: var=storage_volume_attachment_paths

- name: Gather facts about a specific attachment path
  oneview_storage_volume_attachment_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    serverProfileName: "sp-web"
    storageVolumeUri: "/rest/storage-volumes/12345-AAA-BBBB-CCCC-121212AA"
    options:
      - paths:
            # You could inform either the path id or the path uri
            pathId: '9DFC8953-15A4-4EA9-AB65-23AB12AB23' # optional
            # pathUri: '/rest/storage-volume-attachments/123-123-123/paths/123-123-123'
  delegate_to: localhost

- debug: var=storage_volume_attachments
- debug: var=storage_volume_attachment_paths

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| extra_unmanaged_storage_volumes   | Has facts about the extra unmanaged storage volumes. |  When requested, but can be null. |  dict |
| storage_volume_attachment_paths   | Has facts about all paths or a specific attachment path for the specified volume attachment. |  When requested, but can be null. |  dict |
| storage_volume_attachments   | Has all the OneView facts about the Storage Volume Attachments. |  Always, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_storage_volume_template
Manage OneView Storage Volume Template resources.

#### Synopsis
 Provides an interface to manage Storage Volume Template resources. Can create, update and delete.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with Storage Volume Template properties and its associated states.  |
| state  |   Yes  |  | <ul> <li>present</li>  <li>absent</li> </ul> |  Indicates the desired state for the Storage Volume Template resource. `present` will ensure data properties are compliant with OneView. `absent` will remove the resource from OneView, if it exists.  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  |



#### Examples

```yaml

- name: Create a Storage Volume Template
  oneview_storage_volume_template:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
        name: "Volume Template Name"
        description: "Example Template"
        rootTemplateUri: "/rest/storage-volume-templates/5dbaf127-053b-4988-82fe-a80800eef1f3"
        properties: {}

  delegate_to: localhost

- name: Delete the Storage Volume Template
  oneview_storage_volume_template:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: absent
    data:
        name: 'Volume Template Name'
  delegate_to: localhost

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| storage_volume_template   | Has the OneView facts about the Storage Volume Template. |  On 'present' state, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_storage_volume_template_facts
Retrieve facts about Storage Volume Templates of the OneView.

#### Synopsis
 Retrieve facts about Storage Volume Templates of the OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Storage Volume Template name.  |
| options  |   No  |  | |  Retrieve additional facts. Options available: `connectableVolumeTemplates`, `reachableVolumeTemplates`, `compatibleSystems`  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Storage Volume Templates
  oneview_storage_volume_template_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
  delegate_to: localhost

- debug: var=storage_volume_templates

- name: Gather paginated, filtered and sorted facts about Storage Volume Templates
  oneview_storage_volume_template_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 0
      count: 3
      sort: 'name:descending'
      filter: status='OK'

- debug: var=storage_volume_templates

- name: Gather facts about a Storage Volume Template by name
  oneview_storage_volume_template_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "FusionTemplateExample"
  delegate_to: localhost

- debug: var=storage_volume_templates

- name: Gather facts about the connectable Storage Volume Templates
  oneview_storage_volume_template_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "FusionTemplateExample"
    options:
      - connectableVolumeTemplates
  delegate_to: localhost

- debug: var=storage_volume_templates
- debug: var=connectable_volume_templates

- name: Gather facts about the reachable Storage Volume Templates
  oneview_storage_volume_template_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    options:
      - reachableVolumeTemplates
  delegate_to: localhost

- name: Gather facts about Storage Systems compatible to the SVT
  oneview_storage_volume_template_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "{{ volume_template_name }}"
    options:
      - compatibleSystems
  delegate_to: localhost

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| compatible_systems   | Has facts about Storage Systems compatible to the Storage Volume template. API version 500+ only. |  When requested, but can be null. |  dict |
| connectable_volume_templates   | Has facts about the Connectable Storage Volume Templates. API version <= 300  only. |  When requested, but can be null. |  dict |
| reachable_volume_templates   | Has facts about the Reachable Storage Volume Templates. API version 500+ only. |  When requested, but can be null. |  dict |
| storage_volume_templates   | Has all the OneView facts about the Storage Volume Templates. |  Always, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_switch
Provides an interface to remove ToR Switch resources.

#### Synopsis
 Provides an interface to remove Top of Rack(ToR) Switch resources. The switch resource will be removed if it is in an unmanaged state. If the switch resource is associated with a Logical Switch, its removal is treated as a hardware removal only. A reference to the switch is mantained, and the resource is marked as 'Absent'.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   Yes  |  | |  Switch name.  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li>  <li>ports_updated</li> </ul> |  Indicates the desired state for the Switch resource. `present` will update the switch scopes, if they differ from what is declared. `absent` will remove the resource from OneView, if it exists. `ports_updated` will update the switch ports.  |



#### Examples

```yaml

- name: Delete the Switch
  oneview_switch:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: absent
    name: "172.18.16.2"

```



#### Notes

- This resource is only available on C7000 enclosures

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_switch_facts
Retrieve facts about the OneView Switches.

#### Synopsis
 Retrieve facts about the OneView Switches.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Switch name.  |
| options  |   No  |  | |  List with options to gather additional facts about the Switch. Options allowed: `environmentalConfiguration` gets the environmental configuration for a switch.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all switches
  oneview_switch_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200

- name: Gather paginated facts about switches
  oneview_switch_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 0
      count: 3

- debug: var=switches

- name: Gather facts about the switch that matches the specified switch name
  oneview_switch_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "172.18.20.1"

- name: Gather facts about the environmental configuration for the switch that matches the specified switch name
  oneview_switch_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "172.18.20.1"
  options:
    - environmentalConfiguration

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| switch_environmental_configuration   | The environmental configuration for a switch. |  When requested, but can be null. |  dict |
| switches   | The list of switches. |  Always, but can be null. |  list |


#### Notes

- This resource is only available on C7000 enclosures

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_switch_type_facts
Retrieve facts about the OneView Switch Types.

#### Synopsis
 Retrieve facts about the Switch Types from OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Name of the Switch Type.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Switch Types
  oneview_switch_type_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200

- debug: var=switch_types

- name: Gather paginated, filtered and sorted facts about Switch Types
  oneview_switch_type_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 0
      count: 2
      sort: 'name:descending'
      filter: "partNumber='N5K-C56XX'"

- debug: var=switch_types

- name: Gather facts about a Switch Type by name
  oneview_switch_type_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "Name of the Switch Type"

- debug: var=switch_types

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| switch_types   | Has all the OneView facts about the Switch Types. |  Always, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_task_facts
Retrieve facts about the OneView Tasks.

#### Synopsis
 Retrieve facts about the OneView Tasks.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| params  |   No  |  | |  List with parameters to help filter the tasks. Params allowed: `count`, `fields`, `filter`, `query`, `sort`, `start`, `topCount`, `childLimit` and `view`.  |



#### Examples

```yaml

- name: Gather facts about the last 2 tasks
  oneview_task_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      count: 2

- debug: var=tasks

- name: Gather facts about the last 2 tasks associated to Server Profile templates
  oneview_task_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      count: 2
      filter: "associatedResource.resourceCategory='server-profile-templates'"

- debug: var=tasks

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| tasks   | The list of tasks. |  Always, but can be null. |  list |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_unmanaged_device
Manage OneView Unmanaged Device resources.

#### Synopsis
 Provides an interface to manage Unmanaged Device resources. Can create, update, or delete.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with Unmanaged Device properties.  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  Indicates the desired state for the Unmanaged Device resource. `present` will ensure data properties are compliant with OneView. `absent` will remove the resource from OneView, if it exists.  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  |



#### Examples

```yaml

- name: Ensure that the unmanaged device is present
  oneview_unmanaged_device:
    config: "{{ config }}"
    state: present
    data:
      name: 'MyUnmanagedDevice'
      model: 'Procurve 4200VL'
      deviceType: 'Server'
    delegate_to: localhost

- debug: var=unmanaged_device

- name: Add another unmanaged device
  oneview_unmanaged_device:
    config: "{{ config }}"
    state: present
    data:
      name: 'AnotherUnmanagedDevice'
      model: 'Procurve 4200VL'
    delegate_to: localhost

- name: Update the unmanaged device changing the name attribute
  oneview_unmanaged_device:
    config: "{{ config }}"
    state: present
    data:
      name: 'MyUnmanagedDevice'
      newName: 'UnmanagedDeviceRenamed'
    delegate_to: localhost

- debug: var=unmanaged_device

- name: Ensure that the unmanaged device is absent
  oneview_unmanaged_device:
    config: "{{ config }}"
    state: absent
    data:
      name: 'UnmanagedDeviceRenamed'
    delegate_to: localhost

- name: Delete all the unmanaged devices
  oneview_unmanaged_device:
    config: "{{ config }}"
    state: absent
    data:
      filter: "name matches '%'"
    delegate_to: localhost

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| unmanaged_device   | Has the OneView facts about the Unmanaged Device. |  On state 'present'. Can be null. |  dict |


#### Notes

- To rename an Unmanaged Device you must inform a `newName` in the data argument. The rename is non-idempotent

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_unmanaged_device_facts
Retrieve facts about one or more of the OneView Unmanaged Device.

#### Synopsis
 Retrieve facts about one or more of the Unmanaged Device from OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Unmanaged Device name.  |
| options  |   |  | |  List with options to gather additional facts about the Unmanaged Device. Options allowed: `environmental_configuration` gets a description of the environmental configuration for the Unmanaged Device.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Unmanaged Devices
  oneview_unmanaged_device_facts:
    config: "{{ config }}"

- debug: var=unmanaged_devices

- name: Gather paginated, filtered and sorted facts about Unmanaged Devices
  oneview_unmanaged_device_facts:
  config: "{{ config }}"
  params:
    start: 0
    count: 2
    sort: 'name:descending'
    filter: "status='Disabled'"

- debug: var=unmanaged_devices

- name: Gather facts about an Unmanaged Device by name
  oneview_unmanaged_device_facts:
    config: "{{ config }}"
    name: "{{ name }}"

- debug: var=unmanaged_devices

- name: Gather facts about an Unmanaged Device by name with environmental configuration
  oneview_unmanaged_device_facts:
    config: "{{ config }}"
    name: "{{ name }}"
    options:
      - environmental_configuration

- debug: var=unmanaged_device_environmental_configuration

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| unmanaged_device_environmental_configuration   | The description of the environmental configuration for the logical interconnect. |  When requested, but can be null. |  dict |
| unmanaged_devices   | The list of unmanaged devices. |  Always, but can be null. |  list |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_uplink_set
Manage OneView Uplink Set resources.

#### Synopsis
 Provides an interface to manage Uplink Set resources. Can create, update, or delete.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with Uplink Set properties.  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  Indicates the desired state for the Uplink Set resource. `present` will ensure data properties are compliant with OneView. `absent` will remove the resource from OneView, if it exists. The key used to find the resource to perform the operation is a compound key, that consists of the name of the uplink set and the URI (or name) of the Logical Interconnect combined. You can choose to set the Logical Interconnect by logicalInterconnectUri or logicalInterconnectName.  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  |



#### Examples

```yaml

- name: Ensure that the Uplink Set is present
  oneview_uplink_set:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: 'Test Uplink Set'
      status: "OK"
      # You can choose set the Logical Interconnect by logicalInterconnectUri or logicalInterconnectName
      logicalInterconnectName: "Name of the Logical Interconnect"                                   # option 1
      # logicalInterconnectUri: "/rest/logical-interconnects/461a9cef-beef-4916-8be1-926078ffb948"  # option 2
      networkUris: [
         '/rest/ethernet-networks/9e8472ad-5ad1-4cbd-aab1-566b67ffc6a4',
         '/rest/ethernet-networks/28ea7c1a-4930-4432-854b-30cf239226a2'
      ]
      fcNetworkUris: []
      fcoeNetworkUris: []
      portConfigInfos: []
      connectionMode: "Auto"
      networkType: "Ethernet"
      manualLoginRedistributionState: "NotSupported"

- name: Rename the Uplink Set from 'Test Uplink Set' to 'Renamed Uplink Set'
  oneview_uplink_set:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: 'Test Uplink Set'
      newName: 'Renamed Uplink Set'
      logicalInterconnectName: "Name of the Logical Interconnect"

- name: Ensure that the Uplink Set is absent
  oneview_uplink_set:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: absent
    data:
      name: 'Test Uplink Set'
      logicalInterconnectName: "Name of the Logical Interconnect"

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| uplink_set   | Has the OneView facts about the Uplink Set. |  On state 'present'. Can be null. |  dict |


#### Notes

- To rename an uplink set you must inform a `newName` in the data argument. The rename is non-idempotent

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_uplink_set_facts
Retrieve facts about one or more of the OneView Uplink Sets.

#### Synopsis
 Retrieve facts about one or more of the Uplink Sets from OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Uplink Set name.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Uplink Sets
  oneview_uplink_set_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200

- debug: var=uplink_sets

- name: Gather paginated, filtered and sorted facts about Uplink Sets
  oneview_uplink_set_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 0
      count: 2
      sort: 'name:descending'
      filter: "logicalInterconnectUri='/rest/logical-interconnects/4a49ca0d-3782-4c11-b93e-79d8f90c5487'"

- debug: var=uplink_sets

- name: Gather facts about a Uplink Set by name
  oneview_uplink_set_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: logical lnterconnect group name

- debug: var=uplink_sets

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| uplink_sets   | Has all the OneView facts about the Uplink Sets. |  Always, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_user
Manage OneView Users.

#### Synopsis
 Provides an interface to manage Users. Can create, update, and delete.

#### Requirements (on the host that executes the module)
  * python >= 3.4.2
  * hpeOneView >= 6.1.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  List with the User properties.  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> <li>set_password</li> <li>add_role_to_username</li> <li>update_role_to_username</li> <li>remove_role_from_username</li> <li>add_multiple_users</li> <li>delete_multiple_users</li> <li>validate_user_name</li> <li>validate_full_name</li> </ul> |  Indicates the desired state for the User. `present` will ensure data properties are compliant with OneView. `absent` will remove the resource from OneView, if it exists. `set_password` will changes the default administrator's password during first-time appliance setup only. `add_role_to_username` will add a given set of roles to an existing user. `update_role_to_username` will replaces a user's roles with a specified set. `remove_role_from_username` will removes a set of roles that are unrestricted by scope from a user. `add_multiple_users` will adds multiple new local users to the appliance and one must have the user create permissions. `delete_multiple_users` will removes multiple users based on query criteria. `validate_username` will validates the existence of a user with the given user name in the appliance. `validate_fullname` will checks for the existence of a user with the specified full name in the appliance. |



#### Examples

```yaml

- name: Gather facts about all Scopes
  oneview_scope_facts:
    config: "{{ config }}"
  delegate_to: localhost

- name: Create a User
  oneview_user:
    config: "{{ config }}"
    state: present
    data:
      userName: "{{ user_name }}"
      password: "myPass1234"
      emailAddress: "{{ email }}"
      enabled: true
      fullName: "testUser101"
      mobilePhone: '555-2121'
      officePhone: '555-1212'
      permissions:
        - roleName: "Read only"
          scopeUri: "/rest/scopes/6cf6d4da-1b5e-4322-9dff-6ef545ad700f"
        - roleName: "Infrastructure administrator"
          scopeUri: "/rest/scopes/c7cab507-b49a-422d-9765-aff784112092"
  delegate_to: localhost
  register: user_1

- name: Do nothing with the User when no changes are provided
  oneview_user:
    config: "{{ config }}"
    state: present
    data:
      userName: "{{ user_name }}"
      emailAddress: "{{ email }}"
      enabled: true
      fullName: "testUser101"
      mobilePhone: '555-2121'
      officePhone: '555-1212'
      permissions:
        - roleName: "Read only"
          scopeUri: "/rest/scopes/6cf6d4da-1b5e-4322-9dff-6ef545ad700f"
        - roleName: "Infrastructure administrator"
          scopeUri: "/rest/scopes/c7cab507-b49a-422d-9765-aff784112092"
  delegate_to: localhost
  register: user_1

- name: Update the User changing the attribute enabled to False
  oneview_user:
    config: "{{ config }}"
    state: present
    data:
      userName: "{{ user_name }}"
      enabled: false
  delegate_to: localhost

- name: Adds multiple new local users to the appliance
  oneview_user:
    config: "{{ config }}"
    state: add_multiple_users
    data:
      users_list:
        - userName: "{{ user_name }}1"
          password: "myPass1234"
          emailAddress: "{{ email }}"
          enabled: true
          fullName: "testUser101"
          mobilePhone: '555-2121'
          officePhone: '555-1212'
          permissions:
            - roleName: "Read only"
            - roleName: "Infrastructure administrator"
        - userName: "{{ user_name }}2"
          password: "myPass1234"
          emailAddress: "{{ email }}"
          enabled: true
          fullName: "testUser101"
          mobilePhone: '555-2121'
          officePhone: '555-1212'
          permissions:
            - roleName: "Read only"
            - roleName: "Infrastructure administrator"
  delegate_to: localhost
- debug: var=user

- name: Validates the existence of a user with the given user name
  oneview_user:
    config: "{{ config }}"
    state: validate_user_name
    data:
      userName: "testUser"
  delegate_to: localhost
- debug: var=user

- name: Checks for the existence of a user with the specified full name
  oneview_user:
    config: "{{ config }}"
    state: validate_full_name
    data:
      fullName: "testUser101"
  delegate_to: localhost
- debug: var=user

- name: Add role to existing username
  oneview_user:
    config: "{{ config }}"
    state: add_role_to_username
    data:
      userName: "testUser"
      role_list:
        - roleName: "Backup administrator"
        - roleName: "Scope administrator"
  delegate_to: localhost
- debug: var=user

- name: Update role to existing username
  oneview_user:
    config: "{{ config }}"
    state: update_role_to_username
    data:
      userName: "testUser"
      role_list:
        - roleName: "Infrastructure administrator"
        - roleName: "Read only"
  delegate_to: localhost
- debug: var=user

- name: remove role from existing username
  oneview_user:
    config: "{{ config }}"
    state: remove_role_from_username
    data:
      userName: "testUser"
      roleName: "Read only"
  delegate_to: localhost
- debug: var=user

- name: Delete single user
  oneview_user:
    config: "{{ config }}"
    state: absent
    data:
      userName: "testUser"
  delegate_to: localhost
- debug: var=user

- name: Delete multiple users
  oneview_user:
    config: "{{ config }}"
    state: delete_multiple_users
    data:
      users_list:
        - "testUser1"
        - "testUser2"
  delegate_to: localhost
- debug: var=user

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| user   | Has the facts about the OneView Users. |  Always. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_user_facts
Retrieve the facts about one or more of the OneView Users.

#### Synopsis
 Retrieve the facts about one or more of the Users from OneView.

#### Requirements (on the host that executes the module)
  * python >= 3.4.2
  * hpeOneView >= 6.1.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| userName  |   No  |  | |  User name.  |
| role  |   No  |  | |  role name.  |
| options | No  |  |  getUserRoles | Options to get role associated with username. 
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Users
  oneview_user_facts:
    config: "{{ config }}"

- debug: var=users

- name: Gather paginated, filtered and sorted facts about Users
  oneview_user_facts:
    config: "{{ config }}"
    params:
      start: 1
      count: 3
      sort: 'emailAddress:descending'
      filter: 'enabled=true'

- debug: var=users

- name: Gather facts about a User by name
  oneview_user_facts:
    config: "{{ config }}"
    name: "testUser"

- debug: var=users

- name: Gather facts about the users who have permissions that use a specified role
  oneview_user_facts:
    config: "{{ config }}"
    role: "{{ role }}"
  delegate_to: localhost

- debug: var=role

- name: Gather facts about lists of user's roles
  oneview_user_facts:
    config: "{{ config }}"
    userName: "testUser"
    options:
        - getUserRoles
  delegate_to: localhost

- debug: var=users
- debug: var=user_roles

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| users   | It has all the OneView facts about the Users. |  Always, but can be null. |  dict |
| user_roles | It has all the role's associated with Users. | Always. | list |
| role   | It has all the Users with specified role. | Always. but can be null. | list | 


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_version_facts
Returns the range of possible API versions supported by the appliance

#### Synopsis
 Provides an interface to return the range of possible API versions supported by the appliance.

#### Requirements (on the host that executes the module)
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about current and minimum Version
  oneview_version_facts:
    config: "{{ config_file_path }}"

- debug: var=version

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| version   | Has the facts about the OneView current and minimum version. |  When requested, but can not be null |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_volume
Manage OneView Volume resources.

#### Synopsis
 Provides an interface to manage Volume resources. It allows create, update, delete or repair the volume, and create or delete a snapshot.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| data  |   Yes  |  | |  Volume or snapshot data.  |
| export_only  |   |  False  | |  If set to True, when the status is `absent` and the resource exists, it will be removed only from OneView.  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li>  <li>repaired</li>  <li>snapshot_created</li>  <li>snapshot_deleted</li> </ul> |  Indicates the desired state for the Volume resource. `present` creates/adds the resource when it does not exist, otherwise it updates the resource. When the resource already exists, the update operation is non-convergent, since it is always called even though the given options are compliant with the existent data. To change the name of the volume, a `newName` in the _data_ must be provided. `absent` by default deletes a volume from OneView and the storage system. When export_only is True, the volume is removed only from OneView. `repaired` removes extra presentations from a specified volume on the storage system. This operation is non-idempotent. `snapshot_created` creates a snapshot for the volume specified. This operation is non-idempotent. `snapshot_deleted` deletes a snapshot from OneView and the storage system.  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  |



#### Examples

```yaml

- name: Create a Volume with a specified Storage Pool
  oneview_volume:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      properties:
        name: 'Volume with Storage Pool'
        description: 'Test volume with common creation: Storage Pool'
        size: 2147483648  # 2GB
        storagePool: '{{ storage_pool_uri }}'
      templateUri: '/rest/storage-volume-templates/e2f95f1d-de9d-406e-803f-a8aa00da92b0'
      isPermanent: false
      initialScopeUris: ['/rest/scopes/754e0dce-3cbd-4188-8923-edf86f068bf7']
  delegate_to: localhost

- name: Create a volume with a specified Snapshot Pool
  oneview_volume:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      properties:
        name: 'Volume with Snapshot Pool'
        description: 'Test volume with common creation: Storage System + Storage Pool + Snapshot Pool'
        size: 1073741824  # 1GB
        storagePool: '{{ storage_pool_uri }}'
        snapshotPool: '{{ storage_pool_uri }}'
      templateUri: '/rest/storage-volume-templates/e2f95f1d-de9d-406e-803f-a8aa00da92b0'
      isPermanent: false
      initialScopeUris: ['/rest/scopes/754e0dce-3cbd-4188-8923-edf86f068bf7']
  delegate_to: localhost

- name: Add a volume for management by the appliance using the WWN of the volume
  oneview_volume:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 300
    state: present
    data:
      type: AddStorageVolumeV2
      name: 'Volume added with a specific WWN'
      description: 'Test volume added for management: Storage System + Storage Pool + WWN'
      storageSystemUri: '/rest/storage-systems/TXQ1000307'
      wwn: 'DC:32:13:72:47:00:10:00:30:71:47:16:33:58:47:95'
      provisioningParameters:
          shareable: True
  when: wwn is defined

- name: Update the name of the volume to 'Volume with Storage Pool - Renamed' and shareable to false
  oneview_volume:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: 'Volume with Storage Pool'
      newName: 'Volume with Storage Pool - Renamed'
      isShareable: False
    delegate_to: localhost

- name: Remove extra presentations from the specified volume on the storage system
  oneview_volume:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: repaired
    data:
      name: 'Volume with Storage Pool - Renamed'

- name: Create a new snapshot for the specified volume
  oneview_volume:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: snapshot_created
    data:
      name: 'Volume with Snapshot Pool'
      snapshotParameters:
        name: 'test_snapshot'
        description: 'New snapshot'

- name: Delete the snapshot
  oneview_volume:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: snapshot_deleted
    data:
      name: 'Volume with Snapshot Pool'
      snapshotParameters:
        name: 'test_snapshot'

- name: Delete the volume previously created with a Storage Pool
  oneview_volume:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: absent
    data:
      name: 'Volume with Storage Pool - Renamed'

- name: Delete the volume previously created with a Snapshot Pool
  oneview_volume:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: absent
    data:
      name: 'Volume with Snapshot Pool - Renamed'

- name: Delete the volume previously added using the WWN of the volume
  oneview_volume:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: absent
    data:
      name: 'Volume added with a specific WWN'
    export_only: True

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| storage_volume   | Has the facts about the Storage Volume. |  On state 'present', but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_volume_facts
Retrieve facts about the OneView Volumes.

#### Synopsis
 Retrieve facts about the Volumes from OneView.

#### Requirements (on the host that executes the module)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### Options

| Parameter     | Required    | Default  | Choices    | Comments |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional. If the file path is not provided, the configuration will be loaded from environment variables.  |
| name  |   No  |  | |  Volume name.  |
| options  |   No  |  | |  List with options to gather additional facts about Volume and related resources. Options allowed: - `attachableVolumes` - `extraManagedVolumePaths` - `snapshots`. For this option, you may provide a name.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `filter`: A general filter/query string to narrow the list of items returned. `sort`: The sort order of the returned data set.  |



#### Examples

```yaml

- name: Gather facts about all Volumes
  oneview_volume_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
- debug: var=storage_volumes

- name: Gather paginated, filtered and sorted facts about Volumes
  oneview_volume_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    params:
      start: 0
      count: 2
      sort: 'name:descending'
      filter: "provisionType='Thin'"
- debug: var=storage_volumes

- name: "Gather facts about all Volumes, the attachable volumes managed by the appliance and the extra managed
         storage volume paths"
  oneview_volume_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    options:
        - attachableVolumes        # optional
        - extraManagedVolumePaths  # optional
- debug: var=storage_volumes
- debug: var=attachable_volumes
- debug: var=extra_managed_volume_paths


- name: Gather facts about a Volume by name with a list of all snapshots taken
  oneview_volume_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "{{ volume_name }}"
    options:
        - snapshots  # optional
- debug: var=storage_volumes
- debug: var=snapshots


- name: "Gather facts about a Volume with one specific snapshot taken"
  oneview_volume_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    name: "{{ volume_name }}"
    options:
       - snapshots:  # optional
           name: "{{ snapshot_name }}"
- debug: var=storage_volumes
- debug: var=snapshots

```



#### Return Values

| Name          | Description  | Returned | Type       |
| ------------- |-------------| ---------|----------- |
| attachable_volumes   | Has all the facts about the attachable volumes managed by the appliance. |  When requested, but can be null. |  dict |
| extra_managed_volume_paths   | Has all the facts about the extra managed storage volume paths from the appliance. |  When requested, but can be null. |  dict |
| storage_volumes   | Has all the OneView facts about the Volumes. |  Always, but can be null. |  dict |


#### Notes

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


