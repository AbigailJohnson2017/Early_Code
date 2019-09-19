# This program helps optimize chances of a resume being viewed by an ATS by
# allerting the applicant to the most commonly-used words in the job description.
# Program automatically emits commonly-used fillers like "the", "to", etc.

jobd=input("Copy-paste plaintext job description: ", )
words=jobd.split()
counts=dict()
tossout=["will", "use", "more", "how", "and", "to", "the", "for", "a", "of", "in", "their", "is", "be", "you", "your", "with"]
for word in words:
    lword=word.lower()
    if lword in tossout:
        counts[lword]=0
    else:
        counts[lword]=counts.get(lword,0)+1
tmp=list()
for k,v in counts.items():
    if v==0:
        continue
    tmp.append((v,k))
tmp=sorted(tmp, reverse=True)
print(tmp)
for k,v in tmp:
    print(k, v)
