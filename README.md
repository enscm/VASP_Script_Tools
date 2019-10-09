# VASP_Tools
Here are some simple python scripts for VASP DOS/MD data treatment

split_dos_Q.py can split the DOSCAR file into sub-dosfiles, each of them countains (from DOS1 to DOSn) the individual atom information
(energy s-DOS(up) px-DOS(up) py-DOS(up) ...total-DOS); (total DOS for all Atoms is conserved in DOS0)

sum_dos_Q.py can sum the dos split previously by atom type (e.g: to sum up the s, p and d orbitals of file DOS2 (atom number 2))
 or by a sequence of atoms (e.g: sum up the dos from DOS1 to DOS8(8 atoms information) or DOS1 plus DOS8)
