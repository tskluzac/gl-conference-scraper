import HTMLParser

conferences = open('conference.txt','r')

def scrapeActivate(conferences):
    for line in conferences:
        if 'http' in line:
            print('yes!')
        else:
            print('no!')

    return(0)


def infopuller(url):
    shortMonths = ['Jan','Feb','Mar','Apr','May','Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    events = ['abstract', 'submission', 'registration', 'conference']

scrapeActivate(conferences)