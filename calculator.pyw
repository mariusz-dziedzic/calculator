# !pip install PySimpleGUI
import PySimpleGUI as sg

# Theme, you can change this if you want ;)
sg.theme('DarkAmber')


def disabled_point():
    # Disable point button
    window['.'].update(disabled=True)


def enabled_point():
    # Enable point button
    window['.'].update(disabled=False)


def disabled_B():
    # Disable math buttons (without "-")
    # You can get e.g +-2 and this is correct = +(-2)
    window['+'].update(disabled=True),
    window['/'].update(disabled=True),
    window['*'].update(disabled=True),
    window['**'].update(disabled=True),
    window['sqrt'].update(disabled=True),
    window['='].update(disabled=True)


def enabled_B():
    # Enable math buttons
    window['+'].update(disabled=False),
    window['/'].update(disabled=False),
    window['*'].update(disabled=False),
    window['**'].update(disabled=False),
    window['='].update(disabled=False)


def event_e():
    # Assigning to the variable "val" what we click (what appears in 1st Input)
    # Each subsequent operation appends a new value to the previous one
    # "e" means enabled_B function in use
    val = values['first']
    val += event
    window['first'].update(val)
    enabled_B()


def event_de():
    # Same as the previous function but
    # "de" means disabled_B and enabled_point in use
    val = values['first']
    val += event
    window['first'].update(val)
    disabled_B()
    enabled_point()


def event_dd():
    # Same as the previous function but
    # "dd" means disabled_B and disabled_point in use
    val = values['first']
    val += event
    window['first'].update(val)
    disabled_B()
    disabled_point()


def event_ed():
    # Same as the previous function but
    # "ed" means enabled_B and disabled_point in use
    val = values['first']
    val += event
    window['first'].update(val)
    enabled_B()
    disabled_point()


# Font parameters:
font_setup = ('Arial', 11, 'bold')

layout = [
    # Input calculations:
    [sg.Input(key='first',
        disabled_readonly_background_color=('#fecd5a'),
        font=font_setup,
        disabled=True,
        text_color='black')],
    # Input result:
    [sg.Input(key='second',
        disabled_readonly_background_color=('#fecd5a'),
        font=font_setup,
        disabled=True,
        text_color='black')],

    # 1st line buttons:
    [
        sg.Exit(size=(6, 2), button_color=('white', '#950000'), font=font_setup),
        sg.B('Clear', size=(6, 2), button_color=('white', '#950000'), font=font_setup),
        sg.B('Copy result', key="Copy", size=(12, 2), font=font_setup),
        sg.B('←', key="back", size=(6, 2), font=font_setup)
    ],

    # 2nd line buttons:
    [
        sg.B('(', key="(", size=(5, 2), font=font_setup),
        sg.B(')', key=")", size=(5, 2), disabled=True, font=font_setup),
        sg.B('^', key="**", size=(6, 2), disabled=True, font=font_setup),
        sg.B('√', key="sqrt", size=(6, 2), disabled=True, font=font_setup),
        sg.B('%', key="proc", size=(6, 2), font=font_setup),
    ],
    # 3rd line buttons:
    [
        sg.B('7', key="7", size=(8, 5), font=font_setup),
        sg.B('8', key="8", size=(8, 5), font=font_setup),
        sg.B('9', key="9", size=(8, 5), font=font_setup),
        sg.B(':', key="/", size=(8, 5), disabled=True, font=font_setup)
    ],
    # 4th line buttons:
    [
        sg.B('4', key="4", size=(8, 5), font=font_setup),
        sg.B('5', key="5", size=(8, 5), font=font_setup),
        sg.B('6', key="6", size=(8, 5), font=font_setup),
        sg.B('x', key="*", size=(8, 5), disabled=True, font=font_setup)
    ],
    # 5th line buttons:
    [
        sg.B('1', key="1", size=(8, 5), font=font_setup),
        sg.B('2', key="2", size=(8, 5), font=font_setup),
        sg.B('3', key="3", size=(8, 5), font=font_setup),
        sg.B('-', key='-', size=(8, 5), font=font_setup)
    ],
    # 6th line buttons:
    [
        sg.B('0', key="0", size=(8, 5), font=font_setup),
        sg.B('.', key=".", size=(8, 5), font=font_setup),
        sg.B('=', key="=", size=(8, 5), font=font_setup),
        sg.B('+', key="+", size=(8, 5), disabled=True, font=font_setup)
    ],
    # Footer:
    [sg.Text("Mariusz Dziedzic, 2022")]
]

print("History:")  # History in consol ;)
# Main window:
window = sg.Window('Calculator', layout,
    icon='./calc.ico', size=(350, 650),
    element_justification='center')
while True:
    event, values = window.read()

    # Exit
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    # Clean fileds Inputs:
    if event in ("Clear"):
        window['first'].update("")
        window['second'].update("")
        window['('].update(disabled=False)
        disabled_B()

    if event in ("Copy"):
        val = values['second']
        window['first'].update(val)
        window['second'].update("")
        if not val:
            disabled_B()

    if event in ("("):
        window[')'].update(disabled=False)
    # If click number 0-9 and "." unlock "sqrt" button and run event_e():
    if event in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."):
        window['sqrt'].update(disabled=False)
        window['('].update(disabled=True)
        event_e()

    # Delete last input char & block incorrect math operation:
    if event in ("back"):
        val = values['first']
        val = val[:-1]
        try:
            last = val[-1]
            window['first'].update(val)
        except:
            last = ""
            window['first'].update('')
        if not val:
            disabled_B()
            window['('].update(disabled=False)
        elif last not in ["*", "/", "+", "-"]:
            window['('].update(disabled=True)
            enabled_B()
        else:
            disabled_B()
        if last in ["*", "/", "+", "-"]:
            window['('].update(disabled=False)

    # Run appropriate function:
    if event in ("."):
        event_dd()
    if event in (")"):
        window['sqrt'].update(disabled=False)  # NEW LINE
        event_ed()
    if event in ("+", "-", "*", "/", "(", "**"):
        window['('].update(disabled=False)
        event_de()

    # Sqrt operation:
    if event in ("sqrt"):
        val = values['first']
        val += "**(1/2)"
        window['first'].update(val)

    # Count percentage & show result:
    if event in ("proc"):
        # Close the parenthesis if you forget to close it ;)
        if "(" in values['first'] and ")" not in values['first']:
            values['first'] += ")"
        try:
            result = eval(values['first'])
        except:
            result = 0
        # Print in console history:
        result_percent = result*100
        print(values['first'], "=", result_percent, "%")
        # Show result in 2nd Input
        window['second'].update((result_percent, "%"))
        enabled_point()

    # Show result:
    if event in ("="):
        # Close the parenthesis if you forget to close it ;)
        if "(" in values['first'] and ")" not in values['first']:
            values['first'] += ")"
        try:
            result = eval(values['first'])
        except:
            result = 0
        # Print in console history:
        print(values['first'], "=", result)
        # Show result in 2nd Input
        window['second'].update(result)
        enabled_point()

window.close()
