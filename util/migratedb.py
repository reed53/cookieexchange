import boto3


def main():
    db_client = boto3.resource('dynamodb')
    votes_table = db_client.Table('cookieexchange')
    new_table = db_client.Table('phastcompetition')

    for vote in votes_table.scan()['Items']:
        vote['competitionId'] = 'cookie:2024'
        new_table.put_item(Item=vote)


if __name__ == '__main__':
    main()