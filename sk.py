from skpy import Skype
sk = Skype("luminaungucsmub@gmail.com", "IncorrecT@123#") # connect to Skype

sk.user # you
sk.contacts # your contacts
sk.chats # your conversations
contact = sk.contacts["live:.cid.7ae0346b186be43a"]  # receiver id 
contact.chat.sendMsg("This is the skype alert")# message
contact.chat.sendFile(open("/home/sysadmin/lab/sk", "rb"), "env_variable")# file upload
