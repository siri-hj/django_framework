from django import forms

class BootStrap():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            #字段中有属性，保留原来属性，没有属性才增加
            if field.widget.attrs:
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.label
            else:
                field.widget.attrs = {
                    "class": "form-control",
                    "placeholder": field.label
                }

class BootStrapForm(BootStrap, forms.Form):
    pass

class BootStrapModelForm(BootStrap, forms.ModelForm):
    pass
