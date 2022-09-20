
class ConsoleIO:
    def input(self, field, data_type = str, defvalue=None):
        while True:
            result = input(f"Введите {field}")
            try:
                result = data_type(result)
                break
            except:
                print("Некорректное значение")
        return result

    def output(self, title, field=""):
        print(f"{title}: {field}")