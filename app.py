'''

screenshots as a service API main file.

'''

import base64
import json
import logging
import multiprocessing as mp
import os
import sys
import time

from configs import ScreenConfigurations
from flask import Flask, Response, request
from flask import send_file
from flask_restful import Api, Resource, reqparse
from screenshots import ScreenFinder
from screenshots import ScreenShooter

app = Flask(__name__)
api = Api(app)
log = logging.getLogger(__name__)
config = ScreenConfigurations()


@app.route("/")
def hello():
    return config.welcome_msg


@app.route(config.api_url_header_get_screenshots, methods=["GET"])
def screen_show(domain):
    """
    This function shows a particular screen.
    """
    scr_finder = ScreenFinder(config)

    __domain_stored_snap_encoded = scr_finder.find_screen(domain)

    if __domain_stored_snap_encoded =='':
        return Response("Image not found")


    image_decoded = base64.b64decode(__domain_stored_snap_encoded)

    return Response(image_decoded, mimetype=config.mimetype_image)


@app.route(config.api_url_header_post, methods=["POST"])
def recieve_requests():
    """
    This function takes list of URLS as a front controller and delegate to screenshot module to initiate screenshot functionality trigger
    """
    t1 = time.time()
    try:
        data_received = json.loads(request.data)
        print('recieve_requests')
        shooter = ScreenShooter(config)
        shooter.prepare_shooting(data_received)   
        print('API Task completed in try')
    except Exception:
        return Response(json.dumps(get_meaningful_err_msg()), mimetype=config.mimetype_appl_or_json)

    t2 = time.time()
    t3 = t2-t1
    print(' Time taken to process:' + str(t3))
    return Response(json.dumps(config.status_completed), mimetype=config.mimetype_appl_or_json)


def get_meaningful_err_msg():
    return {'status': config.status_failed, 'action': config.status_action, 'details': get_root_cause()}


def get_root_cause():
    return "%s %s" % (str(sys.exc_info()[0]), str(sys.exc_info()[1]))


app.run(debug=True)
