class gobal_v(object):

    _gobal_dict={}

    def set_dict(self,key,value):
        self._gobal_dict[key]=value

    def get_dict(self,key):
        return self._gobal_dict[key]

    def show_dict(self):
        return self._gobal_dict