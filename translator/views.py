from django.shortcuts import render
from . import translate


# Create your views here.
def translator_view(request):
    if request.method == 'POST':
        original_text = request.POST['my_textarea']
        # the first translate is the translate.py file which is a module and the second translate is the function in the
        # file
        output = translate.translate(original_text)
        return render(request, 'translator.html', {'output_text': output, 'original_text': original_text})

    else:
        return render(request, template_name='translator.html')
