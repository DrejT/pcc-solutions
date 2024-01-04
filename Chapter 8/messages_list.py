#show_messages
def show_message(list):
	print(list)

messages = ["whutnow","epic","nut"]
show_message(messages)
print("\n")
#send_messages
sent_messages =[]

def send_messages(messages,sent_messages):
	'''appending messages to sent_messages'''
	while messages:
		for message in messages:
			message = messages.pop()
			print(f"sending message: {message}")
			sent_messages.append(message)

def message(messages,sent_messages):
	'''printing modified list'''
	print(messages)
	for message in sent_messages:
		print(message)
	print("\n")
	print(messages)

send_messages(messages[:],sent_messages)
print("\n")
message(messages,sent_messages)
print("\n")
print(messages)