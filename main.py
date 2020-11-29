from Channels import Ystats

API_KEY="AIzaSyCK2qE6uIz7QLqybqW9SX12r5MokRFkF4M"
channel_id= "UCOmHUn--16B90oW2L6FRR3A"

chs=Ystats(API_KEY,channel_id)
chs.get_channel_statistics()

