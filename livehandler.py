from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent, GiftEvent
from apscheduler.schedulers.background import BackgroundScheduler
from itertools import groupby
# import translators as ts
from itertools import islice


def by_size(words, size):
    result = []
    for word in words:
        if len(word) == size:
            print(word)
            result.append(word)
    return result


class LiveHandler:
    def __init__(self, username):
        self.username = username
        self.list_user_message = []
        self.list_message = []
        self.list_gift = []
        self.scheduler = BackgroundScheduler()
        self.size_word = 6
        self.client: TikTokLiveClient = TikTokLiveClient(unique_id=self.username)

    def connect(self):
        @self.client.on("connect")
        async def on_connect(_: ConnectEvent):
            print("Connected to Room ID:", self.client.room_id)

        self.scheduler.add_job(self.remove_list_comment, 'interval', seconds=30, id="remove_comment")
        self.scheduler.start()
        self.client.run()

    def remove_list_comment(self):
        print("-------------------------------\nClean List\n-------------------------------")
        self.client.remove_listener("comment", self.on_comment)
        self.client.remove_listener("gift", self.on_gift)
        self.scheduler.pause()
        # self.translate()
        list_all = [list(j) for i, j in groupby(sorted(self.list_message))]
        list_all.sort(key=len, reverse=True)
        print("List All", list_all)

        if len(self.list_message) > 0:
            self.list_message.clear()
            self.list_user_message.clear()

        self.setup_listener()
        self.scheduler.resume()

        print("-------------------------------\nRestart\n-------------------------------")

    def translate(self):
        list_all = by_size(self.list_message, self.size_word)
        # list_all = [list(j) for i, j in groupby(sorted(list_all))]
        # print("List All", list_all)
        # if len(list_all) > 0:
        #     print("Translating")
        #     list_all.sort(key=len, reverse=True)
        #     for data in islice(list_all, 3):
        #         print(f"Translate size {len(data)} - {data[0]} - {ts.google(data[0])}")
        # print("Start")
        # self.scheduler.resume()
        # self.setup_listener()

    def count_word(self):
        list_all = [list(j) for i, j in groupby(sorted(self.list_message))]
        list_all.sort(key=len, reverse=True)
        rank = 1
        if len(self.list_message) > 0:
            for data in list_all:
                print(f"Rank {rank} : {len(data)} - {data[0]}")
                rank += 1

    def setup_listener(self):
        self.client.add_listener("comment", self.on_comment)
        self.client.add_listener("gift", self.on_gift)

    async def on_comment(self, event: CommentEvent):
        if event.user.userId not in self.list_user_message:
            self.list_user_message.append(event.user.userId)
            self.list_message.append(event.comment.upper())
        print(f"{len(self.list_message)} -> {len(self.list_user_message)} = {self.list_message}")
        self.count_word()

    async def on_gift(self, event: GiftEvent):
        print(f"{event.user.nickname} -> {event.gift.giftId} -> {event.gift.giftDetails.giftName}")


live = LiveHandler("@tokoummumaher")
live.setup_listener()
live.connect()
