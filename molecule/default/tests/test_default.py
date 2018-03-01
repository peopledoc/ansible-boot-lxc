# -*- coding: utf-8 -*-
import os

import yaml

import testinfra


def test_lxc_container():

    # testinfra uses a plain file for Ansible inventory: create it
    updated_inventory = '%s.new.yml' % os.environ['MOLECULE_INVENTORY_FILE']

    inventory = {
        'all': {
            'children': {
                'lxc': {
                    'hosts': {
                        'testboot.lxc': {}
                    }
                },
                'ungrouped': {}
            }
        },
    }

    with open(updated_inventory, 'w') as output:
        output.write(yaml.dump(inventory))

    host = testinfra.get_host('ansible://testboot.lxc?ansible_inventory=%s' %
                              updated_inventory)

    f = host.file('/srv/tests/canary')

    assert f.exists
    assert f.contains("inception")
    assert not f.contains("not there")
