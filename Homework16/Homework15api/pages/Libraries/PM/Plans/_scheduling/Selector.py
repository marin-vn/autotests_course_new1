from controls import *


@templatename("PM/Plans/_scheduling/Selector")
class Selector(CatalogTemplateList):
    """Панель выбора объекта планирования"""

    plan_obj_panel = Element(By.CSS_SELECTOR, '.plan-Scheduling-Selector__stack', 'Список объектов планирования')
