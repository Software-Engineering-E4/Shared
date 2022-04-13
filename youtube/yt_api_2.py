from googleapiclient.discovery import build 
api_key= 'AIzaSyAvn6yIJd0ovZRR0SSK_OUW6yRG0N4wFg4'
youtube = build('youtube', 'v3', developerKey=api_key)
#START 1README
request = youtube.search().list(
    part='snippet, contentDetails, statistics',
    order='relevance',
    q='cancer colorectal'
)
all_data=[]
response=request.execute()
#FINAL 1README
#START 2README
for i in range(len(response['items'])):
    data = dict(Channel_name =  response ['items'] [i] ['snippet'] ['title'] ,
                Subscribers = response ['items'] [i] ['statistics'] ['subscriberCount'],
                Views = response ['items'] [i] ['statistics'] ['viewCount'],
                Likes = ['items'] [i] ['statistics'] ['likeCount'],
                Dislikes = ['items'] [i] ['statistics'] ['dislikeCount'],
                Comments = ['items'] [i] ['statistics'] ['commentCount'],
                Video_Duration = ['items'] [i] ['contentDetails'] ['duration']
            )
all_data.append(data)
#FINAL 2README
print (all_data)