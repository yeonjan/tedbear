import os
import sys
import urllib.request
import json


def translate(orig_word):
    client_id = "6eD87zNWX_sVSkUKkFPp"
    client_secret = "QRw_5DFxyZ"
    encText = urllib.parse.quote(orig_word)
    data = "source=en&target=ko&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if rescode == 200:
        response_body = response.read()
        return json.loads(response_body.decode('utf-8'))['message']['result']['translatedText']
    else:
        raise ValueError(rescode)


# print(translate("I've been using it as a journal,but also a joke diary."))
# print(translate("I sometimes go to the gym "))
test = ['A "lob shot" is a short, high trajectory shot that lands softly with little roll.',
        'A "rub of the green" occurs when a ball in motion is accidentally deflected or stopped by any outside agency.',
        'A and C.', 'A baby was born.', 'A balanced diet is important in nutrition.',
        'A ball is "lost" if it is not found by the player within five minutes.',
        'A beautiful picture is hanging on the wall.', "A beautiful sky, isn't it?",
        'A big bottle of beer, too, please.', 'A big truck passed my car.',
        'A black bag of this size.|It has a name tag.', 'A blast upset our boat.', 'A Bloody Mary, please.',
        'A book like this is not suitable for you.', 'A book of this kind is not suitable for you.',
        'A box is an extra sir.', 'A bug is in my dish.|Please bring me another one for it.', 'A bug is in my soup.',
        'A burger and some fries.',
        "A call to Japan, please.|This is Yoshiko Imai in room five-forty-three.|I'd like to make a collect call to Noriko Yasuoka in Tokyo.|The number is country code eight-one, city code three, three-two-three-three-three-one-seven-zero.",
        'A car crashed into the wall.', 'A car is coming.', 'A car was driving towards us.',
        'A clod wave hit Washington.', 'A Company pays well.', 'A conditional clause follows after this.',
        'A coordinate clause follows after this.', 'A couple of hours.', 'A couple of week.',
        'A cube is a solid with six square faces.', 'A cyclone was spawned.',
        'A detailed map will become available soon.', 'A dog bit me on the leg.', 'A dog bit my leg.',
        "A doll house, huh?|Maybe that's a good idea.", 'A dollar in New York seems to be worth about one hundred yen.',
        'A dollar wherever you want to go.', 'A dollar will do.', 'A dollar you can get five.',
        'A double room with, a bathroom and air conditioning, please.', 'A family-first way of life is popular now.',
        'A family-oriented lifestyle is popular now.', 'A ferocious-looking bulldog bit my arm.',
        'A few homes have dish washers.', 'A few hours.',
        'A few people say that capitalism is going to become out of date in the twenty-first century.|What do you think?',
        'A few, but they are nothing like this.', 'A fire broke out in a hotel near my house before daybreak.',
        'A firm putt might spin out.', 'A five and five ones, please.', 'A five and five singles, please.',
        'A flock of swans flew over.', 'A foursome.',
        "A Frenchman asked me something the other day, but I couldn't catch the words he said, so, I had the first class last night.",
        'A friend is coming.', 'A friend of mine in Tokyo bought one for me.',
        "A friend of mine was conferred a master's degree yesterday.", 'A friend of mine, whom you know, passed away.',
        'A gardener is mowing the grass in the park.', 'A gentleman.', 'A giraffe has a long neck.', 'A girl.',
        'A good chance is coming up.|She can wear one for the seven-five-three Festival.',
        'A good hat can make you more stylish.', 'A good heart is important.', 'A good idea came to me.',
        "A good idea just came to me, and I want to write it down so I won't forget.",
        "A good idea just hit me, and I want to write it down so I won't forget.",
        "A good idea just occurred to me, and I want to write it down so I won't forget.",
        'A good idea just struck me.', 'A good idea.', 'A good manager listens to employees.', 'A good shot.',
        'A good trade wind is blowing.']
# print(test)
for orig_word in test:
    print(translate(orig_word))
