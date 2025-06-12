from django import forms # Importa o módulo dos formulários do django.

# Classe referente ao formulário de login (nome e senha)
class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control w-full px-4 py-3 bg-gray-800 text-white rounded border border-gray-700 focus:outline-none focus:ring-2 focus:ring-red-500',
                'placeholder': 'Digite o seu nome de login',
                
            }
        )
    )
    senha=forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control w-full px-4 py-3 bg-gray-800 text-white rounded border border-gray-700 focus:outline-none focus:ring-2 focus:ring-red-500',
                'placeholder': 'Digite a sua senha',
            }
        )
    )
    
# Classe referente ao formulário de cadastro
class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label='Nome de Cadastro',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control w-full px-4 py-3 bg-gray-800 text-white rounded border border-gray-700 focus:outline-none focus:ring-2 focus:ring-red-500',
                'placeholder': 'Digite o seu nome de cadastro',
            }
        )
    )
    email=forms.EmailField(
        label='E-mail',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control w-full px-4 py-3 bg-gray-800 text-white rounded border border-gray-700 focus:outline-none focus:ring-2 focus:ring-red-500',
                'placeholder': 'Digite o seu e-mail',
            }
        )
    )
    senha=forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control w-full px-4 py-3 bg-gray-800 text-white rounded border border-gray-700 focus:outline-none focus:ring-2 focus:ring-red-500',
                'placeholder': 'Digite a sua senha',
            }
        ),
    )
    
    
    
    
