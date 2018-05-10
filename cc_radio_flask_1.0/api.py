def gen_url(user_id, hour, category):
    return "https://s3.amazonaws.com/cc-project-s3/{0}/{1}_{2}.mp3".format(user_id, hour, category)


def get_audio_url(user_id):
    """
    category: 0 summary
              1 science
              2 business
              3 sport
              4 world
    """
    dic = {}
    for i in range(0, 24):
        tmp = {}
        for j in range(0, 5):
            tmp[j] = gen_url(user_id, i, j)
        dic[i] = tmp

    return dic