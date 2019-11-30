import json

data = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DevEc2AccessDenied",
            "Effect": "Deny",
            "Action": [
                "ec2:AuthorizeSecurityGroupEgress",
                "ec2:AuthorizeSecurityGroupIngress",
                "ec2:RevokeSecurityGroupEgress",
                "ec2:RevokeSecurityGroupIngress"
            ],
            "Resource": "*"
        },
        {
            "Sid": "DevVPCAccessDenied",
            "Effect": "Deny",
            "Action": [
                "ec2:CreateVpc*",
                "ec2:DeleteVpc*",
                "ec2:ModifyVpc*",
                "ec2:CreateSubnet",
                "ec2:DeleteSubnet",
                "ec2:ModifySubnet*",
                "ec2:CreateNetworkAcl*",
                "ec2:DeleteNetworkAcl*",
                "ec2:ReplaceNetworkAcl*",
                "ec2:CreateInternetGateway",
                "ec2:DeleteInternetGateway",
                "ec2:DetachInternetGateway",
                "ec2:AttachInternetGateway",
                "ec2:CreateNatGateway",
                "ec2:DeleteNatGateway",
                "ec2:CreateVpn*",
                "ec2:DeleteVpn*",
                "ec2:AttachVpn*",
                "ec2:DetachVpn*",
                "ec2:CreateCustomerGateway",
                "ec2:DeleteCustomerGateway",
                "ec2:DetachClassicLinkVpc",
                "ec2:DisableVpcClassicLink",
                "ec2:DisableVpcClassicLinkDnsSupport",
                "ec2:EnableVpcClassicLink",
                "ec2:EnableVpcClassicLinkDnsSupport",
                "ec2:CreateRoute*",
                "ec2:DeleteRoute*",
                "ec2:ReplaceRoute",
                "ec2:DisableVgwRoutePropagation",
                "ec2:EnableVgwRoutePropagation",
                "ec2:AssociateRouteTable",
                "ec2:DisassociateRouteTable",
                "ec2:ReplaceRouteTableAssociation",
                "ec2:AllocateAddress",
                "ec2:MoveAddressToVpc",
                "ec2:RestoreAddressToClassic",
                "ec2:ReleaseAddress"
            ],
            "Resource": "*"
        },
        {
            "Sid": "DevS3AccessDenied",
            "Effect": "Deny",
            "Action": [
                "s3:CreateBucket",
                "s3:DeleteBucket"
            ],
            "Resource": "*"
        },
        {
            "Sid": "ExplicitDenyTagName",
            "Effect": "Deny",
            "Action": [
                "ec2:RunInstances",
                "ec2:CreateVolume",
                "elasticloadbalancing:CreateLoadBalancer",
                "elasticloadbalancing:AddTags",
                "autoscaling:CreateAutoScalingGroup",
                "autoscaling:CreateOrUpdateTags"
            ],
            "Resource": [
                "*"

            ],
            "Condition": {
                "Null": {
                    "aws:RequestTag/Name": "true"
                }
            }
        },
        {
            "Sid": "ExplicitDenyTagComponentId",
            "Effect": "Deny",
            "Action": [
                "ec2:RunInstances",
                "ec2:CreateVolume",
                "elasticloadbalancing:CreateLoadBalancer",
                "elasticloadbalancing:AddTags",
                "autoscaling:CreateAutoScalingGroup",
                "autoscaling:CreateOrUpdateTags"
            ],
            "Resource": [
                "*"
            ],
            "Condition": {
                "Null": {
                    "aws:RequestTag/ComponentId": "true"
                }
            }
        },
        {
            "Sid": "ExplicitDenyTagProject",
            "Effect": "Deny",
            "Action": [
                "ec2:RunInstances",
                "ec2:CreateVolume",
                "elasticloadbalancing:CreateLoadBalancer",
                "elasticloadbalancing:AddTags",
                "autoscaling:CreateAutoScalingGroup",
                "autoscaling:CreateOrUpdateTags"
            ],
            "Resource": [
                "*"
            ],
            "Condition": {
                "Null": {
                    "aws:RequestTag/Project": "true"
                }
            }
        },
        {
            "Sid": "ExplicitDenyTagEnvironment",
            "Effect": "Deny",
            "Action": [
                "ec2:RunInstances",
                "ec2:CreateVolume",
                "elasticloadbalancing:CreateLoadBalancer",
                "elasticloadbalancing:AddTags",
                "autoscaling:CreateAutoScalingGroup",
                "autoscaling:CreateOrUpdateTags"
            ],
            "Resource": [
                "*"
            ],
            "Condition": {
                "Null": {
                    "aws:RequestTag/Environment": "true"
                }
            }
        }
    ]
}

# print(json.dumps(data, indent=

dictionary = data['Statement']
for item in dictionary:
    print(item['Action'])
