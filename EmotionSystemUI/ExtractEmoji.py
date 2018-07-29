import emoji
import csv
from collections import Counter


def contains_target_emoji(tweet):
    """Returns True if at least one of the target emojis appears in a tweet.
    Returns False otherwise."""
    emojis = set(c for c in tweet if c in emoji.UNICODE_EMOJI)
    targets = {'😨', '😱', '😍', '❤', '😳', '😮', '😡', '😠', '😢', '😔',
               '😖', '🤢'}
    return len(emojis & targets) > 0

def extract_emojis(tweet):
    """Searches for emoji characters in a string and removes them.
    Returns a (string, emojis) tuple."""
    emojis = list(c for c in tweet if c in emoji.UNICODE_EMOJI)
    for emoji_ in emojis:
        tweet = tweet.replace(emoji_, '')

    return (tweet, emojis)


def identify_emotions(emojis):
    """Given a list of emojis it identifies the corresponding emotion.
    Returns a list of strings."""
    emotions = set()
    for emoji_ in set(emojis):
        if emoji_ == '😨' or emoji_ == '😱':
            emotions.add("fear")
        if emoji_ == '😍' or emoji_ == '❤':
            emotions.add("happiness")
        if emoji_ == '😳' or emoji_ == '😮':
            emotions.add("surprise")
        if emoji_ == '😡' or emoji_ == '😠':
            emotions.add("anger")
        if emoji_ == '😢' or emoji_ == '😔':
            emotions.add("sadness")
        if emoji_ == '😖' or emoji_ == '🤢':
            emotions.add("disgust")
    return list(emotions)

def print_emotion_ratio():
    """Print frequency and ratio of each of the labels (emotions) in the data."""
    emotions_list = []
    with open('corpus.csv') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')
        for row in csvreader:
            emotions_list.append(row[0])

    c = Counter(emotions_list)
    print("Label distribution in the data:")
    for emotion, frequency in c.most_common():
        print("* {}: {} ({:.2f}%)".format(emotion, frequency,
                                          frequency / len(emotions_list) * 100))


if __name__ == "__main__":
    print_emotion_ratio()
