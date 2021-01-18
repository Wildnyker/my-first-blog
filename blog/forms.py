from django import forms
from .models import Post


class PostForm(forms.ModelForm): # we are inheriting the structure of post to create forms

    class Meta: #
        model = Post #we tell Django which model should be used to create this form (model = Post).
        fields = ('title', 'text',) # here we define which fields from Post model will me avaliable for filling
        # we need to connect it to our html


        #author should be the person who is currently logged in (you!)
        # and created_date should be automatically set when we create a post (i.e. in the code)

