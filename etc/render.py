import os
from argparse import ArgumentParser
from jinja2 import Template

ubuntu_image_map = {
    'ap-northeast-1': 'ami-ea4eae8c',
    'ap-northeast-2': 'ami-d28a53bc',
    'ap-south-1': 'ami-099fe766',
    'ap-southeast-1': 'ami-6f198a0c',
    'ca-central-1': 'ami-9818a7fc',
    'eu-central-1': 'ami-1e339e71',
    'eu-west-1': 'ami-785db401',
    'eu-west-2': 'ami-996372fd',
    'sa-east-1': 'ami-10186f7c',
    'us-east-1': 'ami-cd0f5cb6',
    'us-east-2': 'ami-10547475',
    'us-west-1': 'ami-09d2fb69',
    'us-west-2': 'ami-6e1a0117'
}
"""
def _render_vagrant(region,ak,sk,sg):
    vagrant=Template(open('etc/Vagrantfile.j2').read())
    rendered=vagrant.render(
        access_key=ak,
        secret_key=sk,
        region=region,
        ubuntu_image=ubuntu_image_map[region],
        sg=sg
    )
    f0=open('run/Vagrantfile', 'w+')
    f0.write(rendered); return
"""    
def _render_server_template(region):
    server=Template(open('etc/server.cue-api.cfn.yml.j2').read())
    rendered=server.render(
        region=region,
        ubuntu_image=ubuntu_image_map[region]
    )
    f0=open('run/server.cue-api.cfn.yml', 'w+')
    f0.write(rendered); return

def _render_docker_compose():
    pass

if __name__=='__main__':
    parser=ArgumentParser(description="configure cue-api with environment variables")
    parser.add_argument('region')
    """
    parser.add_argument('ak')
    parser.add_argument('sk')
    """
    args=parser.parse_args()
    """
    _render_vagrant(
        args.region,
        args.ak,
        args.sk
        args.sg
    )
    """
    _render_server_template(args.region)
