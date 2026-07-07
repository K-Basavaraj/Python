"""
This script checks ssh (port 22), checks RDP(port 3389), check all traffic rules (protocol -1)
save a report file and Audit s3 buckets
"""
import boto3
from pathlib import path 
from datetime import datetime

#------------------------------------
# SECURITY GROUP AUDIT 
#----------------------------------------

def audit_secuirty_groups(region="us-east-1"):
    print("connecting to AWS..")
    ec2 = boto3.client("ec2", region_name=region)
    
    print("Fetching secuirty groups..")
    response = ec2.describe_security_groups() 

    groups = response["SecurityGroups"]
    print(f"[Security Groups] Found {len(groups)} in {region}\n")

    problems = []

    for sg in groups: 
        name = sg["GroupName"]
        group_id = sg["GroupId"]

        for rule in sg["IpPermissions"]:
            protocol = rule.get("IpProtocol")
                #if protocol == "-1" or (rule.get("FromPort", 0) <= 22 <= rule.get("ToPort", 0)):
            is_All_traffic = protocol == "-1"
            is_ssh = rule.get("FromPort", 0) <= 22 <= rule.get("ToPort", 0)
            is_rdp = rule.get("FromPort", 0) <= 3389 <= rule.get("ToPort", 0)

            if is_All_traffic or is_ssh or is_rdp: 
                if is_All_traffic: 
                    risk = "All Traffic (all ports, all protocols)"
                elif is_ssh and is_rdp:
                    rsik = "SSH (22) and RDP (3389)"
                elif is_ssh: 
                    risk = "SSH (port 22)" 
                else: 
                    risk = "RDP (port 3389)"

                #Now check: is it open to the whole internet
                for ip_range in rule.get("IpRanges", []):
                    if ip_range.get("CidrIp") == "0.0.0.0/0":
                        problems.append(
                            {
                            "name": name,
                            "id": group_id,
                            "risk": risk,
                            "source": "0.0.0.0/0",
                            }
                        )
                    print(f" {name} ({group_id}) - {risk} open to 0.0.0.0/0")

                #Also check IPV6 
                for ip_range in rule.get("Ipv6Ranges", []):
                    if ip_range.get("CidrIpv6") == "::/0":
                        problems.append(
                            {
                            "name": name,
                            "id": group_id,
                            "risk": risk,
                            "source": "::/0 (IPV6)",
                            }
                        )
                    print(f" {name} ({group_id}) - {risk} open to ::/0 (IPV6)")
    
    return problems   

#-----------------------------------------
# S3 BUCKET audit
# ------------------------------------------
def audit_s3_buckets():
    """
    Check all s3 buckets for versioning. 
    No versioning  = if someone deletes a file, its gone forever 
    """                 
    s3 = boto3.client("s3")
    response = s3.list_buckets()
    buckets = response["buckets"]

    print(f"\n[s3 Buckets] Found {len(buckets)} buckets")

    results = []

    for bucket in buckets:
        name = bucket["Name"]
        created = bucket["CreationDate".strftime("%Y-%m-%d")]

        try: 
            v = s3.get_bucket_versioning(Bucket=name)
            status = v.get("status", "Disabled")
        except Exception as e:
            status = f"Error: {e}"

        if status == "Enabled":
            print("s3 versioing is enabled")
        else:
            print("s3 versioing is disabled")
        
        print(f"{name} - created: {created} - Versioning: {status}")

        results.append(
            {
                "name": name,
                "created": created,
                "versioning": status,
            }
        )

    return results 

#-----------------------------------------
# Genrate Report 
# ------------------------------------------
def save_report(sg_problems, s3_results):
    """
    Everything above printed to terminal. This saves it to a file ssame data, just wrotten to disk 
    s you have a record of it.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"aws_audit_report_{timestamp}.txt"

    lines = [
        f"AWS secuirty audit report",
        f"Genrated: {timestamp}",
        f"",
        f"={'=' *50}",
        f"Secuirty Groups - open to internet"
        f"{'=' *50}"
    ]
    