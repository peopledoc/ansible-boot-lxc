This role instanciates any inventory host that ends with ``.lxc`` and sets it
up for ansible: install python, add your ssh key for root.

Note that you need ``lxc``, ``dsnmasq``, and ``sudo`` to be properly configured.
And ``lxc-python2`` (which require ``lxc-dev``) installed in your ansible
environment. That means that you can create a container with internet access and
that you can resolve it by ``name.lxc``. One way to set this up is to use
`novafloss/ansible-setup <https://github.com/novafloss/ansible-setup>`_

Consider this example inventory::

    [flow]
    flow.lxc lxc_template_options='-r wheezy'

    [rabbitmq]
    rabbitmq.lxc

    [redis]
    redis.lxc

And a playbook like that::

    ---

    - hosts: localhost
      become: true
      become_user: root
      roles:
      - novafloss.boot-lxc

    - hosts: redis
      roles:
      - geerlingguy.redis

    - hosts: rabbitmq
      roles:
      - alexey.rabbitmq

First, novafloss.boot-lxc will start the containers and create them if they
don't exist, then plays will be executed normally on rabbitmq and redis
container hosts.
