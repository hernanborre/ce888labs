from sopel import module
from emo.wdemotions import EmotionDetector

emo = EmotionDetector()

@module.rule('')
def hi(bot, trigger):
    print(trigger)
    print(emo.detect_emotion_in_raw_np(trigger))
    array = emo.detect_emotion_in_raw_np(trigger)
    array = array.tolist()
    array = [int(i) for i in array]
    print(str(array))
    #bot.say(str(array))
    #print(trigger, trigger.nick)
    #bot.say('Hi, ' + trigger.nick)
