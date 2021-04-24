import pymysql
from .celery import app as celery_app


pymysql.install_as_MySQLdb()

# 这将确保在以下情况下始终导入应用程序
# Django启动，以便shared_task将使用此应用程序。
__all__ = ('celery_app',)
