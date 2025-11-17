try:
    f = open('demofile.txt')
try:
    f.write('LorumIpsum')
except:
    print('something went wrong when')
finally:
    f.close()
except:
    print('ok')