from flask import Flask
from ec2_metadata import ec2_metadata
from flask import request
app = Flask(__name__)



@app.route('/')
def my_func():
    instanceID = ec2_metadata.instance_id
    amiLaunch = str(ec2_metadata.ami_launch_index)
    publicHn = ec2_metadata.public_hostname
    pubicIp = ec2_metadata.public_ipv4
    localHn = ec2_metadata.private_hostname
    localIp = ec2_metadata.private_ipv4
    
    result = '<table border="1" style="border-collapse: collapse;"><tbody><tr><td><b>Metadata</b></td><td><b>Value</b></td></tr><tr><td><b>Instance ID</b></td><td>'+instanceID+'</td></tr><tr><td><b>Ami Launch</b></td><td>'+amiLaunch+'</td></tr><tr><td><b>Public Hostname</b></td><td>'+publicHn+'</td></tr><tr><td><b>Public Ipv4</b></td><td>'+pubicIp+'</td></tr><tr><td><b>Local Hostname</b></td><td>'+localHn+'</td></tr><tr><td><b>Local Ipv4</b></td><td>'+localIp+'</td></tr></tbody></table>'
    return result
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')