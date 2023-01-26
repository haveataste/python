#Connect to the API
import shodan
SHODAN_API_KEY = '6gkESaPpDgqIVFE74oAKT227NeUlcUKJ'
api = shodan.Shodan(SHODAN_API_KEY)

def Looking_up_a_host():
    try:
        host = api.host('94.142.241.111')
        for key in host:
            if key != 'data':
                print(key,'--->',host[key])
        for item in host['data']:
            for key in item:
                print(key,'--->',item[key])
        print(host.get('org'))
        print(host.get('location'))
    except shodan.APIError as e:
        print('APIError:',e)
    except:
        print('other error')


def Searching_Shodan():
    try:
        re = api.search('apache')
        print(re)
    except shodan.APIError as e:
        print('APIError:',e)


if __name__ == '__main__':
    Searching_Shodan()
