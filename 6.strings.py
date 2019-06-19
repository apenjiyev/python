text = 'X-DSPAM-Confidence:0.8475'
first=text.find(':')

second=text.find('5')

third=text[first+1:second+1]
print(float(third))
