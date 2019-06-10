from datetime import datetime
from django.db.models import Q
from django.views.generic import View
from django.urls import reverse
from django.http import HttpResponseNotFound
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator

class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')