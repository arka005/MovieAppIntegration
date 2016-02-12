import facebook

#token = "752622311550197|-HuwQum48yl7jX8ztP0DLSBaiu8"
token="926647970743048"
graph = facebook.GraphAPI(token)
profile = graph.get_object("me")
friends = graph.get_connections("me", "friends")

friend_list = [friend['name'] for friend in friends['data']]


