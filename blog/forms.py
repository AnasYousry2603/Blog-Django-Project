from django import forms
from .models import Comment

class Commentform(forms.Form):
    class Meta:
        model = Comment
        fields = "__all__"
        exclude = ["post"]
        labels = {
            "user_name": "You name",
            "user_email": "Your Email",
            "text": "Your Comment"
        }   # changing the name that will appear