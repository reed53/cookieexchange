from argparse import ArgumentParser

import boto3
import matplotlib.pyplot as plt
from boto3.dynamodb.conditions import Key


def main(competition_id: str):
    db_client = boto3.resource('dynamodb')
    votes_table = db_client.Table('phastcompetition')
    results = votes_table.query(KeyConditionExpression=Key('competitionId').eq(competition_id))['Items']
    vote_counts = {}
    for res in results:
        for vote in res['votes']:
            if vote not in vote_counts:
                vote_counts[vote] = 0
            vote_counts[vote] += 1
    plt.bar(list(vote_counts.keys()), list(vote_counts.values()))
    plt.title('Results')
    plt.xlabel('Competitor')
    plt.ylabel('Vote Count')

    plt.show()


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('competition_id', type=str, help='The ID of the competition to plot')
    args = parser.parse_args()
    main(args.competition_id)