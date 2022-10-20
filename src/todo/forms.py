from django import forms

class TodoFormClass(forms.Form):
    title = forms.CharField(max_length=100, label="タイトル", widget=forms.TextInput(
        attrs={'placeholder': 'タイトル...'}))
    content = forms.CharField(max_length=1000, label="内容", widget=forms.Textarea(
        attrs={'placeholder': '内容...'}))
