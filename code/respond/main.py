from .chat import Chat
from .resources import resources
from .flatten import flatten

default_language = 0

def run_it(flattened_res, language, subject, search_str):
    this_chat = Chat(flattened_res, subject, language)
    return this_chat.match(search_str)


class Respond:
    def __init__(self):
        print('Initializing Response System...')
        self.flattened_res = flatten(resources, default_language)

    def get_response(self, search_str, subject):
        rtn = {
            'subject': (),
            'reply': '',
        }

        match = run_it(self.flattened_res, default_language, subject, search_str)
        match_value = match['value']
        print(match, '\n')
        rtn['reply'] = "I'm not sure what you're asking for. Try entering the problem you're having - like 'rent' or 'sick'."
        # If some certainty
        if (match['certainty'] > 0):
            rtn['subject'] = match_value['subject']
            rtn['reply'] = f"It looks like you're looking for {match_value['phrase'][default_language]}."
            if 'children' in match_value:
                children = ', '.join(str(i) for i in match_value['children'])
                # If has 'options' field, use it to introduce children
                if 'options' in match_value:
                    rtn['reply'] += f" {match_value['options'][default_language]} {children}"
                # If not 'options' field, use a default phrase
                else:
                    rtn['reply'] += f" Here are some options: {children}. Which do you need?"
            if 'isLeaf' in match_value:
                # If is a leaf, limit the subject to the previous level
                rtn['subject'] = rtn['subject'][:-1]
                leaf_info = ''
                for key, val in match_value['info'][default_language].items():
                    leaf_info += f'\n{key.capitalize()}: {val}'
                rtn['reply'] += f"{leaf_info}"
        return rtn


def chat_loop():
    reply = "What are you looking for? Press q to exit."
    respond = Respond()
    subject = ()

    while True:
        search_str = input(f'{reply}\n')
        if search_str == 'q':
            print('\nGoodbye!')
            break
        response = respond.get_response(search_str, subject)
        subject = response['subject']
        reply = response['reply']


if __name__ == '__main__':
    chat_loop()
