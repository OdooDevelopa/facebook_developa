import facebook
from urllib import parse

graph = facebook.GraphAPI(version=3.0)

app_id = "990440347794784"
app_secret = '504c5ffedaa4eb0e172df686d6a5361c'
canvas_url = "https://localhost:8069"
perms = ['manage_pages',
         'pages_manage_instant_articles',
         'pages_show_list',
         'publish_pages',
         'read_insights',
         'read_page_mailboxes',
         'publish_to_groups',]
fb_login_url = graph.get_auth_url(app_id, canvas_url, perms)
print(fb_login_url + '&response_type=token')

url = 'https://localhost:8069/?access_token=EAAOEzN0ZAZCWABAF5tZCBPAoTDgzdJ14C7zgZC0jFM1yPuvs6Q4VkZAlfbZCX2r7DrgLu05IMmwb6nzg1R9Ot6xYZCWTPlUzeULEs7iFjZCKBfLlJJFyp1bdzW83XalmByYwztPHgn16KZC1qWcX1g6oBPqV8ntpUYA8a55KC1r8bRaE091LNTY6YI7j3fszy3SEZD&expires_in=6399'
access_token = parse.parse_qs(parse.urlparse(url).query).get('access_token')
print(access_token[0])
