def get_audio_url(user_id, hour, category):
    """
    category: 0 summary
              1 science
              2 business
              3 sport
              4 world
    """
    return "https://s3.amazonaws.com/cc-project-s3/{0}/{1}_{2}.mp3".format(user_id, hour, category)
