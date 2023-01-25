import boto3
#import boto3 which is aws' sdk for python. This is just a simple project ill be combining to my terraform project.

#Gets the EC2 resource 
ec2 = boto3.client('ec2')

#creates the response which returns the description of the ec2s created
response = ec2.describe_instances()

#prints response
print(response)
