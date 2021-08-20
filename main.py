import functions
import buttons


import PySimpleGUI as sg


ICON = 'images/globo.ico'
FONT = 'inherit'


def popup(cep, address, district, state, city):
    text = 'Cep  ->  {}\nRua  ->  {}\nBairro  ->  {}\nEstado  ->  {}\nCidade  ->  {}'
    sg.popup_ok(text.format(cep, address, district, state, city), title='Busca CEP', font=FONT, icon=ICON)


if __name__ == "__main__":
    sg.theme('LightGrey1')

    layout = [[sg.Text('INFO: Digite apenas os números do CEP. Obrigado!')],
              [sg.Text('CEP: '), sg.InputText(key='cep_number')],
              [sg.Button('', image_data=buttons.button_p_base64, key='-Procurar-', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0),
               sg.Button('', image_data=buttons.button_x_base64, key='-Exit-', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)]]

    window = sg.Window('Busca CEP', layout, icon=ICON, font=FONT, grab_anywhere=True)

    while True:
        event, values = window.read()
        if event == '-Procurar-':
            cep_number = functions.validation_cep(values['cep_number'])
            try:
                response = functions.get_response_via_cep(cep_number)
                parsing = functions.return_parsing_json(response)
                objects = functions.returned_objects(parsing)
                cep, address, district, state, city = objects
                popup(cep, address, district, state, city)

            except Exception as error:
                print(error)

        elif event == sg.WIN_CLOSED or event == '-Exit-':
            break

    window.close()
