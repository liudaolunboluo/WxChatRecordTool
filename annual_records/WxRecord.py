class WxRecord:

    def __init__(self, create_time, to_user, from_user):
        self.create_time = create_time
        # 我发给他
        self.to_user = to_user
        # 他发给我
        self.from_user = from_user
