"""
scenario: 
Aws account has "Security groups these are firewalls that control who can connect to your servers. 
soem of them might accidentally allow ssh(remote login) from the entire internet, which is a 
major secuirty risk. 
need to write a script that checks for that

1) wHAT IS boto3? 
its a python lib that aws wrote. it lets you do anything you can do in the aws console(the website) 
but from code. create servers, check secuiorty groups, read s3 files anything. you just call functions.
"""

"""
Test the connection within aws cli
------------------------------
type:  python  #This opens the python interactive shell. 
o/p: Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL

>>> import boto3
>>> ec2=boto3.client("ec2", region_name="us-east-1")
>>> response = ec2.describe_security_groups() 
>>> print(len(response["SecurityGroups"]), "security groups found")
o/p:
5 security groups found
type exit() to leave python shell and get back to normal terminal.
>>> 
"""

#############Creat Script File#########################
import boto3

#connect to aws 
#This creates a "client" - think of it as opening a phone line to aws. 
#"ec2" is the aws service that manages servers and security groups. 
#region_name is which aws data center to check 

print("connecting to AWS..")
ec2 = boto3.client("ec2", region_name="us-east-1")

#ASK AWS for all secuirty groups 
#This one function call. it returns a big dictonary with everything 
#A secuirty group is a firewall. it controls who can connect to your servers. 
print("Fetching secuirty groups..")
response = ec2.describe_security_groups() 
#The response is a dictionary. The secuirty groups are under the key "SecuirtyGroups" 
#Its a list of dictionaries. each dict is one secuirty group. 
groups = response["SecurityGroups"]
print(f"Found {len(groups)} security groups. checking each one..\n")

#check each one 
problem_count = 0 

for sg in groups: 
    #Each secuirty group has a name and an ID. 
    name = sg["GroupName"]
    group_id = sg["GroupId"]

    #"IpPermissions" = the inbound rules. who is allowed to connect? 
    for rule in sg["IpPermissions"]:
        #EACH RULE HAS A PORT RANGE, FromPort and ToPort.
        #we care about port 22 - thats ssh(remote login to a server).
        from_port = rule.get("FromPort", 0)
        to_port = rule.get("ToPort", 0)

        #is port 22 in this group? 
        protocol = rule.get("IpProtocol")
        if protocol == "-1" or (rule.get("FromPort", 0) <= 22 <= rule.get("ToPort", 0)):

            #This rule covers_ssh now: who does it allow? 
            #"IpRanges" is a list of IP addresses that are allowed. 
            for ip_range in rule.get("IpRanges", []):
                cidr = ip_range.get("CidrIp", "")

                #"0.0.0.0/0" means "every ip address on earth". mean anyone can try to ssh into your server
                #thats almost a SECUIRTY RISK
                if cidr == "0.0.0.0/0":
                    problem_count += 1
                    print(f" Problem: {name} ({group_id})")
                    print(f" ssh(port 22) is open to the enitre internet")
                    print()

#summary
print("=" * 40)
if problem_count == 0: 
    print("All clear ! no secuirty groups have ssh to the internet.")
else: 
    print(f" Found {problem_count} secuirty groups with ssh open to 0.0.0.0/0")
    print(" This means anyone on earth can try to log into those servers.")
    print(" you should restrict ssh to you own ip address insted.")

"""
connecting to AWS..
Fetching secuirty groups..
Found 5 security groups. checking each one..

 Problem: allowall (sg-0d28c90919ca96fa1)
 ssh(port 22) is open to the enitre internet

 Problem: allow all ports defult (sg-09a7409ed52f55f70)
 ssh(port 22) is open to the enitre internet

 Problem: awsnsg (sg-06379eec176b454ce)
 ssh(port 22) is open to the enitre internet

========================================
 Found 3 secuirty groups with ssh open to 0.0.0.0/0
 This means anyone on earth can try to log into those servers.
 you should restrict ssh to you own ip address insted.
"""