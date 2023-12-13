codons = {'AAA':'K'}

def translate_with_frame(dna, frames=[1,2,3,-1,-2,-3]):
    #your code here - use the preloaded dict codons for conversions
    if dna=='':
        return ['' for i in range(len(frames))]
    ending = []
    for i in frames:
        reversed_dna = ''
        new_strand = ''
        if i<0 and len(reversed_dna)==0:
            for j in range(len(dna)-1,-1,-1):
                if dna[j] == 'A':
                    reversed_dna += 'T'
                elif dna[j] == 'G':
                    reversed_dna += 'C'
                elif dna[j] == 'C':
                    reversed_dna += 'G'
                else:
                    reversed_dna += 'A'
        if i>0:
            for a in range(abs(i)-1,len(dna)+1,3):
                try:
                    new_strand += codons[dna[a:a+3:]]
                except KeyError:
                    ending.append(new_strand)
            
        elif i<0:
            for a in range(abs(i)-1,len(dna)+1,3):
                try:
                    new_strand += codons[reversed_dna[a:a+3:]]
                except KeyError:
                    ending.append(new_strand)
    return ending

print(translate_with_frame(''))
