class ConvertTime:
    def convert(dt):
        if dt >= 60 and dt < 3600:
            t = divmod(dt, 60)
            return "{}m {}s".format(int(t[0]), int(t[1]))
        elif dt >= 3600:
            h = divmod(dt, 3600)
            m = int(divmod(h[1], 60)[0])
            return "{}h {}m".format(int(h[0]), m)
        else:
            return "{}s".format(int(dt))
    