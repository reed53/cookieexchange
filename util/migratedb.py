import boto3


def main():
    db_client = boto3.resource('dynamodb')
    votes_table = db_client.Table('cookieexchange')

    for vote in votes_table.scan()['Items']:
        print(vote) # will prob need to create a new DB with competition as the partition key and then migrate to that


if __name__ == '__main__':
    main()