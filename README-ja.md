# HPE OneView SDK for Ansible

[English](README.md)
## Build Status 

| 5.50 Branch   | 5.40 Branch   | 5.30 Branch   | 5.20 Branch   | 5.00 Branch   |
| ------------- |:-------------:| -------------:| -------------:| -------------:|
| ![Build status](https://ci.appveyor.com/api/projects/status/u84505l6syp70013?svg=true)| ![Build status](https://ci.appveyor.com/api/projects/status/u84505l6syp70013?svg=true)| ![Build status](https://ci.appveyor.com/api/projects/status/u84505l6syp70013?svg=true)| ![Build status](https://ci.appveyor.com/api/projects/status/u84505l6syp70013?svg=true)| ![Build status](https://ci.appveyor.com/api/projects/status/u84505l6syp70013?svg=true)  

## はじめに
HPE OneViewは今日の複雑なハイブリッドクラウド環境の管理やデプロイをシンプルにするソフトウェアです。HPE OneViewを活用することでデータセンタをソフトウェア定義のデータセンタに移行することが可能になります。また、HPEストレージ、サーバー、ネットワーク等の幅広い製品をカバーしており、ハイブリッドインフラストラクチャ管理の簡素化、自動を可能にします。  
ソフトウェア定義の技術はデプロイやプロビジョニング、アップデートやコンピュートリソースやストレージリソース、さらにはネットワークリソースの統合を可能にします。  
このHPE OneView Ansible SDKはHPE OneView REST APIを通じて、Ansible Playbookの作成を可能にすることでHPE OneView自体をAnsibleから管理することができます。最新のHPE OneView Ansible SDKを確認したい場合は[こちら](https://github.com/HewlettPackard/oneview-ansible/releases/latest)を参照してください。  
それぞれのHPE OneViewリソースへのアクセス等は本Ansibleモジュール\(HPE OneView Ansible SDK\)を通じて行うことができます。また情報収集系モジュール\(facts\)も用意されています。各モジュールについて詳細な使用方法を確認したい場合は[こちら](oneview-ansible-ja.md)を参照してください。

## 最新情報
本HPE OneView AnsibleはHPE OneView REST APIバージョン2200\(HPE OneView v5.50\)をサポートしました。  
その他の機能拡張、修正情報は[こちら](https://github.com/HewlettPackard/oneview-ansible/blob/master/CHANGELOG.md)を参照してください。

## 使用方法
### インストールと設定
HPE OneView SDK for AnsibleはソースコードまたはDockerコンテナからインストール可能です。
	
### 前提条件
HPE OneView SDK for Ansibleを利用するためには以下のバージョン満たす必要があります。
 
	Ansible < 2.9
	Python >= 3.4.2
	HPE OneView Python SDK

## インストール

### ソースコードからのインストール
#### レポジトリのクローン
```bash
$ git clone https://github.com/HewlettPackard/oneview-ansible.git
$ cd oneview-ansible
```

#### 依存Pyhtonパッケージのインストール
```bash
$ pip install -r requirements.txt
```

#### 環境変数の設定
本ライブラリのパスを通すために、`ANSIBLE_LIBRARY`と`ANSIBLE_MODULE_UTILS`の環境変数を以下のように設定してください。

```bash
$ export ANSIBLE_LIBRARY=/path/to/oneview-ansible/library
$ export ANSIBLE_MODULE_UTILS=/path/to/oneview-ansible/library/module_utils/
```

### Dockerイメージ/コンテナからのインストール
本ライブラリのコンテナイメージは [Docker Store](https://store.docker.com/community/images/hewlettpackardenterprise/hpe-oneview-sdk-for-ansible)からダウンロード可能です。 コンテナイメージのタグの命名規則はsdk\_version-OV\_versionとなっています。

#### Dockerコンテナイメージのダウンロード
```bash
$ docker pull hewlettpackardenterprise/hpe-oneview-sdk-for-ansible:v5.9.0-OV5.5
```

#### Dockerコンテナを起動させPlaybook実行用shセッションを作成
```bash
$ docker run -it hewlettpackardenterprise/hpe-oneview-sdk-for-ansible:v5.9.0-OV5.5 /bin/sh
```

[こちら](https://github.com/HewlettPackard/oneview-ansible-samples/blob/master/oneview-ansible-in-container/oneview-ansible-in-container-ja.md)に詳しい使用方法がありますので参照してください。  

## OneViewクライアント設定

### JSON設定ファイル
本Ansible OneViewモジュールを利用するためには、HPE OneViewへの接続のための JSON形式での設定ファイルが必要となります。この設定ファイルはHPE OneViewに認証するためのユーザー名やパスワード、ホスト名、APIバージョン等を記載する必要があります。以下は例となります。  

```json
{
  "ip": "172.25.105.12",
  "credentials": {
    "userName": "Administrator",
    "authLoginDomain": "",
    "password": "secret123"
  },
  "api_version": 2200
}
```

api_versionは呼び出すHPE OneView REST APIバージョンを指定します。api_versionが指定されていない場合は、HPE OneViewからAPIバージョンを受けっとって自動設定します。

プロキシサーバーを利用している場合は以下の例のようにJSON設定ファイルに記載します。
```json
  "proxy": "<proxy_host>:<proxy_port>"
```

🔒  平文で認証情報を設定ファイルに記載しているため、ファイルのパーミッションに注意してください。

Playbook全てに `config` キーの値としてJSON設定ファイルのパスを指定してください。  
以下は例となります。

```yml
- name: Gather facts about the FCoE Network with name 'FCoE Network Test'
  oneview_fcoe_network_facts:
    config: "/path/to/config.json"
    name: "FCoE Network Test"
```

### 環境変数

前途のJSON設定ファイルに記載した内容は環境変数としても設定可能です。

```bash
# Required
export ONEVIEWSDK_IP='172.25.105.12'
export ONEVIEWSDK_USERNAME='Administrator'
export ONEVIEWSDK_PASSWORD='secret123'

# Optional
export ONEVIEWSDK_API_VERSION='2200'
export ONEVIEWSDK_AUTH_LOGIN_DOMAIN='authdomain'
export ONEVIEWSDK_PROXY='<proxy_host>:<proxy_port>'
```

🔒  平文で認証情報が環境変数に設定されるため、権限のないユーザーが環境変数にアクセスできないように注意してください。

環境変数に設定情報を持たせる場合、前途の `config` は使いません。  
以下の例を参照してください。

```yml
- name: Gather facts about the FCoE Network with name 'FCoE Network Test'
  oneview_fcoe_network_facts:
    name: "FCoE Network Test"
```

環境変数に設定をセットした後、Playbookを実行できます。

### Playbook内パラメータ

HPE OneView情報を設定するための３つ目の方法として、Playbook内に明示的に設定する方法です。
この方法は `hostname`, `username`, `password`, `api_version` と `image_streamer_hostname` を直接Playbook内で指定できます。

```yaml
- name: Create a Fibre Channel Network
  oneview_fc_network:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 2200
    state: present
    data:
      name: "{{ network_name }}"
      fabricType: 'FabricAttach'
      linkStabilityTime: '30'
      autoLoginRedistribution: true
  no_log: true
  delegate_to: localhost
```
設定したHPE OneView認証情報がログとして記録されるため、`no_log: true` を使用することを推奨します。

### Ansible Vault使った認証情報の格納

Ansible Vault利用して、認証情報を暗号化して保存できます。

  1. oneview_config.ymlを作成します。
  2. 以下のコマンドを実行してHPE OneViewのユーザー名とパスワードを暗号化します。
     ```ansible-vault
     ansible-vault encrypt_string 'secret123' --name ONEVIEWSDK_PASSWORD
     ```
     注意: このパスワードはPlaybookを実行するときに使われます。
  3. 設定情報と共に暗号化されたパスワードをoneview_config.ymlに記載します。

	    ```yaml
	    # Required
	    ip: 172.168.1.1
	    api_version:2200
	    username: Administrator
	    password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          37646435306637633461376438653439323666383934353234333934616363313164636637376536
          3239356538653537643734626265366662623863323661350a613834313562303635343931356139
          35343863313563363830356638343339373138316539613636336532333065366133386662333833
          6663363236663031340a636562646634323136353737373539326434626137353837333530376665
          3835
	    ```

  4. oneview_config.ymlのパスをvars_fileを使って設定します。

```yaml
- vars_file:
   oneview_config.yml
- name: Create a Fibre Channel Network
  oneview_fc_network:
    hostname: "{{ ip }}"
    username: "{{ username }}"
    password: "{{ password }}"
    api_version: "{{ api_version }}"
    state: present
    data:
      name: "{{ network_name }}"
      fabricType: 'FabricAttach'
      linkStabilityTime: '30'
      autoLoginRedistribution: true
  no_log: true
  delegate_to: localhost
```

oneview_config.ymlのファイル自体を暗号化することもできますが、その場合、ファイル内のパスワードは平文で設定してください。

🔒 暗号化されたパスワードは暗号化する際に作成したパスワードで復号することが可能なので、許可されてないユーザーが暗号化されたファイルまたは値にアクセスできないようにしてください。

5.--ask-vault-passオプションでPlaybookを実行して、パスワードプロンプトに暗号化した際に設定したパスワードを入力します。
```bash   
ansible-playbook example.yml --ask-vault-pass
```
本レポジトリ内の例の多くは平文でOneView認証情報を設定しています。

### OneView APIの設定

本Ansible modules for HPE OneViewはHPE OneViewバージョン 4.00, 4.10, 4.20, 5.00, 5.20, 5.30, 5.40, 5.50をサポートしています。  デフォルトはターゲットとなるHPE OneViewのAPIバージョンを使います。

APIバージョンを指定したい場合、HPE OneViewの認証情報と共にAPIバージョンをJOSNファイルに設定してください。 
```bash
"api_version": 2200
```

または、環境変数に設定することも可能です。
```bash
export ONEVIEWSDK_API_VERSION='2200'
```

設定したAPIバージョンが無効な場合は、ターゲットとなるHPE OneViewのAPIバージョンを使います。

### HPE Synergyイメージストリーマー

本モジュールはHPE Synergyイメージストリーマーもサポートしています。 イメージストリーマー用のモジュールを使う場合はイメージストリーマーのIPをJSON設定ファイルに追記します。

```json
"image_streamer_ip": "100.100.100.100"
```

または、環境変数に設定することも可能です。
```bash
export ONEVIEWSDK_IMAGE_STREAMER_IP='100.100.100.100'
```

## 例
サンプルのPlaybookと使い方は[こちら](/examples)を参照してください。

### Ansible OneViewモジュールの使用例

```yml
- hosts: all
  tasks:

    - name: Ensure that the Fibre Channel Network is present with fabricType 'DirectAttach'
      oneview_fc_network:
        config: "/path/to/config.json"
        state: present
        data:
          name: 'New FC Network'
          fabricType: 'DirectAttach'

    - name: Ensure that Fibre Channel Network is absent
      oneview_fc_network:
        config: "/path/to/config.json"
        state: absent
        data:
          name: 'New FC Network'

    - name: Gather facts about the FCoE Network with name 'Test FCoE Network Facts'
      oneview_fcoe_network_facts:
        config: "/path/to/config.json"
        name: "Test FCoE Network Facts"
```


#### 活用例

- DevOps実践の例としてHPE OneViewを活用したベアメタルサーバープロビジョニング、HPE ICspを使ったOSプロビジョニング、そしてAnsibleを使ったソフトウェア設定があります。詳しくは[こちら](/examples/oneview-web-farm)を参照してください。

- HPE OneViewとHPE Synergyイメージストリーマーを利用したOSデプロイはの例は[こちら](https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/synergy_create_server_profile_with_deployment_plan.yml)、または[こちら](https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/ImageStreamer)を参照してください。

- HPE SynergyイメージストリーマーのアーティファクトバンドルのアップロードとHPE OneViewで提供されるアーティファクトバンドル内のOSビルドプランを利用したブレードサーバーのデプロイに関しては[こちら](https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/synergy_image_streamer.yml)を参照してください。

- HPE OneViewとAnsibleを活用したベアメタルインフラのセットアップ例は以下を参照してください。
  - [C7000 Environment Setup](https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/c7000_environment_setup.yml)
  - [HPE Synergy Environment Setup](https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/synergy_environment_setup.yml)


## ヘルプ

何か問題を抱えていますか?ご自由にissueに登録してください。  
[issue tracker](https://github.com/HewlettPackard/oneview-ansible/issues)

どのようにして新しいissueを登録するのか分からない方は[こちら](https://github.com/HewlettPackard/oneview-ansible/wiki#getting-help---how-can-i-get-help—support)を参照してください。

## ライセンス
This project is licensed under the Apache license. Please see [LICENSE](https://github.com/HewlettPackard/oneview-ansible/blob/master/LICENSE) for more information.

## コントリビュートと機能拡張リクエスト

Ansible Modules for HPE OneViewへのコントリビュートをいつでも歓迎します。詳しくは[こちら](https://github.com/HewlettPackard/oneview-ansible/blob/master/CONTRIBUTING.md)を参照してください。

## その他参考資料 

**HPE OneView Documentation**

[HPE OneView Release Notes](http://hpe.com/info/OneView/docs)

[HPE OneView Support Matrix](http://hpe.com/info/OneView/docs)

[HPE OneView Installation Guide](http://hpe.com/info/OneView/docs)

[HPE OneView User Guide](http://hpe.com/info/OneView/docs)

[HPE OneView Online Help](http://hpe.com/info/OneView/docs)

[HPE OneView REST API Reference](http://hpe.com/info/OneView/docs)

[HPE OneView Firmware Management White Paper](http://hpe.com/info/OneView/docs)

[HPE OneView Deployment and Management White Paper](http://hpe.com/info/OneView/docs)


**HPE OneView Community**

[HPE OneView Community Forums](http://hpe.com/info/oneviewcommunity)

Learn more about HPE OneView at [hpe.com/info/oneview](https://hpe.com/info/oneview)