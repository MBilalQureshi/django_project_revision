from django.shortcuts import render
from django.http import HttpResponse

def about_me(request):

    # 1 request
    print(request.method) # GET
    # The HTTP "request" object contains metadata about the request made to the browser.
    # This includes the request method, as noted above. It also includes any form data, the URL that was called, and any files that were uploaded, among other things.

    # The view can then use the information in the request object to complete a task, such as writing form data to the database.

    # For a full list of the contents of the request object, you can check the https://docs.djangoproject.com/en/4.2/ref/request-response/
    
    # 2 response such as HttpResponse
    # Each view must return a response object to the browser. In our simple example, we have returned a simple HttpResponse. Or as complex as HTML templates

    return HttpResponse('This would be the about page')