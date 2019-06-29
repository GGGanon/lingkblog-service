from flask import Blueprint, request
from lingkblog.services.admin.site import Site as SiteService


bp = Blueprint('site', __name__, url_prefix='/admin-api/sites')

@bp.route('/menus', methods=['GET'])
def menus():
    site = SiteService(request)
    return site.get_menus()

@bp.route('/articles/categories', methods=['GET', 'POST'])
def article_category():
    site = SiteService(request)
    if request.method == 'POST':
        # 新增文章分类
        return site.store_article_category()
    if request.method == 'GET':
        # 获取文章分类列表
        return site.index_article_category()

@bp.route('/articles/categories/<int:id>', methods=['PUT'])
def update_article_category(id):
    site = SiteService(request)
    return site.update_article_category(id)

@bp.route('/config', methods=['GET'])
def get_site_config():
    site = SiteService(request)
    return site.get_site_config()

@bp.route('/config', methods=['PATCH'])
def update_site_config():
    site = SiteService(request)
    return site.update_site_config()