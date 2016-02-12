import facebook

#token = "752622311550197|-HuwQum48yl7jX8ztP0DLSBaiu8"
#token="926647970743048"
#https://graph.facebook.com/752622311550197/accounts/test-users?access_token=752622311550197|-HuwQum48yl7jX8ztP0DLSBaiu8&installed=true&locale=en_GB&permissions=read_stream,read_friendlists,publish_stream
token="CAAKsgYmHrPUBAIE3bmyZCskHUyEBZCOZCFPuNj5gTlE1ZABHCT9EiVoH9ZCRMnIV5fiBdwGgzepvAcYPnauFxiapLky0WbdKCIBy8ytPrtD0PtOVqPbEG8EyB9i7czZCZC5umgc1YF6iANoq00ZBCYCZC8tPhSoGQaxJ60fyixYPX7awr6nzQZCXssEhXQraHxbZAmF5WZClWDR30TjXZAKKjzY4I"
graph = fb.GraphAPI(token)
profile = graph.get_object("me")

friends = graph.get_connections("me", "friends")
##graph.put_object("me", "Akash", message="I am writing on my wall!")
##friend_list = [friend['Bitan'] for friend in friends['data']]
print (len(friends))


