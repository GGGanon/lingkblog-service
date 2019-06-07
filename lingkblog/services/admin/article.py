from lingkblog.services.base import Base
from lingkblog.models.article import Article as ArticleModel
from lingkblog import db

from flask import g


class Admin(Base):

    def get_article_list(self):
        # TODO: 参数验证

        account_id       = g.account_id
        title            = self.request.form['title']
        summary          = self.request.form['summary']
        content_type     = self.request.form['content_type']
        content          = self.request.form['content']
        content_markdown = self.request.form['content_markdown']
        # TODO: word_count 计算
        word_count  = 0
        category_id = self.request.form['category_id']
        tags        = self.request.form['tags']

        article_obj = ArticleModel(
            account_id=account_id,
            title=title,
            summary=summary,
            content_type=content_type,
            content=content,
            content_markdown=content_markdown,
            word_count=word_count,
            category_id=category_id,
            tags=tags
        )
        db.session.add(article_obj)
        db.session.commit()

        return self.return_success({
            'id': article_obj.id,
            'account_id': article_obj.account_id,
            'title': article_obj.title,
            'summary': article_obj.summary,
            'content_type': article_obj.content_type,
            'content': article_obj.content,
            'content_markdown': article_obj.content_markdown,
            'word_count': article_obj.word_count,
            'read': article_obj.read,
            'category_id': article_obj.category_id,
            'tags': article_obj.tags,
            'status': article_obj.status
        })




