import time
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import SendMessageRequest

# Replace with your own values
api_id = '29038310'
api_hash = 'f5668672811e7b9c88ab641248914fdd'
phone_number = '18706869984'
channel_id='-1002113847622'

with TelegramClient('session', api_id, api_hash) as client:
 # Login to your account
 client.connect()

 # List of group usernames or IDs to send message to
 group_list = ['https://t.me/Gainmedia','https://t.me/socialsmarket','https://t.me/socialsmarket','https://t.me/instamarket4u',
               'https://t.me/SocialMarkets','https://t.me/Thejunglemarket','https://t.me/SocialMarkets','https://t.me/GodsMarket','https://t.me/coasts',
               'https://t.me/jezzy_market1','https://t.me/BlossomGroupChat','https://t.me/marketcrews','https://t.me/marketsogu','https://t.me/swapmarket',
               'https://t.me/swapmarket','https://t.me/austinschat','https://t.me/FrozenMarketplace','https://t.me/reacquired','https://t.me/boostingsales',
                'https://t.me/TheLazyMarket','https://t.me/RebelsMarket','https://t.me/ElonsMarket','https://t.me/ZsMarketplace','https://t.me/oghandleschat',
                'https://t.me/marketchatavsnr','https://t.me/vvmarkets','https://t.me/marketisms','https://t.me/machosmarket','https://t.me/instagimx',
               'https://t.me/marketsogu','https://t.me/declassification','https://t.me/accuntsbuyings','https://t.me/marketnoble','https://t.me/emarketchat',
               'https://t.me/social_media_market0','https://t.me/hurricanewts','https://t.me/swapmarket','https://t.me/socialoption',
                'https://t.me/SouthMarket','https://t.me/cockmp','https://t.me/WiredMarket','https://t.me/yeshinzuOxh8e','https://t.me/machosmarkett',
               'https://t.me/LumMarket','https://t.me/jmarkettt','https://t.me/ClampedMP','https://t.me/pikachumarket','https://t.me/topmarts','https://t.me/oasis',
               'https://t.me/TheGangMP','https://t.me/socialmediatalk','https://t.me/hubofmarkets','https://t.me/telewts','https://t.me/wysmarketingchat2',
               'https://t.me/EvolveMarket','https://t.me/explosiveness','https://t.me/beaversmarketplace','https://t.me/GodsMarket','https://t.me/surgemarket',
               'https://t.me/SocialCapitalmarket','https://t.me/instamarket08','https://t.me/solmarkett','https://t.me/SouthMarket','https://t.me/cancelsmarket',
               'https://t.me/boostmaddies','https://t.me/machosmarket','https://t.me/certainlymp','https://t.me/hurricanewts','https://t.me/Marketbigg',
               'https://t.me/SkullMarketChat','https://t.me/venders','https://t.me/marketisms','https://t.me/boostmaddies','https://t.me/vvmarkets','https://t.me/Aknaei']
               
               


 # Get the entity (channel) by its ID
 entity = client.get_entity(int(channel_id))

 # Get the last message from the channel
 message_id=5
 op = client.get_messages(entity,ids=message_id)
 # Iterate through each group and send message
 loop=True
 while loop:
    for group in group_list:
        try:
            client.forward_messages(group,op)
            print(f"Message sent to {group}")
        except Exception as e:
            print(f"Failed to send message to {group}: {e}")
    time.sleep(1800)
