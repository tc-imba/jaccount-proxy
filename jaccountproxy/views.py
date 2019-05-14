from os import path

from flask import request, session, redirect, render_template, url_for, abort
from jaccountproxy import app
from jaccountproxy.model import get_client

from cachelib import SimpleCache

cache = SimpleCache()


@app.route('/authorize', methods=['GET'])
def show_authorize():
    redirect_url = path.join(app.config['HOST_URL'], 'callback')
    recorded_url = request.args.get('redirect_url', 'http://www.example.com/')

    client = get_client()
    url, state = client.get_authorize_url(redirect_url=redirect_url)
    cache.set(key=state, value=recorded_url, timeout=3600)
    return redirect(url)


@app.route('/callback', methods=['GET'])
def show_callback():
    code = request.args.get('code')
    state = request.args.get('state')
    redirect_url = path.join(app.config['HOST_URL'], 'callback')
    recorded_url = cache.get(key=state)

    client = get_client()
    access_token, refresh_token, id_token = client.get_token(code=code, redirect_url=redirect_url)
    return redirect(recorded_url + '?access_token=' + access_token)
