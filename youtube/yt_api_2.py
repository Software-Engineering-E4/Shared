from itertools import dropwhile
from googleapiclient.discovery import build

from DBManager import DBManager

api_key= 'AIzaSyCeNssf_A9u7bjKNu9DZRL3BzSq2AvMZyA'
youtube = build("youtube", "v3", developerKey=api_key)

request = youtube.search().list(
    part="snippet",
    order="relevance",
    q="cancer colorectal",
    maxResults="50",
    type="video",
    location=(38.11295, -102.30703),
    locationRadius=(1000 km)   #README1
)
all_data = []
response = request.execute()

for item in response["items"]:
    data = {
        "id":item["id"]["videoId"],
        "title": item["snippet"]["title"],
        "description": item["snippet"]["description"],
        "user": item["snippet"]["channelTitle"],
        "published_at": item["snippet"]["publishedAt"],
        "channel_id": item["snippet"]["channelId"],
    }
    all_data.append(data)

db = DBManager(
    host="ip-database.ccrihfbatmnt.eu-central-1.rds.amazonaws.com",
    database="ipdatabase",
    password="6kT4Yi1S7AtqErWTxZyD",
    user="admin",
    port="3306"
)
db.set_table_name("youtube_videos")
db.set_keys(
    [
        "id",
        "likes",
        "title",
        "description",
        "subtitles",
        "views",
        "utc_date"
    ]
)
db.reset()


def get_vals_to_insert(response: dict[str, str | int]) -> str:
    out = ""
    for key in db.keys:
        if isinstance(response[key], str):
            formatted = str(response[key]).replace("'", "").replace('"', "")
            out += f"'{formatted}', "
        else:
            out += f"{str(response[key])}, "
    return out[:-2:]


for post in all_data:
    current = {}
    for key in db.keys:
        try:
            current[key] = post[key]
        except:
            current[key] = 0

    statement = f"insert into youtube_videos values({get_vals_to_insert(current)})"
    db.execute(statement)
db.close()
