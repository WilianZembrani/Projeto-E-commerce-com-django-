from django import forms
from django.contrib.auth.models import User
from . import models

class PerfilForm(forms.ModelForm):
    class Meta:
        model = models.Perfil
        fields = '__all__'
        exclude = ('usuario',)

class UserForms(forms.ModelForm):
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput,
        label="Senha"
    )
    
    password2 = forms.CharField(
        required=False,
        widget=forms.PasswordInput,
        label="Confirmação senha"
    )

    def __init__(self, usuario=None, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Corrigido para chamar o método correto
        self.usuario = usuario

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 'password2', 'email')

    def clean(self):
        cleaned_data = super().clean()  # Obtenha os dados limpos do formulário
        validation_error_msgs = {}

        usuario_data = cleaned_data.get('username')
        email_data = cleaned_data.get('email')
        password_data = cleaned_data.get('password')
        password2_data = cleaned_data.get('password2')
        
        usuario_db = User.objects.filter(username=usuario_data).first()
        email_db = User.objects.filter(email=email_data).first()
        
        error_msg_user_exists = 'Usuário já existe'
        error_msg_email_exists = 'Email já existe'
        error_msg_password_match = 'As senhas não conferem'
        error_msg_password_short = 'Sua senha precisa ter pelo menos 6 caracteres' 

        if self.usuario:
            if usuario_db and usuario_data != usuario_db.username:
                validation_error_msgs['username'] = error_msg_user_exists
            
            if email_db and email_data != email_db.email:
                validation_error_msgs['email'] = error_msg_email_exists

            if password_data:
                if password_data != password2_data:
                    validation_error_msgs['password'] = error_msg_password_match
                    validation_error_msgs['password2'] = error_msg_password_match

                if len(password_data) < 6:
                    validation_error_msgs['password'] = error_msg_password_short

        if validation_error_msgs:
            raise forms.ValidationError(validation_error_msgs)
