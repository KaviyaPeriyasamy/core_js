import frappe

def validate(self,action):

    if self.status =="Converted":
        self.custom_make_read_only = 1