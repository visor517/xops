from db.base import metadata, engine
from .tables import visited_links

# сбрасываем
metadata.drop_all(bind=engine)

# создаем таблицы
metadata.create_all(bind=engine)
