from controls import *
from atf.ui import *


@templatename("EDO3/passage:Panel")
class Panel(StickyTemplate):
    """На выполнение"""

    agree = ControlsButton(SabyBy.DATA_QA, 'edo3-PassageList__action-buttons-area', 'Согласовать отгул')
    to_myself = ControlsButton(SabyBy.DATA_QA, 'Lookup__link', 'себе')
