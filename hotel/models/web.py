from xmlrpc import client

server_url = 'http://localhost:8014'
db_name = 'api'
username = 'admin'
password = 'admin'
common = client.ServerProxy('%s/xmlrpc/2/common' %server_url)

version_info = common.version()
print(version_info)

uid = common.authenticate(db_name, username, password, {})


if uid:
	print("Success: User id is", uid)
else:
	print("Failed: wrong credentials")

models = client.ServerProxy('%s/xmlrpc/2/object' %server_url)

partners= models.execute_kw(db_name, uid, password,'res.partner', 'search',[[]])

print("partners...", partners)

partners= models.execute_kw(db_name, uid, password,'res.partner', 'search', [[]],{'offset': 10, 'limit': 5})

print("partners...", partners)

partners_count= models.execute_kw(db_name, uid, password,'res.partner', 'search_count', [[]])

print("partners count...", partners_count)