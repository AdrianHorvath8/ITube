from .models import Comment


from django.forms import ModelForm

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
        labels = {
            "body": ""
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields["body"].widget.attrs.update({"class":"comment-text-field"})
        self.fields["body"].widget.attrs.update({"placeholder":"Add a comment..."})
