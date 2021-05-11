[English](oneview-ansible.md)
# Ansible HPE OneViewモジュール
### モジュール

  * [hpe_icsp_os_deployment - HPE ICspを使用してサーバーにオペレーティングシステムを展開します。](#hpe_icsp_os_deployment)
  * [hpe_icsp_server - ICspでサーバーを追加、削除、構成します。](#hpe_icsp_server)
  * [image_streamer_artifact_bundle - アーティファクトバンドルリソースを管理します。](#image_streamer_artifact_bundle)
  * [image_streamer_artifact_bundle_facts - アーティファクトバンドルに関する情報を取得します。](#image_streamer_artifact_bundle_facts)
  * [image_streamer_build_plan - Image Stream OSビルド計画リソースを管理します。](#image_streamer_build_plan)
  * [image_streamer_build_plan_facts - 1つまたはそれ以上のイメージストリーマービルド計画に関する情報を取得します。](#image_streamer_build_plan_facts)
  * [image_streamer_deployment_group_facts - イメージストリーマー展開グループに関する情報を取します。](#image_streamer_deployment_group_facts)
  * [image_streamer_deployment_plan - イメージストリーマー展開計画リソースを管理します。](#image_streamer_deployment_plan)
  * [image_streamer_deployment_plan_facts - イメージストリーマー展開計画に関する情報を取得します。](#image_streamer_deployment_plan_facts)
  * [image_streamer_golden_image - イメージストリーマーゴールデンイメージリソースを管理します。](#image_streamer_golden_image)
  * [image_streamer_golden_image_facts - イメージストリーマーゴールデンイメージの1つまたはそれ以上に関する情報を取得します。](#image_streamer_golden_image_facts)
  * [image_streamer_os_volume_facts - イメージストリーマーOSボリュームに関する情報を取得します。](#image_streamer_os_volume_facts)
  * [image_streamer_plan_script - イメージストリーマー計画スクリプトリソースを管理します。](#image_streamer_plan_script)
  * [image_streamer_plan_script_facts - イメージストリーマー計画スクリプトに関する情報を取得します。](#image_streamer_plan_script_facts)
  * [oneview_alert_facts - OneViewアラートに関する情報を取得します。](#oneview_alert_facts)
  * [oneview_appliance_configuration_timeconfig_facts - OneViewでサポートされるローケル情報を取得します。](#oneview_appliance_configuration_timeconfig_facts)
  * [oneview_appliance_device_read_community - アプライアンスデバイス読み取りコミュニティストリングを管理します。](#oneview_appliance_device_read_community)
  * [oneview_appliance_device_read_community_facts - アプライアンスデバイス読み取りコミュニティストリングを管理します。](#oneview_appliance_device_read_community_facts)
  * [oneview_appliance_device_snmp_v1_trap_destinations - アプライアンスデバイスのSNMPv1トラップ送信先を管理します。](#oneview_appliance_device_snmp_v1_trap_destinations)
  * [oneview_appliance_device_snmp_v1_trap_destinations_facts - OneViewアプライアンスのSNMPv1トラップ転送先に関する情報を取得します。](#oneview_appliance_device_snmp_v1_trap_destinations_facts)
  * [oneview_appliance_device_snmp_v3_trap_destinations - アプライアンスデバイスのSNMPv3トラップ送信先を管理します。](#oneview_appliance_device_snmp_v3_trap_destinations)
  * [oneview_appliance_device_snmp_v3_trap_destinations_facts - OneViewアプライアンスのSNMPv3トラップ転送先に関する情報を取得します。](#oneview_appliance_device_snmp_v3_trap_destinations_facts)
  * [oneview_appliance_device_snmp_v3_users - アプライアンスデバイスSNMPv3ユーザーを管理します。](#oneview_appliance_device_snmp_v3_users)
  * [oneview_appliance_device_snmp_v3_users_facts - OneViewアプライアンスのSNMPv3ユーザーに関する情報を取得します。](#oneview_appliance_device_snmp_v3_users_facts)
  * [oneview_appliance_ssh_access - OneViewアプライアンスのSSHアクセス設定を管理します。](#oneview_appliance_ssh_access)
  * [oneview_appliance_ssh_access_facts - OneViewアプライアンスのSSHアクセス設定情報を取得します。](#oneview_appliance_ssh_access_facts)
  * [oneview_appliance_time_and_locale_configuration - OneViewアプライアンスの場所と時間構成を管理します。](#oneview_appliance_time_and_locale_configuration)
  * [oneview_appliance_time_and_locale_configuration_facts - OneViewアプライアンスの時間とロケール構成に関する情報を取得します。](#oneview_appliance_time_and_locale_configuration_facts)
  * [oneview_certificates_server - OneView証明書サーバーを管理します。](#oneview_certificates_server)
  * [oneview_certificates_server_facts - OneView証明書サーバー情報を取得します。](#oneview_certificates_server_facts)
  * [oneview_connection_template - OneView接続テンプレートリソースを管理します。](#oneview_connection_template)
  * [oneview_connection_template_facts - OneView接続テンプレートに関する情報を取得します。](#oneview_connection_template_facts)
  * [oneview_datacenter - OneViewデータセンターリソースを管理します。](#oneview_datacenter)
  * [oneview_datacenter_facts - OneViewデータセンターに関する情報を取得します。](#oneview_datacenter_facts)
  * [oneview_drive_enclosure - OneViewドライブエンクロージャーリソースを管理します。](#oneview_drive_enclosure)
  * [oneview_drive_enclosure_facts - 1つ以上のOneViewドライブエンクロージャーに関する情報を取得します。](#oneview_drive_enclosure_facts)
  * [oneview_enclosure - OneViewエンクロージャーリソースを管理します。](#oneview_enclosure)
  * [oneview_enclosure_facts - 1つ以上のエンクロージャーに関する情報を取得します。](#oneview_enclosure_facts)
  * [oneview_enclosure_group - OneViewエンクロージャーグループリソースを管理します。](#oneview_enclosure_group)
  * [oneview_enclosure_group_facts - 1つ以上のOneViewエンクロージャーグループに関する情報を取得します。](#oneview_enclosure_group_facts)
  * [oneview_ethernet_network - OneView Ethernet Networkリソースを管理します。](#oneview_ethernet_network)
  * [oneview_ethernet_network_facts - 1つ以上のOneViewイーサネットネットワークに関する情報を取得します。](#oneview_ethernet_network_facts)
  * [oneview_event - OneViewイベントを管理します。](#oneview_event)
  * [oneview_event_facts - 1つ以上のOneViewイベントに関する情報を取得します。](#oneview_event_facts)
  * [oneview_fabric - OneView Fabricリソースを管理します。](#oneview_fabric)
  * [oneview_fabric_facts - 1つ以上のOneViewファブリックに関する情報を取得します。](#oneview_fabric_facts)
  * [oneview_fc_network - 1つ以上のOneViewファブリックに関する情報を取得します。](#oneview_fc_network)
  * [oneview_fc_network_facts - 1つ以上のOneViewファイバーチャネルネットワークに関する情報を取得します。](#oneview_fc_network_facts)
  * [oneview_fcoe_network - OneView FCoEネットワークリソースを管理します。](#oneview_fcoe_network)
  * [oneview_fcoe_network_facts - 1つ以上のOneView FCoEネットワークに関する情報を取得します。](#oneview_fcoe_network_facts)
  * [oneview_firmware_bundle - OneViewファームウェアバンドルリソースをアップロードします。](#oneview_firmware_bundle)
  * [oneview_firmware_driver - ファームウェアドライバーリソースを削除するためのインターフェイスを提供します。](#oneview_firmware_driver)
  * [oneview_firmware_driver_facts - 1つ以上のOneViewファームウェアドライバーに関する情報を取得します。](#oneview_firmware_driver_facts)
  * [oneview_hypervisor_cluster_profile - OneViewハイパーバイザークラスタープロファイルを管理します。](#oneview_hypervisor_cluster_profile)
  * [oneview_hypervisor_cluster_profile_facts - OneViewハイパーバイザークラスタープロファイル情報を取得します.](#oneview_hypervisor_cluster_profile_facts)
  * [oneview_hypervisor_manager - OneViewハイパーバイザーマネージャーを管理します。](#oneview_hypervisor_manager)
  * [oneview_hypervisor_manager_facts - OneViewハイパーバイザーマネージャー情報を取得します。](#oneview_hypervisor_manager_facts)
  * [oneview_id_pools - OneView IDプールを管理します。](#oneview_id_pools)
  * [oneview_id_pools_facts - OneView IDプール情報を取得します。](#oneview_id_pools_ipv4_facts)
  * [oneview_id_pools_ipv4_range - OneView IDプールのIPV4範囲リソースを管理します。](#oneview_id_pools_ipv4_range)
  * [oneview_id_pools_ipv4_range_facts - 1つ以上のOneView IDプールIPV4範囲に関する情報を取得します。](#oneview_id_pools_ipv4_range_facts)
  * [oneview_id_pools_ipv4_subnet - OneView IDプールのIPV4サブネットリソースを管理します。](#oneview_id_pools_ipv4_subnet)
  * [oneview_id_pools_ipv4_subnet_facts - 1つ以上のOneView IDプールIPV4サブネットに関する情報を取得します。](#oneview_id_pools_ipv4_subnet_facts)
  * [oneview_interconnect - OneView Interconnectリソースを管理します。](#oneview_interconnect)
  * [oneview_interconnect_facts - 1つ以上のOneViewインターコネクトに関する情報を取得します。](#oneview_interconnect_facts)
  * [oneview_interconnect_link_topology_facts - OneView Interconnect Linkトポロジに関する情報を取得します。](#oneview_interconnect_link_topology_facts)
  * [oneview_interconnect_type_facts - 1つ以上のOneViewインターコネクトタイプに関する情報を取得します。](#oneview_interconnect_type_facts)
  * [oneview_internal_link_set_facts - OneView内部リンクセットに関する情報を取得します。](#oneview_internal_link_set_facts)
  * [oneview_label - Oneviewラベルを管理します。](#oneview_label)
  * [oneview_label_facts - Oneviewラベルに関する情報を取得します。](#oneview_label_facts)
  * [oneview_logical_downlinks_facts - 1つ以上のOneView論理ダウンリンクに関する情報を取得します。](#oneview_logical_downlinks_facts)
  * [oneview_logical_enclosure - OneView論理エンクロージャリソースを管理します。](#oneview_logical_enclosure)
  * [oneview_logical_enclosure_facts - 1つ以上のOneView論理エンクロージャーに関する情報を取得します。](#oneview_logical_enclosure_facts)
  * [oneview_logical_interconnect - OneView論理インターコネクトリソースを管理します。](#oneview_logical_interconnect)
  * [oneview_logical_interconnect_facts - 1つ以上のOneView論理インターコネクトに関する情報を取得します。](#oneview_logical_interconnect_facts)
  * [oneview_logical_interconnect_group - OneView論理インターコネクトグループリソースを管理します。](#oneview_logical_interconnect_group)
  * [oneview_logical_interconnect_group_facts - 1つ以上のOneView論理インターコネクトグループに関する情報を取得します。](#oneview_logical_interconnect_group_facts)
  * [oneview_logical_switch - OneView論理スイッチリソースを管理します。](#oneview_logical_switch)
  * [oneview_logical_switch_facts - 1つ以上のOneView論理スイッチに関する情報を取得します。](#oneview_logical_switch_facts)
  * [oneview_logical_switch_group - OneView論理スイッチグループリソースを管理します。](#oneview_logical_switch_group)
  * [oneview_logical_switch_group_facts - OneView論理スイッチグループに関する情報を取得します。](#oneview_logical_switch_group_facts)
  * [oneview_login_detail_facts - ログインの詳細に関する情報を取得します。](#oneview_login_detail_facts)
  * [oneview_managed_san - OneView Managed SANリソースを管理します。](#oneview_managed_san)
  * [oneview_managed_san_facts - OneView Managed SANに関する情報を取得します。](#oneview_managed_san_facts)
  * [oneview_network_set - OneView Network Setリソースを管理します。](#oneview_network_set)
  * [oneview_network_set_facts - OneViewネットワークセットに関する情報を取得します。](#oneview_network_set_facts)
  * [oneview_os_deployment_plan_facts - 1つ以上のOS展開計画に関する情報を取得します。](#oneview_os_deployment_plan_facts)
  * [oneview_os_deployment_server - OneView 展開サーバーリソースを管理します。](#oneview_os_deployment_server)
  * [oneview_os_deployment_server_facts - 1つ以上のOS展開サーバーに関する情報を取得します。](#oneview_os_deployment_server_facts)
  * [oneview_power_device - OneViewパワーデバイスリソースを管理します。](#oneview_power_device)
  * [oneview_power_device_facts - OneViewパワーデバイスに関する情報を取得します。](#oneview_power_device_facts)
  * [oneview_rack - OneViewラックリソースを管理します。](#oneview_rack)
  * [oneview_rack_facts - ラックリソースに関する情報を取得します。](#oneview_rack_facts)
  * [oneview_san_manager - OneView SAN Managerリソースを管理します。](#oneview_san_manager)
  * [oneview_san_manager_facts - 1つ以上のOneView SANマネージャーに関する情報を取得します。](#oneview_san_manager_facts)
  * [oneview_sas_interconnect - OneView SASインターコネクトリソースを管理します。](#oneview_sas_interconnect)
  * [oneview_sas_interconnect_facts - OneView SASインターコネクトに関する情報を取得します。](#oneview_sas_interconnect_facts)
  * [oneview_sas_interconnect_type_facts - OneView SASインターコネクトタイプに関する情報を取得します。](#oneview_sas_interconnect_type_facts)
  * [oneview_sas_logical_interconnect - OneView SAS論理インターコネクトリソースを管理します。](#oneview_sas_logical_interconnect)
  * [oneview_sas_logical_interconnect_facts - 1つ以上のOneView SAS論理インターコネクトに関する情報を取得します。](#oneview_sas_logical_interconnect_facts)
  * [oneview_sas_logical_interconnect_group - OneView SAS論理インターコネクトグループリソースを管理します。](#oneview_sas_logical_interconnect_group)
  * [oneview_sas_logical_interconnect_group_facts - 1つ以上のOneView SAS論理インターコネクトグループに関する情報を取得します。](#oneview_sas_logical_interconnect_group_facts)
  * [oneview_sas_logical_jbod_attachment_facts - 1つ以上のOneView SAS論理インターコネクトグループに関する情報を取得します。](#oneview_sas_logical_jbod_attachment_facts)
  * [oneview_sas_logical_jbod_facts - 1つ以上のOneView SAS論理JBODに関する情報を取得します。](#oneview_sas_logical_jbod_facts)
  * [oneview_scope - OneView Scopeリソースを管理します。](#oneview_scope)
  * [oneview_scope_facts - 1つ以上のOneViewスコープに関する情報を取得します。](#oneview_scope_facts)
  * [oneview_server_hardware - OneViewサーバーハードウェアリソースを管理します。](#oneview_server_hardware)
  * [oneview_server_hardware_facts - OneViewサーバーハードウェアに関する情報を取得します。](#oneview_server_hardware_facts)
  * [oneview_server_hardware_type - OneViewサーバーのハRetrieve facts about Server Hardware Types of the OneView.ードウェアタイプリソースを管理します。](#oneview_server_hardware_type)
  * [oneview_server_hardware_type_facts - OneViewのサーバーハードウェアタイプに関する情報を取得します。](#oneview_server_hardware_type_facts)
  * [oneview_server_profile - OneViewサーバープロファイルリソースを管理します。](#oneview_server_profile)
  * [oneview_server_profile_facts - OneViewサーバープロファイルに関する情報を取得します。](#oneview_server_profile_facts)
  * [oneview_server_profile_template - OneViewサーバープロファイルテンプレートリソースを管理します。](#oneview_server_profile_template)
  * [oneview_server_profile_template_facts - OneViewからサーバープロファイルテンプレートに関する情報を取得します。](#oneview_server_profile_template_facts)
  * [oneview_storage_pool - OneViewストレージプールリソースを管理します。](#oneview_storage_pool)
  * [oneview_storage_pool_facts - 1つ以上のストレージプールに関する情報を取得します。](#oneview_storage_pool_facts)
  * [oneview_storage_system - OneViewストレージシステムリソースを管理します。](#oneview_storage_system)
  * [oneview_storage_system_facts - OneViewストレージシステムに関する情報を取得します。](#oneview_storage_system_facts)
  * [oneview_storage_volume_attachment - 指定したサーバープロファイルから余分なプレゼンテーションを削除するためのインターフェイスを提供します。](#oneview_storage_volume_attachment)
  * [oneview_storage_volume_attachment_facts - OneViewストレージボリュームのアタッチメントに関する情報を取得します。](#oneview_storage_volume_attachment_facts)
  * [oneview_storage_volume_template - OneViewストレージボリュームテンプレートリソースを管理します。](#oneview_storage_volume_template)
  * [oneview_storage_volume_template_facts - OneViewのストレージボリュームテンプレートに関する情報を取得します。](#oneview_storage_volume_template_facts)
  * [oneview_switch - ToRスイッチリソースを削除するためのインターフェイスを提供します。](#oneview_switch)
  * [oneview_switch_facts - OneViewスイッチに関する情報を取得します。](#oneview_switch_facts)
  * [oneview_switch_type_facts - OneViewスイッチタイプに関する情報を取得します。](#oneview_switch_type_facts)
  * [oneview_task_facts - OneViewタスクに関する情報を取得します。](#oneview_task_facts)
  * [oneview_unmanaged_device - OneView管理対象外デバイスリソースを管理します。](#oneview_unmanaged_device)
  * [oneview_unmanaged_device_facts - 1つ以上のOneView管理対象外デバイスに関する情報を取得します。](#oneview_unmanaged_device_facts)
  * [oneview_uplink_set - OneViewアップリンクセットリソースを管理します。](#oneview_uplink_set)
  * [oneview_uplink_set_facts - 1つ以上のOneViewアップリンクセットに関する情報を取得します。](#oneview_uplink_set_facts)
  * [oneview_user - OneViewユーザーを管理します。](#oneview_user)
  * [oneview_user_facts - 1人以上のOneViewユーザーに関する情報を取得します。](#oneview_user_facts)
  * [oneview_version_facts - アプライアンスでサポートされている可能なAPIバージョンの範囲を返します。](#oneview_version_facts)
  * [oneview_volume - OneView Volumeリソースを管理します。](#oneview_volume)
  * [oneview_volume_facts - OneViewボリュームに関する情報を取得します。](#oneview_volume_facts)

---

## hpe_icsp_os_deployment
HPE ICspを使用して、サーバーにオペレーティングシステムを展開します。

#### 概要
 使用可能なICsp OSビルド計画に基づいて、サーバーにオペレーティングシステムを展開します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpICsp >= 1.0.2

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| api_version  |   No  |  300  | |  ICsp API バージョン。  |
| custom_attributes  |   No  |  | |  カスタム属性。  |
| icsp_host  |   Yes  |  | |  ICsp ホスト名。  |
| os_build_plan  |   Yes  |  | |  OS ビルド計画。  |
| password  |   Yes  |  | |  ICsp パスワード。  |
| personality_data  |   No  |  | |  パーソナリティーデータ。  |
| server_id  |   No  |  | |  サーバーID。非推奨。IPアドレスが優先されます（server_ipAddress）。  |
| server_ipAddress  |   No  |  | |  サーバーのiLOのIPアドレス。  |
| username  |   Yes  |  | |  ICsp ユーザー名。  |


 
#### 例

```yaml

- name: OSを展開する
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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| icsp_server   | ICspでプロビジョニングされたサーバーに関する情報を持っています。|  モジュールは正常に実行されますが、nullの場合があります。 |  dict |



---


## hpe_icsp_server
ICspでサーバーを追加、削除、構成します。

#### 概要
 このモジュールを使用すると、Insight Controlサーバープロビジョニング（ICsp）でサーバーを追加、削除、および構成できます。ICspでは、サーバーはしばしばターゲットサーバーと呼ばれ、物理的なProLiantサーバーまたはアクションを実行できる仮想マシンです。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpICsp >= 1.0.2

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| api_version  |   No  |  300  | |  ICsp API バージョン。  |
| icsp_host  |   Yes  |  | |  ICsp ホスト名。  |
| password  |   Yes  |  | |  ICsp パスワード。  |
| server_ipAddress  |   Yes  |  | |  サーバーのiLOのIPアドレス。  |
| server_password  |   Yes  |  | |  サーバーのiLOにログインするために必要なパスワード  |
| server_personality_data  |   No  |  | |  ICspに送信する追加データ。  |
| server_port  |   No  |  [443]  | |  ログイン時に使用するiLOポート。  |
| server_username  |   Yes  |  | |  サーバーのiLOにログインするために必要なユーザー名。  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li>  <li>network_configured</li> </ul> |  ICspサーバーの望ましい状態を示します。'present'は、ICspにリソースを登録します。'absent'は、存在する場合、ICspからリソースを削除します。'network_configured'はネットワーク構成を設定します。  |
| username  |   Yes  |  | |  ICsp ユーザー名。  |


 
#### 例

```yaml

  - name: サーバーがICspに登録されていることを確認してください
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

  - name: サーバーがICspから削除されていることを確認します
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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| target_server   | ICspに追加されたサーバーに関する情報を持っています。|  状態が 'present' および 'network_configured' 。nullの場合があります。 |  dict |



---


## image_streamer_artifact_bundle
アーティファクトバンドルリソースを管理します。

#### 概要
 アーティファクトバンドルを管理するためのインターフェイスを提供します。作成、更新、削除、ダウンロード、アップロード、抽出が可能です

#### 要件 (モジュールを実行するホスト)
  * python >= 3.4.2
  * hpeOneView >= 5.4.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  アーティファクトバンドルプロパティとそれに関連付けられた状態のリスト。  |
| state  |   Yes  |  | <ul> <li>present</li>  <li>absent</li>  <li>downloaded</li>  <li>archive_downloaded</li>  <li>backup_uploaded</li>  <li>backup_created</li>  <li>extracted</li>  <li>backup_extracted</li> </ul> |  Indicates the desired state for the Artifact Bundle resource. `present`は、データプロパティがOneViewに準拠していることを保証します。アーティファクトバンドルが既に存在する場合、名前のみが更新されます。他の属性値の変更は無視されます。`absent`は、存在する場合、OneViewからリソースを削除します。`downloaded`は、指定されたファイルパスにアーティファクトバンドルをダウンロードします。`archive_downloaded`は、アーティファクトバンドルアーカイブを指定されたファイルパスにダウンロードします。`backup_uploaded`は、提供されたファイルパスからアーティファクトバンドルのバックアップをアップロードします。`backup_created`は、アーティファクトバンドルのバックアップを作成します。`extracted`は、アーティファクトバンドルを抽出します。`backup_extracted`は、バックアップからアーティファクトバンドルを抽出します。  |


 
#### 例

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

- name: アーティファクトバンドルを提供されたファイルパスにダウンロードします
  image_streamer_artifact_bundle:
    config: "{{ config }}"
    state: downloaded
    data:
      name: 'Artifact Bundle'
      destinationFilePath: '~/downloaded_artifact.zip'
  delegate_to: localhost

- name: アーティファクトバンドルのアーカイブを提供されたファイルパスにダウンロードします
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

- name: バックアップアーティファクトバンドルをアップロードします
  image_streamer_artifact_bundle:
    config: "{{ config }}"
    state: backup_uploaded
    data:
      deploymentGroupURI: '/rest/deployment-groups/c5a727ef-71e9-4154-a512-6655b168c2e3'
      localBackupArtifactBundleFilePath: '~/uploaded_backup.zip'
  delegate_to: localhost

- name: アーティファクトバンドルのバックアップを作成します
  image_streamer_artifact_bundle:
    config: "{{ config }}"
    state: backup_created
    data:
      deploymentGroupURI: '/rest/deployment-groups/c5a727ef-71e9-4154-a512-6655b168c2e3'
  delegate_to: localhost

- name: アーティファクトバンドルを抽出します
  image_streamer_artifact_bundle:
    config: "{{ config }}"
    state: extracted
    data:
      name: 'Artifact Bundle'
  delegate_to: localhost

- name: アーティファクトバンドルのバックアップを抽出します
  image_streamer_artifact_bundle:
    config: "{{ config }}"
    state: backup_extracted
    data:
      deploymentGroupURI: '/rest/deployment-groups/c5a727ef-71e9-4154-a512-6655b168c2e3'
  delegate_to: localhost

- name: アーティファクトバンドルを更新します
  image_streamer_artifact_bundle:
    config: "{{ config }}"
    state: present
    data:
      name: 'Artifact Bundle'
      newName: 'Artifact Bundle Updated'
  delegate_to: localhost

- name: アーティファクトバンドルを削除します
  image_streamer_artifact_bundle:
    config: "{{ config }}"
    state: absent
    data:
      name: 'Artifact Bundle'
  delegate_to: localhost

```



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| artifact_bundle   | アーティファクトバンドルに関するOneViewの情報がを持っています。|  状態が 'present' および 'extracted'。|  dict |
| artifact_bundle_deployment_group   | 展開グループに関するOneViewの情報を持っています。|  状態が 'backup_extracted'、 'backup_uploaded'、および 'backup_created'。 |  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## image_streamer_artifact_bundle_facts
アーティファクトバンドルに関する情報を取得します。

#### 概要
 アーティファクトバンドルに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 3.4.2
  * hpeOneView >= 5.4.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  アーティファクトバンドルの名前。  |
| options  |   No  |  | |  アーティファクトバンドルに関する追加の情報を収集するオプションをリストします。可能なオプション: `allBackups`は、アーティファクトバンドルのバックアップのリストを取得します。`backupForAnArtifactBundle`は、アーティファクトバンドルのバックアップのリストを取得します。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。 `count`: 返されるリソースの数。 `filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。 `sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| artifact_bundle_backups   | アーティファクトバンドルのバックアップ情報。 |  要求された場合に戻りますが、nullの場合もあります。 |  list |
| artifact_bundles   | アーティファクトバンドル情報。 |  常に戻りますが、nullの場合もあります。 |  list |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## image_streamer_build_plan
Image Stream OSビルド計画リソースを管理します。

#### 概要
 Image Stream OSビルド計画を管理するためのインターフェイスを提供します。作成、更新、削除できます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  OSビルド計画のプロパティとその関連状態を一覧表示します。  |
| state  |   Yes  |  | <ul> <li>present</li>  <li>absent</li> </ul> |  OSビルド計画リソースの望ましい状態を示します。`present`は、データプロパティがSynergyイメージストリーマーに準拠していることを保証します。`absent`は、Synergyyイメージストリーマーからリソースを削除します（存在する場合）。  |


 
#### 例

```yaml

- name: OSビルド計画を作成する
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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| build_plan   | OSビルド計画に関するOneViewのファクトを持っています。|  状態が 'present'。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## image_streamer_build_plan_facts
1つ以上のイメージストリーマービルドプランに関する情報を取得します。

#### 概要
 1つ以上のイメージストリーマービルドプランに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 3.0.1

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  ビルド計画名。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| build_plans   | ビルド計画のリスト。|  常時、ただしnullの場合があります。|  list |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## image_streamer_deployment_group_facts
イメージストリーマーデプロイメントグループに関する情報を収集します。

#### 概要
 イメージストリーマーデプロイメントグループに関する情報を収集します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 3.0.1

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  展開グループの名前。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| deployment_groups   | 展開グループのリスト |  常時、ただし空の場合があります。|  list |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## image_streamer_deployment_plan
イメージストリーマーデプロイメントプランを管理します。

#### 概要
 イメージストリーマーデプロイメントプランを管理するためのインターフェイスを提供します。作成、更新、削除できます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  展開計画のプロパティとその関連状態を一覧表示します。  |
| state  |   Yes  |  | <ul> <li>present</li>  <li>absent</li> </ul> |  展開計画リソースの望ましい状態を示します。`present`は、データプロパティがSynergyイメージストリーマーに準拠していることを保証します。`absent`は、Synergyyイメージストリーマーからリソースを削除します（存在する場合）。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| deployment_plan   | イメージストリーマー展開計画に関するを持っています。|  状態は'present'ですが、nullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## image_streamer_deployment_plan_facts
イメージストリーマーデプロイメントプランに関する情報を取得します。

#### 概要
 イメージストリーマーデプロイメントプランに関する情報を1つまたは複数取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 4.5.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  展開計画名。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| deployment_plans   | イメージストリーマー展開計画に関する情報を取得します。|  常時、ただしnullの場合があります。|  list |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## image_streamer_golden_image
イメージストリーマーゴールデンイメージリソースを管理します。

#### 概要
 イメージストリーマーゴールデンイメージを管理するためのインターフェイスを提供します。作成、追加、更新、および削除できます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  ゴールデンイメージのプロパティとその関連状態を表示します。  |
| state  |   Yes  |  | <ul> <li>present</li>  <li>absent</li>  <li>downloaded</li>  <li>archive_downloaded</li> </ul> |  ゴールデンイメージリソースの望ましい状態を示します。`present`は、データプロパティがSynergyイメージストリーマーに準拠していることを保証します。`absent`は、Synergyyイメージストリーマーからリソースを削除します（存在する場合）。`downloaded`は、提供されたファイルパスにゴールデンイメージをダウンロードします。`archive_downloaded`は、提供されたファイルパスにゴールデンイメージアーカイブをダウンロードします。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| golden_image   | ゴールデンイメージに関するOneViewの情報を持っています。|  状態が 'present'。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## image_streamer_golden_image_facts
イメージストリーマーゴールデンイメージの1つ以上に関する情報を取得します。

#### 概要
 イメージストリーマーゴールデンイメージの1つ以上に関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 3.0.1

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  ゴールデンイメージ名。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| golden_images   | ゴールデンイメージのリスト。|  常時、ただしnullの場合があります。|  list |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## image_streamer_os_volume_facts
イメージストリーマーOSボリュームに関するファクトを取得します。

#### 概要
 イメージストリーマーOSボリュームに関するファクトを取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 3.0.1

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  OSボリュームの名前。  |
| options  |   No  |  | |  OSボリュームに関する追加の情報を収集するオプションを表示します。可能なオプション: `getStorage`はOSボリュームのストレージの詳細を取得します` getArchivedLogs`はOSボリュームのアーカイブされたログを取得します  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| log_file_path   | OS volume archived log file path |   |  str |
| os_volumes   | The list of OS Volumes |  常時、ただし空の場合があります。|  list |
| storage   | OSボリュームのストレージの詳細。 |   |  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## image_streamer_plan_script
イメージストリーマー計画スクリプトリソースを管理します。

#### 概要
 イメージストリーマー計画スクリプト管理するためのインターフェイスを提供します。作成、更新、削除できます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  計画スクリプトのプロパティとそれに関連する状態を表示します。  |
| state  |   Yes  |  | <ul> <li>present</li>  <li>absent</li>  <li>differences_retrieved</li> </ul> |  計画スクリプトリソースの望ましい状態を示します。`present`は、データプロパティがSynergyイメージストリーマーに準拠していることを保証します。`absent`は、Synergyyイメージストリーマーからリソースを削除します（存在する場合）。`differences_retrieved`は、選択された属性に従って、プランスクリプトの変更されたコンテンツを取得します。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| plan_script   | イメージストリーマー計画スクリプトに関する情報を持っています。|  状態は'present'ですが、nullの場合があります。|  dict |
| plan_script_differences   | 選択した属性ごとに、プランスクリプトの変更内容に関する情報を持っています。|  状態が 'differences_retrieved'。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## image_streamer_plan_script_facts
イメージストリーマー計画スクリプトに関する情報を取得します。

#### 概要
 1つ以上のイメージストリーマー計画スクリプトに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 3.0.1

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  計画スクリプト名。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| plan_scripts   | 計画スクリプトのリスト。|  常時、ただしnullの場合があります。|  list |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_alert_facts
OneViewアラートに関する情報を取得します。

#### 概要
 OneViewアラートに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 3.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| params  |   No  |  | |  アラートのフィルタリングに役立つパラメーターを表示します。可能なパラメーター: `count`、`fields`、`filter`、`query`、`sort`、`start`、`view`。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| alerts   | アラートのリスト。|  常時、ただしnullの場合があります。|  list |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_appliance_configuration_timeconfig_facts
OneViewの時間設定情報を収集します。

#### 概要
OneViewの時間設定情報を収集します。

#### 要件 (モジュールを実行するホスト)
  * python >= 3.4.2
  * hpeOneView >= 6.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |



## Example Playbook

```yaml

- name: Gather Facts about Oneview Appliance time configuration
  oneview_appliance_configuration_timeconfig_facts:
    config: "{{ config }}"
  delegate_to: localhost

- debug: var=appliance_configuration_timeconfig

```



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| appliance_configuration_timeconfig   | OneViewアプライアンスがサポートするローケル情報 |  常時、ただしnullの場合があります。 |  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_appliance_device_read_community
アプライアンスデバイス読み取りコミュニティストリングを管理します。

#### 概要
 アプライアンスデバイス読み取りコミュニティ文字列を管理するためのインターフェイスを提供します。更新のみ可能です。これにより、このOneViewインスタンスによって管理/監視されているすべてのサーバーのコミュニティストリングが更新されます。コミュニティストリングでサポートされている文字は、aA-zA、0-9、！、"です

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  アプライアンスデバイス読み取りコミュニティに表示します。  |
| state  |   |  | <ul> <li>present</li> </ul> |  アプライアンスデバイス読み取りコミュニティの望ましい状態を示します。`present`は、データプロパティがOneViewに準拠していることを保証します。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| appliance_device_read_community   | OneViewアプライアンスデバイス読み取りコミュニティに関するすべてのOneViewの情報を持っています。|  常時。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_appliance_device_read_community_facts
OneViewアプライアンスデバイス読み取りコミュニティに関する情報を取得します。

#### 概要
 OneViewアプライアンスデバイス読み取りコミュニティに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| appliance_device_read_community   | OneViewアプライアンスデバイス読み取りコミュニティに関するすべてのOneViewの情報を持っています。|  常時。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_appliance_device_snmp_v1_trap_destinations
OneViewアプライアンスデバイス読み取りコミュニティに関するすべてのOneViewの情報を持っています。

#### 概要
 アプライアンスデバイスのSNMPv1トラップ宛先を管理するためのインターフェイスを提供します。

#### 要件 (モジュールを実行するホスト)
  * python >= 3.4.2
  * hpeOneView >= 6.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   No  |  | |  SNMPv1トラップ送信先プロパティのリスト  |
| name  |   Yes  |  | |  SNMPv1トラップ送信先アドレス  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  アプライアンスデバイスSNMPv1トラップ宛先の望ましい状態を示します。`present`は、データプロパティがOneViewに準拠していることを保証します。`absent`は、存在する場合、OneViewからリソースを削除します。  |



#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| appliance_device_snmp_v1_trap_destinations   | OneViewアプライアンスSNMPv1トラップ転送先に関するすべてのOneViewの情報を持っています。|  状態が 'present'。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_appliance_device_snmp_v1_trap_destinations_facts
OneViewアプライアンスのSNMPv1トラップ転送先に関する情報を取得します。

#### 概要
 アプライアンスには、監視対象または管理対象のサーバーハードウェアから受信したイベントを、SNMPv1トラップとして指定された宛先に転送する機能があります。このモジュールは、アプライアンスのSNMPv1トラップ転送先に関するファクトを取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 3.4.2
  * hpeOneView >= 6.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  SNMPトラップの送信先  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| appliance_device_snmp_v1_trap_destinations   | OneViewアプライアンスSNMPv1トラップ転送先に関するすべてのOneViewの情報を持っています。|  常時。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_appliance_device_snmp_v3_trap_destinations
アプライアンスデバイスのSNMPv3トラップ送信先を管理します。

#### 概要
 アプライアンスデバイスのSNMPv3トラップ宛先を管理するためのインターフェイスを提供します。

#### 要件 (モジュールを実行するホスト)
  * python >= 3.4.2
  * hpeOneView >= 6.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   Yes  |  | |  SNMPv3トラップ宛先アドレス  |
| data  |   Yes  |  | |  SNMPv3トラップ宛先プロパティのリスト  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  アプライアンスデバイスSNMPv3トラップ宛先の望ましい状態を示します。`present`は、データプロパティがOneViewに準拠していることを保証します。`absent`は、存在する場合、OneViewからリソースを削除します。  |


 
#### 例

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
    name: 10.0.0.1
    state: absent
  delegate_to: localhost

```



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| appliance_device_snmp_v3_trap_destinations   | OneViewアプライアンスSNMPv3トラップ宛先に関するすべての情報。|  状態が 'present'。nullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_appliance_device_snmp_v3_trap_destinations_facts
OneViewアプライアンスのSNMPv3トラップ転送先に関する情報を取得します。

#### 概要
 アプライアンスには、監視対象または管理対象のサーバーハードウェアから受信したイベントを、SNMPv3トラップとして指定された宛先に転送する機能があります。このモジュールは、アプライアンスのSNMPv3トラップ転送先に関するファクトを取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 3.4.2
  * hpeOneView >= 6.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  トラップの送信先名  |
| params  |   No  |  | |  リソースのリストを区切り、フィルタリングし、ソートするためのパラメータのリスト。許可されるパラメータは次の通りです。`start`：0ベースのインデックスを使用して最初に返されるアイテム `count`：返すリソースの数 `filter`：返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列 `sort`：返されたデータセットのソート順  |



#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| appliance_device_snmp_v3_trap_destinations   | OneViewアプライアンスSNMPv3トラップ転送先に関するすべてのOneViewの情報を持っています。|  常時。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_appliance_device_snmp_v3_users
アプライアンスデバイスのSNMPv3ユーザーを管理します。

#### 概要
 アプライアンスデバイスSNMPv3ユーザーを管理するためのインターフェイスを提供します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  SNMPv3ユーザープロパティのリスト  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li>  <li>set_password</li> </ul> |  アプライアンスデバイスSNMPv3ユーザーの望ましい状態を示します。`present`は、データプロパティがOneViewに準拠していることを保証します。`absent`は、存在する場合、OneViewからリソースを削除します。`set_password`はユーザーのパスワードを指定された値に設定します。この操作は冪等ではありません。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| appliance_device_snmp_v3_users   | OneViewアプライアンスSNMPv3ユーザーに関するすべてのOneViewの情報を持っています。|   'present' と 'set_password’の状態。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_appliance_device_snmp_v3_users_facts
OneViewアプライアンスSNMPv3ユーザーに関する情報を取得します。

#### 概要
 SNMPv3ユーザーは、関連する宛先にSNMPv3トラップを送信するために使用されます。1人のユーザーを複数の宛先に割り当てることができます。このモジュールは、アプライアンスのSNMPv3ユーザーに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |


 
#### 例

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
      filter: 「securityLevel='Authentication and privacy'"
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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| appliance_device_snmp_v3_users   | OneViewアプライアンスSNMPv3ユーザーに関するすべてのOneViewの情報を持っています。|  常時。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---

## oneview_appliance_ssh_access
OneViewアプライアンスのSSHアクセスを管理します。

#### 概要
 OneViewアプライアンスのSSHアクセスをオン・オフをします。

#### 要件 (モジュールを実行するホスト)
  * python >= 3.4.2
  * hpeOneView >= 6.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |  Yes  |  | |  SSHアクセスのプロパティとその状態をリストします。



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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| appliance_ssh_access   | OneViewアプライアンスSSHアクセス設定の全ての情報。 |  'present'ステータスまたはnull |  dict |
| data  |   Yes  |  | |  OneViewアプライアンスSSHアクセス設定プロパティのリスト。  |
| state  |   |  | <ul> <li>present</li> </ul> |  OneViewアプライアンスSSHアクセス設定に関する状態を示します。`present` は設定項目がOneViewに準拠していることを示します。  |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---

## oneview_appliance_ssh_access_facts
OneViewアプライアンスSSHアクセスに関する情報の取得

#### 概要
OneViewアプライアンスSSHアクセスに関する情報の取得

#### 要件 (モジュールを実行するホスト)
  * python >= 3.4.2
  * hpeOneView >= 6.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |



## Example Playbook

```yaml

- name: Gather facts about the Appliance SSH Access
  oneview_appliance_ssh_access_facts:
    config: "{{ config }}"
  delegate_to: localhost

- debug: var=appliance_ssh_access

```



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| appliance_ssh_access   | OneViewアプライアンスSSHアクセス設定の全ての情報。 |  常に  |  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_appliance_time_and_locale_configuration
OneViewアプライアンスのロケールと時間構成を管理します。

#### 概要
 アプライアンスのロケールと時間設定を管理するためのインターフェイスを提供します。更新のみ可能です。

#### 要件 (モジュールを実行するホスト)
  * python >= 3.4.2
  * hpeOneView >= 6.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  Appliance LocaleおよびTime Configurationプロパティを表示します。  |
| state  |   |  | <ul> <li>present</li> </ul> |  アプライアンスのロケールと時間の構成に必要な状態を示します。`present`は、データプロパティがOneViewに準拠していることを保証します。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| appliance_time_and_locale_configuration   | OneViewアプライアンスのロケールと時間の構成に関する情報があります。|  状態が 'present'。nullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_appliance_time_and_locale_configuration_facts
OneViewアプライアンスの時間とロケール構成に関する情報を取得します。

#### 概要
 OneViewアプライアンスの時間とロケール構成に関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 3.4.2
  * hpeOneView >= 6.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |


 
#### 例

```yaml

- name: Gather facts about the Appliance time and locale configuration
  oneview_appliance_time_and_locale_configuration_facts:
    config: "{{ config }}"
  delegate_to: localhost

- debug: var=appliance_time_and_locale_configuration

```



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| appliance_time_and_locale_configuration   | アプライアンスの時間とロケール構成に関するすべてのOneViewの情報を持っています。|  常時。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_certificates_server
OneView証明書サーバーを管理します。

#### 概要
 OneView証明書サーバーを管理するインターフェースを提供します。 作成、更新、削除が可能です。

#### 要件 (モジュールを実行するホスト)
  * hpeOneView >= 5.4.0
  * python >= 3.4.2

#### オプション

| パラメータ     | 必須    | デフォルト  | 選択    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。設定ファイルをリンクさせる、または環境変数の使い方については注記を確認してください。 |
| data  |   Yes  |  | |  証明書サーバー情報をセットします。  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  証明書サーバーの希望の状態を指定します。`present`はデータプロパティがOneViewに準拠していることを保証します。 `absent`は指定したリソースが存在する場合、そのリソースをOneViewから削除します。  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  指定したetagが現在のリソースに付与しているetagに一致する場合のみ処理します。  |


 
#### 例

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



#### 注記

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples

- The OneView API version used will directly affect returned and expected fields in resources. Information on setting the desired API version and can be found at: https://github.com/HewlettPackard/oneview-ansible#setting-your-oneview-version


---


## oneview_certificates_server_facts
Retrieve the facts about one or more of the OneView Certificates Server.

#### 概要
 Retrieve the facts about one or more of the Certificates Server from OneView.

#### 要件 (モジュールを実行するホスト)
  * hpeOneView >= 5.4.0
  * python >= 3.4.2

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional and when used should be present in the host running the ansible commands. If the file path is not provided, the configuration will be loaded from environment variables. For links to example configuration files or how to use the environment variables verify the notes section.  |
| aliasName  |   No  |  | |  Certificates Server aliasName.  |
| remote  |   No  |  | |  Remote Server Certificate.  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| certificates_servers   | 証明書サーバーの全ての情報を保持します。 |  常に値が戻されますが、nullの場合があります。 |  dict |
| remote_certificate     | リモートサーバー証明書情報を保持します。 |  要求した場合、値が戻されます。 |  dict |

#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- その他のHPE OneView AnsibleモジュールのPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples

- 使用されるOneViewAPIバージョンによって、リソース対しての設定値と戻り値が変わる場合があります。APIバージョン別の設定に関する情報は、次のURLにあります。: https://github.com/HewlettPackard/oneview-ansible#setting-your-oneview-version


---



## oneview_connection_template
OneView接続テンプレートリソースを管理します。

#### 概要
 接続テンプレートリソースを管理するためのインターフェイスを提供します。更新できます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  接続テンプレートのプロパティとその関連状態を表示します。  |
| state  |   Yes  |  | <ul> <li>present</li> </ul> |  接続テンプレートリソースの望ましい状態を示します。`present`は、データプロパティがOneViewに準拠していることを保証します。  |


 
#### 例

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
            typicalBandwidth : 2000
        newName : "CT-23"
  delegate_to: localhost

```



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| connection_template   | 接続テンプレートに関するOneViewの情報を持っています。|  'present'の状態ですが、nullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_connection_template_facts
OneView接続テンプレートに関する情報を取得します。

#### 概要
 OneView接続テンプレートに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  接続テンプレート名。  |
| options  |   No  |  | |  接続テンプレート関連のリソースに関する追加の情報を収集するオプションを表示します。可能なオプション: `defaultConnectionTemplate`.  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| connection_templates   | 接続テンプレートに関するすべてのOneViewの情報を持っています。|  常時、defaultConnectionTemplateが要求された場合を除く。nullの場合があります。|  dict |
| default_connection_template   | デフォルト接続テンプレートに関する情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_datacenter
OneViewデータセンターリソースを管理します。

#### 概要
 データセンターのリソースを管理するためのインターフェイスを提供します。追加、更新、削除できます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  データセンターのプロパティとその関連状態を表示します。  |
| state  |   Yes  |  | <ul> <li>present</li>  <li>absent</li> </ul> |  データセンターリソースの望ましい状態を示します。`present`は、データプロパティがOneViewに準拠していることを保証します。`absent`は、存在する場合、OneViewからリソースを削除します。  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  ETag検証が有効になっている場合、リソースの現在のETagがデータで提供されているETagと一致する場合にのみ、リクエストが条件付きで処理されます。  |


 
#### 例

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

- name: データセンターの名前を変更します
  oneview_datacenter:
    config: "{{ config }}"
    state: absent
    data:
        name: 'My Datacenter'
  delegate_to: localhost

```



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| datacenter   | データセンターに関するOneViewの情報を持っています。|  状態が 'present'。nullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_datacenter_facts
OneViewデータセンターに関する情報を取得します。

#### 概要
 OneViewデータセンターに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 2.0.1

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  データセンター名。  |
| options  |   No  |  | |  追加の情報を取得します。利用可能なオプション: 'visualContent'.  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| datacenter_visual_content   | データセンターのビジュアルコンテンツに関する情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| datacenters   | データセンターに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_drive_enclosure
OneViewドライブエンクロージャーリソースを管理します。

#### 概要
 ドライブエンクロージャーリソースを管理するためのインターフェイスを提供します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 3.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  ドライブエンクロージャのプロパティを表示します。  |
| state  |   |  | <ul> <li>power_state_set</li>  <li>uid_state_set</li>  <li>hard_reset_state_set</li>  <li>refresh_state_set</li> </ul> |  ドライブエンクロージャーリソースの望ましい状態を示します。`power_state_set`は、ドライブエンクロージャーの電源状態を設定します。`uid_state_set`はドライブエンクロージャーのuid状態を設定します。`hard_reset_state_set`は、ドライブエンクロージャーのハードリセットを要求します。`refresh_state_set`はドライブエンクロージャーを更新します。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| drive_enclosure   | ドライブエンクロージャーに関する情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

-このリソースは、HPE Synergyでのみ利用可能です。

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_drive_enclosure_facts
1つ以上のOneViewドライブエンクロージャーに関する情報を取得します。

#### 概要
 OneViewから1つ以上のドライブエンクロージャーに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 3.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  ドライブエンクロージャー名。  |
| options  |   No  |  | |  ドライブエンクロージャ関ー連のリソースに関する追加の情報を収集するオプションを表示します。可能なオプション: `portMap`。追加の情報を収集するには、ドライブエンクロージャー名を通知する必要があります。それ以外の場合、これらのオプションは無視されます。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| drive_enclosure_port_map   | ドライブエンクロージャポートマップに関するすべてのOneViewの情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| drive_enclosures   | ドライブエンクロージャーに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

-このリソースは、HPE Synergyでのみ利用可能です。

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_enclosure
OneViewエンクロージャーリソースを管理します。

#### 概要
 エンクロージャリソースを管理するためのインターフェイスを提供します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  エンクロージャーのプロパティを表示します。  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li>  <li>reconfigured</li>  <li>refreshed</li>  <li>appliance_bays_powered_on</li>  <li>uid_on</li>  <li>uid_off</li>  <li>manager_bays_uid_on</li>  <li>manager_bays_uid_off</li>  <li>manager_bays_power_state_e_fuse</li>  <li>manager_bays_power_state_reset</li>  <li>appliance_bays_power_state_e_fuse</li>  <li>device_bays_power_state_e_fuse</li>  <li>device_bays_power_state_reset</li>  <li>interconnect_bays_power_state_e_fuse</li>  <li>manager_bays_role_active</li>  <li>device_bays_ipv4_removed</li>  <li>interconnect_bays_ipv4_removed</li>  <li>support_data_collection_set</li>  <li>create_certificate_request</li>  <li>get_certificate_request</li>  <li>import_certificate_request</li> </ul> |  エンクロージャーリソースの望ましい状態を示します。`present`は、データプロパティがOneViewに準拠していることを保証します。属性`newName`を指定してエンクロージャーの名前を変更できます。属性 `rackName`を指定してラックの名前を変更することもできます。`absent`は、存在する場合、OneViewからリソースを削除します。`reconfigured`は、アプライアンスの構成をエンクロージャーに再適用します。これには、エンクロージャー追加の一部として実行されたのと同じ構成ステップの実行が含まれます。 `refreshed`は、相互接続やサーバーを含むすべてのコンポーネントとともにエンクロージャーを更新します。新しいハードウェアが追加され、エンクロージャー内に存在しなくなったハードウェアは削除されます。`appliance_bays_powered_on`は、アプライアンスベイの電源状態をオンに設定します。`uid_on`は、UID状態をオンに設定します。`uid_off`は、UID状態をオフに設定します。`manager_bays_uid_on`は、SynergyフレームリンクモジュールのUID状態をオンに設定します。`manager_bays_uid_off`は、SynergyフレームリンクモジュールのUID状態をオフに設定します。`manager_bays_power_state_e_fuse`は、パス内のSynergyフレームリンクモジュールベイを電子ヒューズします。`manager_bays_power_state_reset`は、パス内のSynergyフレームリンクモジュールベイをリセットします。`appliance_bays_power_state_e_fuse`は、パス内のアプライアンスベイを電子ヒューズします。`device_bays_power_state_e_fuse`は、パス内のデバイスベイを電子ヒューズします。`device_bays_power_state_reset`は、パスのデバイスベイをリセットします。`interconnect_bays_power_state_e_fuse`は、パス内のICベイを電子ヒューズします。`manager_bays_role_active`は、アクティブなSynergyフレームリンクモジュールを設定します。「device_bays_ipv4_removed」は、デバイスベイのIPv4アドレスを解放します。`interconnect_bays_ipv4_removed`は、インターコネクトベイのIPv4アドレスを解放します。`support_data_collection_set`は、エンクロージャーのサポートデータ収集状態を設定します。この状態でサポートされる値は、`PendingCollection`、`Completed`、`Error`、`NotSupported`です。`create_certificate_request`はエンクロージャーの証明書署名要求（CSR）を作成します。`get_certificate_request`は、同じURIへの以前のPOSTによって生成されたエンクロージャーの証明書署名要求（CSR）を返します。`import_certificate_request`は、署名されたサーバー証明書をエンクロージャーにインポートして、アプライアンスとの安全な通信に使用します。  |


 
#### 例

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
      password : ‘{{ enclosure_password }}'
      name: ‘Test-Enclosure'
      licensingIntent : ‘OneView'

- name: Updates the enclosure to have a name of "Test-Enclosure-Renamed".
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: ‘Test-Enclosure'
      newName : 'Test-Enclosure-Renamed'

- name: Reconfigure the enclosure "Test-Enclosure"
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: reconfigured
    data:
      name: ‘Test-Enclosure'

- name: Ensure that enclosure is absent
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: absent
    data:
      name: ‘Test-Enclosure'

- name: Ensure that an enclosure is refreshed
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: refreshed
    data:
      name: ‘Test-Enclosure'
      refreshState: Refreshing

- name: Create certificate signing request
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: create_certificate_request
    data:
      name: ‘Test-Enclosure'
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
      name: ‘Test-Enclosure'
      bay_number: 1

- name: Import certificate signing request
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: import_certificate_request
    data:
      name: ‘Test-Enclosure'
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
      name: ‘Test-Enclosure'
      calibratedMaxPower: 1700

- name: Set the appliance bay power state on
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: appliance_bays_powered_on
    data:
      name: ‘Test-Enclosure'
      bayNumber: 1

- name: Set the appliance UID state on
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: uid_on
    data:
      name: ‘Test-Enclosure'

- name: Set the appliance UID state off
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: uid_off
    data:
      name: ‘Test-Enclosure'

- name: Set the UID for the Synergy Frame Link Module state on
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: manager_bays_uid_on
    data:
      name: ‘Test-Enclosure'
      bayNumber: 1

- name: Set the UID for the Synergy Frame Link Module state off
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: manager_bays_uid_off
    data:
      name: ‘Test-Enclosure'
      bayNumber: 1

- name: E-Fuse the Synergy Frame Link Module bay 1
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: manager_bays_power_state_e_fuse
    data:
      name: ‘Test-Enclosure'
      bayNumber: 1

- name: Reset the Synergy Frame Link Module bay 1
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: manager_bays_power_state_reset
    data:
      name: ‘Test-Enclosure'
      bayNumber: 1

- name: E-Fuse the appliance bay 1
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: appliance_bays_power_state_e_fuse
    data:
      name: ‘Test-Enclosure'
      bayNumber: 1

- name: E-Fuse the device bay 10
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: device_bays_power_state_e_fuse
    data:
      name: ‘Test-Enclosure'
      bayNumber: 10

- name: Reset the device bay 8
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: device_bays_power_state_reset
    data:
      name: ‘Test-Enclosure'
      bayNumber: 8

- name: E-Fuse the IC bay 3
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: interconnect_bays_power_state_e_fuse
    data:
      name: ‘Test-Enclosure'
      bayNumber: 3

- name: Set the active Synergy Frame Link Module on bay 2
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: manager_bays_role_active
    data:
      name: ‘Test-Enclosure'
      bayNumber: 2

- name: Release IPv4 address in the bay 2
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: device_bays_ipv4_removed
    data:
      name: ‘Test-Enclosure'
      bayNumber: 2

- name: Release IPv4 address in the bay 2
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: interconnect_bays_ipv4_removed
    data:
      name: ‘Test-Enclosure'
      bayNumber: 2

- name: Set the supportDataCollectionState for the enclosure
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: support_data_collection_set
    data:
      name: ‘Test-Enclosure'
      supportDataCollectionState: 'PendingCollection'

- name: Ensure that the Enclosure is present and is inserted in the desired scopes
  oneview_enclosure:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: ‘Test-Enclosure'
      scopeUris:
        - '/rest/scopes/00SC123456'
        - '/rest/scopes/01SC123456'

```



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| enclosure   | エンクロージャーに関するすべての情報を持っています。|  状態が'present'、'reconfigured'、'refreshed'。nullの場合があります。|  dict |


#### 注記

- これらの状態は、HPE Synergyでのみ使用可能です。 `appliance_bays_powered_on`, `uid_on`, `uid_off`, `manager_bays_uid_on`, `manager_bays_uid_off`, `manager_bays_power_state_e_fuse`, `manager_bays_power_state_reset`, `appliance_bays_power_state_e_fuse`, `device_bays_power_state_e_fuse`, `device_bays_power_state_reset`, `interconnect_bays_power_state_e_fuse`, `manager_bays_role_active`, `device_bays_ipv4_removed` and `interconnect_bays_ipv4_removed`

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_enclosure_facts
1つ以上のエンクロージャーに関する情報を取得します

#### 概要
 OneViewから1つ以上のエンクロージャーに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   |  | |  エンクロージャー名。  |
| options  |   |  | |  エンクロージャーおよび関連リソースに関する追加の情報を収集するオプションを表示します。可能なオプション: `script`、`environmentalConfiguration`、`utilization`。オプション`utilization`には、特定のパラメーターを指定できます。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| enclosure_environmental_configuration   | エンクロージャーの環境構成に関するすべてのOneViewの情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| enclosure_script   | エンクロージャーのスクリプトに関するすべてのOneViewの情報を持っています。|  要求された場合、ただしnullの場合があります。 |  string |
| enclosure_utilization   | エンクロージャーの利用に関するすべてのOneViewの情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| enclosures   | エンクロージャーに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_enclosure_group
OneViewエンクロージャーグループリソースを管理します。

#### 概要
 エンクロージャーグループリソースを管理するためのインターフェイスを提供します。作成、更新、または削除できます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  エンクロージャーグループのプロパティのリスト。  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  エンクロージャーグループリソースの望ましい状態を示します。`present`は、データプロパティがOneViewに準拠していることを保証します。`absent`は、存在する場合、OneViewからリソースを削除します。  |


 
#### 例

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
        stackingMode: 
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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| enclosure_group   | エンクロージャーグループに関する情報を持っています。|  状態が 'present'。nullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_enclosure_group_facts
1つ以上のOneViewエンクロージャーグループに関する情報を取得します。

#### 概要
 OneViewから1つ以上のエンクロージャーグループに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  エンクロージャーグループ名。  |
| options  |   No  |  | |  エンクロージャーグループに関する追加の情報を収集するオプションを表示します。可能なオプション: `configuration_script`は、エンクロージャーグループの構成スクリプトを取得します。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| enclosure_group_script   | エンクロージャーグループの構成スクリプト。|  要求された場合、ただしnullの場合があります。|  string |
| enclosure_groups   | エンクロージャーグループに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |

#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_ethernet_network
OneViewイーサネットネットワークリソースを管理します。

#### 概要
 イーサネットネットワークリソースを管理するためのインターフェイスを提供します。作成、更新、または削除できます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  イーサネットネットワークプロパティのリスト。  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li>  <li>default_bandwidth_reset</li> </ul> |  イーサネットネットワークリソースの望ましい状態を示します。`present`は、データプロパティがOneViewに準拠していることを保証します。`absent`は、存在する場合、OneViewからリソースを削除します。`default_bandwidth_reset`は、ネットワーク接続テンプレートをデフォルトにリセットします。  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  ETag検証が有効になっている場合、リソースの現在のETagがデータで提供されているETagと一致する場合にのみ、リクエストが条件付きで処理されます。  |


 
#### 例

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
          typicalBandwidth: 2000
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
        typicalBandwidth: 2000

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| ethernet_network   | イーサネットネットワークに関する情報を持っています。|  状態 'present'nullの場合があります。|  dict |
| ethernet_network_bulk   | バルクインサートの影響を受けるイーサネットネットワークに関する情報を持っています。|   'vlanIdRange' 属性がデータ引数にある場合。nullの場合があります。|  dict |
| ethernet_network_connection_template   | イーサネットネットワーク接続テンプレートに関する情報を持っています。|  状態が 'default_bandwidth_reset'。nullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_ethernet_network_facts
1つ以上のOneViewイーサネットネットワークに関する情報を取得します。

#### 概要
 OneViewから1つ以上のイーサネットネットワークに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  イーサネットネットワーク名。  |
| options  |   No  |  | |  イーサネットネットワークおよび関連リソースに関する追加の情報を収集するオプションを表示します。可能なオプション: `associatedProfiles` と `associatedUplinkGroups`。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| enet_associated_profiles   | イーサネットネットワークを使用しているプロファイルに関するOneViewのすべての情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| enet_associated_uplink_groups   | イーサネットネットワークを使用しているアップリンクセットに関するすべてのOneViewの情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| ethernet_networks   | イーサネットネットワークに関するOneViewのすべての情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_event
OneViewイベントを管理します。

#### 概要
 イベントを管理するためのインターフェイスを提供します。作成のみ可能です。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 3.2.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  イベントプロパティのリスト。  |
| state  |   |  | <ul> <li>present</li> </ul> |  イベントの望ましい状態を示します。`present`は、データプロパティがOneViewに準拠していることを保証します。この操作は冪等ではありません。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| event   | OneViewイベントに関する情報を持っています。|  状態 'present'nullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_event_facts
1つ以上のOneViewイベントに関する情報を取得します。

#### 概要
 OneViewから1つ以上のイベントに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 3.2.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  イベント名。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| events   | イベントに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_fabric
OneView Fabricリソースを管理します。

#### 概要
 OneViewでファブリックを管理するためのインターフェイスを提供します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  ファブリックプロパティのリスト。  |
| name  |   No  |  | |  ファブリック名。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| fabric   | ファブリックに関するすべてのOneView情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

このモジュールは、HPE Synergyでのみ利用可能です。

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_fabric_facts
1つまたは複数のOneViewファブリックに関する情報を取得します。

#### 概要
 OneViewから1つ以上のファブリックに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 2.0.1

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  ファブリック名。  |
| options  |   No  |  | |  ファブリックおよび関連リソースに関する追加の情報を収集するオプションを表示します。可能なオプション: `reservedVlanRange`.  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| fabric_reserved_vlan_range   | 予約されたVLAN範囲に関するすべてのOneViewの情報を持っています |  要求された場合、nullの場合があります。|  dict |
| fabrics   | ファブリックに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_fc_network
OneViewファイバーチャネルネットワークリソースを管理します。

#### 概要
 ファイバーチャネルネットワークリソースを管理するためのインターフェイスを提供します。作成、更新、および削除できます。

#### 要件 (モジュールを実行するホスト)
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  ファイバーチャネルネットワークのプロパティを表示します。  |
ファイバーチャネルネットワークリソースの望ましい状態を示します。`present`は、データプロパティがOneViewに準拠していることを保証します。`absent`は、存在する場合、OneViewからリソースを削除します。  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  ETag検証が有効になっている場合、リソースの現在のETagがデータで提供されているETagと一致する場合にのみ、リクエストが条件付きで処理されます。  |


 
#### 例

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
    api_version: 2200
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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| fc_network   | 管理対象のOneView FCネットワークに関する情報を持っています。|  状態 'present'nullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_fc_network_facts
1つ以上のOneViewファイバーチャネルネットワークに関する情報を取得します

#### 概要
 OneViewから1つ以上のファイバーチャネルネットワークに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   |  | |  ファイバーチャネルネットワーク名。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| fc_networks   | ファイバーチャネルネットワークに関するOneViewのすべての情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_fcoe_network
OneView FCoEネットワークリソースを管理します

#### 概要
 FCoEネットワークリソースを管理するためのインターフェイスを提供します。作成、更新、または削除できます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  FCoEネットワークプロパティのリスト。  |
| state  |   |  present  | <ul> <li>present</li>  <li>absent</li> </ul> |  FCoEネットワークリソースの望ましい状態を示します。`present`は、データプロパティがOneViewに準拠していることを保証します。`absent`は、存在する場合、OneViewからリソースを削除します。  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  ETag検証が有効になっている場合、リソースの現在のETagがデータで提供されているETagと一致する場合にのみ、リクエストが条件付きで処理されます。  |


 
#### 例

```yaml

- name: デフォルト構成を使用してFCoEネットワークが存在すすようにします
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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| fcoe_network   | OneView FCoEネットワークに関する情報を持っています。|  状態 'present'nullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_fcoe_network_facts
1つ以上のOneView FCoEネットワークに関する情報を取得します

#### 概要
 OneViewから1つ以上のFCoEネットワークに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   |  | |  FCoEネットワーク名。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| fcoe_networks   | FCoEネットワークに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_firmware_bundle
OneViewファームウェアバンドルリソースをアップロードします。

#### 概要
 SPP ISOイメージファイルまたはホットフィックスファイルをアプライアンスにアップロードします。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 2.0.1

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| file_path  |   Yes  |  | |  ロードするローカルファイルのフルパス。  |
| state  |   |  | <ul> <li>present</li> </ul> |  ファームウェアドライバーリソースの望ましい状態を示します。`present`は、ファームウェアバンドルがOneViewにあることを保証します。  |


 
#### 例

```yaml

- name: Ensure that the Firmware Driver is present
  oneview_firmware_bundle:
    config: "{{ config_file_path }}"
    state: present
    file_path: "/home/user/Downloads/hp-firmware-hdd-a1b08f8a6b-HPGH-1.1.x86_64.rpm"


```



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| firmware_bundle   | OneViewファームウェアバンドルに関する情報を持っています。|  常時。nullの場合があります。|  dict |


#### 注記

- このモージュールは、冪等ではありません。

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_firmware_driver
ファームウェアドライバーリソースを削除するためのインターフェイスを提供します。

#### 概要
 ファームウェアドライバーリソースを削除するためのインターフェイスを提供します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   No  |  | |  ファームウェアドライバーのプロパティを表示します。  |
| name  |   No  |  | |  ファームウェアドライバー名。  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  ファームウェアドライバーの望ましい状態を示します。`present`は、データプロパティがOneViewに準拠していることを保証します。`absent`は、存在する場合、OneViewからリソースを削除します。  |


 
#### 例

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



#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_firmware_driver_facts
1つ以上のOneViewファームウェアドライバーに関する情報を取得します。

#### 概要
 OneViewから1つ以上のファームウェアドライバーに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  ファームウェアドライバー名。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| firmware_drivers   | ファームウェアドライバーに関するOneViewのすべての情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_hypervisor_cluster_profile
OneViewハイパーバイザークラスタープロファイルを管理します。

#### 概要
 ハイパーバイザークラスタープロファイルを管理するためのインターフェースを提供します。作成、更新、削除が可能です。

#### 要件 (モジュールを実行するホスト)
  * hpeOneView >= 5.4.0
  * python >= 3.4.2

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。設定ファイルをリンクさせる、または環境変数の使い方については注記を確認してください。  |
| data  |   Yes  |  | |  ハイパーバイザークラスタープロファイル情報をセットします.  |
| params  |     |  | |  フラグを強制します。  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  ハイパーバイザークラスタープロファイルの希望の状態を指定します。`present`はデータプロパティがOneViewに準拠していることを保証します。 `absent`は指定したリソースが存在する場合、そのリソースをOneViewから削除します。  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  指定したetagが現在のリソースに付与しているetagに一致する場合のみ処理します。  |


 
#### 例

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



#### 注記

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples

- The OneView API version used will directly affect returned and expected fields in resources. Information on setting the desired API version and can be found at: https://github.com/HewlettPackard/oneview-ansible#setting-your-oneview-version


---


## oneview_hypervisor_cluster_profile_facts
Retrieve the facts about one or more of the OneView Hypervisor Cluster Profiles.

#### 概要
 Retrieve the facts about one or more of the Hypervisor Cluster Profiles from OneView.

#### 要件 (モジュールを実行するホスト)
  * hpeOneView >= 5.4.0
  * python >= 3.4.2

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional and when used should be present in the host running the ansible commands. If the file path is not provided, the configuration will be loaded from environment variables. For links to example configuration files or how to use the environment variables verify the notes section.  |
| name  |   No  |  | |  Hypervisor Cluster Profile name.  |
| options  |   No  |  | |  Hypervisor Cluster Profile compliance.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `sort`: The sort order of the returned data set.  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| hypervisor_cluster_profiles   | ハイパーバイザークラスタープロファイルの全ての情報を保持します。 |  常に値が戻されますが、nullの場合があります。 |  dict |
| hypervisor_cluster_profile_compliance_preview   | ハイパーバイザークラスタープロファイルコンプライアンスプレビューの全ての情報を保持します. |  要求した場合、値が戻されます。 |  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- その他のHPE OneView AnsibleモジュールのPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples

- 使用されるOneViewAPIバージョンによって、リソース対しての設定値と戻り値が変わる場合があります。APIバージョン別の設定に関する情報は、次のURLにあります。: https://github.com/HewlettPackard/oneview-ansible#setting-your-oneview-version


---



## oneview_hypervisor_manager
OneViewハイパーバイザマネージャーを管理します。

#### 概要
 ハイパーバイザーマネージャーを管理するためのインターフェースを提供します。作成、更新、削除が可能です。

#### 要件 (モジュールを実行するホスト)
  * hpeOneView >= 5.4.0
  * python >= 3.4.2

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。設定ファイルをリンクさせる、または環境変数の使い方については注記を確認してください。  |
| data  |   Yes  |  | |  ハイパーバイザーマネージャー情報をセットします。  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  ハイパーバイザーマネージャーの希望の状態を指定します。presentはデータプロパティがOneViewに準拠していることを保証します。 absentは指定したリソースが存在する場合、そのリソースをOneViewから削除します。  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  指定したetagが現在のリソースに付与しているetagに一致する場合のみ処理します。  |


 
#### 例

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



#### 注記

- A sample configuration file for the config parameter can be found at: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- Check how to use environment variables for configuration at: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- Additional Playbooks for the HPE OneView Ansible modules can be found at: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples

- The OneView API version used will directly affect returned and expected fields in resources. Information on setting the desired API version and can be found at: https://github.com/HewlettPackard/oneview-ansible#setting-your-oneview-version


---


## oneview_hypervisor_manager_facts
Retrieve the facts about one or more of the OneView Hypervisor Managers.

#### 概要
 Retrieve the facts about one or more of the Hypervisor Managers from OneView.

#### 要件 (モジュールを実行するホスト)
  * hpeOneView >= 5.4.0
  * python >= 3.4.2

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   |  | |  Path to a .json configuration file containing the OneView client configuration. The configuration file is optional and when used should be present in the host running the ansible commands. If the file path is not provided, the configuration will be loaded from environment variables. For links to example configuration files or how to use the environment variables verify the notes section.  |
| name  |   No  |  | |  Hypervisor Manager name.  |
| params  |   No  |  | |  List of params to delimit, filter and sort the list of resources.  params allowed: `start`: The first item to return, using 0-based indexing. `count`: The number of resources to return. `sort`: The sort order of the returned data set.  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| hypervisor_managers   | ハイパーバイザーマネージャーの全ての情報 |  常に返しますがnullのときもあります。 |  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- その他のHPE OneView AnsibleモジュールのPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples

- 使用されるOneViewAPIバージョンによって、リソース対しての設定値と戻り値が変わる場合があります。APIバージョン別の設定に関する情報は、次のURLにあります。: https://github.com/HewlettPackard/oneview-ansible#setting-your-oneview-version


---


## oneview_id_pools
OneView IDプールを管理します。

#### 概要
ID プールを管理するためのインターフェースを提供します。 作成、更新、削除ができます。

#### 要件 (モジュールを実行するホスト)
  * python >= 3.4.2
  * hpeOneView >= 6.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  IDプール情報のリスト  |
| state  |   |  | <ul> <li>allocate</li>  <li>collect</li> </ul> |  希望の状態を指定します。 `allocate` はIDセットを予約します。 `collect`は占有されたIDセットを収集します。  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  ETag検証が有効になっている場合、リソースの現在のETagがデータで提供されているETagと一致する場合にのみ、リクエストが条件付きで処理されます。  |

#### 例

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

#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| id_pools | OneView IDプール情報 |  'collect'またはnullの状態 |  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- その他のHPE OneView AnsibleモジュールのPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_id_pools_facts
OneView IDプール情報を取得します。

#### 概要
IDプールを管理するインターフェースを提供します。 スキーマ取得や検証、IDレンジ作成が可能です。

#### 要件 (モジュールを実行するホスト)
  * python >= 3.4.2
  * hpeOneView >= 6.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  IDプール情報のリスト  |
| state  |   |  | <ul> <li>schema</li>  <li>validate</li> </ul> |  希望の状態を指定します。 `schema` はIDプールのスキーマを取得します。 `validate`はIDが検証済み稼働かを確認します。  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  ETag検証が有効になっている場合、リソースの現在のETagがデータで提供されているETagと一致する場合にのみ、リクエストが条件付きで処理されます。  |

#### 例

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

#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| id_pools_facts | OneView IDプールの情報 |  'generate'またはnull |  dict |

#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- その他のHPE OneView AnsibleモジュールのPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_id_pools_ipv4_range
OneView IDプールのIPV4範囲リソースを管理します。

#### 概要
 IDプールのIPV4範囲リソースを管理するためのインターフェイスを提供します。作成、更新、または削除できます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  IDプールIPV4範囲プロパティのリスト。  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  IDプールのIPV4範囲リソースの望ましい状態を示します。`present` は、データプロパティがOneViewに準拠していることを保証します。`absent`は、存在する場合、OneViewからリソースを削除します。  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  ETag検証が有効になっている場合、リソースの現在のETagがデータで提供されているETagと一致する場合にのみ、リクエストが条件付きで処理されます。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| id_pools_ipv4_range   | OneView IDプールIPV4範囲に関する情報を持っています。|  状態 'present'nullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_id_pools_ipv4_range_facts
1つ以上のOneView IDプールIPV4範囲に関する情報を取得します。

#### 概要
 OneViewから1つ以上のIDプールIPV4範囲に関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 4.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  IDプールIPV4範囲名。  |
| options  |   No  |  | |  IPv4範囲および関連リソースに関する追加の情報を収集するオプションを表示します。可能なオプション: `allocatedFragments` は、範囲内で割り当てられたすべてのフラグメントを取得します。`freeFragments`は、IPv4範囲内のすべての空きフラグメントを取得します。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |
| uri  |   No  |  | |  IDプールIPV4範囲IDまたはURI。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| id_pools_ipv4_ranges   | IDプールIPV4範囲に関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |
| id_pools_ipv4_ranges_allocated_fragments   | IDプールIPV4範囲に割り当てられたフラグメントに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |
| id_pools_ipv4_ranges_free_fragments   | ID Pools IPV4 Range Freeフラグメントに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_id_pools_ipv4_subnet
OneView IDプールのIPV4サブネットリソースを管理します。

#### 概要
 OneView IDプールのIPV4リソースリソースを管理します。作成、更新、または削除できます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 4.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  IDプールIPV4サブネットプロパティを持つリスト。  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  IDプールIPV4サブネットリソースの望ましい状態を示します。`present` は、データプロパティがOneViewに準拠していることを保証します。`absent`は、存在する場合、OneViewからリソースを削除します。  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  ETag検証が有効になっている場合、リソースの現在のETagがデータで提供されているETagと一致する場合にのみ、リクエストが条件付きで処理されます。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| id_pools_ipv4_subnet   | OneView IDプールIPV4サブネットに関する情報を持っています。|  状態 'present'nullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_id_pools_ipv4_subnet_facts
1つ以上のOneView IDプールIPV4サブネットに関するファクトを取得します。

#### 概要
 OneViewから1つ以上のIDプールIPV4サブネットに関するファクトを取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 2.0.1

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  IDプールIPV4サブネット名。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |
| uri  |   No  |  | |  IDプールIPV4サブネットIDまたはURI。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| id_pools_ipv4_subnets   | IDプールIPV4サブネットに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_interconnect
OneViewインターコネクトリソースを管理します。

#### 概要
 インターコネクトリソースを管理するインターフェイスを提供します。電源状態、UIDライト状態の変更、デバイスのリセット、ポート保護のリセット、相互接続ポートの更新ができます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 3.3.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| ip  |   No  |  | |  インターコネクトIPアドレス。  |
| name  |   No  |  | |  インターコネクト名。  |
| ports  |   No  |  | |  更新するポートを表示します。このオプションは`update_ports` 状態と一緒に使用する必要があります。  |
| state  |   |  | <ul> <li>powered_on</li>  <li>powered_off</li>  <li>uid_on</li>  <li>uid_off</li>  <li>device_reset</li>  <li>update_ports</li>  <li>reset_port_protection</li>  <li>reconfigured</li> </ul> |  インターコネクトリソースの望ましい状態を示します。`powered_on`は、電源をオンにします。`powered_off`は、電源をオフにします。`uid_on`は、UIDライトをオンにします。`uid_off`は、UIDライトをオフにします。`device_reset`は、デバイスのリセットを実行します。`update_ports`は、相互接続ポートを更新します。`reset_port_protection`は、ポート保護のリセットをトリガーします。`reconfigured`は、相互接続にアプライアンスの構成を再適用します。これには、エンクロージャーによるインターコネクト追加の一部として実行されたのと同じ構成手順の実行が含まれます。  |


 
#### 例

```yaml

- name: 「0000A66102、インターコネクト2」という名前のインターコネクトの電源をオフにします
  oneview_interconnect:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: 'powered_off'
    name: '0000A66102, interconnect 2'

- name: 「0000A66102、インターコネクト2」という名前のインターコネクトのUIDライトを「オン」にします
  oneview_interconnect:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: 'uid_on'
    name: '0000A66102, interconnect 2'

- name: IP 172.18.1.114と一致するインターコネクトのUIDランプを「オフ」にします
  oneview_interconnect:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: 'uid_on'
    ip: '172.18.1.114'

- name: IP 172.18.1.114と一致するインターコネクトを再構成します
  oneview_interconnect:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: 'reconfigured'
    ip: '172.18.1.114'

```



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| interconnect   | OneViewインターコネクトに関する情報を持っています。|  常時。nullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_interconnect_facts
1つ以上のOneViewインターコネクトに関する情報を取得します。

#### 概要
 OneViewから1つ以上のインターコネクトに関するファクトを取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 3.3.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  インターコネクト名。  |
| options  |   No  |  | |  インターコネクトに関する追加の情報を収集するオプションを表示します。可能なオプション: `nameServers`は、インターコネクトの名前付きサーバーを取得します。`statistics`は、インターコネクトから統計を取得します。`portStatistics`は、インターコネクト上の指定されたポート名の統計を取得します。`subPortStatistics`は、インターコネクトのサブポート統計を取得します。`ports`は、すべての相互接続ポートを取得します。`port`は、特定の相互接続ポートを取得します。`pluggableModuleInformation`は、すべてのSFP情報を取得します。  追加のファクトを収集するには、インターコネクト名を通知する必要があります。それ以外の場合、これらのオプションは無視されます。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| interconnect_name_servers   | インターコネクトの名前付きサーバー。|  要求された場合、ただしnullの場合があります。|  list |
| interconnect_pluggable_module_information   | プラグインされたSFP情報。|  要求された場合、ただしnullの場合があります。|  list |
| interconnect_port   | インターコネクトポート。|  要求された場合、ただしnullの場合があります。|  dict |
| interconnect_port_statistics   | インターコネクト上の指定されたポート名の統計。|  要求された場合、ただしnullの場合があります。|  dict |
| interconnect_ports   | すべてのインターコネクトポート。|  要求された場合、ただしnullの場合があります。|  list |
| interconnect_statistics   | インターコネクト統計に関するすべてのOneViewの情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| interconnect_subport_statistics   | インターコネクトのサブポート統計。|  要求された場合、ただしnullの場合があります。|  dict |
| interconnects   | インターコネクトのリスト。|  常時、ただしnullの場合があります。|  list |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_interconnect_link_topology_facts
OneView Interconnect Linkトポロジに関する情報を取得します。

#### 概要
 OneViewからインターコネクトリンクトポロジに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 3.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  インターコネクトリンクトポロジの名前。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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

- name: 
  oneview_interconnect_link_topology_facts:
    config: "{{ config_path }}"
    name: "Name of the Interconnect Link Topologies"

- debug: var=interconnect_link_topologies

```



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| interconnect_link_topologies   | インターコネクトリンクトポロジーに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

-このリソースは、HPE Synergyでのみ利用可能です。

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_interconnect_type_facts
1つ以上のOneViewインターコネクトタイプに関する情報を取得します。

#### 概要
 OneViewから1つ以上のインターコネクトタイプに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  インターコネクトタイプ名。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| interconnect_types   | インターコネクトタイプに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_internal_link_set_facts
OneView内部リンクセットに関する情報を取得します。

#### 概要
 OneViewから内部リンクセットに関する情報を取得します。すべての内部リンクセットを取得するか、名前でフィルタリングすることができます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  内部リンクセットの名前。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。 `query`: 返されるリソースのリストを絞り込むための一般的なクエリ文字列。 `fields`: 結果セットで返されるフィールドを指定します。 `view`: 定義済みのビューの名前を指定して、リソースまたはコレクションの属性の特定のサブセットを返します。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| internal_link_sets   | 内部リンクセットに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- このリソースは、APIバージョン300以降で使用可能です

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_label
OneViewラベルを管理します。

#### 概要
リソースに付与されたラベルを管理します。

#### 要件 (モジュールを実行するホスト)
  * python >= 3.4.2
  * hpeOneView >= 6.1.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  ラベル名  |
| uri | No |  | | ラベルURI  |
| resourceUri | No | | リソースURI   |


#### 例

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

#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| label   | ラベルを持っているリソース |  常に |  dict |

#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---

## oneview_label_facts
OneViewラベル情報を取得します。

#### 概要
ラベルリストを取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 3.4.2
  * hpeOneView >= 6.1.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルタリング、およびソートするためのパラメーターリスト。  次のパラメータが使用できます。 `start`: 0ベースインデックスとしたときの最初のアイテム。 `count`: 取得するリソース数。 `filter`: 取得するアイテムをフィルタリングするためのフィルター/クエリ文字列。 `sort`: 返り値の順番のソート。|
| name  |   No  |  | |  ラベル名  |
| resourceUri | No | | リソースURI   |


#### 例

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

#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| labels   | ラベルのリスト |  常に、nullの場合もあり |  dict |


## oneview_logical_downlinks_facts
1つ以上のOneView論理ダウンリンクに関する情報を取得します。

#### 概要
 OneViewから1つ以上の論理ダウンリンクに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 2.0.1

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| excludeEthernet  |   No  |  | |  論理ダウンリンクからイーサネットネットワークに関する情報を除外します。  |
| name  |   No  |  | |  論理ダウンリンク名。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| logical_downlinks   | 論理ダウンリンクのリスト。|  常時、ただしnullの場合があります。|  list |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_logical_enclosure
OneView論理エンクロージャリソースを管理します。

#### 概要
 論理エンクロージャリソースを管理するためのインターフェイスを提供します。作成、更新、ファームウェアの更新、ダンプの実行、構成スクリプトの更新、構成の再適用、グループからの更新、または削除ができます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  論理エンクロージャーのプロパティとその関連状態のリスト。  |
| state  |   Yes  |  | <ul> <li>present</li>  <li>firmware_updated</li>  <li>script_updated</li>  <li>dumped</li>  <li>reconfigured</li>  <li>updated_from_group</li>  <li>absent</li> </ul> |  論理エンクロージャリソースの望ましい状態を示します。`present`は、データプロパティがOneViewに準拠していることを保証します。属性`newName`を指定してエンクロージャーの名前を変更できます。`firmware_updated`は、論理エンクロージャーのファームウェアを更新します。`script_updated`は、論理エンクロージャー構成スクリプトを更新します。`dumped`は、論理エンクロージャーのサポートダンプを生成します。`reconfigured`は、論理エンクロージャーに関連付けられているすべてのエンクロージャーを再構成します。`updated_from_group`は、論理エンクロージャーをエンクロージャーグループと一致させます。`absent`は、存在する場合、OneViewからリソースを削除します。  |


 
#### 例

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
            If-Match: '*'
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
            If-Match: '*'
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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| configuration_script   | 論理エンクロージャー構成スクリプトに関する情報を持っています。|  状態が 'script_updated'。nullの場合があります。|  dict |
| generated_dump_uri   | 論理エンクロージャーで生成されたサポートダンプURIに関する情報を持っています。|  状態が 'dumped'。nullの場合があります。|  dict |
| logical_enclosure   | OneView論理エンクロージャーに関する情報を持っています。| 状態が 'present'、'firmware_updated'、'reconfigured、'updated_from_group'、'absent'。nullの場合があります。|  dict |


#### 注記

- `absent`状態と`present`状態を介して行われる論理エンクロージャーの作成は、HPE Synergyでのみ使用できます。

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_logical_enclosure_facts
1つ以上のOneView論理エンクロージャーに関する情報を取得します。

#### 概要
 OneViewから1つ以上の論理エンクロージャーに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  論理エンクロージャー名。  |
| options  |   No  |  | |  論理エンクロージャーおよび関連リソースに関する追加の情報を収集するオプションを表示します。可能なオプション: script。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| logical_enclosure_script   | 論理エンクロージャーのスクリプトに関する情報を持っています。|  必要な場合、ただしnullの場合があります。|  dict |
| logical_enclosures   | 論理エンクロージャーに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_logical_interconnect
OneView論理インターコネクトリソースを管理します。

#### 概要
 論理インターコネクトリソースを管理するためのインターフェイスを提供します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.6.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  オプションを表示します。  |
| state  |   |  | <ul> <li>compliant</li>  <li>ethernet_settings_updated</li>  <li>internal_networks_updated</li>  <li>settings_updated</li>  <li>forwarding_information_base_generated</li>  <li>qos_aggregated_configuration_updated</li>  <li>snmp_configuration_updated</li>  <li>port_monitor_updated</li>  <li>configuration_updated</li>  <li>firmware_installed</li>  <li>telemetry_configuration_updated</li> </ul> |  論理インターコネクトリソースの望ましい状態を示します。`compliant`は、論理インターコネクトを一貫した状態に戻します。`ethernet_settings_updated`は、論理インターコネクトのイーサネットインターコネクト設定を更新します。`internal_networks_updated`は、論理インターコネクトの内部ネットワークを更新します。この操作は冪等ではありません。`settings_updated`は、論理インターコネクトの設定を更新します。`forwarding_information_base_generated`は、論理インターコネクトの転送情報ベースダンプファイルを生成します。この操作は非冪等で非同期です。「qos_aggregated_configuration_updated」は、論理インターコネクトのQoS集約構成を更新します。`snmp_configuration_updated`は、論理インターコネクトのSNMP設定を更新します。`port_monitor_updated`は、論理インターコネクトのポートモニター設定を更新します。「configuration_updated」は、すべての管理対象インターコネクトに論理インターコネクト構成を非同期的に適用または再適用します。この操作は冪等ではありません。`firmware_installed`は、ファームウェアを論理インターコネクトにインストールします。ファームウェアの更新でサポートされる3つの操作は、ステージング（ファームウェアをインターコネクトにアップロード）、アクティベート（ファームウェアをインターコネクトにインストール）、およびアップデート（ステージングとアクティベートを順番に行う）です。それらはすべて非冪等です。`telemetry_configuration_updated`は、論理インターコネクトのテレメトリ構成を更新します。`scopes_updated`は、論理インターコネクトに関連付けられたスコープを更新します。  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  ETag検証が有効になっている場合、リソースの現在のETagがデータで提供されているETagと一致する場合にのみ、リクエストが条件付きで処理されます。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| interconnect_fib   | 転送情報ベースに関するOneViewの情報を持っています。|  状態が'forwarding_information_base_generated'、ただしnullの場合があります。|  dict |
| li_firmware   | インストールされたファームウェアに関するOneViewの情報を持っています。|  状態が'firmware_installed'、ただし、nullの場合があります。|  dict |
| port_monitor   | ポートモニターの構成に関するOneViewの情報がある|  状態が'port_monitor_updated'、ただし、nullの場合があります。|  dict |
| qos_configuration   | QoS構成に関するOneViewの情報を持っています。|  状態が「qos_aggregated_configuration_updated」状態ですが、nullの場合があります。|  dict |
| scope_uris   | 指定された論理インターコネクトが挿入されるスコープURIを持っています。|  状態が'scopes_updated’、ただし、nullの場合があります。|  dict |
| snmp_configuration   | SNMP構成に関するOneViewの情報を持っています。|  状態が'snmp_configuration_updated'、ただし、nullの場合があります。|  dict |
| igmp_settings   | IGMP設定情報 |  igmp_settings_updatedというステータスまたはnull |  dict |
| port_flap_settings   | ポートフラップ設定情報 |  port_flap_settings_updatedというステータスまたはnull |  dict |
| li_inconsistency_report   | 不整合情報 |  bulk_inconsistency_validatedというステータスまたはnull |  dict |
| storage_volume_template   | 論理インターコネクトに関するOneViewの情報を持っています。|  状態が 'compliant'、'ethernet_settings_updated'、'internal_networks_updated'、'settings_updated'、'configuration_updated'、ただし、nullの場合があります。|  dict |
| telemetry_configuration   | テレメトリ構成に関するOneViewの情報を持っています。|  状態が'telemetry_configuration_updated'、ただし、nullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_logical_interconnect_facts
1つ以上のOneView論理インターコネクトに関する情報を取得します。

#### 概要
 1つ以上のOneView論理インターコネクトに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpeOneView >= 5.6.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  論理インターコネクト名。  |
| options  |   No  |  | |  論理インターコネクトに関する追加の情報を収集するオプションを表示します。可能なオプション: `qos_aggregated_configuration`は、論理インターコネクトのQoS集約構成を取得します。`snmp_configuration`は、論理インターコネクトのSNMP設定を取得します。`port_monitor`は、論理インターコネクトのポートモニター構成を取得します。「internal_vlans」は、論理インターコネクト上のプロビジョニングされたネットワークの内部VLAN IDを取得します。`forwarding_information_base`は、論理インターコネクトの転送情報ベースデータを取得します。`firmware`は、論理インターコネクトのインストール済みファームウェアを取得します。`unassigned_ports`は、アナライザーポートへの割り当てに適格なメンバー相互接続からポートのコレクションを取得します。`unassigned_uplink_ports`は、アナライザーポートへの割り当てに適格なメンバー相互接続からアップリンクポートのコレクションを取得します。`telemetry_configuration`は、論理インターコネクトのテレメトリ構成を取得します。`ethernet_settings`は、論理インターコネクトのイーサネット相互接続設定を取得します。- これらのオプションは、`name`が指定されている場合にのみ有効です。それ以外の場合は無視されます。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| ethernet_settings   |  イーサネットインターコネクト設定。|  要求された場合、ただしnullの場合があります。|  dict |
| firmware   | 論理インターコネクト用にインストールされたファームウェア。|  要求された場合、ただしnullの場合があります。|  dict |
| forwarding_information_base   | 論理インターコネクトの転送情報ベースデータ。|  要求された場合、ただしnullの場合があります。|  dict |
| internal_vlans   | 論理インターコネクト上のプロビジョニングされたネットワークの内部VLAN ID。|  要求された場合、ただしnullの場合があります。|  dict |
| logical_interconnects   | 論理インターコネクトのリスト。|  常時、ただしnullの場合があります。|  list |
| port_monitor   | 論理インターコネクトのポートモニター構成。|  要求された場合、ただしnullの場合があります。|  dict |
| qos_aggregated_configuration   | 論理インターコネクトのQoS集約構成。|  要求された場合、ただしnullの場合があります。|  dict |
| snmp_configuration   | 論理インターコネクトのSNMP構成。|  要求された場合、ただしnullの場合があります。|  dict |
| igmp_settings   | 論理インターコネクトのIGMP情報 |  要求された場合、ただしnullの場合があります。 |  dict |
| telemetry_configuration   | 論理インターコネクトのテレメトリー構成。|  要求された場合、ただしnullの場合があります。|  dict |
| unassigned_ports   | 論理インターコネクトのアナライザーポートへの割り当てに適格なメンバーインターコネクトからのポートのコレクション。|  要求された場合、ただしnullの場合があります。|  dict |
| unassigned_uplink_ports   | 論理インターコネクト上のアナライザーポートへの割り当てに適格なメンバーインターコネクトからのアップリンクポートのコレクション。|  要求された場合、ただしnullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_logical_interconnect_group
OneView論理インターコネクトグループリソースを管理します。

#### 概要
 論理インターコネクトグループリソースを管理するためのインターフェイスを提供します。作成、更新、または削除できます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  論理インターコネクトグループのプロパティを表示します。  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  論理インターコネクトグループリソースの望ましい状態を示します。`present` は、データプロパティがOneViewに準拠していることを保証します。`absent`は、存在する場合、OneViewからリソースを削除します。  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  ETag検証が有効になっている場合、リソースの現在のETagがデータで提供されているETagと一致する場合にのみ、リクエストが条件付きで処理されます。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| logical_interconnect_group   | OneView論理インターコネクトグループに関する情報を持っています。|  状態 'present'nullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_logical_interconnect_group_facts
1つ以上のOneView論理インターコネクトグループに関するファクトを取得します

#### 概要
 OneViewから1つ以上の論理インターコネクトグループに関するファクトを取得します

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   |  | |  論理インターコネクトグループ名。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| logical_interconnect_groups   | 論理インターコネクトグループに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_logical_switch
OneView論理スイッチリソースを管理します。

#### 概要
 論理スイッチリソースを管理するためのインターフェイスを提供します。作成、更新、削除、または更新できます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 4.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  論理スイッチのプロパティを表示します。`logicalSwitchGroupName`または `logicalSwitchGroupUri`で論理スイッチグループを設定できます。  |
| state  |   Yes  |  | <ul> <li>present</li>  <li>updated</li>  <li>absent</li>  <li>refreshed</li> </ul> |  論理スイッチリソースの望ましい状態を示します。`present`は、論理スイッチが存在しない場合に作成します。論理スイッチを更新するには、代わりに `updated`状態を使用します。`updated`は論理スイッチが更新されることを保証します。現在、OneViewは、論理スイッチの資格情報、スコープ、および名前の更新のみをサポートしています。論理スイッチの名前を変更するには、データの`newName`を指定する必要があります。更新操作は冪等ではありません。`absent`は、存在する場合、OneViewからリソースを削除します。`refreshed`は、論理スイッチのトップオブラックスイッチを回収します。この操作は冪等ではありません。  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  ETag検証が有効になっている場合、リソースの現在のETagがデータで提供されているETagと一致する場合にのみ、リクエストが条件付きで処理されます。  |


 
#### 例

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
      scopeUris: # このフィールドは、OneView 3.10までのみ利用可能です
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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| logical_switch   | OneView論理スイッチに関する情報を持っています。|  状態が 'present'、'updated'、'refreshed'。nullの場合があります。|  dict |


#### 注記

- このリソースは、C7000エンクロージャーでのみ使用可能です

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_logical_switch_facts
1つ以上のOneView論理スイッチに関する情報を取得します。

#### 概要
 OneViewから1つ以上の論理スイッチに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 2.0.1

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  論理スイッチ名。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| logical_switches   | 論理スイッチに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- このリソースは、C7000エンクロージャーでのみ使用可能です

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_logical_switch_group


#### 概要
 論理スイッチグループリソースを管理するためのインターフェイスを提供します。追加、更新、削除できます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  論理スイッチグループのプロパティとそれに関連付けられた状態を表示します。  |
| state  |   Yes  |  | <ul> <li>present</li>  <li>absent</li> </ul> |  論理スイッチグループリソースの望ましい状態を示します。`present` は、データプロパティがOneViewに準拠していることを保証します。`absent`は、存在する場合、OneViewからリソースを削除します。  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  ETag検証が有効になっている場合、リソースの現在のETagがデータで提供されているETagと一致する場合にのみ、リクエストが条件付きで処理されます。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| logical_switch_group   | 論理スイッチグループに関するOneViewの情報を持っています。|  状態 'present'nullの場合があります。|  dict |


#### 注記

- このリソースは、C7000エンクロージャーでのみ使用可能です

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_logical_switch_group_facts
OneView論理スイッチグループに関する情報を取得します。

#### 概要
 OneViewの論理スイッチグループに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  論理スイッチグループ名。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| logical_switch_groups   | 論理スイッチグループに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- このリソースは、C7000エンクロージャーでのみ使用可能です

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_login_detail_facts
ログインの詳細に関する情報を取得します

#### 概要
 oneviewからログインの詳細に関する情報を取得します

#### 要件 (モジュールを実行するホスト)
  * hpOneView >= 4.3.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |


 
#### 例

```yaml

- name: Gather facts about login details
  oneview_login_detail_facts:
    config: "{{ config }}"
    delegate_to: localhost

- debug: var=login_details

```



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| login_details   | Lists all the login details |  常時、ただし、nullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_managed_san
OneView Managed SANリソースを管理します。

#### 概要
 Managed SANリソースを管理するためのインターフェイスを提供します。管理対象SANを更新し、更新状態を設定し、SANエンドポイントCSVファイルを作成し、予期しないゾーニングの問題レポートを作成できます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  管理対象SANプロパティとその関連状態を表示します。警告: 'present' 状態では、publicAttributesの内容が既存のリストを置き換えます。そのため、指定されたリストからパブリック属性を除外すると、情報上リストが削除されます。  |
| state  |   Yes  |  | <ul> <li>present</li>  <li>refresh_state_set</li>  <li>endpoints_csv_file_created</li>  <li>issues_report_created</li> </ul> |  管理対象SANリソースの望ましい状態を示します。`present`は、データプロパティがOneViewに準拠していることを保証します。`refresh_state_set`は、管理対象SANの更新状態を更新します。`endpoints_csv_file_created`は、SANエンドポイントCSVファイルを作成します。`issues_report_created`は、SANの予期しないゾーニングレポートを作成します。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| managed_san   | 管理されているSANの情報を保持します。 |  状態は'present'または'refresh_state_set'が戻されますが、nullの場合もあります。 |  dict |
| managed_san_endpoints   | 作成されたSANエンドポイントCSVをの情報を保持します。 |  状態は'endpoints_csv_file_created'が戻りますが、nullの場合もあります。 |  dict |
| managed_san_issues   | 予期せぬゾーニングの情報を保持します。 |  状態は'issues_report_created'が戻りますが、nullの場合もあります。 |  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_managed_san_facts
OneView Managed に関する情報を取得します。

#### 概要
 OneView Managed SANに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  管理対象SANの名前。  |
| options  |   No  |  | |  管理対象SANに関する追加の情報を収集するオプションを表示します。可能なオプション: 「endpoints」は、名前で識別されるSAN内のエンドポイントのリストを取得します。`wwn`は、情報に基づいたWWN`locate`に関連付けられた管理対象SANのリストを取得します。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`query`: 返されるリソースのリストを絞り込むための一般的なクエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| managed_san_endpoints   | 名前で識別されるSAN内のエンドポイントのリスト。|  要求された場合、ただしnullの場合があります。|  dict |
| managed_sans   | 管理対象SANのリスト。|  常時、ただしnullの場合があります。|  list |
| wwn_associated_sans   | 提供されたWWNとSANの間の関連付けのリスト。|  要求された場合、ただしnullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_network_set
OneView ネットワークセットリソースを管理します。

#### 概要
 ネットワークセットリソースを管理するためのインターフェイスを提供します。作成、更新、または削除できます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 4.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  ネットワークセットプロパティのリスト。  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  ネットワークセットリソースの望ましい状態を示します。`present`は、データプロパティがOneViewに準拠していることを保証します。`absent`は、存在する場合、OneViewからリソースを削除します。  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  ETag検証が有効になっている場合、リソースの現在のETagがデータで提供されているETagと一致する場合にのみ、リクエストが条件付きで処理されます。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
OneViewネットワークセットに関する情報を取得します。|  状態は'present'ですが、nullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_network_set_facts
OneViewネットワークセットに関する情報を取得します

#### 概要
 OneViewからネットワークセットに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * hpOneView >= 2.0.1

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   |  | |  ネットワークセット名。  |
| options  |   |  | |  ネットワークセットに関する情報を収集するオプションを表示します。 Option allowed: `withoutEthernet`. オプション`withoutEthernet`は、イーサネットネットワークを除くnetwork_setsのリストを取得します。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| network_sets   | ネットワークセットに関するすべてのOneViewの情報を持っています。|  常時、ただし、空の場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_os_deployment_plan_facts
1つ以上のOS展開計画に関する情報を取得します。

#### 概要
 OneViewから1つ以上のOS展開計画に関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 3.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  OS展開計画名。  |
| options  |   No  |  | |  OS展開計画に関する情報を収集するためのオプションを表示します。Option allowed: `osCustomAttributesForServerProfile` オプション` osCustomAttributesForServerProfile`は、サーバープロファイル用に準備された編集可能なOSカスタム属性のリストを取得します。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| os_deployment_plan_custom_attributes   | サーバープロファイル形式のOs展開計画の編集可能なカスタム属性の情報を持っています。|  要求された場合、ただし、空の場合があります。|  dict |
| os_deployment_plans   | OS展開計画に関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_os_deployment_server
OneView展開サーバーリソースを管理します。

#### 概要
 展開サーバーリソースを管理するためのインターフェイスを提供します。作成、更新、または削除できます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 3.1.1

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  展開サーバープロパティのリスト。  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  展開サーバーリソースの望ましい状態を示します。`present` は、データプロパティがOneViewに準拠していることを保証します。`absent`は、存在する場合、OneViewからリソースを削除します。  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  ETag検証が有効になっている場合、リソースの現在のETagがデータで提供されているETagと一致する場合にのみ、リクエストが条件付きで処理されます。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| os_deployment_server   | 展開サーバーに関する情報を持っています。|  状態 'present'nullの場合があります。|  dict |


#### 注記

-次のデータについては、名前またはURIを指定できます: `mgmtNetworkName` または `mgmtNetworkUri`、および `applianceName` または `applianceUri`

- このリソースは、HPE Synergyでのみ利用可能です

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_os_deployment_server_facts
1つ以上のOS展開サーバーに関する情報を取得します。

#### 概要
 OneViewから1つ以上のOS展開サーバーに関するファクトを取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 3.1.1

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  OS展開サーバー名。  |
| options  |   No  |  | |  OS展開サーバーと関連リソースに関する追加の情報を収集するオプションを表示します。可能なオプション: `networks`、`appliances`、`appliance`。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。`query`: 返されるリソースのリストを絞り込むための一般的なクエリ文字列。`fields`: 結果セットで返されるフィールドを指定します。`view`: 定義済みのビューの名前を指定して、リソースまたはコレクションの属性の特定のサブセットを返します。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| os_deployment_server_appliance   | 特定のイメージストリーマーリソースに関する情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| os_deployment_server_appliances   | すべてのイメージストリーマーリソースに関するすべてのOneViewの情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| os_deployment_server_networks   | OneViewネットワークに関するすべてのOneViewの情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| os_deployment_servers   | OS展開サーバーに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- このリソースは、HPE Synergyでのみ利用可能です

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_power_device
OneView Power Deviceリソースを管理します。

#### 概要
 電力供給デバイスのリソースを管理するためのインターフェイスを提供します。電源状態の追加、更新、削除、変更、UID状態の変更、状態の更新ができます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  パワーデバイスのプロパティとその関連状態を表示します。  |
| state  |   Yes  |  | <ul> <li>present</li>  <li>discovered</li>  <li>absent</li>  <li>power_state_set</li>  <li>refresh_state_set</li>  <li>uid_state_set</li> </ul> |  パワーデバイスリソースの望ましい状態を示します。`present` は、データプロパティがOneViewに準拠していることを保証します。`discovered`は、iPDUをOneViewに追加します。`absent`は、存在する場合、OneViewからリソースを削除します。`power_state_set`は、パワーデバイスの電力状態を設定します。`refresh_state_set`は、パワーデバイスのリフレッシュ状態を設定します。`uid_state_set`は、パワーデバイスのUID状態を設定します。  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  ETag検証が有効になっている場合、リソースの現在のETagがデータで提供されているETagと一致する場合にのみ、リクエストが条件付きで処理されます。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| power_device   | パワーデバイスに関するOneViewの情報を持っています。|  状態が 'present'、'discovered'、'power_state_set'、'refresh_state_set'、'uid_state_set'。nullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_power_device_facts
OneViewパワーデバイスに関する情報を取得します。

#### 概要
 OneViewから電力供給デバイスに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 2.0.1

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  パワーデバイス名。  |
| options  |   No  |  | |  パワーデバイスに関する追加の情報を収集するオプションをリストします。可能なオプション: `powerState`、`uidState`、`utilization`  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`query`: 返されるリソースのリストを絞り込むための一般的なクエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| power_device_power_state   | パワーデバイスの電源状態に関するすべての情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| power_device_uid_state   | パワーデバイスのUID状態に関するすべての情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| power_device_utilization   | パワーデバイスの利用に関するすべての情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| power_devices   | パワーデバイスに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_rack
OneViewラックリソースを管理します。

#### 概要
 ラックリソースを管理するためのインターフェイスを提供します。作成、更新、および削除できます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  ラックのプロパティを表示します。  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  ラックリソースの望ましい状態を示します。`present` は、データプロパティがOneViewに準拠していることを保証します。ラックの名前を変更するには、データの_newName_を指定する必要があります。`absent`は、存在する場合、OneViewからリソースを削除します。  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  ETag検証が有効になっている場合、リソースの現在のETagがデータで提供されているETagと一致する場合にのみ、リクエストが条件付きで処理されます。  |


 
#### 例

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
      width: 1200
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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| rack   | OneViewラックに関する情報を持っています。|  状態 'present'nullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_rack_facts
Rackリソースに関する情報を取得します。

#### 概要
 ラックリソースのリストを取得します。名前によるフィルターを使用して、特定のラックを取得できます。名前を指定すると、デバイストポロジに関する情報を取得できます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 2.0.1

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  ラック名。  |
| options  |   No  |  | |  追加の情報を取得します。 オプションとして'deviceTopology'が使えます。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| rack_device_topology   | ラックリソースのトポロジ情報を取得します。|  要求された場合、ただしnullの場合があります。|  dict |
| racks   | ラックに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_san_manager
OneView SAN Managerリソースを管理します。

#### 概要
 SAN Managerリソースを管理するためのインターフェイスを提供します。作成、更新、または削除できます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 3.1.1

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  SAN Managerプロパティを表示します。  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li>  <li>connection_information_set</li> </ul> |  アップリンクセットリソースの望ましい状態を示します。`present`は、データプロパティがOneViewに準拠していることを保証します。`absent`は、存在する場合、OneViewからリソースを削除します。`connection_information_set`は、SAN Managerの接続情報を更新します。この操作は冪等ではありません。  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  ETag検証が有効になっている場合、リソースの現在のETagがデータで提供されているETagと一致する場合にのみ、リクエストが条件付きで処理されます。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| san_manager   | SAN Managerに関するOneViewの情報を持っています。|  状態 'present'nullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_san_manager_facts
1つ以上のOneView SANマネージャーに関する情報を取得します。

#### 概要
 OneViewから1つ以上のSANマネージャーに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * hpOneView >= 2.0.1

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| params  |   |  | |  リソースのリストを区切り、フィルター、ソートするためのパラメーターのリスト。  可能なパラメーター: - `start`: 0から始まるインデックスを使用して返される最初のアイテム。 - `count`: 返されるリソースの数。 - `query`: 返されるリソースのリストを絞り込むための一般的なクエリ文字列。 - `sort`: 返されたデータセットのソート順。  |
| provider_display_name  |   |  | |  プロバイダーの表示名。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| san_managers   | SANマネージャーに関するOneViewのすべての情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_sas_interconnect
OneView SASインターコネクトリソースを管理します。

#### 概要
 SASインターコネクトを管理するためのインターフェイスを提供します。電源状態、UIDライト状態の変更、ソフトおよびハードリセットの実行、SASインターコネクト状態の更新ができます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   Yes  |  | |  SASインターコネクト名。  |
| state  |   |  | <ul> <li>powered_on</li>  <li>powered_off</li>  <li>uid_on</li>  <li>uid_off</li>  <li>soft_reset</li>  <li>hard_reset</li>  <li>refreshed</li> </ul> |  スイッチの望ましい状態を示します。`powered_on`は、電源をオンにします。`powered_off`は、電源をオフにします。`uid_on`は、UIDライトをオンにします。`uid_off`は、UIDライトをオフにします。`soft_reset`は、ソフトリセットを実行します。`hard_reset`は、ハードリセットを実行します。`refreshed`は、更新を実行します。  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  ETag検証が有効になっている場合、リソースの現在のETagがデータで提供されているETagと一致する場合にのみ、リクエストが条件付きで処理されます。  |


 
#### 例

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



#### 注記

- このリソースは、HPE Synergyでのみ利用可能です

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_sas_interconnect_facts
OneView SASインターコネクトに関する情報を取得します。

#### 概要
 OneView SASインターコネクトに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  SASインターコネクト名。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| sas_interconnects   | SASインターコネクトのリスト。|  常時、ただしnullの場合があります。|  list |


#### 注記

- このリソースは、HPE Synergyでのみ利用可能です

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_sas_interconnect_type_facts
OneView SASインターコネクトタイプに関する情報を取得します。

#### 概要
 OneViewからSASインターコネクトタイプに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  SASインターコネクトタイプの名前。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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
    config:   "{{ config }}"
    params:
      start: 0
      count: 3
      sort: 'name:descending'
      filter: "enclosureType='SY12000'"

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| sas_interconnect_types   | SASインターコネクトタイプに関するOneViewのすべての情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- このリソースは、HPE Synergyでのみ利用可能です

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_sas_logical_interconnect
OneView SAS論理インターコネクトリソースを管理します。

#### 概要
 SAS論理インターコネクトリソースを管理するためのインターフェイスを提供します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
SAS論理インターコネクトのプロパティとその関連状態を表示します。  |
| state  |   Yes  |  | <ul> <li>compliant</li>  <li>drive_enclosure_replaced</li>  <li>configuration_updated</li>  <li>firmware_updated</li> </ul> |  SAS論理インターコネクトリソースの望ましい状態を示します。`compliant`は、SAS論理インターコネクトのリストを一貫した状態に戻します。`Configuration_updated` は、SAS論理インターコネクト構成をすべての管理対象インターコネクトに非同期的に適用または再適用します。`firmware_updated`は、ファームウェアをSAS論理インターコネクトにインストールします。`drive_enclosure_replaced`は、ファームウェアをSAS論理インターコネクトにインストールします。* それらはすべて冪等ではありません。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| li_firmware   | 更新されたファームウェアに関するOneViewの情報を持っています。|  状態が'firmware_updated'、ただし、nullの場合があります。|  dict |
| sas_logical_interconnect   | SAS論理インターコネクトに関するOneViewの情報を持っています。|  状態が 'drive_enclosure_replaced'、'configuration_updated'、ただし、nullの場合があります。|  dict |


#### 注記

- このリソースは、HPE Synergyでのみ利用可能です

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_sas_logical_interconnect_facts
1つ以上のOneView SAS論理インターコネクトに関する情報を取得します。

#### 概要
 1つ以上のOneView SAS論理インターコネクトに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  SAS論理インターコネクト名。  |
| options  |   No  |  | |  SAS論理インターコネクトに関する追加の情報を収集するオプションを表示します。`firmware`は、SAS論理インターコネクトのインストール済みファームウェアを取得します。  これらのオプションは、name`が指定されている場合にのみ有効です。それ以外の場合は無視されます。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| sas_logical_interconnect_firmware   | SAS論理インターコネクト用にインストールされたファームウェア。|  要求された場合、ただしnullの場合があります。|  dict |
| sas_logical_interconnects   | SAS論理インターコネクトのリスト。|  常時、ただしnullの場合があります。|  list |


#### 注記

- このリソースは、HPE Synergyでのみ利用可能です

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_sas_logical_interconnect_group
OneView SAS論理インターコネクトグループリソースを管理します。

#### 概要
 SAS論理インターコネクトグループリソースを管理するためのインターフェイスを提供します。作成、更新、または削除できます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  SAS論理インターコネクトグループのプロパティを表示します。  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  SAS論理インターコネクトグループリソースの望ましい状態を示します。`present` は、データプロパティがOneViewに準拠していることを保証します。`absent`は、存在する場合、OneViewからリソースを削除します。  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  ETag検証が有効になっている場合、リソースの現在のETagがデータで提供されているETagと一致する場合にのみ、リクエストが条件付きで処理されます。  |


 
#### 例

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
      enclosureType: "SY12000"
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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| sas_logical_interconnect_group   | OneView SAS論理インターコネクトグループに関する情報を持っています。|  状態 'present'nullの場合があります。|  dict |


#### 注記

- このリソースは、HPE Synergyでのみ利用可能です

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_sas_logical_interconnect_group_facts
1つ以上のOneView SAS論理インターコネクトグループに関する情報を取得します。

#### 概要
 OneViewから1つ以上のSAS論理インターコネクトグループに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  SAS論理インターコネクトグループの名前。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| sas_logical_interconnect_groups   | SAS論理インターコネクトグループに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- このリソースは、HPE Synergyでのみ利用可能です

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_sas_logical_jbod_attachment_facts
1つ以上のOneView SAS論理JBODアタッチメントに関する情報を取得します。

#### 概要
 OneViewから1つ以上のSAS論理JBODアタッチメントに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 3.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  SAS論理JBODアタッチメントの名前。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| sas_logical_jbod_attachments   | SAS論理JBOD添付ファイルに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- このリソースは、HPE Synergyでのみ利用可能です

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_sas_logical_jbod_facts
OneViewから1つ以上のSAS論理JBODアタッチメントに関する情報を取得します。

#### 概要
 OneViewから1つ以上のSAS論理JBODに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 3.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  SAS論理JBODの名前。  |
| options  |   No  |  | |  SAS論理JBODおよび関連リソースに関する追加の情報を収集するオプションを表示します。可能なオプション: `drives`.  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| sas_logical_jbod_drives   | SAS論理JBODに割り当てられたドライブのリストに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |
| sas_logical_jbods   | SAS論理JBODに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- このリソースは、HPE Synergyでのみ利用可能です

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_scope
OneView Scopeリソースを管理します。

#### 概要
 スコープを管理するためのインターフェイスを提供します。リソース割り当てを追加または削除することにより、スコープを作成、更新、または削除でき、スコープメンバーシップを変更できます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  スコーププロパティを表示します。  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li>  <li>resource_assignments_updated</li> </ul> |  スコープリソースの望ましい状態を示します。`present`は、データプロパティがOneViewに準拠していることを保証します。`absent`は、存在する場合、OneViewからリソースを削除します。`resource_assignments_updated`は、リソースの割り当てを追加または削除することでスコープメンバーシップを変更します。この操作は冪等ではありません。  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  ETag検証が有効になっている場合、リソースの現在のETagがデータで提供されているETagと一致する場合にのみ、リクエストが条件付きで処理されます。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| scope   | スコープに関する情報を持っています。|  状態が 'present' および 'resource_assignments_updated'、ただし、nullの場合があります。|  dict |


#### 注記

- このリソースは、APIバージョン300以降で使用できます。

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_scope_facts
1つ以上のOneViewスコープに関する情報を取得します。

#### 概要
 OneViewから1つ以上のスコープに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 3.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  スコープの名前。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  params allowed: c(start): 0から始まるインデックスを使用して、最初に返されるアイテム、c(カウント): 返されるリソースの数。 c(クエリ）：返されるリソースのリストを絞り込むための一般的なクエリ文字列。 c（ソート）：返されたデータセットのソート順。 c（ビュー）：定義済みのビューの名前を指定して、リソースまたはコレクションの属性の特定のサブセットを返します。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| scopes   | スコープに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- このリソースは、APIバージョン300以降で使用できます。

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_server_hardware
OneViewサーバーハードウェアリソースを管理します。

#### 概要
 サーバーハードウェアリソースを管理するためのインターフェイスを提供します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  サーバーハードウェアのプロパティとその関連状態を表示します。  |
| state  |   Yes  |  | <ul> <li>present</li>  <li>absent</li>  <li>power_state_set</li>  <li>refresh_state_set</li>  <li>ilo_firmware_version_updated</li>  <li>ilo_state_reset</li>  <li>uid_state_on</li>  <li>uid_state_off</li>  <li>environmental_configuration_set</li>  <li>multiple_servers_added</li> </ul> |  サーバーハードウェアリソースの望ましい状態を示します。`present` は、データプロパティがOneViewに準拠していることを保証します。`absent`は、存在する場合、OneViewからリソースを削除します。`power_state_set`は、サーバーハードウェアの電源状態を設定します。`refresh_state_set`は、サーバーハードウェアの更新状態を設定します。`ilo_firmware_version_updated`は、サーバーハードウェアのiLOファームウェアバージョンを更新します。`ilo_state_reset`は、iLOの状態をリセットします。`uid_state_on`は、必要に応じて、UID状態を設定します。`uid_state_off`は、必要に応じて、UID状態をオフにします。`environmental_configuration_set`は、サーバーハードウェアの環境設定を設定します。`multiple_servers_added`は、複数のラックマウントサーバーを追加します。  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  ETag検証が有効になっている場合、リソースの現在のETagがデータで提供されているETagと一致する場合にのみ、リクエストが条件付きで処理されます。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| server_hardware   | サーバーハードウェアに関するOneViewの情報を持っています。|  状態が 'present'、'power_state_set'、'refresh_state_set'、'ilo_firmware_version_updated'。nullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_server_hardware_facts
OneViewサーバーハードウェアに関する情報を取得します。

#### 概要
 OneViewからサーバーハードウェアに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメータ     | 必須    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。設定ファイルをリンクさせる、または環境変数の使い方については注記を確認してください。  |
| name  |   No  |  | |  サーバーハードウェア名。  |
| uri  |   No  |  | |  サーバーハードウェアURI。  |
| options  |   No  |  | |  追加のサーバーハードウェア関連リソース情報を収集するためのオプションをセットします。オプションは`bios`, `javaRemoteConsoleUrl`、`environmentalConfig`、`iloSsoUrl`、`remoteConsoleUrl`、`utilization`、`firmware`、`firmwares`、 `physicalServerHardware`が選択できます。  |
| params  |   No  |  | |  リソースの区切る、フィルターする、ソートするためのパラメータをセットします。パラメータは0ベースのインデックスを最初に返す`start`、リソースの数を表す`count`、 戻り値をフィルタリングするための文字列を設定する`filter`、戻り値の順番を指定する`sort`が指定できます。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| server_hardware_bios   | サーバーハードウェアBIOSに関するすべての情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| server_hardware_env_config   | サーバーハードウェアの環境構成に関するすべての情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| server_hardware_firmware   | サーバーハードウェアファームウェアに関するすべての情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| server_hardware_firmwares   | すべてのサーバーにわたるファームウェアインベントリに関するすべての情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| server_hardware_ilo_sso_url   | サーバーハードウェアのiLO SSO URLに関する情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| server_hardware_java_remote_console_url   | サーバーハードウェアjavaリモートコンソールURLに関する情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| server_hardware_physical_server_hardware   | 'SDX'パーティションを記述するすべての情報を持っています。SDXエンクロージャーでのみ使用されます。|  要求された場合、ただしnullの場合があります。|  dict |
| server_hardware_remote_console_url   | サーバーハードウェアのリモートコンソールURLに関する情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| server_hardware_utilization   | サーバーハードウェアの使用率に関するすべての情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| server_hardware_utilization   | サーバーハードウェアに関するOneViewのすべての情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

-オプション`firmware`と`firmwares`は、APIバージョン300以降でのみ使用できます。

-オプション`physicalServerHardware`は、SDXエンクロージャーのAPIバージョン500以降でのみ使用できます。

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_server_hardware_type
OneViewサーバーのハードウェアタイプリソースを管理します。

#### 概要
 サーバーハードウェアタイプリソースを管理するためのインターフェイスを提供します。更新および削除できます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  サーバーハードウェアタイプのプロパティとその関連状態を表示します。  |
| state  |   Yes  |  | <ul> <li>present</li>  <li>absent</li> </ul> |  サーバーハードウェアタイプリソースの望ましい状態を示します。`present` は、データプロパティがOneViewに準拠していることを保証します。`absent`は、存在する場合、OneViewからリソースを削除します。  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  ETag検証が有効になっている場合、リソースの現在のETagがデータで提供されているETagと一致する場合にのみ、リクエストが条件付きで処理されます。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| server_hardware_type   | サーバーハードウェアタイプに関するOneViewの情報を持っています。|  状態 'present'nullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_server_hardware_type_facts
OneViewのサーバーハードウェアタイプに関する情報を取得します。

#### 概要
 OneViewのサーバーハードウェアタイプに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  サーバーハードウェアタイプ名。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| server_hardware_types   | サーバーハードウェアタイプに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_server_profile
OneViewサーバープロファイルリソースを管理します。

#### 概要
 OneViewサーバープロファイルリソースを管理します。  `present`状態では、サーバーハードウェアが提供されていない場合、サーバープロファイル設定に基づいてサーバーハードウェアが自動的に選択されます。

#### 要件 (モジュールを実行するホスト)
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| auto_assign_server_hardware  |   |  True  | <ul> <li>True</li>  <li>False</li> </ul> |  サーバーハードウェアを自動的に取得してサーバープロファイルに割り当てる必要があるかどうかを示すブール値。trueに設定すると、作成および更新は、使用可能なサーバーハードウェアがサーバープロファイルに割り当てられるようにします。falseに設定すると、作成中にサーバーハードウェアが指定されていない場合、プロファイルは'unassigned’として作成されます。プロファイルに既にサーバーハードウェアが割り当てられており、serverHardwareNameまたはserverHardwareUriがNoneに指定されている場合、サーバープロファイルのサーバーハードウェアは割り当てられていません。  |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  サーバープロファイルプロパティのリスト。  |
| params  |   No  |  | |  クエリパラメータを使用した辞書。  |
| state  |   |  present  | <ul> <li>present</li>  <li>absent</li>  <li>compliant</li> </ul> |  プレイブックの実行が終了するまでのサーバープロファイルリソースの望ましい状態を示します。`present` は、データプロパティがOneViewに準拠していることを保証します。この操作により、サーバープロファイルを構成する前にサーバーハードウェアの電源がオフになります。完了すると、サーバーハードウェアの電源が入ります。`absent`は、存在する場合、OneViewからリソースを削除します。このオプションが指定された場合、 `compliant`はサーバープロファイルをサーバープロファイルテンプレートに準拠させます。オフライン更新がある場合は、コンプライアンスの問題を修正する前にサーバーハードウェアをオフにし、その後でオンにします。  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  ETag検証が有効になっている場合、リソースの現在のETagがデータで提供されているETagと一致する場合にのみ、リクエストが条件付きで処理されます。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| compliance_preview   | サーバープロファイルをそのテンプレートと一致させるために必要な手動および自動更新に関するOneViewの情報を持っています。|  状態が 'present' および 'compliant'。|  dict |
| created   | サーバープロファイルが作成されたかどうかを示します。|  状態が 'present' および 'compliant'。 |  bool |
| serial_number   | サーバープロファイルのシリアル番号があります。|  状態が 'present' および 'compliant'。|  dict |
| server_hardware   | サーバーハードウェアに関するOneViewの情報を持っています。|  状態が 'present' および 'compliant'。|  dict |
| server_profile   | サーバープロファイルに関するOneViewの情報を持っています。|  状態が 'present' および 'compliant'。|  dict |


#### 注記

- 次のデータの場合、名前またはURIを指定できます：: enclosureGroupName または enclosureGroupUri、osDeploymentPlanName または osDeploymentPlanUri (osDeploymentSettings)、networkName または networkUri (接続リスト)、volumeName or volumeUri (volumeAttachmentsリスト)、volumeStoragePoolName または volumeStoragePoolUri (on the volumeAttachments list)、volumeStorageSystemName または volumeStorageSystemUri (volumeAttachmentsリスト)、serverHardwareTypeName または  serverHardwareTypeUri、enclosureName または enclosureUri、firmwareBaselineName または firmwareBaselineUri (ファームウェア)、sasLogicalJBODName または sasLogicalJBODUri (on the sasLogicalJBODs list) および initialScopeNames または initialScopeUris

volumeAttachmentsリストでvolumeUriをnullとして定義すると、ボリュームが存在しないことが認識されるため、サーバープロファイルとともに作成されます。このオプションを実行するたびに、新しいボリュームを作成する必要があることが常に認識されるため、これはべき等ではないことに注意してください。ボリュームをAnsibleで確保してから、目的のサーバープロファイルに割り当てることを強く推奨しています。存在しないため、サーバープロファイルとともに作成されます

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_server_profile_facts
OneViewサーバープロファイルに関する情報を取得します。

#### 概要
 OneViewからサーバープロファイルに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   |  | |  サーバープロファイル名。  |
| options  |   |  | |  サーバープロファイル関連のリソースに関する追加の情報を収集するオプションを表示します。可能なオプション: `schema`、`compliancePreview`、`profilePorts`、`messages`, `transformation`、`available_networks`、`available_servers`、`available_storage_system`、`available_storage_systems`、`available_targets`、`newProfileTemplate`、  `compliancePreview`、`messages`、`newProfileTemplate`、および`transformation`に関する情報を収集するには、サーバープロファイル名が必要です。それ以外の場合、これらのオプションは無視されます。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |
| uri  |   |  | |  サーバープロファイルuri。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| server_profile_available_networks   | サーバープロファイルで使用可能なイーサネットネットワーク、ファイバーチャネルネットワーク、およびネットワークセットのリストと、それぞれのポートに関するすべての情報と、それぞれのポートがあります。|  要求された場合、ただしnullの場合があります。|  dict |
| server_profile_available_servers   | 利用可能なサーバーのリストに関する情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| server_profile_available_storage_system   | サーバープロファイルで利用可能な特定のストレージシステムとそれに関連するボリュームに関する情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| server_profile_available_storage_systems   | サーバープロファイルで利用可能なストレージシステムとそれに関連するボリュームのリストに関する情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| server_profile_available_targets   | サーバープロファイルへの割り当てに使用できるターゲットサーバーと空のデバイスベイに関する情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| server_profile_compliance_preview   | サーバープロファイルをそのテンプレートに準拠させるために必要な手動および自動更新に関するすべての情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| server_profile_messages   | プロファイルに関連付けられたプロファイルステータスメッセージに関する情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| server_profile_new_profile_template   | サーバープロファイルテンプレートの生成に使用できる、サーバープロファイルから派生した情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| server_profile_profile_ports   | プロファイルに関連付けられているポートモデルに関する情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| server_profile_schema   | サーバープロファイルスキームに関する情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| server_profile_transformation   | 新しいサーバーハードウェアタイプやエンクロージャグループを提供することにより、既存のプロファイルの変換に関する情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| server_profiles   | サーバープロファイルに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_server_profile_template
OneViewサーバープロファイルテンプレートリソースを管理します。

#### 概要
 サーバープロファイルテンプレートを作成、変更、および削除するためのインターフェイスを提供します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  サーバープロファイルテンプレートのプロパティを含む辞書。  |
| params  |   No  |  | |  クエリパラメータを使用した辞書。  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  サーバープロファイルテンプレートの望ましい状態を示します。`present` は、データプロパティがOneViewに準拠していることを保証します。`absent`は、存在する場合、OneViewからリソースを削除します。  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  ETag検証が有効になっている場合、リソースの現在のETagがデータで提供されているETagと一致する場合にのみ、リクエストが条件付きで処理されます。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| server_profile_template   | サーバープロファイルテンプレートに関するOneViewの情報を持っています。|  状態 'present'nullの場合があります。|  dict |


#### 注記

-次のデータについては、名前またはURIを指定できます: enclosureGroupName or enclosureGroupUri, osDeploymentPlanName または osDeploymentPlanUri (osDeploymentSettings)、networkName または networkUri (接続リスト)、volumeName または volumeUri (volumeAttachmentsリスト)、volumeStoragePoolName または volumeStoragePoolUri (volumeAttachmentsリスト)、volumeStorageSystemName または volumeStorageSystemUri (volumeAttachmentsリスト)、serverHardwareTypeName または  serverHardwareTypeUri、enclosureName または enclosureUri、firmwareBaselineName または firmwareBaselineUri (ファームウェア)、sasLogicalJBODName または sasLogicalJBODUri (sasLogicalJBODsリスト) および initialScopeNames または initialScopeUris

volumeAttachmentsリストでvolumeUriをnullとして定義すると、ボリュームが存在しないことが認識されるため、サーバープロファイルとともに作成されます。このオプションを実行するたびに、新しいボリュームを作成する必要があることが常に認識されるため、これはべき等ではないことに注意してください。ボリュームをAnsibleで確保してから、目的のサーバープロファイルテンプレートに割り当てることを強く推奨しています。

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_server_profile_template_facts
OneViewからサーバープロファイルテンプレートに関する情報を取得します。

#### 概要
 OneViewからサーバープロファイルテンプレートに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   |  | |  サーバープロファイルテンプレート名。  |
| options  |   |  | |  サーバープロファイルテンプレートリソースに関する追加の情報を収集するオプションを表示します。可能なオプション: `new_profile`、`transformation`、`available_networks`。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |
| uri  |   |  | |  サーバープロファイルテンプレートuri。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| new_profile   | このテンプレートに基づいた構成を持つプロファイルオブジェクト。|  要求された場合、ただしnullの場合があります。|  dict |
| server_profile_template_available_networks   | サーバープロファイルで使用可能なイーサネットネットワーク、ファイバーチャネルネットワーク、およびネットワークセットのリストと、それぞれのポートに関するすべての情報と、それぞれのポートがあります。|  要求された場合、ただしnullの場合があります。|  dict |
| server_profile_templates   | サーバープロファイルテンプレートに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- オプション `transformation`はAPIバージョン300以降でのみ利用可能です。

- オプション `available_networks`はAPIバージョン600以降でのみ利用可能です。

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_storage_pool
OneViewストレージプールリソースを管理します。

#### 概要
 ストレージプールリソースを管理するためのインターフェイスを提供します。追加および削除できます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 4.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  ストレージプールのプロパティとその関連状態を表示します。  |
| state  |   Yes  |  | <ul> <li>present</li>  <li>absent</li> </ul> |  ストレージプールリソースの望ましい状態を示します。`present` は、データプロパティがOneViewに準拠していることを保証します。API500以降では、状態を更新することのみが可能です。`absent`は、存在する場合、OneViewからリソースを削除します。API500以降、不在状態は不変です。  |


 
#### 例

```yaml

- name: Create a Storage Pool (prior to API500)
  oneview_storage_pool:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
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
    api_version: 2200
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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| storage_pool   | ストレージプールに関するOneViewの情報を持っています。|  'present'の状態ですが、nullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_storage_pool_facts
1つ以上のストレージプールに関する情報を取得します。

#### 概要
 OneViewから1つ以上のストレージプールに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 4.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  ストレージプール名。  |
| options  |   No  |  | |  ストレージプールに関する追加の情報を収集するオプションを表示します。可能なオプション: `reachableStoragePools`は、ネットワークパラメーターに基づいて到達可能なストレージプールのリストを取得します。ネットワークパラメータが指定されていない場合は、すべてが取得されます。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| storage_pools   | ストレージプールに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |
Reachableストレージプールに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_storage_system
OneViewストレージシステムリソースを管理します。

#### 概要
 ストレージシステムリソースを管理するためのインターフェイスを提供します。追加、更新、削除できます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  ストレージシステムのプロパティとその関連状態を表示します。  |
| state  |   Yes  |  | <ul> <li>present</li>  <li>absent</li> </ul> |  ストレージシステムリソースの望ましい状態を示します。`present` は、データプロパティがOneViewに準拠していることを保証します。`absent`は、存在する場合、OneViewからリソースを削除します。  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  ETag検証が有効になっている場合、リソースの現在のETagがデータで提供されているETagと一致する場合にのみ、リクエストが条件付きで処理されます。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| storage_system   | ストレージシステムに関するOneViewの情報を持っています。|  状態 'present'nullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_storage_system_facts
OneViewストレージシステムに関する情報を取得します。

#### 概要
 OneViewからストレージシステムに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 4.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   |  | |  ストレージシステム名。  |
| options  |   |  | |  ストレージシステムと関連リソースに関する追加の情報を収集するオプションを表示します。可能なオプション: `hostTypes`は、サポートされているホストタイプのリストを取得します。`storagePools`は、指定されたストレージシステムに属するストレージプールのリストを取得します。`reachablePorts`は、ストレージシステムの到達可能なポートのリストを取得します。`params`を受け入れます。追加の `networks`リストパラメータを使用して、これらのみの検索を制限できます。`templates`は、ストレージシステムに属するストレージテンプレートのリストを取得します。  `storagePools`、`reachablePorts`、および`templates`に関する情報を収集するには、引数`name`、`ip_hostname`、または`hostname`のいずれかを通知する必要があります。それ以外の場合、このオプションは無視されます。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |
| storage_hostname  |   |  | |  ストレージシステムのIPまたはホスト名。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| storage_system_host_types   | サポートされているホストタイプに関するすべてのOneViewの情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| storage_system_pools   | ストレージシステム-ストレージプールに関するすべてのOneViewの情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| storage_system_reachable_ports   | ストレージシステムの到達可能ポートに関するすべてのOneViewの情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| storage_system_templates   | ストレージシステム-ストレージテンプレートに関するすべてのOneViewの情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| storage_systems   | ストレージシステムに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_storage_volume_attachment
指定されたサーバープロファイルから余分なプレゼンテーションを削除するためのインターフェイスを提供します。

#### 概要
 指定されたサーバープロファイルから余分なプレゼンテーションを削除するためのインターフェイスを提供します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 2.0.1

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| server_profile  |   Yes  |  | |  サーバープロファイル名またはサーバープロファイルURI |
| state  |   Yes  |  | <ul> <li>extra_presentations_removed</li> </ul> |  ストレージボリュームアタッチメントの望ましい状態を示します。`extra_presentations_removed`は、指定されたサーバープロファイルから余分なプレゼンテーションを削除します。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| server_profile   | 修復されたサーバープロファイルに関するすべてのOneViewの情報を持っています。|  常時。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_storage_volume_attachment_facts
OneViewストレージボリュームのアタッチメントに関する情報を取得します。

#### 概要
 OneViewストレージボリュームのアタッチメントに関する情報を取得します。特定のストレージボリュームアタッチメントに関する情報を収集するには、_storageVolumeAttachmentUri_オプションに通知する必要があります。サーバープロファイルとボリュームによって特定のストレージボリュームのアタッチメントを取得することもできます。このオプションでは、_serverProfileName_オプションと_storageVolumeName_または_storageVolumeUri_パラメーターに通知する必要があります。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 2.0.1

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| options  |   No  |  | |  追加の情報を取得します。利用可能なオプション: `extraUnmanagedStorageVolumes`は、追加のアンマネージドストレージボリュームのリストを取得します。`paths`は、指定されたボリュームアタッチメントのすべてのパスまたは特定のアタッチメントパスを取得します。特定のパスを取得するには、「pathUri」または「pathId」に通知する必要があります  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |
| serverProfileName  |   No  |  | |  サーバープロファイル名。  |
| storageVolumeAttachmentUri  |   No  |  | |  ストレージボリュームアタッチメントURI。  |
| storageVolumeName  |   No  |  | |  ストレージボリューム名。  |
| storageVolumeUri  |   No  |  | |  ストレージボリュームuri。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| extra_unmanaged_storage_volumes   | 追加の非管理対象ストレージボリュームに関する情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
Has facts about all 指定されたボリュームアタッチメントのすべてのパスまたは特定のアタッチメントパスに関する情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| storage_volume_attachments   | ストレージボリュームの添付ファイルに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_storage_volume_template
OneViewストレージボリュームテンプレートリソースを管理します。

#### 概要
 ストレージボリュームテンプレートリソースを管理するためのインターフェイスを提供します。作成、更新、削除できます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  ストレージボリュームテンプレートのプロパティとその関連状態を表示します。  |
| state  |   Yes  |  | <ul> <li>present</li>  <li>absent</li> </ul> |  ストレージボリュームテンプレートリソースの望ましい状態を示します。`present` は、データプロパティがOneViewに準拠していることを保証します。`absent`は、存在する場合、OneViewからリソースを削除します。  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  ETag検証が有効になっている場合、リソースの現在のETagがデータで提供されているETagと一致する場合にのみ、リクエストが条件付きで処理されます。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| storage_volume_template   | ストレージボリュームテンプレートに関するOneViewの情報を持っています。|  'present'の状態ですが、nullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_storage_volume_template_facts
Retrieve facts about Storage Volume Templates of the OneView.

#### 概要
 Retrieve facts about Storage Volume Templates of the OneView.

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 2.0.1

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  ストレージボリュームテンプレート名。  |
| options  |   No  |  | |  追加の情報を取得します。 オプションとして `connectableVolumeTemplates`, `reachableVolumeTemplates`, `compatibleSystems`が使えます。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| compatible_systems   | ストレージボリュームテンプレートと互換性のあるストレージシステムに関する情報を持っています。APIバージョン500以降のみ。|  要求された場合、ただしnullの場合があります。|  dict |
| connectable_volume_templates   | 接続可能なストレージボリュームテンプレートに関する情報を持っています。APIバージョン<= 300のみ。|  要求された場合、ただしnullの場合があります。|  dict |
| reachable_volume_templates   | Reachable Storage Volumeテンプレートに関する情報を持っています。APIバージョン500以降のみ。|  要求された場合、ただしnullの場合があります。|  dict |
| storage_volume_templates   | ストレージボリュームテンプレートに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_switch
ToRスイッチリソースを削除するためのインターフェイスを提供します。

#### 概要
 Top of Rack（ToR）スイッチリソースを削除するためのインターフェーイスを提供します。スイッチリソースは、管理されていない状態の場合は削除されます。スイッチリソースが論理スイッチに関連付けられている場合、その削除はハードウェアの削除としてのみ扱われます。スイッチへの参照は保持され、リソースは 'Absent'としてマークされます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 4.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   Yes  |  | |  スイッチ名。  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li>  <li>ports_updated</li> </ul> |  スイッチリソースの望ましい状態を示します。`present`は、宣言されているものと異なる場合、スイッチスコープを更新します。`absent`は、存在する場合、OneViewからリソースを削除します。`ports_updated`は、スイッチポートを更新します。  |


 
#### 例

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



#### 注記

- このリソースは、C7000エンクロージャーでのみ使用可能です

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_switch_facts
Retrieve facts about the OneView Switches.

#### 概要
 Retrieve facts about the OneView Switches.

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 2.0.1

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  スイッチ名。  |
| options  |   No  |  | |  スイッチに関する追加の情報を収集するオプションを表示します。可能なオプション: `environmentalConfiguration`は、スイッチの環境設定を取得します。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| switch_environmental_configuration   | スイッチの環境設定。|  要求された場合、ただしnullの場合があります。|  dict |
| switches   | スイッチのリスト。|  常時、ただしnullの場合があります。|  list |


#### 注記

- このリソースは、C7000エンクロージャーでのみ使用可能です

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_switch_type_facts
Retrieve facts about the OneView Switch Types.

#### 概要
 Retrieve facts about the Switch Types from OneView.

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 5.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  スイッチタイプの名前。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| switch_types   | スイッチタイプに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_task_facts
OneViewタスクに関する情報を取得します。

#### 概要
 OneViewタスクに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 2.0.1

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| params  |   No  |  | |  タスクのフィルタリングに役立つパラメータを表示します。使用可能なパラメーター: `count`、`fields`、`filter`、`query`、`sort`、`start`、`view`。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| tasks   | タスクのリスト。|  常時、ただしnullの場合があります。|  list |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_unmanaged_device
OneView非管理対象デバイスリソースを管理します。

#### 概要
 非管理対象デバイスリソースを管理するためのインターフェイスを提供します。作成、更新、または削除できます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  非管理対象デバイスのプロパティのリスト。  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  非管理対象デバイスリソースの望ましい状態を示します。`present` は、データプロパティがOneViewに準拠していることを保証します。`absent`は、存在する場合、OneViewからリソースを削除します。  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  ETag検証が有効になっている場合、リソースの現在のETagがデータで提供されているETagと一致する場合にのみ、リクエストが条件付きで処理されます。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| unmanaged_device   | 非管理対象デバイスに関するOneViewの情報を持っています。|  状態 'present'nullの場合があります。|  dict |


#### 注記

- 非管理対象デバイスの名前を変更するには、データ引数で`newName`を通知する必要があります。名前の変更はで冪等ではありません

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_unmanaged_device_facts
1つ以上のOneView非管理対象デバイスに関する情報を取得します。

#### 概要
 OneViewから1つ以上の管理対象外デバイスに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 2.0.1

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  非管理対象デバイス名。  |
| options  |   |  | |  非管理対象デバイスに関する追加の情報を収集するオプションを表示します。可能なオプション: `environmental_configuration`は、非管理対象デバイスの環境設定の説明を取得します。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| unmanaged_device_environmental_configuration   | 論理インターコネクトの環境構成の説明。|  要求された場合、ただしnullの場合があります。|  dict |
| unmanaged_devices   | 非管理対象デバイスのリスト。|  常時、ただしnullの場合があります。|  list |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_uplink_set
OneViewアップリンクセットリソースを管理します。

#### 概要
 アップリンクセットリソースを管理するためのインターフェイスを提供します。作成、更新、または削除できます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpeOneView >= 5.4.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  アップリンクセットプロパティのリスト。  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> </ul> |  アップリンクセットリソースの望ましい状態を示します。`present` は、データプロパティがOneViewに準拠していることを保証します。`absent`は、存在する場合、OneViewからリソースを削除します。操作を実行するリソースを見つけるために使用されるキーは複合キーであり、アップリンクセットの名前と論理インターコネクトのURI（または名前）の組み合わせで構成されます。logicalInterconnectUriまたはlogicalInterconnectNameによって論理インターコネクトを設定することを選択できます。  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  ETag検証が有効になっている場合、リソースの現在のETagがデータで提供されているETagと一致する場合にのみ、リクエストが条件付きで処理されます。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| uplink_set   | アップリンクセットに関するOneViewの情報を持っています。|  状態 'present'nullの場合があります。|  dict |


#### 注記

-アップリンクセットの名前を変更するには、データ引数で`newName` を指定する必要があります。名前の変更は冪等ではありません

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_uplink_set_facts
1つ以上のOneViewアップリンクセットに関する情報を取得します。

#### 概要
 OneViewから1つ以上のアップリンクセットに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 2.0.1

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  アップリンクセット名。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| uplink_sets   | アップリンクセットに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_user
OneViewユーザーを管理します。

#### 概要
 ユーザーを管理するためのインターフェイスを提供します。作成、更新、および削除できます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 3.2.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  ユーザープロパティを表示します。  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li> <li>set_password</li> <li>add_role_to_username</li> <li>update_role_to_username</li> <li>remove_role_from_username</li> <li>add_multiple_users</li> <li>delete_multiple_users</li> <li>validate_user_name</li> <li>validate_full_name</li> </ul> |  ユーザーの状態を指定します。 `present` は、データプロパティがOneViewに存在していることを保証します。`absent`は、存在する場合、OneViewからリソースを削除します。 `set_password` 初期セットアップ時にデフォルトのadministratorパスワードを変更します。`add_role_to_username`はユーザーにロールのセットを与えます。 `update_role_to_username`はユーザーに付与したロールのセットを更新します。 `remove_role_from_username`はスコープによって制限されていないロールのセットをユーザーから削除します。 `add_multiple_users`は複数の新しいローカルユーザーを追加します。（ユーザー作成権限を持ったユーザーが必要です。） `delete_multiple_users`はクエリ条件に基づいて複数のユーザーを削除します。 `validate_username`は指定されたユーザー名を持つユーザーの存在を確認します。 `validate_fullname`は指定されたフルネームをもつユーザーの存在を確認します。 |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| user   | OneViewユーザーに関する情報を持っています。|  常に|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_user_facts
1人以上のOneViewユーザーに関する情報を取得します。

#### 概要
 OneViewから1人以上のユーザーに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 3.4.2
  * hpeOneView >= 6.1.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| nameName  |   No  |  | |  ユーザー名。  |
| role  |   No  |  | |  ロール名  |
| options | No  |  |  getUserRoles | ユーザー名に関連付けられたロールを取得するオプション
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| users   | ユーザーに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |
| user_roles | ユーザーに紐づけられた全てのロール | 常時 | list |
| role   | It has all the Users with specified role. |  常時、ただしnullの場合があります。 | list | 


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_version_facts
アプライアンスでサポートされている可能なAPIバージョンの範囲を返します。

#### 概要
 アプライアンスでサポートされる可能なAPIバージョンの範囲を返すインターフェイスを提供します。

#### 要件 (モジュールを実行するホスト)
  * hpOneView >= 4.3.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

```yaml

- name: Gather facts about current and minimum Version
  oneview_version_facts:
    config: "{{ config_file_path }}"

- debug: var=version

```



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| version   | OneViewの現在および最小バージョンに関する情報を持っています。|  要求された場合、nullの場合があります |  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_volume
OneView Volumeリソースを管理します。

#### 概要
 ボリュームリソースを管理するためのインターフェイスを提供します。ボリュームを作成、更新、削除、または修復し、スナップショットを作成または削除できます。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 4.0.0

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| data  |   Yes  |  | |  ボリュームまたはスナップショットデータ。  |
| export_only  |   |  False  | |  Trueに設定すると、ステータスが `absent`でリソースが存在する場合、OneViewからのみ削除されます。  |
| state  |   |  | <ul> <li>present</li>  <li>absent</li>  <li>repaired</li>  <li>snapshot_created</li>  <li>snapshot_deleted</li> </ul> |  ボリュームリソースの望ましい状態を示します。`present`は、リソースが存在しない場合にリソースを作成/追加し、存在しない場合はリソースを更新します。リソースが既に存在する場合、指定されたオプションが既存のデータに準拠している場合でも常に呼び出されるため、更新操作は非集中的です。ボリュームの名前を変更するには、\_data\_の `newName`を提供する必要があります。`absent`は、デフォルトでOneViewとストレージシステムからボリュームを削除します。export_onlyがTrueの場合、ボリュームはOneViewからのみ削除されます。`repaired`は、ストレージシステム上の指定されたボリュームから余分なプレゼンテーションを削除します。この操作は冪等ではありません。`snapshot_created`は、指定されたボリュームのスナップショットを作成します。この操作は冪等ではありません。` snapshot_deleted `は、OneViewとストレージシステムからスナップショットを削除します。  |
| validate_etag  |   |  True  | <ul> <li>true</li>  <li>false</li> </ul> |  ETag検証が有効になっている場合、リソースの現在のETagがデータで提供されているETagと一致する場合にのみ、リクエストが条件付きで処理されます。  |


 
#### 例

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
    api_version: 2200
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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| storage_volume   | ストレージボリュームに関する情報を持っています。|  状態は'present'ですが、nullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


## oneview_volume_facts
OneViewボリュームに関する情報を取得します。

#### 概要
 OneViewからボリュームに関する情報を取得します。

#### 要件 (モジュールを実行するホスト)
  * python >= 2.7.9
  * hpOneView >= 2.0.1

#### オプション

| パラメーター     | 必要    | デフォルト  | 選択肢    | コメント |
| ------------- |-------------| ---------|----------- |--------- |
| config  |   No  |  | |  OneViewクライアント構成を含む.json構成ファイルへのパス。構成ファイルはオプションです。ファイルパスが指定されていない場合、構成は環境変数からロードされます。  |
| name  |   No  |  | |  ボリューム名。  |
| options  |   No  |  | |  ボリュームおよび関連リソースに関する追加の情報を収集するオプションを表示します。可能なオプション: - `attachableVolumes` - `extraManagedVolumePaths` - `snapshots`。このオプションでは、名前を指定できます。  |
| params  |   No  |  | |  リソースのリストを区切り、フィルター、ソートするパラメーターのリスト。  可能なパラメーター: `start`: 0から始まるインデックスを使用して返される最初のアイテム。`count`: 返されるリソースの数。`filter`: 返されるアイテムのリストを絞り込むための一般的なフィルター/クエリ文字列。`sort`: 返されたデータセットのソート順。  |


 
#### 例

```yaml

- name: Gather facts about all Volumes
  oneview_volume_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
- debug: var=storage_volumes

- name: 
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



#### 戻り値

| 名前          | 説明  | 戻り | タイプ       |
| ------------- |-------------| ---------|----------- |
| attachable_volumes   | アプライアンスによって管理される接続可能なボリュームに関するすべての情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| extra_managed_volume_paths   | アプライアンスからの追加の管理ストレージボリュームパスに関するすべての情報を持っています。|  要求された場合、ただしnullの場合があります。|  dict |
| storage_volumes   | ボリュームに関するすべてのOneViewの情報を持っています。|  常時、ただしnullの場合があります。|  dict |


#### 注記

- configパラメーターのサンプル構成ファイルは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json

- 構成用の環境変数の使用方法は、次の場所で確認してください。: https://github.com/HewlettPackard/oneview-ansible#environment-variables

- HPE OneView Ansibleモジュールの追加のPlaybookは、次の場所にあります。: https://github.com/HewlettPackard/oneview-ansible/tree/master/examples


---


<!-- 20210511 https://github.com/HewlettPackard/oneview-ansible/compare/cd5d7e471bd6c5c1d6f9d75156c1514892e1f3b4%E2%80%A6815f410663f9601ad6ef0a787a898478abcc7e13# -->