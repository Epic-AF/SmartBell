from pushbullet import Pushbullet


apiKey = "o.giFKbcb02CDCluBRGLZ9q5VwSXC6fWGz"
pb = Pushbullet(apiKey)

push = pb.push_note("This is the title", "This is the body")

