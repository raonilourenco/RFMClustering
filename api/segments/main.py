import pandas as pd
from flask import jsonify

def get_segment(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        We expect an ID or a list of IDs
    Returns:
        A json with IDs as keys and the segment as value.
    """
    ids = request.args.getlist('id')
    data = pd.read_csv('costumers.csv',header=0)
    return jsonify(
        data[data['CustomerID'].isin(ids)][['CustomerID', 'Segment']].set_index('CustomerID').to_dict()['Segment']
    )
