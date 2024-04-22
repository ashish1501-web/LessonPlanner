topic=""
def set_topic(input):
    global topic
    topic=input

def get_topic_to_scrape():
    global topic
    print("get_topic_to_scrape"+topic)
    return topic