from django.shortcuts import render
from django.http import HttpResponse
import sqlalchemy as sa
from sqlalchemy import orm

from bigtiger.core.exceptions import DBError, SuspiciousOperation, DBRefError
from models import User, db


session = db.get_session()


def index(request):
    query = session.query(User)
    rows = query.all_dict()
    print rows

    # return HttpResponse('<h1>hello</h1>')
    return render(request, 'base.html', {'rows': rows})
