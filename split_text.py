import sys
import os
import getopt
from itertools import islice


def main(argv):

    # verify numbers of arguments
    if len(argv) < 6:
        print('Number of arguments invalid')
        print('Try with:')
        print('find_synonym.py -i <inputfile obo> -n <number of files> -t <number of terms> -o <ouputfile obo>')
        sys.exit()
    # end if

    url = ''
    output = ''
    n_files = -1
    n_terms = 100000

    try:
        opts, args = getopt.getopt(argv, "hi:n:t:o:", ["ifile=", "n=", "t=","ofile="])
    except getopt.GetoptError:
        print('find_synonym.py -i <inputfile obo> -n <number of files> -t <number of terms> -o <ouputfile obo>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('find_synonym.py -i <inputfile obo> -n <number of files> -t <number of terms> -o <ouputfile obo>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            url = arg
        elif opt in ("-n", "--n"):
            n_files = arg
        elif opt in ("-t", "--t"):
            n_terms = arg
        elif opt in ("-o", "--ofile"):
            output = arg
    # end for

    file_input = os.path.basename(url)
    filename_input, file_extension_input = os.path.splitext(file_input)

    file_output = os.path.basename(output)
    filename_output, file_extension_output = os.path.splitext(file_output)

    # verify if input obo file exist
    print(url)
    if not os.path.isfile(url):
        print('Input .obo File does not exist')
        sys.exit()
    # end if

    # verify if input file is a obo
    if not file_extension_input == '.obo':
        print('Input File must have a .obo extension')
        sys.exit()
    # end if

    print(output)
    # verify if input file is a obo
    if not (file_extension_output == '.obo'):
        print('Output File must have a .obo extension')
        sys.exit()
    # end if

    # get header
    current_line = 0
    config_text = ""
    with open(url) as infile:
        for line in infile:
            if '[Term]' in line:
                break
            config_text += line
            current_line += 1

    count_files = 0
    if n_files == -1:
        n_files = 10
    while count_files < int(n_files):
        count_terms = 0
        file_name = output.split('.')[0] + '-' + str(count_files) + '.obo'
        with open(file_name, 'a') as file_output:
            file_output.write(config_text)
            with open(url) as infile:
                # jump to current line
                for line in islice(infile, current_line, None):
                    if count_terms > int(n_terms) and '[Term]' in line:
                        break
                    if '[Term]' in line:
                        count_terms += 1
                    file_output.write(line)
                    current_line += 1
                else:
                    break
            count_files += 1
            print('file ' + str(count_files) + ' written')


if __name__ == "__main__":
    main(sys.argv[1:])


