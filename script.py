horoscopes = {"aries": "You're able to influence others. Today you may be put on the spot in front of many people. You will handle it well!",
             "taurus": "You will get an unexpected windfall today. It might be in cash, but more likely it will be an opportunity. A business partner might push you into a more lucrative area. Whatever it is, you're going to excel.",
             "gemini": "You have a sharp mind. You don't use it to anywhere near its capacity. Your brain is like a thoroughbred horse, trained to run at high speed. This type of animal should not be penned up. Your mind needs room to exercise and grow.",
             "cancer": "You need a day off. Try to rest. Curl up with a good book. Only go out if you're feeling absolutely stir crazy. Indulge your need to refresh yourself. Everything will fall into place.",
             "leo": "You can expect a lot social contact. Just when you thought you'd never receive another invite, three come your way. Resist the urge to decline. You will meet a very interesting person.",
             "virgo": "You are very persuasive. If you aren't already an attorney, you should be. Your career is about to skyrocket. Success is all but guaranteed for you. If you have a partner to share this with you are doubly blessed.",
             "libra": "Your focus is on point today. Your abilities are amazingly sharp. You could sell anything to anybody! Make the most of this by beginning a new project you've been considering.",
             "scorpio": "You will be incredibly creative today. If you're unable to take time to paint or write, at least take small steps to ensure your abilities don't go to waste. Sign up for a class or joining a writing group! The social contact will give your talents a big boost.",
             "sagittarius": "Today you will want to be alone with your thoughts. You may not be very cooperative if you do try to go out. Indulge yourself. You might want to spend some time in meditation. Listen to yourself. You're on the verge of a major self-discovery.",
             "capricorn": "Today you will make a leap in your career. Your intellect and communicative skills have paved the way for your advancement. You have been hard at work and it's about to pay off big!",
             "aquarius": "This is an ideal day to put some plans into action. Your imagination and creativity are hightened, and you're having a way with words. You are guaranteed to have a brilliant idea.",
             "pisces": "This is an ideal day to follow through with your recent plans. Your creativity and inspiration are shining bright. You could make a deal with anyone. If you're ready to pitch a big idea, try it now."}

print("What's your name?")
name = input()
print("What's your sign?")
sign = input().lower().strip()

if sign in ["aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn", "aqaurius", "pisces"]:    
      horoscope = horoscopes[sign]
      print("Hello " + name + " " + horoscope)
else:
    while sign not in ["aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn", "aqaurius", "pisces"]:
      print("I can't find that sign.  Please choose between: Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, Capricorn, Aqaurius, or Pisces")
      sign = input().lower().strip()
      if sign in ["aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn", "aqaurius", "pisces"]:    
        horoscope = horoscopes[sign]
        print("Hello " + name + " " + horoscope)
        break
    
    