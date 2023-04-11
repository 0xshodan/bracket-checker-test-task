class BracketChecker:
    """
    Класс для проверки корректности групп скобок
    """

    def __init__(self) -> None:
        self._stack: list[str] = []

    def _push(self, value: str) -> None:
        """
        Вспомогательный метод, так как стек нужно максимально скрыть,
        взаимодействие с ним должно происходить только в определенных методах
        """
        self._stack.append(value)

    def _pop(self) -> str:
        """
        Вспомогательный метод, так как стек нужно максимально скрыть,
        взаимодействие с ним должно происходить только в определенных методах

        :return: открывающую скобку со стека
        """
        return self._stack.pop()

    def _reset_stack(self) -> None:
        """
        Метод для обнуления стека
        """
        self._stack = []

    @property
    def _is_stack_empty(self) -> bool:
        """
        Получить состояние стека
        :return: True если стек пустой, False, если нет
        """
        return not self._stack

    def validate_code(self, code: str) -> bool:
        """
        Метод для проверки кода(строки со скобками) на корректность

        :param str code: Код который необходимо проверить
        :return: True если количество скобок корректено, False, если нет
        """
        self._reset_stack()  # Обнуление стека, чтобы при многократном вызове этого метода он работал корректно

        open_brackets = ("(", "{", "[")
        closed_brackets = (")", "}", "]")
        # Делаем такие кортежи чтобы избежать "magic" кортежей в коде

        for char in code:
            if char in open_brackets:
                self._push(char)
            elif char in closed_brackets:
                # Следующая конструкция была сделана для отлавливания IndexError при self._stack.pop()
                # Exception может возникать при ситуации когда закрывающих скобок больше чем открывающих
                try:
                    stack_bracket = self._pop()
                except IndexError:
                    return False
                # Так как в кортежах open и closed brackets по индексу
                # закрывающая скобка соответствует открывающей, можно
                # можно воспользоваться этим свойством
                bracket_index = open_brackets.index(stack_bracket)
                if char != closed_brackets[bracket_index]:
                    return False
        # Если выполнение кода дошло до этого момента, то либо
        # группы скобок расположены корректно, либо открывающих скобок
        # оказалось больше чем закрывающих, в таком случае расположение
        # скобок неккоректно, поэтому нужно проверить пустой ли на данный момент стек
        return self._is_stack_empty
