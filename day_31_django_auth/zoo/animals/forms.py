from django.forms import ModelForm, CharField, Field
from .models import Animal


class AnimalCreateForm(ModelForm):
    class Meta:
        model = Animal
        fields = "name", "age", "kind", "description"

    name = CharField(max_length=64, label="Animal name")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            print("name: ", name, "field: ", field)
            # field.label_suffix = " ="
            field.attrs["class"] = "model-form"
            # field.label = ...
