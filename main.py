from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent, GiftEvent
import pixxo

# Instantiate the client with the user's username
client: TikTokLiveClient = TikTokLiveClient(unique_id="@sang_adipati.13")


# Define how you want to handle specific events via decorator
@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("Connected to Room ID:", client.room_id)


# Notice no decorator?
async def on_comment(event: CommentEvent):
    print(f"{event.user.nickname} -> {event.comment} -> {event.user.profilePicture}")


async def on_gift(event: GiftEvent):
    print(
        f"{event.user.nickname} -> {event.gift.giftId} -> {event.gift.giftDetails.giftName} -> {event.gift.repeatCount} X -> {event.gift.giftDetails.diamondCount} Diamond -> {event.gift.repeatEnd}")


# Define handling an event via "callback"
client.add_listener("comment", on_comment)
# client.add_listener("gift", on_gift)

if __name__ == '__main__':
    # Run the client and block the main thread
    # await client.start() to run non-blocking
    client.run()

    list1 = [1, 2]
    list2 = [3, 4]

    sumIndexList = [list2[0], list2[1]]

    # pixxooo = pixxo.Pixoo("6C:5D:63:77:B1:7D")
    # pixxooo.connect()
    # pixxooo.draw_pic()
