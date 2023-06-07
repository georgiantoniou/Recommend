class Configuration:
    def __init__(self, adict):
        self.__dict__.update(adict)
    def set(self, key, value):
        self.__dict__[key] = value
    def shortname(self):
        l = []
        if hasattr(self, 'recommend_freq'):
            l.append("freq={}".format(self.recommend_freq))
        l.append("qps={}".format(self.recommend_qps))
        return '-'.join(l)
