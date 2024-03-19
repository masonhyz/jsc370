from googleapiclient.discovery import build
import pandas as pd
import seaborn as sns


api_key = "AIzaSyB1X0mAb0CP6t6WTUyXZypJTxwxg5meybw"
channel_id = "UCpLcXDC0x516xkamfP3-JHg"
YT = build("youtube", "v3", developerKey=api_key)


def get_channel_stats(youtube, channel_id):
    request = youtube.channels().list(
        part='snippet,contentDetails,statistics',
        id=channel_id)
    response = request.execute()

    data = dict(Channel_name=response['items'][0]['snippet']['title'],
                Subscribers=response['items'][0]['statistics']['subscriberCount'],
                Views=response['items'][0]['statistics']['viewCount'],
                Total_videos=response['items'][0]['statistics']['videoCount'])
    return data

print(get_channel_stats(YT, channel_id))
