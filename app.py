from flask import Flask, Response, request
import requests
from random import randint
from colors import colors_
from mongoengine import Document, StringField, DateTimeField
from config import connect_db
import datetime
from helpers import domain

app = Flask(__name__)

connect_db()


class AvatarData(Document):
    uhid = StringField(max_length=50)
    initials = StringField()
    color = StringField()
    date_modified = DateTimeField(default=datetime.datetime.now)



"""
API Scheme:
GET /v1/:initials/
GET /v1/:initials/:hex_color/
GET /v1/:initials/:hex_color/:identifier/
"""
svg_template = """ 
<svg width="500" height="500" xmlns="http://www.w3.org/2000/svg">
 <g>
  <rect id="svg_1" height="500" width="500" y="0" x="0" stroke-width="0" 
  stroke="#000000" fill="#{}"/>
  <text transform="matrix(1.158432126045227,0,0,1.158432126045227,-41.15026923827827,-17.281479248777032) " 
  xml:space="preserve" text-anchor="middle" font-family="Sans-serif" font-size="150" id="svg_2" y="283" x="253" 
  stroke-linecap="null" stroke-linejoin="null" stroke-width="0" stroke="#000000" fill="#ffffff">{}</text>
  <rect id="svg_2" height="500" width="500" y="0" x="0" stroke-width="0" 
  stroke="#000000" fill-opacity="0.0" />
 </g>
</svg>
"""
@app.route('/v1/<initials>/')
def init(initials):
    try:
        host = domain(request.referrer)
    except:
        host = 'unknown'
    uhid = '{}_{}'.format(initials,host)
    obj = AvatarData.objects(uhid=uhid).first()
    if not obj:
        randy = randint(0,920)
        color = colors_[randy]
        svg = svg_template.format(color,initials)

        newobj = AvatarData(uhid=uhid, initials=initials, color=color)
        newobj.save()
    else:
        initials = obj.initials
        color = obj.color
        svg = svg_template.format(color,initials)

    return Response(svg, status=200, mimetype='image/svg+xml')

@app.route('/v1/<initials>/<color>/')
def init_color(initials, color):
    try:
        host = domain(request.referrer)
    except:
        host = 'unknown'
    uhid = '{}_{}_{}'.format(initials,color,host)
    obj = AvatarData.objects(uhid=uhid).first()
    if not obj:
        svg = svg_template.format(color,initials)
        newobj = AvatarData(uhid=uhid, initials=initials, color=color)
        newobj.save()
    else:
        initials = obj.initials
        color = obj.color
        svg = svg_template.format(color,initials)

    return Response(svg, status=200, mimetype='image/svg+xml')

@app.route('/v1/<initials>/<color>/<ident>/')
def init_color_ident(initials, color, ident):
    try:
        host = domain(request.referrer)
    except:
        host = 'unknown'
    uhid = '{}_{}_{}_{}'.format(initials,color,ident,host)
    obj = AvatarData.objects(uhid=uhid).first()
    if not obj:
        if color == '!':
            randy = randint(0,920)
            color = colors_[randy]

        svg = svg_template.format(color,initials)
        newobj = AvatarData(uhid=uhid, initials=initials, color=color)
        newobj.save()
    else:
        initials = obj.initials
        color = obj.color
        svg = svg_template.format(color,initials)

    return Response(svg, status=200, mimetype='image/svg+xml')


if __name__ == "__main__":
    app.run(debug=True)


