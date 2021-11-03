from django import forms

#   Создать форму для пользователя с полями first_name, last_name, age, email, phone_number
# сделать валидацию для first_name, last_name должны начинаться с заглавной буквы,
# age должен быть позитивным числом и старше 14,
# phone_number должен начинаться с +996 и содержать 10 цифр
# Создать метод обработчик формы user()


def is_capital(value):
    if value[0] != value[0].title():
        raise forms.ValidationError('First letter must be uppercase!')


def valid_age(value):
    if value < 14:
        raise forms.ValidationError('You should be older than 14!')


def valid_phone_number(value):
    if value[0:4] != '+996' or len(value) != 10:
        raise forms.ValidationError('Phone number must start with "+996" and contain 10 digits!')


class UserForm(forms.Form):
    first_name = forms.CharField(max_length=25, validators=[is_capital])
    last_name = forms.CharField(max_length=25, validators=[is_capital])
    age = forms.IntegerField(validators=[valid_age])
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=10, validators=[valid_phone_number])
