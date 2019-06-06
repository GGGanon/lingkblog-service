from flask import Blueprint, request
from lingkblog.services.admin.site import Site as SiteService

bp = Blueprint('site', __name__, url_prefix='/admin-api/sites')

@bp.route('/menus', methods=["GET"])
def menus():
    site = SiteService(request)
    return site.get_menus()
    