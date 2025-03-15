import logging
from typing import Any

import boto3
from boto3.dynamodb.conditions import Attr

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

VOTES_TABLE = None

DYNAMO_CLIENT = None

# The current competition. Set in the backend so tech-savvy users can't modify previous results
COMPETITION = 'pie:2025'


def get_votes_table() -> Any:
    """
    Gets the votes table
    :return: the votes table
    """
    global VOTES_TABLE, DYNAMO_CLIENT
    if VOTES_TABLE is None:
        DYNAMO_CLIENT = boto3.resource('dynamodb')
        VOTES_TABLE = DYNAMO_CLIENT.Table('phastcompetition')

    return VOTES_TABLE


def lambda_handler(event, context) -> dict:
    if 'voter' not in event or 'votes' not in event:
        return {'error': 'Invalid Request'}
    voter = event['voter'].lower()
    votes = [vote.lower() for vote in event['votes']]
    if voter in votes:
        return {'error': 'You can\'t vote for yourself!'}

    if len(votes) != 3:
        return {'error': 'You must vote for 3 people!'}

    if len(set(votes)) != 3:
        return {'error': 'You cannot vote for the same person twice!'}
    table = get_votes_table()
    try:
        table.put_item(Item={'voter': voter, 'votes': votes, 'competitionId': COMPETITION},
                       ConditionExpression=Attr('competitionId').not_exists() & Attr('voter').not_exists())
    except DYNAMO_CLIENT.meta.client.exceptions.ConditionalCheckFailedException:
        return {'error': 'You can\'t vote twice!'}
    return {}
