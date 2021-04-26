#!/usr/bin/python
# -*- coding: utf-8 -*-
###
# Copyright (2021) Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###

import copy
import mock
import pytest

from hpe_test_utils import OneViewBaseTest
from oneview_module_loader import TaskModule

ERROR_MSG = 'Fake message error'

TASK = {
    "associatedResource": {
        "associationType": "MANAGED_BY",
        "resourceCategory": "server-profile-templates",
        "resourceName": "ProfileTemplate101",
        "resourceUri": "/rest/server-profile-templates/fa6d2aff-7579-4240-91d4-89fe8e40d6f9"
    },
    "created": "2016-09-06T15:16:23.638Z",
    "modified": "2016-09-06T15:16:24.249Z",
    "owner": "administrator",
    "taskState": "Running",
    "taskStatus": "Successfully deleted server profile template: ProfileTemplate101 ",
    "type": "TaskResourceV2",
    "uri": "/rest/tasks/D2B856D2-5939-421B-BDCA-FBF7D8961A89",
    "isCancellable": True
}

ALL_TASKS = [TASK]


TASK = dict(
    config='config.json',
    data=dict(name='Add'))

PARAMS_FOR_PATCH = dict(
    config='config.json',
    data=dict(
        associatedResource=dict(
           associationType='MANAGED_BY',
           resourceCategory='certificates'),
        name='Add',
        taskState='Running',
        taskType='User',
        owner='Administrator',
        isCancellable=True,
        uri="/rest/tasks/D2B856D2-5939-421B-BDCA-FBF7D8961A89")
)


@pytest.mark.resource(TestTaskModule='tasks')
class TestTaskModule(OneViewBaseTest):
    def test_should_validate_patch(self):
        self.resource.get_by_name.return_value = self.resource
        resource_data = PARAMS_FOR_PATCH.copy()
        self.resource.data = resource_data

        patch_return = resource_data.copy()
        patch_return['taskState'] = 'Cancelling'
        patch_return_obj = self.resource.copy()
        patch_return_obj.data = patch_return
        self.resource.patch.return_value = patch_return_obj

        self.mock_ansible_module.params = copy.deepcopy(PARAMS_FOR_PATCH)

        TaskModule().run()

        self.mock_ansible_module.exit_json.assert_called_once_with(
            changed=True,
            msg=TaskModule.MSG_TASK_UPDATED,
            ansible_facts=dict(tasks=self.resource.data)
        )


if __name__ == '__main__':
    pytest.main([__file__])
