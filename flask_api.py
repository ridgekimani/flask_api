"""
This is a simple flask api that gets bucket lists
It also implements functionality to get a specific bucket
"""

import datetime
from flask import Flask, jsonify, abort

APP = Flask(__name__)


BUCKET_LISTS = [
    {
        'user': 'test@user.com',
        'bucket_name': 'test_bucket',
        'description': 'Test description',
        'category': 'Health',
        'created': datetime.date(2017, 7, 19),
        'key': '00000000'
    },
    {
        'user': 'test@user1.com',
        'bucket_name': 'test_bucket1',
        'description': 'Test description1',
        'category': 'Health',
        'created': datetime.date(2017, 7, 19),
        'key': '11111111'
    }
]


@APP.route('/bucketlist/api/v1.0/bucketlists/<bucket_id>', methods=['GET'])
def get_bucketlist(bucket_id):
    """
    This function is used to get a specific bucket id
    :param bucket_id:
    :return: json response
    """
    bucket = [item for item in BUCKET_LISTS if item['key'] == bucket_id]
    if len(bucket) == 0:
        abort(404)
    return jsonify({'bucket_list': bucket})


@APP.route('/bucketlist/api/v1.0/bucketlists/', methods=['GET'])
def get_bucketlists():
    """
    This functinn is used to get the whole bucket list
    :return: json
    """
    return jsonify({'bucket_lists': BUCKET_LISTS})


if __name__ == '__main__':
    APP.run()
