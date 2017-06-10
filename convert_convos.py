import json
import sys
import os

try:
    inputfile = sys.argv[1]
except IndexError:
    print "Please provide the name of a textfile containing json data from http://terminal.sexy as an argument"
    exit()

current_working_dir_contents = os.listdir(".")

if "_custom.scss" not in current_working_dir_contents:
    print "\n_custom.scss not in path\n"
    exit()
try: 
    with open(inputfile) as f:
        new_copy = json.loads(f.read())
        new_colors = new_copy['color']
except IOError:
    print '\n"'+inputfile+'" not found\n'
    exit()

color_1 = new_colors[3]
color_2 = new_colors[2]
color_4 = new_colors[4]
color_5 = new_colors[12]
color_8 = new_colors[11]
color_9 = new_colors[7]
color_10 = new_colors[14]
color_16 = new_copy['foreground']
color_17 = new_colors[15]
color_20 = new_colors[1]
background_color_1 = new_colors[2]
background_color_2 = new_copy['background']
background_color_3 = new_colors[12]
background_color_6 = new_colors[8]
background_color_7 = new_colors[4]
background_color_8 = new_colors[1]
background_color_11 = new_colors[5]


with open('_custom.scss', 'r') as f:
    lines = f.readlines()
    lines[0] = '$color_1: '+color_1+';'
    lines[1] = '$color_2: '+color_2+';' 
    lines[3] = '$color_4: '+color_4+';'
    lines[4] = '$color_5: '+color_5+';'
    lines[7] = '$color_8: '+color_8+';'
    lines[8] = '$color_9: '+color_9+';'

    lines[9] = '$color_10: '+color_10+';'
    lines[15] = '$color_16: '+color_16+';'
    lines[16] = '$color_17: '+color_17+';'
    lines[19] = '$color_20: '+color_20+';'
    lines[24] = '$background_color_1: '+background_color_1+';'
    lines[25] = '$background_color_2: '+background_color_2+';'
    lines[26] = '$background_color_3: '+background_color_3+';'
    lines[29] = '$background_color_6: '+background_color_6+';'
    lines[30] = '$background_color_7: '+background_color_7+';'
    lines[31] = '$background_color_8: '+background_color_8+';'
    lines[34] = '$background_color_11: '+background_color_11+';'
	
#print lines[0:35]
with open('_custom.scss.new', 'w') as f:
    for line in lines:
        f.write("%s\n" % line.strip())
print '\nCreated "_custom.scss.new"\n'

