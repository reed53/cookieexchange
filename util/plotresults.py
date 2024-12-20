import boto3
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def main():
    db_client = boto3.resource('dynamodb')
    votes_table = db_client.Table('cookieexchange')
    results = votes_table.scan()['Items']
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
    main()