from modeller import *

env = Environ()
aln = Alignment(env)
mdl = Model(env, file='7P03', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='7P03A', atom_files='7P03.pdb')
aln.append(file='PTX3.ali', align_codes='PTX3')
aln.align2d(max_gap_length=50)
aln.write(file='PTX3-7P03A.ali', alignment_format='PIR')
aln.write(file='PTX3-7P03A.pap', alignment_format='PAP')
