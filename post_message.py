import facebook
from facebook import GraphAPIError
from random import randint


def post_a_feed(page_id, access_token):
    page_graph = facebook.GraphAPI(access_token=access_token, version=3.0)
    response = page_graph.put_object(
       parent_object=page_id,
       connection_name="feed",
       message=randint(0,100),
       link="https://www.facebook.com")
    print ('Đã post lên facebook feed: %s' % response)
    return response['id']


def get_a_feed(fid, access_token):
    feed = facebook.GraphAPI(access_token=access_token, version=3.0)\
        .get_object(id=fid, fields='message')
    return feed


access_token = 'EAAOEzN0ZAZCWABAF5tZCBPAoTDgzdJ14C7zgZC0jFM1yPuvs6Q4VkZAlfbZCX2r7DrgLu05IMmwb6nzg1R9Ot6xYZCWTPlUzeULEs7iFjZCKBfLlJJFyp1bdzW83XalmByYwztPHgn16KZC1qWcX1g6oBPqV8ntpUYA8a55KC1r8bRaE091LNTY6YI7j3fszy3SEZD'
graph = facebook.GraphAPI(access_token=access_token, version=3.0)
accounts = graph.get_connections('me', 'accounts')

if accounts.get('data'):
    pages = accounts['data']
    for p in pages:
        if p['name'] == 'DWO':
            fid = post_a_feed(p['id'],p['access_token'])
            print(get_a_feed(fid, p['access_token']))

print('-' * 20)


