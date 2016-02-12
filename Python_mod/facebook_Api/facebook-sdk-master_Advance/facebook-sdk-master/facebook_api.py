import facebook
##C:\Python34\facebook_Api\facebook-sdk-master_Advance\facebook-sdk-master
#token = "752622311550197|-HuwQum48yl7jX8ztP0DLSBaiu8"
#token="926647970743048"
#https://graph.facebook.com/752622311550197/accounts/test-users?access_token=752622311550197|-HuwQum48yl7jX8ztP0DLSBaiu8&installed=true&locale=en_GB&permissions=read_stream,read_friendlists,publish_stream
token="CAACEdEose0cBAMzlAqPIg9pn3UrsumYLVZBORHO6t1nCxONQUAJjHS8Ajcy2rGphLka5MRBOHBIDRCFhPS0cm1J1Kl8h6RikQgmjbZAsswxVqdPIlX10JKKU91fgmemDboAlvZBZCe1HCFMCIzu2svDj7sktmCFyXZCGueemHqHgGQsZBQvzz0deOFMIvzF75A5JlotxDZAfbSmxtmHZB8Lu"
api_version = "v2.0"

graph = facebook.GraphAPI(token)
profile = graph.get_object("me")
print(profile['name'])
data = graph.request('/search?q=Airlift&type=user')
##data = graph.request('search', {'q': 'Mastizadee', 'type': 'page'})
## Working Fine
##data = graph.request('search', {'q': 'Airlift', 'type': 'post'})
print (data)
##friends = graph.get_connections("me", "friends",api_version)
friends = graph.get_connections(profile['id'], 'friends')["data"]
##friends = graph.get_connections(profile['id'], 'posts')                             
##graph.put_object("me", "Akash", message="I am writing on my wall!")
    ##friend_list = [friend['Bitan'] for friend in friends['data']]
##print (len(friends))

##for post in friends
   ## print(post["message"])


