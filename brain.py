﻿#!/usr/bin/python# -*- coding: UTF_8 -*-import randomclass allIn():    """This is temporarily something which will make a player randomly leave a table."""    def __init__(self, forcedToPlay=False):        self.name = "allIn"        self.forcedToPlay = forcedToPlay    def tossACoin(self):        return bool(random.getrandbits(1))    def wantToJoinAGame(self):        if self.forcedToPlay:            return True        else:            return self.tossACoin()    def wantToLeaveAGame(self):        if self.forcedToPlay:            return False        else:            return self.tossACoin()if __name__ == "__main__":    pass