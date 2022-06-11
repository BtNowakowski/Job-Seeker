from justjoinit import just_join
from pracujpl import pracuj
from nofluffjobs import nofluffjobs

links = just_join() + pracuj() + nofluffjobs()
with open('job.txt','w') as notepad:
    print(*links, file=notepad, sep='\n\n')