import time, os, sys
import inspect
from os import environ as env

from  novaclient import client
import keystoneclient.v3.client as ksclient
from keystoneauth1 import loading
from keystoneauth1 import session

loader = loading.get_plugin_loader('password')

auth = loader.load_from_options(auth_url=env['OS_AUTH_URL'],
                                username=env['OS_USERNAME'],
                                password=env['OS_PASSWORD'],
                                project_name=env['OS_PROJECT_NAME'],
                                project_domain_name=env['OS_USER_DOMAIN_NAME'],
                                project_id=env['OS_PROJECT_ID'],
                                user_domain_name=env['OS_USER_DOMAIN_NAME'])

sess = session.Session(auth=auth)
nova = client.Client('2.1', session=sess)

if "group7_master" not in list(map(lambda x:x.name, nova.keypairs.list())):
    if input("Is this the master_node?[yes/no]") == "yes":
        with open("/home/ubuntu/.ssh/id_rsa.pub") as k:
            nova.keypairs.create("group7_master", public_key=k.readline())
        print("Key pair of this master node is generated as 'group7_master'.")
    else:
        print("Please run this script only on the master node!")
