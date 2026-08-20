from modeller import *

env = Environ()
aln = Alignment(env)
mdl = Model(env, file='8WOI', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='8WOIA', atom_files='8WOI.pdb')
aln.append(file='PTX4.ali', align_codes='PTX4')
aln.align2d(max_gap_length=50)
aln.write(file='PTX4-8WOIA.ali', alignment_format='PIR')
aln.write(file='PTX4-8WOIA.pap', alignment_format='PAP')
