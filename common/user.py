class User:
    nickname = ''
    fname = ''
    lname = ''

    @staticmethod
    def set_nickname(nickname):
        User.nickname = nickname

    @staticmethod
    def get_nickname():
        return User.nickname

    @staticmethod
    def set_fname(fname):
        User.fname = fname

    @staticmethod
    def get_fname():
        return User.fname

    @staticmethod
    def set_lname(lname):
        User.lname = lname

    @staticmethod
    def get_lname():
        return User.lname

    @staticmethod
    def get_name():
        return User.fname + " " + User.lname

    @staticmethod
    def get_shortName():
        short_name = User.fname[0] + User.lname[0]
        return short_name
