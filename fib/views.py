from django.shortcuts import render, get_object_or_404, redirect
from .models import Fibonacci
from .forms import FibForm
#memoize to cache data
from memoize import memoize

# view for home page
def home(request):

    if request.method == "POST":
        form = FibForm(request.POST)
        # get the user input
        num = int(request.POST.get('parameter'))
        # perform Fibonacci recursion
        result = Fibonacci(num, fibo(num))
        # commit to db
        result.save()
        print fibo(num)
        return redirect('answer', pk=result.pk)

    else:
        form = FibForm()
    return render(request, 'fib/index.html', {'form': form})

# view for answer
def answer(request, pk):
    ans = get_object_or_404(Fibonacci, pk=pk)
    return render(request, 'fib/answer.html', {'ans': ans})

# Fibonacci function using caching
def memoize(f):
    cache = {}
    return lambda *args: cache[args] if args in cache else cache.update({args: f(*args)}) or cache[args]

@memoize
def fibo(n):
    return n if n < 2 else fibo(n-2) + fibo(n-1)
