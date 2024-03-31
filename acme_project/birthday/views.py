from django.shortcuts import render, redirect, get_object_or_404
from .forms import BirthdayForm, Birthday
from .utils import calculate_birthday_countdown


def birthday(request, pk=None):
    instance = get_object_or_404(Birthday, pk=pk) if pk is not None else None
    form = BirthdayForm(request.POST or None, instance=instance)
    context = {'form': form}
    if form.is_valid():
        form.save()
        birthday_countdown = calculate_birthday_countdown(
            form.cleaned_data['birthday']
        )
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


def delete_birthday(request, pk):
    instance = get_object_or_404(Birthday, pk=pk)
    form = BirthdayForm(instance=instance)
    context = {'form': form}
    if request.method == 'POST':
        instance.delete()
        return redirect('birthday:list')
    return render(request, 'birthday/birthday.html', context)
