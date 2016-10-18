from pushbullet import Pushbullet


apiKey = "Api_goes_here"
pb = Pushbullet(apiKey)

push = pb.push_note("This is the title", "This is the body")

