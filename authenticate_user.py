import boto3
import json
import sys
import getopt

def sign_in(str_client_id, str_user_pool_id, str_username, str_password, client):
    signin_response=client.initiate_auth(
        AuthFlow="USER_PASSWORD_AUTH",
        AuthParameters={
            "USERNAME": str_username,
            "PASSWORD": str_password
        },
        ClientId=str_client_id
    )
    
    print(signin_response['AuthenticationResult']['IdToken'])


# sign_in

def usage():
    print("Syntax: authenticate_user.py --username=<username> --pool-id=<user pool id> --client-id=<app client id> --password=<password> --region=aws-region-code")
    print("All variables are required.")
def main(argv):

    try:
        opts, args=getopt.getopt(argv, '', ["username=", "pool-id=", "client-id=", "region=", "password="])
    except getopt.GetoptError as e:
        print(e.msg)
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-u", "--username"):
            str_username=arg
        elif opt in ("-p", "--pool-id"):
            str_user_pool_id=arg
        elif opt in ("-c", "--client-id"):
            str_client_id=arg
        elif opt in ("-r", "--region"):
            str_region=arg
        elif opt in ("-pw", "--password"):
            str_password=arg
        else:
            usage()
        # if opt
    # for opt,arg

    print("authenticate_user")
    print("-----------")
    try:
        print('username: ' + str_username)
        print('user pool id: ' + str_user_pool_id)
        print('app client id: ' + str_client_id)
        print('password: ' + str_password)
        print('region: ' + str_region)
    except UnboundLocalError:
        usage()
        sys.exit(2)

    client = boto3.client("cognito-idp", region_name=str_region)

    print("Performing authentication...  ")
    sign_in(str_client_id, str_user_pool_id, str_username, str_password, client)

# main()

main(sys.argv[1:])

