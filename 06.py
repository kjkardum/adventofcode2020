print(sum(len({*i}.intersection(*i.split()))for i in open('input.txt').read().split('\n\n')))