import pickle
import os

def post_code_command(command):
    bot_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    post_code_path = os.path.join(bot_dir,'static','bot','csv','code_fukush.csv')
    try:    
        left, center, right = command.split()
        results = []
        with open(post_code_path, encoding='utf-8') as f:
            for line in f:
                post, _ , address01, address02 = line.split(',')
                if center in address01:
                    if right in address02:
                        results.append(post)
                        results.append(address01)
                        results.append(address02)
                else:
                        response = f'住所が存在しません。'
        if len(results) > 0:
            response = "<br>".join(results)
            response = "<br>" + response
    except ValueError:
        response = '郵便　〇〇市　〇〇と入力してください。'
    
            
    return response
