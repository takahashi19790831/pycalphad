import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pycalphad import Database, binplot, variables as v
import os

tdb_path = os.path.expanduser('~/tdb/pycalphad-sandbox-master/alfe_sei.TDB')

dbf = Database(tdb_path)
comps = ['AL', 'FE', 'VA'] # VAは空孔(Vacancy)
phases = list(dbf.phases.keys()) # データベースにある全相を対象にする
conds = {
    v.X('FE'): (1e-4, 1, 0.02), # マグネシウムの組成 0〜1
    v.T: (300, 2000, 20),    # 温度 300K〜1000K
    v.P: 101325              # 1気圧
}

# 3. 相図の計算と描画
binplot(dbf, comps, phases, conds, lavel_phases=True)

plt.savefig('al_fe_phase_diagram.png')

