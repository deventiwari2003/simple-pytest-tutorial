from decimal import Decimal
import traceback
class Valdx:
    def __init__(self):
        pass

    def validate_decimal(self,data):
        dcx: Decimal = 0.0
        flag = True
        try:
            dcx = Decimal(data)
            flag = True
        except ValueError as vx:
            flag = False
        except Exception as e:
            print(traceback.format_exc())
            flag = False
        if not flag:
            return (-1, None)
        return (0, dcx)

    def validate_integer(self,data):
        dcx: int = 0.0
        flag = True
        try:
            dcx = int(data)
            flag = True
        except ValueError as vx:
            flag = False
        except Exception as e:
            print(traceback.format_exc())
            flag = False
        if not flag:
            return (-1, None)
        return (0, dcx)
