from pylab import *

dict1 = {'Education': {0: 3666411.0, 1: 841547.0, 2: 511340.0}, 'Productivity': {0: 194868165.0, 1: 309372687.0, 2: 304810991.0}, 'Finance': {0: 95896871.0, 1: 116937635.0, 2: 281042059.0}, 'Entertainment': {0: 643102086.0, 1: 545015430.0, 2: 934226414.0}, 'Communication': {0: 1960404688.0, 1: 2148140420.0, 2: 3091010653.0}, 'Travel': {0: 93785572.0, 1: 489767245.0, 2: 277088167.0}, 'Personalization': {0: 1308626489.0, 1: 764852543.0, 2: 1627312011.0}, 'Libraries': {0: 618805.0, 1: 197563.0, 2: 87888.0}, 'Game': {0: 266734417.0, 1: 98074653.0, 2: 177816473.0}, 'Weather': {0: 34246257.0, 1: 37888139.0, 2: 70903852.0}, 'Health': {0: 61995532.0, 1: 24810937.0, 2: 98182712.0}, 'Social': {0: 337444961.0, 1: 304060977.0, 2: 583003122.0}, 'Lifestyle': {0: 140506918.0, 1: 80944031.0, 2: 342793260.0}, 'Books': {0: 30260021.0, 1: 44414053.0, 2: 137961863.0}}

dict2 = {'Education': {0: 20, 1: 4, 2: 16}, 'Productivity': {0: 2635, 1: 2595, 2: 3290}, 'Finance': {0: 617, 1: 722, 2: 846}, 'Entertainment': {0: 1541, 1: 1606, 2: 2533}, 'Communication': {0: 12180, 1: 13282, 2: 15959}, 'Travel': {0: 421, 1: 507, 2: 581}, 'Personalization': {0: 2802, 1: 2460, 2: 3223}, 'Libraries': {0: 13, 1: 8, 2: 11}, 'Game': {0: 329, 1: 328, 2: 470}, 'Weather': {0: 853, 1: 1038, 2: 1155}, 'Health': {0: 240, 1: 229, 2: 468}, 'Social': {0: 2504, 1: 2773, 2: 3371}, 'Lifestyle': {0: 558, 1: 562, 2: 948}, 'Books': {0: 88, 1: 87, 2: 140}}

len1 = len(dict2.keys())

pos = arange(len1) + .5

# val1 = [sum(dict1[a].values()) for a in dict1.keys()]
val2 = [sum(dict2[a].values()) for a in dict2.keys()]

# vval = [val1[i]/val2[i] for i in range(len(val1))]

"""
figure(1)
barh(pos, val2, align='center')
yticks(pos, dict2.keys())
xlabel('Total Times')
title('Category Usage Total Times')

show()
"""
keys = dict1.keys()
for i in range(1, len1+1):
    figure(i, figsize=(6, 6))
    ax = axes([0.1, 0.1, 0.8, 0.8])

    fracs1 = [dict1[keys[i-1]][a]/sum(dict1[keys[i-1]].values()) for a in [0, 1, 2]]
    fracs2 = [dict2[keys[i-1]][a]/float(sum(dict2[keys[i-1]].values())) for a in [0, 1, 2]]

    fracs = [fracs1[d]/fracs2[d] for d in range(len(fracs1))]

    explode = (0, 0, 0)
    labels = 'Morning', 'Afternoon', 'Evening'

    pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = ("g", "r", "y"))

    title(' %s Usage Per Duration Percentage'%(keys[i-1]))
    print keys[i-1] 
    savefig('%s_per.png'%(keys[i-1]))




