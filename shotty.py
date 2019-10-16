import boto3

<<<<<<< HEAD
#script
=======
>>>>>>> 9181126535ca0dc32fd40b44853e28ffa9d03848
if __name__ == '__main__':
    session = boto3.Session(profile_name='shotty')
    ec2 = session.resource('ec2')
    for i in ec2.instances.all():
        print(i)
