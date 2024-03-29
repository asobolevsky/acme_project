from django.shortcuts import render, redirect
from .forms import BirthdayForm, Birthday
from .utils import calculate_birthday_countdown


def birthday(request):
    form = BirthdayForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        form.save()
        birthday_countdown = calculate_birthday_countdown(
            form.cleaned_data['birthday']
        )
        form.full_clean()
        context.update({'birthday_countdown': birthday_countdown})
    return render(request, 'birthday/birthday.html', context)


def birthday_list(request):
    birthdays = (
        Birthday.objects.all()
        .order_by('id')
    )
    context = {'birthdays': birthdays}
    return render(request, 'birthday/birthday_list.html', context)


def birthday_save(request):
    form = BirthdayForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('birthday:create')
