import traceback

# Logger
from utils.Logger import Logger

number1 = 20
number2 = 1


def main():
    try:
        result = number1 / number2
        Logger.add_to_log("info", "El resultado es: {}".format(result))
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        print("No se puede dividir entre 0...")


main()
