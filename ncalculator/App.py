from tkinter import ttk, Tk, StringVar
from typing import Callable
from enum import Enum

try:
    from statemachine import StateMachine, State, Transition
except ImportError:
    from .statemachine import StateMachine, State, Transition

class SymbolType(Enum):
    BIN_OP = ["*", "-", "+", "/"]
    UN_OP = ["1/"]
    DIGIT = [str(i) for i in range(0, 10)]

class App():
    FONT = ('Arial', 20, 'bold')

    def __init__(self):
        self.SPECIAL_BUTTONS: dict[str, Callable] = {
            'MC': lambda: print('aa'),
            'MR': lambda: print('aaa'),
            'M+': lambda: print('aaaa'),
            'M-': lambda: print('aaaaa'),
            'MS': lambda: print('aaaaaa')
        }
        self.BUTTONS: dict[str, Callable] = {
            '%': lambda: self._add_symbol('%'),
            '√': lambda: self._add_symbol('b'),
            'x²': lambda: self._add_symbol('**2'),
            '1/x': lambda: self._add_symbol('1/', insert_to_begin=True),
            'CE': lambda: self._clear(),
            'C': lambda: self._clear(),
            '⌫': lambda: self._delete_symbol(),
            '/': lambda: self._add_symbol('/'),
            '7': lambda: self._add_symbol('7'),
            '8': lambda: self._add_symbol('8'),
            '9': lambda: self._add_symbol('9'),
            '*': lambda: self._add_symbol('*'),
            '4': lambda: self._add_symbol('4'),
            '5': lambda: self._add_symbol('5'),
            '6': lambda: self._add_symbol('6'),
            '-': lambda: self._add_symbol('-'),
            '1': lambda: self._add_symbol('1'),
            '2': lambda: self._add_symbol('2'),
            '3': lambda: self._add_symbol('3'),
            '+': lambda: self._add_symbol('+'),
            '±': lambda: self._toggle(),
            '0': lambda: self._add_symbol('0'),
            '.': lambda: self._add_symbol('.'),
            '=': lambda: self._eval()}
        self.window = Tk()
        self.window.title('Calculator')
        self.frame = ttk.Frame(self.window)
        self.window.geometry('410x500+20+20')
        self.window.resizable(False, True),
        self.__text_field()
        self._init_state_machine()

    def _init_state_machine(self) -> None:
        states = (
            State("Start", {"symbols": []}),
            State("Digits", {"symbols": [str(i) for i in range(0, 10)]}),
            State("UnOperator", {"symbols": ["sqrt", "1/"]}),
            State("BinOperator", {"symbols": ["+", "-", "/", "*"]}),
            State("Eval", {}),
            State("Error", {})
        )
        
        transitions = (Transition("Start", "Digits"),
                       Transition("Start", "UnOperator"),
                       Transition("Digits", "Digits"),
                       Transition("Digits", "BinOperator"),
                       Transition("Digits", "Eval"),
                       Transition("UnOperator", "Digits"),
                       Transition("UnOperator", "Eval"),
                       Transition("BinOperator", "Digits"),
                       Transition("BinOperator", "UnOperator"),
                       Transition("Eval", "Digits"),
                       Transition("Eval", "Error"))
    
        start_state = "Start"
        
        self.sm = StateMachine(states=states, transitions=transitions, start_node=start_state)

    def __text_field(self) -> None:
        self.text = StringVar(self.window, value='')
        entry: ttk.Label = ttk.Label(justify='left', anchor='se',
                                     textvariable=self.text, background='#FFFFFF', padding=(30, 10), font=self.FONT)
        entry.grid(row=0, column=0, columnspan=20, sticky='nsew')

        self.window.grid_rowconfigure(0, weight=2)
        for i in range(len(self.SPECIAL_BUTTONS.keys())):
            btn_text = list(self.SPECIAL_BUTTONS.keys())[i]
            ttk.Button(
                self.window,
                text=btn_text, command=self.SPECIAL_BUTTONS[btn_text]).grid(
                row=1,
                column=i * 4,
                sticky='snwe',
                columnspan=4)
        row = 2
        first_button_on_row = True
        for i in range(len(self.BUTTONS.keys())):
            col = i % 4
            btn_text = list(self.BUTTONS.keys())[i]
            ttk.Button(
                self.window,
                text=btn_text,
                command=self.BUTTONS[btn_text]).grid(
                row=row,
                column=col * 5,
                sticky='snwe',
                columnspan=5)
            if (i + 1) % 4 == 0 and not first_button_on_row:
                row += 1
                first_button_on_row = True
            else:
                first_button_on_row = False

    def _m_read(self):
        pass

    def _m_clear(self):
        pass

    def _m_save(self):
        pass

    def _m_add(self):
        pass

    def _m_sum(self):
        pass

    def sqrt(sefl):
        pass

    def _clear(self):
        self.text.set('')

    def _delete_symbol(self):
        if len(self.text.get()) > 0:
            self.text.set(self.text.get()[:-1])

    def _toggle(self):
        txt = self.text.get()
        if txt[0].isdigit():
            self.text.set('-' + txt)
        elif txt[0] == '-':
            self.text.set(txt[1:])

    def _check(self, symbol) -> bool:
        if symbol in SymbolType.DIGIT.value and self.sm.travel("Digits"):
            return True
        elif symbol in SymbolType.BIN_OP.value and self.sm.travel("BinOperator"):
            return True
        elif symbol in SymbolType.UN_OP.value and self.sm.travel("UnOperator"):
            return True
        
        print("Ввел хуйню")
        
        return False

    def _add_symbol(self, symbol: str, insert_to_begin=False) -> None:
        if self.sm.current_state == "Error":
            self.sm.reset()
            self._clear()
        if self._check(symbol):
            if insert_to_begin:
                self.text.set(symbol + self.text.get())
            else:
                self.text.set(self.text.get() + symbol)

    def _eval(self):
        if self.sm.travel("Eval"):
            try:
                self.text.set(eval(self.text.get()))
                self.sm.travel("Digits")
            except Exception:
                self.text.set('ERROR')
                self.sm.travel("Error")

    def __validate():
        pass

    def run(self):
        self.window.mainloop()
