from django.core.exceptions import ValidationError
from django import forms
from pironapp.models import User


def get_login_user_info(v_email, v_password):
    user_info = User.objects.filter(login_id=v_email, password=v_password)
    return user_info


class LoginForm(forms.Form):
    login_id = forms.CharField(
        widget=forms.TextInput(attrs={
            "id": "login_id",
            "class": "form-control input-field",
            "placeholder": "メールアドレス"
        }), required=True
    )

    login_pass = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "id": "login_pass",
            "class": "form-control input-field",
            "placeholder": "パスワード"
        }), required=True
    )

    def clean(self):
        cleaned_data = super().clean()
        login_id = cleaned_data.get('login_id')
        login_pass = cleaned_data.get('login_pass')

        if not (login_id and login_pass):
            raise ValidationError('ログインIDとパスワードを入力してください。')

        user_info = get_login_user_info(login_id, login_pass)
        if not user_info.count() == 1:
            raise ValidationError('ログインIDまたはパスワードが正しくありません。')
        
        return user_info        
